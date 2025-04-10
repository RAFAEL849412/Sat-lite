import subprocess
import sys
import os
import stat
import logging

# Configuração do log
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Função para instalar o módulo watchdog sem mensagens
def install_watchdog():
    try:
        import watchdog
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "watchdog"])

# Garantir que o watchdog esteja instalado antes de continuar
install_watchdog()

# Agora que o módulo está instalado, podemos importá-lo
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Função para conceder permissões de execução ao arquivo
def conceder_permissoes(file_path):
    if os.path.exists(file_path):
        os.chmod(file_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)

# Classe de observador para o watchdog
class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".txt"):  # Exemplo: Monitorando arquivos .txt
            pass  # Nenhuma mensagem será exibida

# Função principal
def main():
    # Caminho do arquivo que você quer garantir a permissão de execução
    file_path = 'satellite.py'  # Altere para o caminho do seu arquivo

    # Conceder permissões de execução ao arquivo
    conceder_permissoes(file_path)

    # Configura o diretório a ser monitorado
    path = "./"  # Diretório atual

    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)

    observer.start()

    try:
        while True:
            pass  # Mantém o script rodando
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()

# Chama a função principal
if __name__ == "__main__":
    main()
