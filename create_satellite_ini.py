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
# Exemplo de configuração para satellite.ini
[DEFAULT]
setting1 = valor1
setting2 = valor2
"""

# Cria e escreve o conteúdo no arquivo satellite.ini
with open(satellite_ini_path, 'w') as file:
    file.write(satellite_ini_content)

print(f"Arquivo {satellite_ini_path} criado com sucesso!")
