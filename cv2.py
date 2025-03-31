import requests
import platform
import os
from ftplib import FTP

class RemoteShell:
    def __init__(self):
        # URL para obter os dados TLE dos satélites Starlink
        self.tle_url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=tle"
        # URL para acessar satellites.pro remotamente
        self.satellites_pro_url = "https://satellites.pro/"
        # Configurações do servidor FTP
        self.ftp_server = "ftp.osuosl.org"
        self.ftp_port = 21
        self.ftp_user = 'anonymous'
        self.ftp_password = 'ashley'

    def download_starlink_tle(self):
        """Baixa os dados TLE dos satélites Starlink e salva no arquivo starlink.tle."""
        print("🛰️ Baixando dados dos satélites Starlink...")
        response = requests.get(self.tle_url)
        
        if response.status_code == 200:
            with open("starlink.tle", "w") as file:
                file.write(response.text)
            print("✅ Dados dos satélites Starlink salvos em 'starlink.tle'.")
        else:
            print(f"❌ Erro ao acessar os dados TLE. Código HTTP: {response.status_code}")

    def access_satellites_pro(self):
        """Acessa remotamente o site satellites.pro e adiciona seu conteúdo ao arquivo starlink.tle."""
        print(f"🌐 Acessando {self.satellites_pro_url} para coletar dados...")
        response = requests.get(self.satellites_pro_url)

        if response.status_code == 200:
            print("✅ Acesso realizado com sucesso ao satellites.pro.")
            # Adiciona o conteúdo de satellites.pro ao arquivo starlink.tle
            with open("starlink.tle", "a") as file:  # 'a' adiciona sem sobrescrever
                file.write("\n# Dados de satellites.pro:\n")
                file.write(response.text)
            print("✅ O conteúdo de satellites.pro foi adicionado ao arquivo 'starlink.tle'.")
        else:
            print(f"❌ Erro ao acessar satellites.pro. Código HTTP: {response.status_code}")

    def remote_ftp_command(self, command):
        """Conecta ao servidor FTP remotamente e executa comandos como 'list', 'get', 'put'."""
        try:
            ftp = FTP()
            ftp.connect(self.ftp_server, self.ftp_port)
            ftp.login(user=self.ftp_user, passwd=self.ftp_password)

            if command.lower().startswith('list'):
                return '\n'.join(ftp.nlst())
            elif command.lower().startswith('get'):
                filename = command.split(' ')[1]
                with open(filename, 'wb') as f:
                    ftp.retrbinary(f'RETR {filename}', f.write)
                return f"Arquivo '{filename}' baixado com sucesso."
            elif command.lower().startswith('put'):
                filename = command.split(' ')[1]
                with open(filename, 'rb') as f:
                    ftp.storbinary(f'STOR {filename}', f)
                return f"Arquivo '{filename}' enviado com sucesso."
            else:
                return "Comando FTP desconhecido."
        except Exception as e:
            return f"Erro no comando FTP: {e}"

    def execute_command(self, command):
        """Executa um comando local no sistema e retorna a saída."""
        try:
            output = os.popen(command).read()
            return output
        except Exception as e:
            return f"Erro ao executar o comando: {e}"

    def get_system_info(self):
        """Retorna informações do sistema."""
        try:
            system_info = (
                f"System: {platform.system()} {platform.release()}\n"
                f"Node Name: {platform.node()}\n"
                f"Processor: {platform.processor()}\n"
                f"Machine: {platform.machine()}\n"
                f"Python Version: {platform.python_version()}\n"
            )
            return system_info
        except Exception as e:
            return f"Erro ao obter informações do sistema: {e}"

    def main(self):
        """Executa a sequência remota sem interação do usuário."""
        print("Iniciando a execução remota...\n")

        # 1. Baixar dados TLE dos satélites Starlink
        self.download_starlink_tle()
        
        # 2. Acessar o site satellites.pro e combinar os dados no arquivo starlink.tle
        self.access_satellites_pro()

        # 3. Exibir informações do sistema local
        print("\nInformações do sistema:")
        print(self.get_system_info())

        # 4. (Opcional) Executar comando FTP de exemplo (listar arquivos no FTP)
        print("\nComando FTP 'list':")
        print(self.remote_ftp_command('list'))

        # 5. (Opcional) Executar comando local para listar arquivos no diretório atual
        print("\nComando local 'ls':")
        print(self.execute_command('ls'))

        print("\nExecução finalizada.")

if __name__ == "__main__":
    remote_shell = RemoteShell()
    remote_shell.main()

