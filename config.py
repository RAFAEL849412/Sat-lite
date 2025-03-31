import subprocess
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configuração do log
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Função para instalar o módulo watchdog
def install_watchdog():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "watchdog"])

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ImportError:
    logging.info("Módulo watchdog não encontrado. Instalando...")
    install_watchdog()
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler

# Classe Satellite
class Satellite:
    def __init__(self, name, altitude, status="active"):
        self.name = name
        self.altitude = altitude
        self.status = status
        self.robot_control = None

    def configure_robot(self, robot_type, configuration_params):
        logging.info(f"Configurando robô no satélite {self.name} com tipo {robot_type}.")
        self.robot_control = Robot(robot_type, configuration_params)

    def update(self, altitude=None, status=None, robot_type=None, new_config=None):
        if altitude is not None:
            self.altitude = altitude
            logging.info(f"A altitude do satélite {self.name} foi atualizada para {altitude} km.")

        if status is not None:
            self.status = status
            logging.info(f"Status do satélite {self.name} foi atualizado para {status}.")

        if robot_type:
            if self.robot_control:
                self.robot_control.update(robot_type, new_config)
                logging.info(f"Robô encontrado no satélite {self.name}. Atualização realizada.")
            else:
                logging.warning(f"Robô não encontrado no satélite {self.name}. Configuração de robô não realizada.")

    def get_info(self):
        info = {
            "satellite_name": self.name,
            "altitude": self.altitude,
            "status": self.status
        }
        if self.robot_control:
            info["robot"] = self.robot_control.get_info()
        else:
            info["robot"] = "Robô não encontrado no satélite."
        return info

# Classe Robot
class Robot:
    def __init__(self, robot_type, configuration_params):
        self.robot_type = robot_type
        self.configuration_params = configuration_params

    def update(self, robot_type, new_config):
        self.robot_type = robot_type
        if new_config:
            self.configuration_params.update(new_config)
        logging.info(f"Robô atualizado para o tipo {robot_type} com novas configurações: {self.configuration_params}")

    def get_info(self):
        return {
            "robot_type": self.robot_type,
            "configuration_params": self.configuration_params
        }

# Função para configurar e atualizar o satélite programaticamente
def configure_and_update_satellite():
    logging.info("Iniciando configuração e atualização do satélite e robô...")
    satellite = Satellite(name="Satélite 1", altitude=500, status="active")

    logging.info("Tentando configurar o robô...")
    satellite.configure_robot("Explorador", {"velocidade": 100, "energia": 80})

    logging.info("\nAtualizando configurações...")
    satellite.update(altitude=600, status="inactive", robot_type="Comunicador", new_config={"velocidade": 120, "energia": 90})

    logging.info("\nConfiguração atualizada:")
    info = satellite.get_info()
    for key, value in info.items():
        logging.info(f"{key}: {value}")

# Classe de observador para o watchdog
class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".txt"):  # Exemplo: Monitorando arquivos .txt
            logging.info(f"Arquivo modificado: {event.src_path}")
            configure_and_update_satellite()

# Função principal
def main():
    # Configura o diretório a ser monitorado
    path = "./"  # Diretorio corrente ou outro caminho que você deseje monitorar

    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)

    logging.info(f"Iniciando monitoramento de alterações no diretório: {path}")
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        logging.info("Monitoramento interrompido.")
    
    observer.join()

# Chama a função principal para iniciar o monitoramento
if __name__ == "__main__":
    main()
        
