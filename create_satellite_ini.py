import os

def create_satellite_ini():
    # Caminho absoluto para onde o satellite.ini deve estar
    satellite_ini_path = "/Sat-lite/.github/workflows/satellite.ini"

    # Garante que os diretórios no caminho existam
    os.makedirs(os.path.dirname(satellite_ini_path), exist_ok=True)

    # Verifica se o arquivo já existe
    if not os.path.exists(satellite_ini_path):
        print("Arquivo satellite.ini ausente. Criando agora...")

        # Conteúdo do arquivo
        satellite_ini_content = """
[time]
year = 2023
month = 1
day = 16
delta = 60
window = morning

[observation]
observatory = lasilla
satellite = ALL
lowest_altitude_satellite = 30
sun_zenith_lowest = 100
sun_zenith_highest = 111

[tle]
download = True
name = satellite.py

[directory]
work = /Sat-lite/
output = /Sat-lite/.github/workflows

[file]
simple = observing-details
complete = visible

[configuration]
processes = 12

[ftp_primary]
server = ftp2.osuosl.org
port = 21
username = anonymous
password = ashley
remote_dir = https://ftp2.osuosl.org/pub/almalinux-kitten/almalinux-gpg-keys-latest-10.aarch64.rpm

[ftp_secondary]
server = ftp.osuosl.org
port = 21
username = anonymous
password = ashley
remote_dir = https://ftp.osuosl.org/pub/almalinux/almalinux-gpg-keys-latest-9.aarch64.rpm
"""
        try:
            with open(satellite_ini_path, 'w') as file:
                file.write(satellite_ini_content.strip())
            print(f"Arquivo criado com sucesso: {satellite_ini_path}")
        except Exception as e:
            print(f"Erro ao criar o arquivo: {e}")
    else:
        print("Arquivo satellite.ini já existe.")

# Executa a função
if __name__ == "__main__":
    create_satellite_ini()
