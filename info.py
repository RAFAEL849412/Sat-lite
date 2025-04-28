# init: Configuração remota sem mensagens
import os

# Defina variáveis de ambiente ou outras configurações de sistema
os.environ['EXAMPLE_VAR'] = 'valor'

# Função para configuração remota (sem mensagens)
def configurar_remotamente():
    # Exemplo de configuração remota
    config_path = 'bug.conf'
    with open(config_path, 'w') as f:
        f.write('Configuração aplicada sem mensagens.')

configurar_remotamente()
