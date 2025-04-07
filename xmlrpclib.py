#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import socket
import platform
import psutil
import time
import locale
import json


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
        'cpu_freq': psutil.cpu_freq()._asdict(),
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


def start_client(host, port):
    client = socket()
    try:
        client.connect((host, port))
        print(f"[+] Conectado a {host}:{port}")
        
        while True:
            command = client.recv(1024).decode().strip()
            print(f"[>] Comando recebido: {command}")
            
            if command == "exit":
                client.send(b"Desconectando...")
                break
            elif command == "sysinfo":
                client.send(get_system_info().encode())
            else:
                client.send(f"Comando desconhecido: {command}".encode())

            client.send(b"OK")
    
    except Exception as e:
        print(f"[!] Erro: {e}")
    finally:
        client.close()
        print("[*] Conexão encerrada.")


if __name__ == '__main__':
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        start_client(config['host'], config['port'])
    except FileNotFoundError:
        print("Arquivo 'config.json' não encontrado!")
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo de configuração.")
