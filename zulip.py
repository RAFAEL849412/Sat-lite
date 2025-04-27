import os
import json
import requests
import subprocess
import sys
from datetime import datetime

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    from bs4 import BeautifulSoup
except ImportError:
    install('beautifulsoup4')
    from bs4 import BeautifulSoup

def scrape_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        emails = {mailto_link['href'].replace('mailto:', '') for mailto_link in soup.find_all('a', href=True) if 'mailto:' in mailto_link['href']}
        links = {link['href'] for link in soup.find_all('a', href=True)}
        
        return list(emails), list(links)
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")
        return [], []

def load_or_create_json(file_path, default_data):
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                if not isinstance(data, dict):
                    raise ValueError("Formato inválido")
        except (json.JSONDecodeError, ValueError):
            print(f"Erro ao ler {file_path}, recriando com dados padrão.")
            data = default_data
    else:
        data = default_data
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    return data

def main():
    sat_lite_dir = '/Sat-lite'
    os.makedirs(sat_lite_dir, exist_ok=True)

    config_file_path = os.path.join(sat_lite_dir, 'configure.json')
    cookies_file_path = os.path.join(sat_lite_dir, 'cookies.json')
    data_file_path = os.path.join(sat_lite_dir, 'data.json')
    status_file_path = os.path.join(sat_lite_dir, 'satellite_status.json')

    default_config_data = {"websites": [
        'https://github.com/RAFAEL849412/Sat-lite',
        'https://github.com/Eitol/starlink-client'
    ]}
    default_cookies_data = []
    default_data_data = {"emails": [], "links": []}
    default_status_data = {"status": "active", "last_update": None}

    config_data = load_or_create_json(config_file_path, default_config_data)
    cookies_data = load_or_create_json(cookies_file_path, default_cookies_data)
    data_data = load_or_create_json(data_file_path, default_data_data)
    status_data = load_or_create_json(status_file_path, default_status_data)

    data_data.setdefault("emails", [])
    data_data.setdefault("links", [])
    
    all_emails, all_links = set(data_data["emails"]), set(data_data["links"])

    for website in config_data.get("websites", []):
        print(f"Rastreando: {website}")
        emails, links = scrape_page(website)
        all_emails.update(emails)
        all_links.update(links)

    data_data["emails"] = list(all_emails)
    data_data["links"] = list(all_links)

    with open(data_file_path, 'w') as data_file:
        json.dump(data_data, data_file, indent=4)

    print(f"Dados coletados e salvos em {data_file_path}")

    with open(cookies_file_path, 'w') as cookies_file:
        json.dump(cookies_data, cookies_file, indent=4)

    # Atualizar status
    status_data["last_update"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(status_file_path, 'w') as status_file:
        json.dump(status_data, status_file, indent=4)
    print(f"Status atualizado e salvo em {status_file_path}")

if __name__ == '__main__':
    main()
