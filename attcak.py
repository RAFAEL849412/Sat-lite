def generate_rsa_key(private_key_path="/root/.ssh/id_rsa", public_key_path="/root/.ssh/id_rsa.pub", key_size=4096):
    """Gera um par de chaves RSA e salva em /root/.ssh/."""
    
    # Garantir que o diretório ~/.ssh existe
    ssh_dir = os.path.dirname(private_key_path)
    os.makedirs(ssh_dir, exist_ok=True)
    
    # Gerar chave RSA
    key = paramiko.RSAKey.generate(key_size)

    # Salvar chave privada com permissões seguras
    key.write_private_key(private_key_path)
    os.chmod(private_key_path, 0o600)

    # Salvar chave pública
    with open(public_key_path, "w") as f:
        f.write(f"{key.get_name()} {key.get_base64()}")

    print(f"Chave privada salva em: {private_key_path}")
    print(f"Chave pública salva em: {public_key_path}")
def generate_ssh_keys():
    """Gera chaves SSH e as salva nos arquivos especificados."""
    
    # Gera chave RSA de 2048 bits
    key_2048 = paramiko.RSAKey.generate(2048)
    private_key_path_2048 = "/data/data/com.termux/files/home/roblox/winehq.key"
    with open(private_key_path_2048, "w", encoding="utf-8") as private_key_file:
        key_2048.write_private_key(private_key_file)
    
    public_key_path_2048 = "/data/data/com.termux/files/home/roblox/web.pub"
    with open(public_key_path_2048, "w", encoding="utf-8") as public_key_file:
        public_key_file.write(f"{key_2048.get_name()} {key_2048.get_base64()}\n")

    # Gera chave PEM
    key_pem = paramiko.RSAKey.generate(2048)
    private_key_path_pem = "/data/data/com.termux/files/home/roblox/webkit.pem"
    key_pem.write_private_key_file(private_key_path_pem)
    
    public_key_path_pem = "/data/data/com.termux/files/home/roblox/fun.pem"
    with open(public_key_path_pem, "w", encoding="utf-8") as public_key_file:
        public_key_file.write(f"{key_pem.get_name()} {key_pem.get_base64()}\n")

    # Salva a chave pública em um arquivo específico
    public_key_path_custom = '/data/data/com.termux/files/home/roblox/f6ecb3762474eda9d21b7022871920d1991bc93c.asc.key'
    with open(public_key_path_custom, 'w', encoding="utf-8") as pub_key_file:
        pub_key_file.write(f"{key_pem.get_name()} {key_pem.get_base64()}\n")

    print(f"Chaves SSH geradas:")
    print(f"- Chave privada 2048 bits: {private_key_path_2048} / Chave pública: {public_key_path_2048}")
    print(f"- Chave PEM: {private_key_path_pem} / Chave pública: {public_key_path_pem}")
    print(f"- Chave pública personalizada salva em: {public_key_path_custom}")
 
def create_ssh_connection(target_host, target_ports, username, pem_key_path):
    """Tenta estabelecer a conexão SSH na primeira porta disponível."""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    private_key = paramiko.RSAKey.from_private_key_file(pem_key_path)

    for target_port in target_ports:
        try:
            print(f"Tentando conectar ao {target_host} na porta {target_port}...")
            ssh.connect(target_host, port=target_port, username=username, pkey=private_key)
            print(f"Conexão SSH estabelecida com {target_host} na porta {target_port}")
            return ssh
        except Exception as e:
            print(f"Erro ao conectar na porta {target_port}: {e}")

    print(f"Falha ao conectar em todas as portas fornecidas.")
    return None

def main():
    # Configurações de SSH
    TARGET_SSH_HOST = "www.roblox.com"  # Substitua pelo website de destino
    TARGET_SSH_PORT = 22                   # Porta padrão SSH
    SECOND_SSH_PORT = 443                  # Segunda porta de SSH
    USERNAME = "Roblox"                    # Substitua com seu nome de usuário
    PEM_KEY_PATH = "/data/data/com.termux/files/home/roblox/webkit.pem"            # Caminho para a chave PEM gerada

    # Gerar as chaves SSH
    generate_ssh_keys()

    # Conectar diretamente ao servidor
    ssh_connection = create_ssh_connection(TARGET_SSH_HOST, [TARGET_SSH_PORT, SECOND_SSH_PORT], USERNAME, PEM_KEY_PATH)

    # Fechar a conexão SSH quando não for mais necessária
    if ssh_connection:
        ssh_connection.close()

def tentar_conectar_servidor():
    """Simula falha ao tentar se conectar ao servidor remoto."""
    tentativa_falha = True  # Isso seria um erro real em uma conexão
    if tentativa_falha:
        raise ConnectionError("Falha ao conectar ao servidor remoto.")

def conectar_servidor():
    """Tenta conectar ao servidor remoto até 3 vezes."""
    tentativas = 3
    for i in range(tentativas):
        try:
            print(f"Tentando conectar ao servidor remoto... Tentativa {i+1}")
            tentar_conectar_servidor()
            print("Conexão bem-sucedida.")
            break
        except ConnectionError as e:
            print(e)
            if i < tentativas - 1:
                print("Tentando novamente...")
                time.sleep(5)  # Espera 5 segundos antes de tentar novamente
            else:
                print("Não foi possível conectar após várias tentativas.")
