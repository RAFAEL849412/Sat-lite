#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import hashlib
import requests
import platform
from prettytable import PrettyTable

# Lista para armazenar notificações enviadas
notification_log = []

def calculate_hashes(file_path):
    hasher_md5 = hashlib.md5()
    hasher_sha1 = hashlib.sha1()
    hasher_sha256 = hashlib.sha256()

    try:
        with open(file_path, 'rb') as file:
            buf = file.read(65536)
            while len(buf) > 0:
                hasher_md5.update(buf)
                hasher_sha1.update(buf)
                hasher_sha256.update(buf)
                buf = file.read(65536)
    except FileNotFoundError:
        return None  # Retorna None caso o arquivo não exista ou não possa ser acessado

    return hasher_md5.hexdigest(), hasher_sha1.hexdigest(), hasher_sha256.hexdigest()

def classify_malware(file_hashes, malware_classification):
    for hash_value in file_hashes:
        if hash_value in malware_classification:
            return malware_classification[hash_value]
    return "Unknown"

def send_notification(message):
    """Envia uma notificação e registra a mensagem no log"""
    notification_log.append(message)
    print(f"Notificação: {message}")

def delete_file(file_path):
    """Deleta o arquivo e registra a ação"""
    try:
        os.remove(file_path)
        send_notification(f"Arquivo deletado: {file_path}")
    except Exception as e:
        send_notification(f"Erro ao tentar excluir o arquivo {file_path}: {str(e)}")

def scan_file(file_path, malicious_hashes, malware_classification, table):
    file_hashes = calculate_hashes(file_path)
    if file_hashes is None:
        return  # Ignora arquivos que não existem mais ou não podem ser lidos

    for hash_value in file_hashes:
        if hash_value in malicious_hashes:
            malware_type = classify_malware(file_hashes, malware_classification)
            table.add_row([file_path, malware_type])
            send_notification(f"Ameaça detectada: {file_path} - {malware_type}")
            delete_file(file_path)  # Exclui o arquivo detectado
            os.system('cls' if platform.system() == 'Windows' else 'clear')
            print(table)
            break

def scan_directory(directory, malicious_hashes, malware_classification, counter, table):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                scan_file(file_path, malicious_hashes, malware_classification, table)
                counter[0] += 1
            except PermissionError:
                pass
            except KeyboardInterrupt:
                raise
    return counter

if __name__ == "__main__":
    print("Iniciando antivírus...")
    url = "https://raw.githubusercontent.com/RAFAEL849412/Sat-lite/refs/heads/main/hashes.txt"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    malicious_hashes = set(response.text.splitlines())

    malware_classification = {
        "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8": "Ransomware",
        "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855": "Trojan",
        "8754c2a98e3b9c86aa49d4a35b8835e5fc6d5e6f53d6bce44a7f8db9c524de7a": "Virus",
        "3dc3c3f1bce75e029b1c7a8db9a20dfb2c6f68c925b1898db0d49f7a1d0520a6": "Spyware",
        "d301f9c47a8dd8331c4597feefcb056d08e3a3b4c4f4d03f9c1436a1a5f5b6b5": "Adware",
        "1e8a9f5127d527fb9c97d7fd8be2b883cc7f75e20e437d7b19db69b42c42220c": "Worm"
    }

    if platform.system() == 'Windows':
        directories_to_scan = ["C:\\", "D:\\", "E:\\"]
    elif platform.system() == 'Linux':
        directories_to_scan = ["/usr", "/home", "/"]
    else:
        print("Sistema operacional não suportado.")
        directories_to_scan = []

    start_time = time.time()
    counter = [0]

    table = PrettyTable()
    table.field_names = ["Caminho do Arquivo", "Tipo de Ameaça"]

    try:
        for directory in directories_to_scan:
            counter = scan_directory(directory, malicious_hashes, malware_classification, counter, table)
    except KeyboardInterrupt:
        print("O programa foi interrompido pelo usuário")

    end_time = time.time()
    elapsed_time = end_time - start_time

    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print(table)
    print(f"\nTotal de arquivos verificados: {counter[0]}")
    print(f"Tempo de execução: {elapsed_time:.2f} segundos")
    print("Esse antivírus foi desenvolvido por Halil Deniz. Em caso de dúvidas, entre em contato.")
    print("\nRegistro de notificações enviadas:")
    for notification in notification_log:
        print(notification)
