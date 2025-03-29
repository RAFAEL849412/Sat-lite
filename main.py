import requests
from skyfield.api import load, wgs84
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pytz

def download_tle_data(url, filename="satellites.tle"):
    """Baixa dados TLE dos satélites e salva em um arquivo."""
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'w') as file:
            file.write(response.text)
        print("Dados TLE baixados com sucesso.")
    else:
        print("Falha ao baixar dados TLE. Código de status: {}".format(response.status_code))

def main():
    # URL para baixar dados TLE dos satélites Starlink
    tle_url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=tle"

    # Baixar os dados TLE
    download_tle_data(tle_url)

    # Carregar dados TLE usando Skyfield
    satellites = load.tle_file("satellites.tle")

    # Definir a localização do observador (São Francisco, CA)
    observer_location = wgs84.latlon(37.7749, -122.4194)

    # Criar objeto de tempo com fuso horário UTC
    ts = load.timescale()
    start_time = ts.utc(datetime.now(pytz.utc))  # Tempo UTC

    # Selecionar um satélite (o primeiro da lista)
    if not satellites:
        print("Nenhum satélite encontrado no arquivo TLE.")
        return
    sat = satellites[0]

    # Listas para armazenar dados de altitude, azimute e tempo
    altitudes, azimuths, times = [], [], []

    # Loop para calcular a posição do satélite ao longo de 60 segundos
    for i in range(60):  # Para cada segundo
        t = ts.utc(start_time.utc_datetime() + timedelta(seconds=i))  # Avançar o tempo
        difference = sat - observer_location
        topocentric = difference.at(t)  # Posição em relação ao observador
        alt, az, _ = topocentric.altaz()  # Altitude e azimute

        altitudes.append(alt.degrees)
        azimuths.append(az.degrees)
        times.append((start_time.utc_datetime() + timedelta(seconds=i)).strftime('%H:%M:%S'))

    # Criar gráficos
    plt.figure(figsize=(10, 5))

    # Gráfico de Altitude
    plt.subplot(2, 1, 1)
    plt.plot(times, altitudes, label="Altitude (graus)")
    plt.title("Rastreamento do Satélite: {}".format(sat.name))
    plt.xlabel("Tempo (HH:MM:SS)")
    plt.ylabel("Altitude (graus)")
    plt.xticks(rotation=45, fontsize=8)
    plt.grid()
    plt.legend()

    # Gráfico de Azimute
    plt.subplot(2, 1, 2)
    plt.plot(times, azimuths, label="Azimute (graus)", color="orange")
    plt.xlabel("Tempo (HH:MM:SS)")
    plt.ylabel("Azimute (graus)")
    plt.xticks(rotation=45, fontsize=8)
    plt.grid()
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
