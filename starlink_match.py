import requests
import matplotlib.pyplot as plt
import numpy as np
import time
import os

# Certifique-se de ter o pacote skyfield instalado
try:
    pass
except ImportError:
    os.system('python3 -m pip install skyfield')

# Verificar se a plataforma é suportada
if os.name != 'posix':
    raise ImportError('this platform is not supported: {}'.format(
        'failed to acquire X connection: Bad display name ""', DisplayNameError('')
    ))

# Verificar se a variável de ambiente DISPLAY está configurada
if 'DISPLAY' not in os.environ:
    os.environ['DISPLAY'] = ':0'
    print("DISPLAY environment variable was not set. Setting DISPLAY to ':0'.")

# Função para baixar os dados TLE
def download_tle():
    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=tle"
    response = requests.get(url)
    
    if response.status_code == 200:
        with open('starlink.tle', 'w') as file:
            file.write(response.text)
    else:
        print(f"Erro ao baixar TLE, código de status: {response.status_code}")

# Função principal
def main():
    # Baixar os dados TLE (caso necessário)
    download_tle()

    # Este código não funcionará sem a biblioteca skyfield
    print("A biblioteca skyfield foi removida. O código precisa ser ajustado para funcionar sem ela.")

if __name__ == "__main__":
    main()
