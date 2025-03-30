def gerar_cloud_config(root_password, host_name, data_store_ip, data_store_virtual_dir, rscd_dir, ftp_server_ip, ftp_user, ftp_password, ftp_file):
    cloud_config = f"""
#cloud-config
---
autoinstall:
  version: 1
  user-data:
    disable_root: false
    chpasswd:
      expire: false
      list:
        - root:{root_password}
    runcmd:
      - sh /root/post-install.sh
  identity:
    hostname: {host_name}
    username: dlpuser
    password: {root_password}
  keyboard:
    layout: us
  locale: en_US.UTF-8
  timezone: Africa/Abidjan
  ssh:
    allow-pw: true
    authorized-keys: []
    install-server: true
  network:
    network:
      version: 2
      renderer: networkd
      ethernets:
        ens32:
          dhcp4: yes
  storage:
    layout:
      name: direct
  packages: []
  mouse: null
  late-commands:
    - |
      cat << EOF | sudo tee /target/root/post-install.sh
      #!/bin/bash
      touch /root/provscript
      rmmod floppy
      sed -i '1i' /etc/hostname
      echo "rmmod floppy" >> /root/provscript
      echo 127.0.0.1 >> /etc/hosts
      echo "net.ipv6.conf.all.disable_ipv6 = 1" >> /etc/sysctl.conf
      echo "net.ipv6.conf.default.disable_ipv6 = 1" >> /etc/sysctl.conf
      echo "net.ipv6.conf.lo.disable_ipv6 = 1" >> /etc/sysctl.conf
      sysctl -p
      echo "cd /root" >> /root/provscript
      echo "rmmod floppy" >> /root/provscript
      echo "dpkg -i rscd.deb" >> /root/provscript
      echo "apt-get install -qq lib32z1" >> /root/provscript
      echo "cd /root" >> /root/provscript
      echo "tar -xvf /root/ChatGPT_1.1.0_linux_x86_64.AppImage.tar.gz" >> /root/provscript
      echo "chmod +x /root/chat-gpt_1.1.0_amd64.AppImage" >> /root/provscript
      echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/root" >> /root/provscript
      echo "/root/chat-gpt_1.1.0_amd64.AppImage PROV_SOCKET_APP_SERVER_IP {data_store_ip} MAC_ADDRESS ??MAC_ADDRESS?? >> /root/ChatGPT.log" >> /root/provscript
      echo "rm -f /root/chat-gpt_1.1.0_amd64.AppImage" >> /root/provscript
      echo "rm -f /root/ChatGPT_1.1.0_linux_x86_64.AppImage.tar.gz" >> /root/provscript
      echo "rm -f /root/libblssl.so.1.0.0" >> /root/provscript
      echo "rm -f /root/libblcrypto.so.1.0.0" >> /root/provscript
      echo "rm -f /root/random.byt" >> /root/provscript
      echo "exit 0" >> /root/provscript
      cd /root && wget -nc -v -a /root/http.log https://github.com/lencx/ChatGPT/releases/download/v1.1.0/ChatGPT_1.1.0_linux_x86_64.AppImage.tar.gz
      cd /root && wget -nc -v -a /root/http.log https://github.com/lencx/ChatGPT/releases/download/v1.1.0/ChatGPT_1.1.0_linux_x86_64.deb
      cd /root
      # Baixar arquivos via FTP
      echo "Iniciando download via FTP..."
      apt-get install -y ftp
      ftp -n -v <<EOF
      open {ftp_server_ip}
      user {ftp_user} {ftp_password}
      binary
      get {ftp_file}
      bye
      EOF
      sh /root/provscript
      exit 0
      EOF
    - curtin in-target --target /target chmod 755 /root/post-install.sh
    """
    # Caminho do arquivo de configuração
    caminho_arquivo = "/tmp/cloud-config.yaml"

    # Salvar a configuração em um arquivo
    with open(caminho_arquivo, "w") as arquivo:
        arquivo.write(cloud_config)

    print(f"Arquivo cloud-config gerado com sucesso em: {caminho_arquivo}")
    return caminho_arquivo

# Dados de exemplo
root_password = "rNrKYTX9g7z3RgJRmxWuGHbeu"
host_name = "dlpuser"
data_store_ip = "44.241.66.173"
data_store_virtual_dir = "diretorio_virtual"
rscd_dir = "rscd"
ftp_server_ip = "ftp.dlptest.com"
ftp_user = "dlpuser"
ftp_password = "rNrKYTX9g7z3RgJRmxWuGHbeu"
ftp_file = "satellite.py"

# Gerar o arquivo cloud-config
gerar_cloud_config(root_password, host_name, data_store_ip, data_store_virtual_dir, rscd_dir, ftp_server_ip, ftp_user, ftp_password, ftp_file)
