#cloud-config
autoinstall:
    version: 1
#    network:
#        network:
#            version: 2
#            ethernets:
#                ens192:
#                    dhcp4: true
#                    dhcp-identifier: mac
    early-commands:
        # Stop ssh for packer
        - sudo systemctl stop ssh
    locale: de_DE
    keyboard:
        layout: de
    ssh:
        install-server: yes
        allow-pw: yes
    storage:
        layout:
            name: direct
    apt:
        primary:
            - arches: [i386, amd64]
              uri: "http://de.archive.ubuntu.com/ubuntu/"
    packages:
        - open-vm-tools
    user-data:
        package_update: false
        package_upgrade: false
        package_reboot_if_required: false
        disable_root: false
        timezone: Europe/Berlin
        users:
        - default
        - name: ansible
          passwd: $6$rounds=4096$N2CzjWelQcBt48$nNyIeaoGQTUEvUj2mba8d7t1oO2g1pmuAHMwdqwOEB61dwLgN8W.FPsu79R2FeMuBjc2PeCwHlzEx4xso3Fe0
          shell: /bin/bash
          lock-passwd: false
          sudo: ALL=(ALL) NOPASSWD:ALL
          groups: users, admin
        chpasswd:
          expire: false
          list:
            - ubuntu:$6$rounds=4096$N2CzjWelQcBt48$nNyIeaoGQTUEvUj2mba8d7t1oO2g1pmuAHMwdqwOEB61dwLgN8W.FPsu79R2FeMuBjc2PeCwHlzEx4xso3Fe0
    late-commands:
        - sed -i -e 's/^#\?PasswordAuthentication.*/PasswordAuthentication yes/g' /target/etc/ssh/sshd_config
        - sed -i -e 's/^#\?PermitRootLogin.*/PermitRootLogin yes/g' /target/etc/ssh/sshd_config
#        - sed -i 's/^#*\(send dhcp-client-identifier\).*$/\1 = hardware;/' /etc/dhcp/dhclient.conf

