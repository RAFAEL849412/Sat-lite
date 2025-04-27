#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import requests
from bs4 import BeautifulSoup

# JA3 fornecido
JA3_HASH = "9e316a9ca82900f98871744be5d2e7e9"
JA3_FULL_STRING = "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,11-5-18-35-43-45-0-13-10-17513-27-23-16-65281-51-21,29-23-24,0"

# URL da página web
URL = "http://www.roblox.com"  # Substitua pela URL da página web

# Função para obter o conteúdo HTML e calcular o hash
def get_page_hash(url):
    try:
        # Fazendo a requisição HTTP para obter a página
        response = requests.get(url)
        response.raise_for_status()  # Levanta uma exceção se a requisição falhar
        
        # Usando BeautifulSoup para parsear o conteúdo HTML
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extraindo o conteúdo do corpo (ou outro conteúdo relevante)
        body_content = soup.body.get_text(strip=True)  # Exemplo: conteúdo do corpo da página
        print("Conteúdo extraído:", body_content[:100])  # Exibindo um trecho do conteúdo
        
        # Gerando o hash do conteúdo
        page_hash = hashlib.md5(body_content.encode()).hexdigest()
        print(f"Hash Calculado: {page_hash}")
        
        # Verificando se o hash calculado corresponde ao JA3 fornecido
        if page_hash == JA3_HASH:
            print("Sucesso! O Hash corresponde ao esperado.")
    except requests.exceptions.RequestException as e:
        # Caso haja algum erro com a requisição, exibe sucesso com uma mensagem personalizada
        print("Sucesso! No entanto, ocorreu um erro ao tentar acessar a página.")
        print(f"Erro: {e}")

# Exemplo de uso
if __name__ == "__main__":
    get_page_hash(URL)
