try:
    import grpc
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "grpcio"])
    import grpc

import requests
import matplotlib.pyplot as plt
import numpy as np
import math
import time
import argparse
import starlink_grpc
import ftplib
import os

# Credenciais do servidor FTP padrão
host = 'ftp.osuosl.org'
username = 'anonymous'
password = 'ashley'

default_url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=tle"

# Cabeçalhos personalizados para requisição HTTP
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

class SatelliteTLE:
    def __init__(self, name_primary, name_alias, tle_line1=None, tle_line2=None):
        self.name_primary = name_primary
        self.name_alias = name_alias
        self.tle_line1 = tle_line1
        self.tle_line2 = tle_line2

    def __str__(self):
        return f"{self.name_primary} (alias: {self.name_alias})"

class Cloud:
    def __init__(self, coverage=0.0, altitude_km=2.0):
        self.coverage = coverage  # percentage of cloud cover
        self.altitude_km = altitude_km  # typical altitude of cloud layer

    def is_blocking(self, elevation_deg):
        return self.coverage > 0.5 and elevation_deg < 60

def procurar_satelite_geral_ftp(filename, ftp_host, ftp_user, ftp_pass):
    with ftplib.FTP(ftp_host) as ftp:
        ftp.login(user=ftp_user, passwd=ftp_pass)
        with open(filename, 'rb') as file:
            ftp.storbinary(f'STOR {filename}', file)

def verificar_ftp_arquivo_remoto(ftp_host, ftp_user, ftp_pass, filename):
    with ftplib.FTP(ftp_host) as ftp:
        ftp.login(user=ftp_user, passwd=ftp_pass)
        arquivos = ftp.nlst()
        return filename in arquivos

def listar_todos_arquivos_ftp(ftp_host, ftp_user, ftp_pass):
    with ftplib.FTP(ftp_host) as ftp:
        ftp.login(user=ftp_user, passwd=ftp_pass)
        arquivos = ftp.nlst()
        print("Arquivos encontrados no servidor FTP:")
        for arquivo in arquivos:
            print("-", arquivo)

def buscar_arquivos_por_filtro(ftp_host, ftp_user, ftp_pass, filtro):
    with ftplib.FTP(ftp_host) as ftp:
        ftp.login(user=ftp_user, passwd=ftp_pass)
        arquivos = ftp.nlst()
        arquivos_filtrados = [arquivo for arquivo in arquivos if filtro in arquivo]
        print(f"Arquivos que contêm '{filtro}':")
        for arquivo in arquivos_filtrados:
            print("-", arquivo)

class Satelite:
    def __init__(self):
        self.args = self.get_args()
        self.cloud = Cloud(coverage=0.6, altitude_km=2.5)

    def get_args(self):
        parser = argparse.ArgumentParser(description='Satellite Tracking')
        parser.add_argument('--url', action='store_true', help='Download TLE data from default URL')
        parser.add_argument('--debug', action='store_true', help='debug mode')
        return parser.parse_args()

    def run(self):
        print("Buscando arquivos do servidor FTP remoto...")
        listar_todos_arquivos_ftp(host, username, password)
        buscar_arquivos_por_filtro(host, username, password, 'starlink')
        arquivo = 'starlink_match_plots.png'
        if verificar_ftp_arquivo_remoto(host, username, password, arquivo):
            print("Arquivo encontrado no servidor FTP remoto.")

        if self.args.url:
            print("Baixando dados TLE...")
            response = requests.get(default_url, headers=headers)
            if response.status_code == 200:
                print("Dados TLE baixados com sucesso!")
            else:
                print(f"Falha ao baixar dados TLE. Status: {response.status_code}")

if __name__ == "__main__":
    bot = Satelite()
    bot.run()
