import requests
import matplotlib.pyplot as plt
import numpy as np
import time
import website # Adicionando a importação do módulo website
def test_w_sp_py_lib(site_url, file_path, username, password):
    from office365.sharepoint.client_context import ClientContext   # , UserCredential
    import tempfile

    ctx = ClientContext(site_url).with_user_credentials(username, password)
    web = ctx.web.get().execute_query()
    print(web.url)

    file = ctx.web.get_file_by_server_relative_path(file_path).get().execute_query()
    print("File size: ", file.length)
    print("File name: ", file.name)
    print("File url: ", file.serverRelativeUrl)

    # download_path = Path(tempfile.mkdtemp()).joinpath(Path(file_path).name)
    # with open(download_path, "wb") as local_file:
    #     file = (
    #         ctx.web.get_file_by_server_relative_url(file_path)
    #         .download(local_file)
    #         .execute_query()
    #     )
    #     print(
    #         f"'{file.server_relative_path}' file has been downloaded into {local_file.name}"
    #     )


# Função para baixar os dados TLE
def download_tle():
    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=tle"
    response = requests.get(url)

    if response.status_code == 200:
        with open('starlink.tle', 'w') as file:
            file.write(response.text)
    else:
        print(f"Erro ao baixar TLE, código de status: {response.status_code}")

# Função para definir a localização fixa do observador (sem usar IP)
def get_location():
    # Exemplo de localização fixa: Nova York (latitude e longitude)
    return Topos(latitude_degrees=40.7128, longitude_degrees=-74.0060)

# Função para configurar o website
def config_website():
    try:
        with open('website-config.py', 'r') as file:
            config = file.read()
            print("Configuração do website carregada com sucesso.")
            print(config)
    except FileNotFoundError:
        print("Arquivo de configuração do website não encontrado.")

# Função principal
def main():
    # Baixar os dados TLE (caso necessário)
    download_tle()

    # Carregar os dados TLE
    satellites = load.tle_file('starlink.tle')

    # Obter a localização do observador
    observer_location = get_location()

    # Obter a escala de tempo
    ts = load.timescale()

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
