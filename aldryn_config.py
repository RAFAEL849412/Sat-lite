import requests
import re
import sys

# Função para verificar se a URL é válida
def url_checker(url):
    regex = re.compile(
        r'^(http|https)://'  # Deve começar com http ou https
        r'([a-zA-Z0-9.-]+)'  # Nome do domínio
        r'(:[0-9]{1,5})?'    # Porta (opcional)
        r'(/.*)?$',          # Caminho (opcional)
        re.IGNORECASE
    )
    if not re.match(regex, url):
        raise ValueError("URL inválida. Por favor, insira uma URL válida começando com http ou https.")

# Função para encurtar a URL usando o serviço is.gd
def shorten_url(url):
    api_url = f"https://is.gd/create.php?format=simple&url={url}"
    try:
        response = requests.get(api_url, timeout=10)  # Adicionado timeout para evitar travamentos
        response.raise_for_status()  # Levanta exceções para respostas HTTP de erro
        if response.text.startswith("Error:"):
            raise ValueError("Erro ao encurtar a URL. Verifique o formato da URL.")
        return response.text
    except requests.RequestException as e:
        raise ConnectionError(f"Erro ao conectar ao serviço de encurtamento: {e}")

# Função principal do script
def main():
    print("### Verificador e Encurtador de URL ###\n")
    try:
        # Solicita ao usuário a URL para verificar
        phish_url = input("Cole a URL (com http ou https): ").strip()
        url_checker(phish_url)  # Verifica a URL

        # Encurta a URL
        print("Processando e modificando a URL...")
        short_url = shorten_url(phish_url)

        print(f"Aqui está a URL encurtada: {short_url}")
    except ValueError as ve:
        print(f"[Erro] {ve}")
    except ConnectionError as ce:
        print(f"[Erro] {ce}")
    except Exception as e:
        print(f"[Erro inesperado] {e}")
        sys.exit(1)  # Encerra o programa com código de erro

if __name__ == "__main__":
    main()
