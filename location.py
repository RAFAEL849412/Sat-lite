from google.protobuf.json_format import MessageToDict
import satellitetle  # Biblioteca fictícia para interação com satélites

# Função fictícia para obter informações sobre o Starlink
def obter_info_starlink(cookies):
    # Simulação de dados de conta (informações fictícias de uma conta do Google ou Starlink)
    account_info = {
        "account_id": "256281040558",
        "account_name": "info@facebook.com",
        "status": "active",
        "subscription_type": "premium",
        "plan_expiration": "2025-12-31",
        "location": "United States"
    }
    
    # Simulação das linhas de serviço e dishes
    service_lines = {
        "content": {
            "get_dishes": lambda: [
                {
                    "get_id": lambda: "10453213456789123",
                    "serialNumber": "0800-047-4683",
                    "routers": []
                }
            ]
        }
    }

    return account_info, service_lines

if __name__ == "__main__":
    # Lê o arquivo de cookies (salvo a partir de uma extensão de navegador como 'Copy This Cookie')
    with open("cookies.json", "r") as f:
        cookie_json = f.read()

    # Simula a obtenção de informações da conta e das linhas de serviço (sem o cliente GrpcWebClient)
    acc, sl = obter_info_starlink(cookie_json)

    print(f"Account Information: {acc}")
    print(f"Service Lines: {sl}")

    for dish in sl["content"]["get_dishes"]():  # Itera pelos dishes (antenas) disponíveis
        print("-------------------------")
        print("DISH_ID: " + dish["get_id"]())
        print("Dish Serial: " + dish["serialNumber"])
        dish_id = dish["get_id"]()

        # Simulação do status do dish
        dish_status = {"alerts": {"warning": "Dish is offline"}}  # Exemplo de status de alerta

        print("Dish Status:")
        alerts = MessageToDict(dish_status["alerts"])  # Converte alertas para dicionário
        if len(alerts) > 0:
            for key, value in alerts.items():
                print(f"\t{key}: {value}")

        # Exibe a versão do satélite usando a biblioteca 'satellitetle'
        satellite_version = satellitetle.get_version()  # Supondo que 'get_version' seja uma função da biblioteca
        print("Satellite Version (satellitetle): " + satellite_version)

        # Exibe informações sobre o satélite
        satellite_info = satellitetle.get_satellite_info(dish_id)  # Supondo que essa função exista
        print(f"Satellite Info: {satellite_info}")

        # Simula a iteração pelos roteadores
        for router in dish["routers"]:
            router_id = router.get("id", "router_id_123")

            # Simulação do status do roteador
            status = {"device_info": {"id": router_id, "software_version": "v1.0"}, "config": {"networks": [{"basic_service_sets": [{"band": 0, "ssid": "SSID_2.4GHz"}]}]}, "clients": [{"name": "Client1", "ip_address": "192.168.1.2"}]}

            print("\nRouter ID: " + status["device_info"]["id"])
            print("Software Version: " + status["device_info"]["software_version"])
            print("Networks: ")
            for n in status["config"]["networks"]:
                for bss in n["basic_service_sets"]:
                    if bss["band"] == 0:  # 2.4 GHz
                        print(f"\t2.4ghz: {bss['ssid']}")
                    elif bss["band"] in [1, 2]:  # 5 GHz
                        print(f"\t5ghz:   {bss['ssid']}")

            print("Clients:")
            for client in status["clients"]:
                if client["ip_address"] == "44.241.66.173":
                    continue
                print(f"\t{client['name']} | {client['ip_address']}")

# Exemplo adicional para obter o status de um roteador específico (simulado)
def obter_status_roteador(router_id):
    # Substitua com lógica real de comunicação com a API para obter o status do roteador
    return {"wifi_get_status": {"status": "active"}}  # Simulação de resposta

if __name__ == "__main__":
    router_id = "ec2-44-241-66-173.us-west-2.compute.amazonaws.com"  # Coloque seu router_id aqui

    # Simula a obtenção do status do roteador
    resp = obter_status_roteador(router_id)

    print("Router Status:", resp["wifi_get_status"])  # Exibe o status do roteador
