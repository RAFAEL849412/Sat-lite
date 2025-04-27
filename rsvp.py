import socket
import threading
import time

# Configuração
HOSTS = ['127.0.0.1', 'google.com', 'github.com']  # Lista de hosts para verificação
CHECK_INTERVAL = 60  # Intervalo entre verificações em segundos

def check_host(host):
    """
    Verifica a conectividade com um host.
    """
    try:
        print(f"Verificando conexão com {host}...")
        ip = socket.gethostbyname(host)
        with socket.create_connection((ip, 80), timeout=10):
            print(f"{host} está acessível.")
    except Exception as e:
        print(f"Erro ao acessar {host}: {e}")

def monitor_hosts():
    """
    Monitora a conectividade com a lista de hosts em intervalos definidos.
    """
    while True:
        threads = []
        for host in HOSTS:
            thread = threading.Thread(target=check_host, args=(host,))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        print(f"Aguardando {CHECK_INTERVAL} segundos para a próxima verificação...")
        time.sleep(CHECK_INTERVAL)

if __name__ == '__main__':
    try:
        monitor_hosts()
    except KeyboardInterrupt:
        print("Monitoramento encerrado pelo usuário.")
