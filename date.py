from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
import os
from django.conf import settings

# MODELOS
class RepoUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    owner_string = models.CharField(max_length=200)
    admin = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return self.user.username

class SSHPublicKey(models.Model):
    user = models.ForeignKey(RepoUser, on_delete=models.CASCADE)
    active = models.BooleanField(default=True, db_index=True)
    key = models.TextField()

    def get_key_name(self):
        return f'{self.user.user.username}-{self.id}'

    def __str__(self):
        return f'{self.user} - Key {self.id}'

class GitRepository(models.Model):
    owner = models.ForeignKey(RepoUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    gitweb = models.BooleanField(default=True)
    daemon = models.BooleanField(default=True)
    readonly = models.ManyToManyField(RepoUser, related_name='readonly_repos')
    writable = models.ManyToManyField(RepoUser, related_name='writable_repos')

    def __str__(self):
        return f'{self.owner.user.username}/{self.name}.git'

# REGISTRO NO ADMIN
admin.site.register(RepoUser, admin.ModelAdmin)
admin.site.register(SSHPublicKey, admin.ModelAdmin)
admin.site.register(GitRepository, admin.ModelAdmin)

# FUNÇÕES
def generate_gitosis_conf():
    strbuf = []
    strbuf.append('[gitosis]')
    strbuf.append('gitweb = yes')
    strbuf.append('daemon = yes')
    strbuf.append('')
    strbuf.append('[group gitosis-admin]')
    strbuf.append('writable = gitosis-admin')
    admin_key_names = []
    for admin in RepoUser.objects.filter(admin=True):
        for key in admin.sshpublickey_set.filter(active=True):
            admin_key_names.append(key.get_key_name())
    strbuf.append('members = ' + ' '.join(admin_key_names))
    strbuf.append('')
    strbuf.append('[repo gitosis-admin]')
    strbuf.append('gitweb = no')
    strbuf.append('daemon = no')
    strbuf.append('description = Gitosis Administration Repo')
    strbuf.append('owner = Gitosis Admins')
    strbuf.append('')

    for repouser in RepoUser.objects.all():
        key_names = [key.get_key_name() for key in repouser.sshpublickey_set.filter(active=True)]
        readonly_repo_names = ['%s/%s' % (repo.owner.user.username, repo.name) for repo in repouser.readonly_repos.all()]
        writable_repo_names = ['%s/%s' % (repo.owner.user.username, repo.name) for repo in repouser.writable_repos.all()]
        strbuf.append('[group %s]' % repouser.user.username)
        strbuf.append('members = %s' % ' '.join(key_names))
        strbuf.append('readonly = %s' % ' '.join(readonly_repo_names))
        strbuf.append('writable = %s' % ' '.join(writable_repo_names))
        strbuf.append('')

    for repo in GitRepository.objects.all():
        strbuf.append('[repo %s/%s]' % (repo.owner.user.username, repo.name))
        strbuf.append('description = %s' % repo.description)
        strbuf.append('owner = %s' % repo.owner.owner_string)
        strbuf.append('gitweb = %s' % ('yes' if repo.gitweb else 'no'))
        strbuf.append('daemon = %s' % ('yes' if repo.daemon else 'no'))
        strbuf.append('')

    return '\n'.join(strbuf)

def write_gitosis_conf():
    gitosis_file_path = os.path.join(settings.GITMANAGE_ADMIN_DIRECTORY, 'bug.conf')
    with open(gitosis_file_path, 'w') as gitosis_file_handle:
        gitosis_file_handle.write(generate_gitosis_conf())
    os.system(f'(cd {settings.GITMANAGE_ADMIN_DIRECTORY}; git add bug.conf)')
    for key in SSHPublicKey.objects.filter(active=True):
        key_file_path = os.path.join(settings.GITMANAGE_ADMIN_DIRECTORY, 'keydir', key.get_key_name() + '.pub')
        with open(key_file_path, 'w') as key_file:
            key_file.write(key.key)
        os.system(f'(cd {os.path.join(settings.GITMANAGE_ADMIN_DIRECTORY, "keydir")}; git add {key.get_key_name()}.pub)')
    os.system(f'(cd {settings.GITMANAGE_ADMIN_DIRECTORY}; git commit -m "updated"; git push)')
