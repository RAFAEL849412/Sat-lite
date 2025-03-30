import os

# Caminho para o diretório .github/workflows
workflow_dir = os.path.join(os.getcwd(), '.github', 'workflows')

# Verifica se o diretório .github/workflows existe, se não, cria o diretório
if not os.path.exists(workflow_dir):
    os.makedirs(workflow_dir)

# Caminho para o arquivo satellite.ini
satellite_ini_path = os.path.join(workflow_dir, 'satellite.ini')

# Conteúdo do arquivo satellite.ini
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
work = /nova/
output = /nova/bin/info

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

# Cria e escreve o conteúdo no arquivo satellite.ini
with open(satellite_ini_path, 'w') as file:
    file.write(satellite_ini_content)

print(f"Arquivo {satellite_ini_path} criado com sucesso!")
