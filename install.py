import subprocess
import sys

def checar_se_root():
    """Verifica se o script está sendo executado como root."""
    if not (sys.platform.startswith('linux') and subprocess.getuid() == 0):
        print("Erro: Este script deve ser executado como root ou com sudo.")
        sys.exit(1)

def verificar_pacote_instalado(pacote):
    """Verifica se o pacote está instalado."""
    try:
        subprocess.run(["command", "-v", pacote], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"O pacote {pacote} já está instalado.")
    except subprocess.CalledProcessError:
        print(f"O pacote {pacote} não está instalado.")
        return False
    return True

def instalar_pacote(pacote):
    """Instala o pacote se não estiver instalado."""
    try:
        print(f"Instalando o pacote {pacote}...")
        subprocess.run(["apt", "update"], check=True)
        subprocess.run(["apt", "install", "-y", pacote], check=True)
        print(f"O pacote {pacote} foi instalado com sucesso.")
    except subprocess.CalledProcessError:
        print(f"Erro ao instalar o pacote {pacote}.")
        sys.exit(1)

def main():
    print("Olá! Verificando requisitos para instalação...")
    
    # Verifica se o script está sendo executado como root
    checar_se_root()
    
    # Nome do pacote a ser instalado
    pacote = "curl"

    # Verifica se o pacote está instalado e, se necessário, instala
    if not verificar_pacote_instalado(pacote):
        instalar_pacote(pacote)

    print("Verificação concluída. O cliente está pronto para uso!")

if __name__ == "__main__":
    main()
