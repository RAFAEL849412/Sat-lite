import socket
import urllib3
from urllib3 import PoolManager

def connect_to_satellite(ip, ports):
    """Conectar a um satélite e enviar um comando STATUS."""
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(5)  # Define um tempo limite de 5 segundos
                print(f"Conectando ao satélite {ip}:{port}...")
                s.connect((ip, port))
                print(f"Conexão estabelecida na porta {port}!")

                command = "STATUS\n"
                s.sendall(command.encode())
                print(f"Comando enviado: {command.strip()}")

                response = s.recv(1024).decode()
                print(f"Resposta do satélite na porta {port}: {response}")

        except socket.timeout:
            print(f"Conexão ao satélite na porta {port} excedeu o tempo limite.")
        except Exception as e:
            print(f"Erro ao conectar ao satélite na porta {port}: {e}")

def fetch_url(url):
    """Função para fazer uma requisição HTTP GET a uma URL."""
    http = PoolManager()

    try:
        response = http.request('GET', url)
        print(f"Status: {response.status}")
        print(response.data[:200])  # Exibe os primeiros 200 caracteres da resposta
        return response.status  # Retorna o status da resposta
    except urllib3.exceptions.RequestError as e:
        print(f"Erro ocorrido: {e}")
        return None  # Retorna None em caso de erro

def conectar_servidor(host, porta):
    """Conectar a um servidor TCP e enviar uma mensagem."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, porta))
            print(f"Conectado a {host}:{porta}")

            mensagem = "Olá, servidor!"
            s.sendall(mensagem.encode())

            resposta = s.recv(1024).decode()
            print(f"Resposta do servidor: {resposta}")

        except ConnectionRefusedError:
            print(f"Falha ao conectar a {host}:{porta} (Conexão recusada)")
        except Exception as e:
            print(f"Erro ao conectar a {host}:{porta}: {e}")

def main():
    # Configurações do satélite (substitua pelos valores reais)
    SATELLITE_PORTS = [80]  # Lista de portas

    # Chamando a função para conectar ao satélite
    # O IP do satélite foi removido

    # URLs das APIs e coordenadas
    longitude = -46.625290  # Exemplo de longitude
    latitude = -23.533773   # Exemplo de latitude
    date = '2025-10-19'     # Formato de data YYYY-MM-DD

    # Chaves de API
    api_key_1 = "dCMllHNj3NTcxNTU2NDEsIm9yaWdpbiI6Imh0dHBzOi8vc2F0ZWxsaXRlcy5wcm8ifQ.TQRfj1QKXWHMDHPNErlzD2DoQrZTLVvN"  # Primeira chave
    api_key_2 = "ceb8ab75da308ea820546375e9230dd9"  # Segunda chave

    # URLs das APIs
    url_2 = 'https://satellite-map.gosur.com'  # Substitua pela URL real do segundo site

    # Verifica se as coordenadas estão definidas
    if longitude is not None and latitude is not None:
        print(f"A localização é: Longitude = {longitude}, Latitude = {latitude}")

        # Acessa dados do segundo site
        print("Acessando dados do segundo site...")
        satellite_data_2 = fetch_url(url_2)
        print(satellite_data_2)
    else:
        print("As coordenadas não foram definidas.")

    # Conectar a um servidor TCP
    hosts = [{"host": "44.237.78.176", "porta": 7000}]
    for servidor in hosts:
        conectar_servidor(servidor["host"], servidor["porta"])

# Rodando a função principal
if __name__ == "__main__":
    main()
