import socket
import sys
import server
from datetime import datetime

def receive_file(host, port, file_size):
    # Criação do socket UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.bind(('', port))  # bind no mesmo porta para receber os dados

    # Envia uma mensagem para o servidor
    msg = b"Hello Server!"
    client_socket.sendto(msg, (host, port))

    # Prepara o arquivo para salvar os dados recebidos
    with open('File_Received.txt', 'wb') as f:
        print('Iniciando o recebimento de dados...')
        data = b""
        while len(data) < file_size:
            packet, addr = client_socket.recvfrom(1024)
            data += packet
            print(f"Recebido {len(packet)} bytes, total até agora: {len(data)} bytes - {datetime.now()}")

        # Grava os dados recebidos no arquivo
        f.write(data)
    
    print('Arquivo recebido com sucesso!')
    client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python starlink_client.py <host> <port> <tamanho_arquivo>")
        sys.exit(1)
    
    host = sys.argv[1]
    port = int(sys.argv[2])
    file_size = int(sys.argv[3])
    
    receive_file(host, port, file_size)
