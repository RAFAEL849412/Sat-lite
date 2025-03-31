import matplotlib.pyplot as plt
import numpy as np
import requests
import os
import time

# Função para baixar os dados TLE
def download_tle():
    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=tle"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        with open('starlink.tle', 'w') as file:
            file.write(response.text)
        print("Dados TLE baixados com sucesso.")
    except requests.RequestException as e:
        print(f"Erro ao baixar os dados TLE: {e}")
        exit(1)

# Função para obter a localização do observador
def get_location():
    return (40.7128, -74.0060)

# Função para plotar a posição do satélite
def plot_satellite_position(azimuth, altitude):
    plt.figure(figsize=(6, 6))
    plt.polar(np.radians(azimuth), 90 - altitude, marker='o')
    plt.title('Posição do Satélite')
    plt.show()
    plt.close()

# Função para calcular a posição do satélite (simulada)
def calculate_position(tle_data, observer_location, time_offset):
    azimuth = 45 + time_offset
    altitude = 60
    return azimuth, altitude

def main():
    if not os.path.exists('starlink.tle'):
        download_tle()

    with open('starlink.tle', 'r') as file:
        tle_data = file.readlines()

    observer_location = get_location()

    for i in range(0, len(tle_data), 3):
        satellite_name = tle_data[i].strip()
        tle_line1 = tle_data[i+1].strip()
        tle_line2 = tle_data[i+2].strip()

        for time_offset in range(0, 360, 10):
            azimuth, altitude = calculate_position((satellite_name, tle_line1, tle_line2), observer_location, time_offset)
            print(f"{satellite_name} - Altitude: {altitude:.2f}°, Azimute: {azimuth:.2f}°")
            plot_satellite_position(azimuth, altitude)
            time.sleep(0.5)

if __name__ == "__main__":
    main()
