class Satellite:
    def __init__(self, name, altitude, status="active"):
        self.name = name
        self.altitude = altitude
        self.status = status
        self.robot_control = None
    
    def configure_robot(self, robot_type, configuration_params):
        self.robot_control = Robot(robot_type, configuration_params)
        print(f"Robô configurado no satélite {self.name} com tipo {robot_type}.")

    def update(self, altitude=None, status=None, robot_type=None, new_config=None):
        if altitude is not None:
            self.altitude = altitude
            print(f"A altitude do satélite {self.name} foi atualizada para {altitude} km.")
        
        if status is not None:
            self.status = status
            print(f"Status do satélite {self.name} foi atualizado para {status}.")
        
        if robot_type:
            if self.robot_control:
                self.robot_control.update(robot_type, new_config)
                print(f"Robô encontrado no satélite {self.name}. Atualização realizada.")
            else:
                print(f"Robô não encontrado no satélite {self.name}. Configuração de robô não realizada.")
    
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

class Robot:
    def __init__(self, robot_type, configuration_params):
        self.robot_type = robot_type
        self.configuration_params = configuration_params

    def update(self, robot_type, new_config):
        self.robot_type = robot_type
        if new_config:
            self.configuration_params.update(new_config)
        print(f"Robô atualizado para o tipo {robot_type} com novas configurações: {self.configuration_params}")

    def get_info(self):
        return {
            "robot_type": self.robot_type,
            "configuration_params": self.configuration_params
        }

# Função para configurar e atualizar o satélite programaticamente
def configure_and_update_satellite():
    # Configuração inicial do satélite e do robô
    satellite = Satellite(name="Satélite 1", altitude=500, status="active")
    
    # Caso o robô ainda não tenha sido configurado
    print("Tentando configurar o robô...")
    satellite.configure_robot("Explorador", {"velocidade": 100, "energia": 80})

    # Atualização do satélite e do robô
    print("\nAtualizando configurações...")
    satellite.update(altitude=600, status="inactive", robot_type="Comunicador", new_config={"velocidade": 120, "energia": 90})
    
    # Exibindo as configurações após a atualização
    print("\nConfiguração atualizada:")
    info = satellite.get_info()
    for key, value in info.items():
        print(f"{key}: {value}")

# Chama a função de configuração e atualização
configure_and_update_satellite()
