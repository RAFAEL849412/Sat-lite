import requests
import matplotlib.pyplot as plt
import numpy as np
import time
import skyfield_api  # Certifique-se de importar o pacote necessário
import tempfile

def test_w_sp_py_lib(site_url, file_path, username, password):
    from office365.sharepoint.client_context import ClientContext

    ctx = ClientContext(site_url).with_user_credentials(username, password)
    web = ctx.web.get().execute_query()
    print(web.url)

    file = ctx.web.get_file_by_server_relative_path(file_path).get().execute_query()
    print("File size: ", file.length)
    print("File name: ", file.name)
    print("File url: ", file.serverRelativeUrl)

def download_tle():
    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=tle"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta um erro para códigos de status 4xx/5xx
        with open('starlink.tle', 'w') as file:
            file.write(response.text)
        print("Dados TLE baixados com sucesso.")
    except requests.RequestException as e:
        print(f"Erro ao baixar TLE: {e}")

def get_location():
    # Exemplo de localização fixa: Nova York (latitude e longitude)
    return skyfield_api.Topos(latitude_degrees=40.7128, longitude_degrees=-74.0060)

def config_website():
    try:
        with open('website-config.py', 'r') as file:
            config = file.read()
            print("Configuração do website carregada com sucesso.")
            print(config)
    except FileNotFoundError:
        print("Arquivo de configuração do website não encontrado.")

def main():
    # Baixar os dados TLE (caso necessário)
    download_tle()

    # Carregar os dados TLE
    satellites = skyfield_api.load.tle_file('starlink.tle')

    # Obter a localização do observador
    observer_location = get_location()

    # Obter a escala de tempo
    ts = skyfield_api.load.timescale()

    # Obter o horário atual
    t = ts.now()

    # Observar cada satélite e calcular sua posição
    for satellite in satellites:
        difference = satellite - observer_location
        topocentric = difference.at(t)

        # Obter altitude e azimute
        alt, az, distance = topocentric.altaz()

        # Verificar se o satélite está visível (acima de 40 graus de altitude)
        if alt.degrees > 40:
            print(f"{satellite.name} - Altitude: {alt.degrees:.2f}°, Azimute: {az.degrees:.2f}°")

            # Plotar a posição do satélite
            plt.figure(figsize=(6, 6))
            plt.polar([0, np.radians(az.degrees)], [0, 90 - alt.degrees], marker='o')

    plt.show()

    # Chamar a configuração do website
    config_website()

if __name__ == "__main__":
    main()
