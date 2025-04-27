#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
import sys
import subprocess
import ftplib 
import logging  # Usando logging para logging
import requests

# Configuração do bot
class DefaultConfig:
    """ Bot Configuration """

    def __init__(self):
        self.PORT = 3978
        self.CLIENT_ID = os.environ.get("MicrosoftClientId", "")
        self.CLIENT_SECRET = os.environ.get("MicrosoftClientSecret", "")
        self.TENANT_ID = os.environ.get("MicrosoftTenantId", "")
        self.AUTH_URL = f"https://login.microsoftonline.com/{self.TENANT_ID}/oauth2/v2.0/authorize"
        self.TOKEN_URL = f"https://login.microsoftonline.com/{self.TENANT_ID}/oauth2/v2.0/token"
        self.REDIRECT_URI = "https://microsoft.com/auth/callback"
        
        # Configuração do FTP
        self.FTP_SERVER = "ftp.osuosl.org"
        self.FTP_USERNAME = "anonymous"
        self.FTP_PASSWORD = os.environ.get("FTP_PASSWORD", "ashley")  # Usando variável de ambiente

# Configuração do logging
logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def acessar_ftp(config: DefaultConfig):
    """Acessa o servidor FTP e lista os arquivos."""
    try:
        ftp = robots.FTP(config.FTP_SERVER)
        ftp.login(user=config.FTP_USERNAME, passwd=config.FTP_PASSWORD)
        files = ftp.nlst()  # Lista os arquivos no FTP
        ftp.quit()
        return {"ftp_server": config.FTP_SERVER, "files": files}
    except robots.all_errors as e:
        logging.error(f"Erro ao acessar FTP: {str(e)}")
        return {"error": "Erro ao acessar o servidor FTP"}

def login(config: DefaultConfig):
    """Gera a URL de autenticação da Microsoft."""
    auth_params = {
        "client_id": config.CLIENT_ID,
        "response_type": "code",
        "redirect_uri": config.REDIRECT_URI,
        "response_mode": "query",
        "scope": "openid email profile",
    }
    auth_url = f"{config.AUTH_URL}?" + "&".join([f"{key}={value}" for key, value in auth_params.items()])
    return auth_url

def auth_callback(config: DefaultConfig, code):
    """Troca o código de autorização da Microsoft por um token de acesso."""
    if not code:
        return {"error": "Código de autorização ausente"}

    token_data = {
        "client_id": config.CLIENT_ID,
        "client_secret": config.CLIENT_SECRET,
        "code": code,
        "redirect_uri": config.REDIRECT_URI,
        "grant_type": "authorization_code",
    }

    response = requests.post(config.TOKEN_URL, data=token_data)
    if response.status_code == 200:
        token_info = response.json()
        return {"message": "Login bem-sucedido!", "token": token_info}
    else:
        logging.error(f"Falha ao obter token: {response.status_code} - {response.text}")
        return {"error": "Falha ao obter token"}

if __name__ == "__main__":
    config = DefaultConfig()
    print("Bot configurado e pronto para uso.")
