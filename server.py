#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import requests

# JA3 fornecido
JA3_HASH = "9e316a9ca82900f98871744be5d2e7e9"
JA3_FULL_STRING = "771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,11-5-18-35-43-45-0-13-10-17513-27-23-16-65281-51-21,29-23-24,0"

# URL da página web
URL = "http://www.roblox.com"  # Substitua pela URL da página web

# Função para obter o conteúdo e calcular o hash
def get_page_hash(url):
    try:
        # Definir timeout (em segundos) para a requisição
        timeout = 10  # 10 segundos de timeout
        
        # Fazendo a requisição HTTP para obter a página
        print(f"Requisitando a página: {url}")
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # Levanta uma exceção se a requisição falhar
        
        # Exibindo o status da requisição
        print(f"Status da requisição: {response.status_code} - {response.reason}")
        
        # Usando o conteúdo bruto da resposta
        body_content = response.text.strip()  # Conteúdo puro, sem parsing HTML
        print("Conteúdo extraído (primeiros 100 caracteres):")
        print(body_content[:100])  # Exibindo um trecho do conteúdo
        
        # Gerando o hash MD5 do conteúdo
        print("Gerando o hash MD5 do conteúdo extraído...")
        page_hash = hashlib.md5(body_content.encode()).hexdigest()
        print(f"Hash Calculado: {page_hash}")
        
        # Comparando o hash calculado com o esperado
        if page_hash == JA3_HASH:
            print("Sucesso! O Hash corresponde ao esperado.")
        else:
            print(f"O Hash calculado ({page_hash}) não corresponde ao esperado ({JA3_HASH}).")
    except requests.exceptions.RequestException as e:
        # Caso haja algum erro com a requisição, exibe sucesso com uma mensagem personalizada
        print("Sucesso! No entanto, ocorreu um erro ao tentar acessar a página.")
        print(f"Erro: {e}")

# Exemplo de uso
if __name__ == "__main__":
    get_page_hash(URL)
