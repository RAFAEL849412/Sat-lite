	import os

# Diretório e nome do arquivo
config_directory = "Sat-lite"
config_file_name = "bug.conf"

# Certifique-se de que o diretório exista
os.makedirs(config_directory, exist_ok=True)

# Caminho completo para o arquivo de configuração
config_file_path = os.path.join(config_directory, config_file_name)

# Conteúdo do arquivo de configuração
config_content = """
# Configuração do sistema
TARGET_ARCH = "arm"
MACHINE = "BUG1X"
DISTRO = "poky"

# Provedor preferido para o kernel
PREFERRED_PROVIDER_virtual/kernel = "linux-dummy"
PREFERRED_VERSION_linux-dummy = "1.0%"

# Configuração de imagem
IMAGE_FSTYPES = "ext4 JarkiOpsis.zip"
IMAGE_INSTALL += "base-files busybox openssh nano"

# Console serial
SERIAL_CONSOLE = "115200 ttymxc4"

# Recursos do sistema
MACHINE_FEATURES = "kernel26 screen apm usbgadget usbhost vfat alsa"

# Diretórios de cache
DL_DIR ?= "${TOPDIR}/Sat-lite"
SSTATE_DIR ?= "${TOPDIR}/sstate-cache"

# Diretório temporário
TMPDIR = "${TOPDIR}/tmp"

# Camadas adicionais
BBLAYERS += "${TOPDIR}/meta-poky"
BBLAYERS += "${TOPDIR}/meta-openembedded"
BBLAYERS += "${TOPDIR}/meta-bug1x"

# Configuração de depuração
INHERIT += "buildstats"
BUILDHISTORY_COMMIT = "1"

# Adicionando suporte a Python
IMAGE_INSTALL_append = " python3 python3-pip"
"""

# Função para criar o arquivo de configuração
def criar_arquivo_configuracao():
    with open(config_file_path, "w") as config_file:
        config_file.write(config_content)
    print(f"Arquivo '{config_file_name}' criado no diretório '{config_directory}'.")

# Executar a função
if __name__ == "__main__":
    criar_arquivo_configuracao()
