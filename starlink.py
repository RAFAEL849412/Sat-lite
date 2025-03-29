from ftplib import FTP

# Função para conectar ao servidor FTP
def conectar_ftp(host, usuario, senha):
    ftp = FTP(host)
    ftp.login(usuario, senha)
    return ftp

# Função para listar arquivos no diretório remoto
def listar_arquivos(ftp):
    print("Arquivos no diretório atual:")
    ftp.retrlines('LIST')

# Função para enviar um arquivo para o servidor FTP
def enviar_arquivo(ftp, arquivo_local):
    with open(arquivo_local, 'rb') as file:
        ftp.storbinary(f'STOR {arquivo_local}', file)

# Função para baixar um arquivo do servidor FTP
def baixar_arquivo(ftp, arquivo_local):
    with open(arquivo_local, 'wb') as file:
        ftp.retrbinary(f'RETR {arquivo_local}', file.write)

# Função principal
def main():
    # Configurações do servidor FTP
    ftp_host = 'ftp.belnet.be'  # Preencha com o servidor FTP
    ftp_user = 'anonymous'  # Preencha com o seu usuário
    ftp_passwd = 'ashley'  # Preencha com a sua senha

    # Conectar ao servidor FTP
    ftp = conectar_ftp(ftp_host, ftp_user, ftp_passwd)

    # Listar arquivos no diretório remoto
    listar_arquivos(ftp)

    # Enviar um arquivo para o servidor FTP
    # Preencha com o caminho do arquivo local
    enviar_arquivo(ftp, 'solvers.zip')

    # Baixar um arquivo do servidor FTP
    # Preencha com o caminho para salvar o arquivo localmente
    baixar_arquivo(ftp, 'aosSystem-20160810-std-x86_64.squashfs.xz')

    # Fechar a conexão FTP
    ftp.quit()

# Executar o script
if __name__ == '__main__':
    main()
