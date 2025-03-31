import requests
import re

# Função para verificar se a URL começa com http ou https
def url_checker(url):
    if not (url.startswith("http://") or url.startswith("https://")):
        print("[!] URL inválida. Por favor, use http ou https.")
        exit(1)

# Função para encurtar a URL usando o serviço is.gd
def shorten_url(url):
    api_url = f"https://is.gd/create.php?format=simple&url={url}"
    response = requests.get(api_url)
    return response.text

# Função principal do script
def main():
    print("### Verificador e Encurtador de URL ###\n")

    # Solicita ao usuário a URL para verificar
    phish_url = input("Cole a URL (com http ou https): ")
    url_checker(phish_url)  # Verifica a URL

    # Encurta a URL
    print("Processando e modificando a URL...")
    short_url = shorten_url(phish_url)

    print(f"Aqui está a URL encurtada: {short_url}")

if __name__ == "__main__":
    main()
