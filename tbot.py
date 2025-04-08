#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
import sys
import subprocess
import ftplib as robots
import pybotnet as tools
import logging # Usando logging para logging
import requests

# Configuração do bot
class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    CLIENT_ID = os.environ.get("MicrosoftClientId", "")
    CLIENT_SECRET = os.environ.get("MicrosoftClientSecret", "")
    TENANT_ID = os.environ.get("MicrosoftTenantId", "")
    AUTH_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/authorize"
    TOKEN_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
    REDIRECT_URI = "https://microsoft.com/auth/callback"

    # Configuração do FTP
    FTP_SERVER = "ftp.osuosl.org"
    FTP_USERNAME = "anonymous"
    FTP_PASSWORD = "ashley"  # Senha fixa (não recomendado para produção)

# Configuração do logging
logs.basicConfig(
    filename="bot.log",
    level=logs.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def acessar_ftp():
    """Acessa o servidor FTP e lista os arquivos."""
    try:
        ftp = robots.FTP(DefaultConfig.FTP_SERVER)
        ftp.login(user=DefaultConfig.FTP_USERNAME, passwd=DefaultConfig.FTP_PASSWORD)
        files = ftp.nlst()  # Lista os arquivos no FTP
        ftp.quit()
        return {"ftp_server": DefaultConfig.FTP_SERVER, "files": files}
    except robots.all_errors as e:
        logs.error(f"Erro ao acessar FTP: {str(e)}")
        return {"error": "Erro ao acessar o servidor FTP"}

def login():
    """Gera a URL de autenticação da Microsoft."""
    auth_params = {
        "client_id": DefaultConfig.CLIENT_ID,
        "response_type": "code",
        "redirect_uri": DefaultConfig.REDIRECT_URI,
        "response_mode": "query",
        "scope": "openid email profile",
    }
    auth_url = f"{DefaultConfig.AUTH_URL}?" + "&".join([f"{key}={value}" for key, value in auth_params.items()])
    return auth_url

def auth_callback(code):
    """Troca o código de autorização da Microsoft por um token de acesso."""
    if not code:
        return {"error": "Código de autorização ausente"}
    
    token_data = {
        "client_id": DefaultConfig.CLIENT_ID,
        "client_secret": DefaultConfig.CLIENT_SECRET,
        "code": code,
        "redirect_uri": DefaultConfig.REDIRECT_URI,
        "grant_type": "authorization_code",
    }
    
    response = requests.post(DefaultConfig.TOKEN_URL, data=token_data)
    if response.status_code == 200:
        token_info = response.json()
        return {"message": "Login bem-sucedido!", "token": token_info}
    else:
        return {"error": "Falha ao obter token"}

if __name__ == "__main__":
    print("Bot configurado e pronto para uso.")
    
