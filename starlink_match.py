import requests
import matplotlib.pyplot as plt
import numpy as np
from skyfield.api import Topos, load
import os

# Função para baixar os dados TLE
def download_tle():
    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=tle"
    try:
        response = requests.get(url)
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
    return Topos(latitude_degrees=40.7128, longitude_degrees=-74.0060)

# Função para plotar a posição do satélite
def plot_satellite_position(azimuth, altitude):
    # Geração do gráfico polar para a posição do satélite
    plt.figure(figsize=(6, 6))
    plt.polar(np.radians(azimuth), 90 - altitude, marker='o')
    plt.title('Posição do Satélite')
    plt.show()

def main():
    # Baixar dados TLE, se necessário
    if not os.path.exists('starlink.tle'):
        download_tle()

    # Carregar os dados TLE
    satellites = load.tle_file('starlink.tle')

    # Obter a localização do observador
    observer_location = get_location()

    # Obter o objeto de timescale do SkyField
    ts = load.timescale()

    # Obter a hora atual
    t = ts.now()

    # Iterar sobre os satélites e calcular suas posições
    for satellite in satellites:
        difference = satellite - observer_location
        topocentric = difference.at(t)

        # Obter altitude, azimute e distância
        alt, az, distance = topocentric.altaz()

        # Verificar se o satélite está visível (altitude > 40 graus)
        if alt.degrees > 40:
            print(f"{satellite.name} - Altitude: {alt.degrees:.2f}°, Azimute: {az.degrees:.2f}°")
            
            # Plotar a posição do satélite
            plot_satellite_position(az.degrees, alt.degrees)

if __name__ == "__main__":
    main()

