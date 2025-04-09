#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re
import json
import time
from urllib.parse import urljoin

# Cabeçalhos falsos estilo Roblox
HEADERS = {
    "User-Agent": "Roblox/WinInet",
    "Referer": "https://www.roblox.com/"
}

# URL do JSON no GitHub
COMANDOS_URL = "https://raw.githubusercontent.com/RAFAEL849412/Sat-lite/main/comandos.json"

# Diretórios comuns a verificar
PATHS_COMUNS = ["/admin", "/login", "/dashboard", "/robots.txt", "/config"]

# Headers de segurança recomendados
HEADERS_SEGURANCA = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "X-XSS-Protection"
]

# Carrega o JSON remoto
def carregar_comandos():
    try:
        r = requests.get(COMANDOS_URL)
        return r.json()
    except Exception as e:
        print(f"[!] Erro ao carregar comandos: {e}")
        return None

# Scanner de headers de segurança
def verificar_headers_seguranca(headers):
    print("\n[+] Verificando headers de segurança:")
    for h in HEADERS_SEGURANCA:
        if h in headers:
            print(f" - {h}: OK")
        else:
            print(f" - {h}: AUSENTE")

# Scanner de paths comuns
def verificar_paths(base_url, session):
    print("\n[+] Verificando diretórios comuns:")
    for path in PATHS_COMUNS:
        full_url = urljoin(base_url, path)
        try:
            resp = session.get(full_url)
            print(f" - {path} => {resp.status_code}")
        except Exception:
            print(f" - {path} => ERRO")

# Executa um único comando
def executar_comando(comando):
    session = requests.Session()
    session.headers.update(HEADERS)

    try:
        print(f"\n[+] Acessando: {comando['url']}")
        resp = session.get(comando['url'])
        print(f"[+] Status: {resp.status_code}")

        if comando.get("mostrar_cabecalhos"):
            print("\n[+] Cabeçalhos:")
            for k, v in resp.headers.items():
                print(f" - {k}: {v}")

        if comando.get("mostrar_cookies"):
            print("\n[+] Cookies:")
            for cookie in session.cookies:
                print(f" - {cookie.name} = {cookie.value}")

        if comando.get("buscar_tokens"):
            tokens = re.findall(r"[\w-]{24,}\.[\w-]{6,}\.[\w-]{27,}", resp.text)
            if tokens:
                print("\n[+] Tokens encontrados:")
                for t in tokens:
                    print(f" - {t}")
            else:
                print("\n[+] Nenhum token encontrado.")

        if comando.get("verificar_paths"):
            verificar_paths(comando['url'], session)

        if comando.get("verificar_headers_seguranca"):
            verificar_headers_seguranca(resp.headers)

    except Exception as e:
        print(f"[!] Erro ao executar comando: {e}")

# Função principal encapsulada
def main():
    comandos = carregar_comandos()
    if comandos:
        if isinstance(comandos, list):
            for idx, cmd in enumerate(comandos):
                print(f"\n==== Comando #{idx + 1} ====")
                executar_comando(cmd)
                time.sleep(2)
        else:
            executar_comando(comandos)

# Execução principal
if __name__ == "__main__":
    main()
