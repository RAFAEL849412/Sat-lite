import os
import platform
import subprocess
import sys
import json

# Lista de pacotes a serem instalados
PACKAGES = [
    "git", "python3", "python3-pip", "iputils-ping",
    "nmap", "bluez", "aircrack-ng", "dsniff", "psmisc"
]

RAVEN_STORM_REPO = "https://github.com/Taguar258/Raven-Storm.git"
INSTALL_SCRIPT = "install_to_bin.sh"
PROFILE_FILE = "user_profile.json"

def load_profile():
    """Carrega o perfil do usuário de um arquivo JSON."""
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_profile(profile):
    """Salva o perfil do usuário em um arquivo JSON."""
    with open(PROFILE_FILE, "w") as f:
        json.dump(profile, f, indent=4)

def ask_for_profile_info():
    """Solicita informações de perfil do usuário."""
    print("[i] Não foi encontrado perfil. Por favor, forneça algumas informações.")
    name = input("Qual é o seu nome? ")
    preferences = input("Quais são suas preferências para o uso do script? ")
    
    profile = {
        "name": name,
        "preferences": preferences
    }

    save_profile(profile)
    return profile

def run_command(command):
    """Executa um comando no terminal e trata erros."""
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"[!] Falha ao executar: {command}")

def detect_os():
    """Detecta o sistema operacional e retorna o gerenciador de pacotes adequado."""
    system = platform.system().lower()
    if system == "linux":
        if os.path.isfile("/etc/debian_version"):
            return "apt"
        elif os.path.isfile("/etc/arch-release"):
            return "pacman"
        elif os.path.isfile("/etc/fedora-release"):
            return "dnf"
    elif system == "darwin":
        return "brew"
    elif system == "windows":
        return "wsl"
    return None

def install_packages(package_manager):
    """Instala os pacotes necessários usando o gerenciador de pacotes correto."""
    if package_manager == "apt":
        run_command("sudo apt-get update")
        run_command(f"sudo apt-get install -y {' '.join(PACKAGES)}")
    elif package_manager == "pacman":
        run_command(f"sudo pacman --noconfirm -S {' '.join(PACKAGES)}")
    elif package_manager == "dnf":
        run_command(f"sudo dnf install -y {' '.join(PACKAGES)}")
    elif package_manager == "brew":
        run_command(f"brew install {' '.join(PACKAGES)}")
    else:
        print("[!] Sistema não suportado. Instale os pacotes manualmente.")

def install_raven_storm():
    """Baixa e instala o Raven-Storm."""
    if not os.path.exists("Raven-Storm"):
        run_command(f"git clone {RAVEN_STORM_REPO}")
    os.chdir("Raven-Storm")
    run_command("pip3 install -r requirements.txt")
    run_command(f"sudo bash ./{INSTALL_SCRIPT}")

def generate_kickstart_file(profile_name, repo_url, timezone, language='en_US.UTF-8'):
    """Gera um arquivo Kickstart personalizado para automatizar a instalação."""
    ks_template = f"""
# Kickstart Configuração Gerada pelo Script Python

# Linguagem e região
lang {language}
keyboard US
timezone {timezone} --isUtc

# Repositório
url --url={repo_url}

# Instalação de pacotes
%packages
@core
%end

# Configurações de rede
network --bootproto=dhcp --device=eth0 --onboot=yes --ipv6=auto --noipv6

# Configuração de partições
autopart --type=lvm

# Instalação do carregador de inicialização
bootloader --append="rhgb quiet"

# Finalizando
%post
echo "Instalação do sistema operacional completada."
%end
"""
    # Salvar o arquivo Kickstart
    with open(f"profile", 'w') as file:
        file.write(ks_template)
    print(f"Arquivo Kickstart gerado com sucesso: {profile_name}.ks")

def main():
    """Função principal."""
    # Carregar ou pedir o perfil
    profile = load_profile() or ask_for_profile_info()
    print(f"[i] Perfil carregado para {profile['name']}")
    print(f"[i] Preferências: {profile['preferences']}")

    print("[i] Detectando sistema operacional...")
    package_manager = detect_os()

    if not package_manager:
        print("[!] Sistema não suportado. Instale os pacotes manualmente.")
        sys.exit(1)

    print(f"[i] Sistema detectado. Usando {package_manager} para instalação.")
    install_packages(package_manager)
    install_raven_storm()

    # Gerar arquivo Kickstart
    profile_name = profile['name']  # Usando o nome do perfil
    repo_url = "https://buildlogs.centos.org/centos/7/os/x86_64-latest/Packages/"  # Exemplo de repositório
    timezone = "America/Sao_Paulo"  # Exemplo de fuso horário
    generate_kickstart_file(profile_name, repo_url, timezone)

    print("[i] Instalação concluída.")

if __name__ == "__main__":
    main()
