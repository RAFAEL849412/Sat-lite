import os
import subprocess

def check_proxy():
    """Verifica se o proxy está ativado e desativa, se necessário."""
    try:
        # Verifica as configurações de proxy do ambiente
        proxy = os.environ.get('http_proxy') or os.environ.get('https_proxy')
        if proxy:
            print(f"Proxy ativado: {proxy}")
            # Desativando o proxy (removendo variáveis de ambiente)
            os.environ.pop('http_proxy', None)
            os.environ.pop('https_proxy', None)
            print("Proxy desativado.")
        else:
            print("Nenhum proxy ativado.")
    except Exception as e:
        print(f"Erro ao verificar/desativar o proxy: {e}")

def check_process(process_names):
    """Verifica se processos específicos estão em execução no Ubuntu."""
    for process in process_names:
        try:
            result = subprocess.run(['pgrep', '-x', process], stdout=subprocess.PIPE, text=True)
            if result.stdout:
                print(f"Processo '{process}' está em execução.")
            else:
                print(f"Processo '{process}' não encontrado.")
        except Exception as e:
            print(f"Erro ao verificar processo {process}: {e}")

def check_service(service_names):
    """Verifica o status de serviços específicos no Ubuntu usando systemctl."""
    for service in service_names:
        try:
            result = subprocess.run(['systemctl', 'is-active', service], stdout=subprocess.PIPE, text=True)
            status = result.stdout.strip()
            if status == "active":
                print(f"Serviço '{service}' está ativo.")
            else:
                print(f"Serviço '{service}' não está ativo.")
        except Exception as e:
            print(f"Erro ao verificar serviço {service}: {e}")

def main():
    """Função principal que chama as verificações."""
    processes_to_check = ['firefox', 'chrome']  # Altere conforme necessário
    services_to_check = ['ssh', 'network-manager']  # Altere conforme necessário

    check_proxy()
    check_process(processes_to_check)
    check_service(services_to_check)

if __name__ == "__main__":
    main()
