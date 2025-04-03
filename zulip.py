import subprocess
import sys
import os
import json
import requests
from bs4 import BeautifulSoup

# Verificar e instalar as dependências, caso não estejam instaladas
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Instalar BeautifulSoup4 e Requests se não estiverem instalados
try:
    import requests
except ImportError:
    print("Instalando requests...")
    install('requests')

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Instalando beautifulsoup4...")
    install('beautifulsoup4')

# Criar o diretório /Sat-lite se não existir
sat_lite_dir = '/Sat-lite'
if not os.path.exists(sat_lite_dir):
    os.makedirs(sat_lite_dir)

# Caminhos para os arquivos
config_file_path = os.path.join(sat_lite_dir, 'configure.json')
cookies_file_path = os.path.join(sat_lite_dir, 'cookies.json')
data_file_path = os.path.join(sat_lite_dir, 'data.json')

# Verificar se o arquivo configure.json existe, se não, usar uma configuração padrão
if os.path.exists(config_file_path):
    with open(config_file_path, 'r') as config_file:
        config_data = json.load(config_file)
    print("O arquivo configure.json foi encontrado.")
else:
    config_data = {"websites": []}  # Usar lista vazia de websites como padrão

# Verificar se o arquivo cookies.json existe, caso contrário, criar um vazio
if not os.path.exists(cookies_file_path):
    with open(cookies_file_path, 'w') as cookies_file:
        json.dump([], cookies_file)

# Carregar cookies de cookies.json
with open(cookies_file_path, 'r') as cookies_file:
    cookies = json.load(cookies_file)

# Verificar se o arquivo data.json existe, caso contrário, criar um vazio
if not os.path.exists(data_file_path):
    with open(data_file_path, 'w') as data_file:
        json.dump({"emails": [], "domains": []}, data_file)

# Carregar dados de data.json
with open(data_file_path, 'r') as data_file:
    data = json.load(data_file)

# Listas para armazenar dados
robotstxt_allowed = []  # Regras permitidas do robots.txt
robotstxt_disallowed = []  # Regras bloqueadas do robots.txt
collected_pages = []  # Páginas que o crawler irá acessar
collected_domains = []  # Domínios encontrados

# Função para verificar o arquivo robots.txt
def robots_txt(domain_name):
    try:
        address_of_robots_text = 'http://' + domain_name + '/robots.txt'
        req_ = requests.head(address_of_robots_text)
        if req_.status_code < 400:
            scrapped_txt = requests.get(address_of_robots_text, stream=True, timeout=0.5)
            rob_txt = []
            all_lines = scrapped_txt.iter_lines()
            for iline in all_lines:
                rob_txt.append(iline)
            for line in rob_txt:
                if b'Disallow:' in line:
                    line = str(line)
                    robotstxt_disallowed.append(line.split(': ')[1].split(' ')[0])
                elif b'Allow:' in line:
                    line = str(line)
                    robotstxt_allowed.append(line.split(': ')[1].split(' ')[0])
    except requests.exceptions.RequestException as e:
        print(e)

# Carregar URLs do arquivo de configuração (caso existam)
website_addresses = config_data.get("websites", [])

# Verificar as URLs listadas no arquivo de configuração
if len(website_addresses) > 0:
    for nm in website_addresses:
        domain_name = nm.split('//')[-1].split('/')[0]  # Extrair nome do domínio
        robots_txt(domain_name)  # Chamar função para verificar robots.txt
        if len(robotstxt_disallowed) < 1:  # Se não houver restrições
            collected_pages.append(nm)
        else:
            for eachline in robotstxt_disallowed:
                if not eachline in nm and not nm in collected_pages:
                    collected_pages.append(nm)

# Coletar e-mails e links de páginas coletadas
all_email_addresses = data["emails"]
all_domains = data["domains"]
for sub_page in collected_pages:
    try:
        print(f"Acessando página: {sub_page}")
        page = requests.get(sub_page, timeout=0.5, stream=False)
        soup = BeautifulSoup(page.text, 'html.parser')

        # Coletar e-mails encontrados na página
        email_soup = soup.select('a[href^="mailto"]')
        for email_address in email_soup:
            email_address = email_address.text
            print(f"E-mail encontrado: {email_address}")  # Exibir e-mail encontrado
            if email_address not in all_email_addresses:
                all_email_addresses.append(email_address)

        # Coletar links encontrados na página
        scrapped_links = soup.find_all('a', href=True)
        for a in scrapped_links:
            if domain_name not in a['href'] and 'http' in a['href']:
                r_domain = a['href'].split('//')[-1].split('/')[0]  # Extrair domínio do link
                if r_domain not in all_domains:
                    print(f"Domínio encontrado: {r_domain}")  # Exibir domínio encontrado
                    all_domains.append(r_domain)

        # Salvar os dados coletados (e-mails e domínios) no arquivo data.json
        data["emails"] = all_email_addresses
        data["domains"] = all_domains
        with open(data_file_path, 'w') as data_file:
            json.dump(data, data_file)

        # Salvar cookies (se necessário) em cookies.json
        with open(cookies_file_path, 'w') as cookies_file:
            json.dump(cookies, cookies_file)

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a página {sub_page}: {e}")
