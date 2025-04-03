import os
import json
import requests
import subprocess
import sys

# Função para instalar pacotes usando pip
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Instalar BeautifulSoup4 se não estiver instalado
try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Instalando BeautifulSoup4...")
    install('beautifulsoup4')
    from bs4 import BeautifulSoup  # Tenta importar após a instalação

# Função para coletar e-mails e links de uma página
def scrape_page(url):
    try:
        # Fazer o request para a página
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve erro no request (status 4xx ou 5xx)

        # Parsear o conteúdo da página com BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Coletar e-mails encontrados na página
        emails = []
        for mailto_link in soup.find_all('a', href=True):
            if 'mailto:' in mailto_link['href']:
                emails.append(mailto_link['href'].replace('mailto:', ''))

        # Coletar todos os links da página
        links = []
        for link in soup.find_all('a', href=True):
            links.append(link['href'])

        return emails, links

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")
        return [], []

# Função para carregar ou criar arquivos JSON
def load_or_create_json(file_path, default_data):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
                # Garantir que o arquivo seja um dicionário
                if isinstance(data, list):
                    print(f"Formato inválido encontrado em {file_path}, corrigindo para dicionário.")
                    data = default_data
                # Verificar e corrigir a estrutura de dados
                if "emails" not in data:
                    data["emails"] = []
                if "links" not in data:
                    data["links"] = []
                return data
            except json.JSONDecodeError:
                print(f"Erro ao ler {file_path}, criando um novo arquivo com dados padrão.")
                return default_data
    else:
        # Se o arquivo não existir, cria com dados padrão
        with open(file_path, 'w') as file:
            json.dump(default_data, file, indent=4)
        return default_data

# Função principal
def main():
    # Criar o diretório /Sat-lite se não existir
    sat_lite_dir = '/Sat-lite'
    if not os.path.exists(sat_lite_dir):
        os.makedirs(sat_lite_dir)

    # Caminhos para os arquivos JSON
    config_file_path = os.path.join(sat_lite_dir, 'configure.json')
    cookies_file_path = os.path.join(sat_lite_dir, 'cookies.json')
    data_file_path = os.path.join(sat_lite_dir, 'data.json')

    # Dados padrão para os arquivos
    default_config_data = {
        "websites": [
            'https://github.com/RAFAEL849412/Sat-lite', 
            'https://github.com/Eitol/starlink-client'
        ]
    }
    default_cookies_data = []
    default_data_data = {"emails": [], "links": []}

    # Carregar arquivos JSON ou criar novos com dados padrão
    config_data = load_or_create_json(config_file_path, default_config_data)
    cookies_data = load_or_create_json(cookies_file_path, default_cookies_data)
    data_data = load_or_create_json(data_file_path, default_data_data)

    # Listas para armazenar dados coletados
    all_emails = data_data["emails"]
    all_links = data_data["links"]

    # Rastrear cada website
    for website in config_data["websites"]:
        print(f"Rastreando: {website}")
        emails, links = scrape_page(website)
        all_emails.extend(emails)
        all_links.extend(links)

    # Remover duplicatas
    all_emails = list(set(all_emails))
    all_links = list(set(all_links))

    # Salvar dados coletados no arquivo data.json
    data_data["emails"] = all_emails
    data_data["links"] = all_links

    with open(data_file_path, 'w') as data_file:
        json.dump(data_data, data_file, indent=4)

    print(f"Dados coletados e salvos em {data_file_path}")

    # Salvar cookies em cookies.json
    with open(cookies_file_path, 'w') as cookies_file:
        json.dump(cookies_data, cookies_file, indent=4)

if __name__ == '__main__':
    main()
    
