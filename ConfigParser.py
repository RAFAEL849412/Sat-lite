import satellite
import socket

def configurar_conexao(ip, porta):
    try:
        # Criar o socket TCP/IP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Configurar o tempo de espera para conexão
        sock.settimeout(10)  # Timeout de 10 segundos

        # Conectar ao IP e porta fornecidos
        sock.connect((ip, porta))
        print(f"Conectado a {ip} na porta {porta}")
        
        # Se desejar enviar ou receber dados, pode configurar aqui
        # Exemplo: sock.sendall(b"Hello, server!")
        
        # Fechar a conexão após uso
        sock.close()

    except socket.timeout:
        print(f"Falha na conexão: Tempo esgotado ao tentar conectar a {ip}:{porta}")
    except socket.error as e:
        print(f"Erro de socket: {e}")
    except Exception as e:
        print(f"Erro geral: {e}")

# Configurar IP e porta para a conexão
ip_address = '128.116.99.3'
port = 80  # Substitua pela porta correta

configurar_conexao(ip_address, port)
