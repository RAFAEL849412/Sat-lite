import requests
import matplotlib.pyplot as plt
import numpy as np
import skyfield
import os

# Função para baixar os dados TLE
def download_tle():
    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=tle"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Levanta um erro para status de falha
        with open('starlink.tle', 'w') as file:
            file.write(response.text)
        print("Dados TLE baixados com sucesso.")
    except requests.RequestException as e:
        print(f"Erro ao baixar os dados TLE: {e}")
        exit(1)  # Encerra o script se o download falhar

# Função para obter a localização do observador
def get_location():
    # Exemplo de localização fixa: Nova Iorque (latitude e longitude)
    return (40.7128, -74.0060)

# Função para plotar a posição do satélite
def plot_satellite_position(azimuth, altitude):
    # Geração do gráfico polar para a posição do satélite
    plt.figure(figsize=(6, 6))
    plt.polar(np.radians(azimuth), 90 - altitude, marker='o')
    plt.title('Posição do Satélite')
    plt.show()
    
    # Fechar a figura para liberar memória
    plt.close()

# Função para calcular a posição do satélite
def calculate_position(tle_data, observer_location):
    # Aqui você pode implementar cálculos básicos baseados nos dados TLE,
    # mas o cálculo real de órbitas precisa de bibliotecas como skyfield ou pyephem.
    # Para fins de demonstração, estamos simulando o comportamento.
    azimuth = 45  # Simulação de azimute
    altitude = 60  # Simulação de altitude
    return azimuth, altitude

def main():
    # Baixar dados TLE, se necessário
    if not os.path.exists('starlink.tle'):
        download_tle()

    # Carregar os dados TLE
    with open('starlink.tle', 'r') as file:
        tle_data = file.readlines()

    # Obter a localização do observador
    observer_location = get_location()

    # Iterar sobre os satélites e calcular suas posições
    for i in range(0, len(tle_data), 3):
        satellite_name = tle_data[i].strip()
        tle_line1 = tle_data[i+1].strip()
        tle_line2 = tle_data[i+2].strip()

        # Calcular a posição do satélite
        azimuth, altitude = calculate_position((satellite_name, tle_line1, tle_line2), observer_location)

        # Exibir a posição do satélite
        print(f"{satellite_name} - Altitude: {altitude:.2f}°, Azimute: {azimuth:.2f}°")
        
        # Plotar a posição do satélite
        plot_satellite_position(azimuth, altitude)

if __name__ == "__main__":
    main()
    
