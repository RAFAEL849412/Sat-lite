import requests
import platform
import os

class RemoteShell:
    def __init__(self):
        # URL para acessar os dados diretamente (sem retornar HTML)
        self.satellites_earth_url = 'https://satellite.earth/data'  # Exemplo de URL para obter dados diretamente
        self.ftp_server = "ftp.osuosl.org"
        self.ftp_port = 21
        self.ftp_user = 'anonymous'
        self.ftp_password = 'ashley'

    def execute_command(self, command):
        """Executa um comando no sistema e retorna a saída."""
        try:
            output = os.popen(command).read()
            return output
        except Exception as e:
            return f"Erro ao executar o comando: {e}"

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
            return f"Erro ao obter informações do sistema: {e}"

    def connect_to_satellite(self):
        """Conecta ao servidor remoto e acessa um recurso ou arquivo."""
        try:
            print(f"Conectando ao servidor remoto: {self.satellites_earth_url}...")
            response = requests.get(self.satellites_earth_url)

            # Verifica se a requisição foi bem-sucedida
            if response.status_code == 200:
                # Se o conteúdo for binário ou em outro formato esperado, trata aqui
                return f"Conexão bem-sucedida ao {self.satellites_earth_url}."
            else:
                return f"Erro ao acessar o servidor remoto. Status code: {response.status_code}"
        except Exception as e:
            return f"Erro ao conectar ao servidor remoto: {e}"

    def remote_ftp_command(self, command):
        """Conecta ao servidor FTP remotamente e executa comandos como 'list', 'get', etc."""
        try:
            from ftplib import FTP
            ftp = FTP()
            ftp.connect(self.ftp_server, self.ftp_port)
            ftp.login(user=self.ftp_user, passwd=self.ftp_password)

            if command.lower().startswith('list'):
                return '\n'.join(ftp.nlst())  # Lista arquivos no servidor FTP
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

    def main(self):
        """Executa uma sequência remota sem interação do usuário."""

        # Tarefa pré-definida
        print("Iniciando a execução remota...\n")

        # Conectando ao servidor remoto
        satellite_output = self.connect_to_satellite()
        print(satellite_output)

        # Executando informações do sistema local
        system_info = self.get_system_info()
        print(system_info)

        # (Opcional) Executando um comando no FTP
        ftp_output = self.remote_ftp_command('list')  # Comando de exemplo para listar arquivos no servidor FTP
        print(ftp_output)

        # Realizando algum comando local (opcional)
        command_output = self.execute_command('ls')  # Comando de exemplo: listar arquivos no diretório atual
        print(command_output)

        print("Execução finalizada.")

if __name__ == "__main__":
    remote_shell = RemoteShell()
    remote_shell.main()
