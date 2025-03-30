import ftplib
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Configurações dos servidores FTP
ftp_servers = [
    {
        'host': '44.241.66.173',
        'user': 'dlpuser',
        'password': 'rNrKYTX9g7z3RgJRmxWuGHbeu'
    },
    {
        'host': 'ftp.dlptest.com',
        'user': 'dlpuser',
        'password': 'rNrKYTX9g7z3RgJRmxWuGHbeu'
    }
]

# Função para conectar ao servidor FTP e listar arquivos
def connect_and_list_files(server):
    try:
        ftp = ftplib.FTP(server['host'])  # Conectar ao servidor FTP
        ftp.login(server['user'], server['password'])  # Fazer login
        logging.info(f"Conectado ao servidor FTP: {server['host']}")

        # Listar arquivos no diretório atual
        files = ftp.nlst()  # Obter lista de arquivos
        logging.info("Arquivos no diretório:")
        for file in files:
            logging.info(file)

        ftp.quit()  # Fechar a conexão
    except ftplib.all_errors as e:
        logging.error(f"Erro ao conectar ao servidor FTP {server['host']}: {e}")

# Função para fazer upload de um arquivo
def upload_file(server, file_name):
    try:
        ftp = ftplib.FTP(server['host'])  # Conectar ao servidor FTP
        ftp.login(server['user'], server['password'])  # Fazer login
        logging.info(f"Conectado ao servidor FTP {server['host']} para upload.")

        # Verificar se o arquivo existe
        if os.path.isfile(file_name):
            with open(file_name, 'rb') as file:  # Abrir o arquivo em modo binário
                ftp.storbinary(f'STOR {os.path.basename(file_name)}', file)  # Enviar o arquivo
            logging.info(f"Arquivo '{file_name}' enviado com sucesso para o FTP {server['host']}.")
        else:
            logging.warning(f"Arquivo '{file_name}' não encontrado.")

        ftp.quit()  # Fechar a conexão
    except ftplib.all_errors as e:
        logging.error(f"Erro ao fazer upload do arquivo para o servidor FTP {server['host']}: {e}")

def main():
    # Listar arquivos em ambos os servidores FTP
    for server in ftp_servers:
        connect_and_list_files(server)

    # Fazer upload de um arquivo para ambos os servidores (substitua 'seu_arquivo.txt' pelo nome do arquivo que deseja enviar)
    file_to_upload = 'make.py'  # Substitua pelo caminho do seu arquivo
    for server in ftp_servers:
        upload_file(server, file_to_upload)

if __name__ == "__main__":
    main()
