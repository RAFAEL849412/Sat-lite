#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os

# Simula função do protobuf
def MessageToDict(data):
    return dict(data)

# Simula a biblioteca de satélite fictícia
class satellitetle:
    @staticmethod
    def get_version():
        return "Starlink-Sim-v1.2.3"

    @staticmethod
    def get_satellite_info(dish_id):
        return {
            "dish_id": dish_id,
            "model": "Dishy McFlatface",
            "firmware": "G2-2025.01",
            "altitude_km": 550,
            "orbit": "LEO"
        }

# Função para obter informações da conta e dos dishes
def obter_info_starlink(cookies):
    account_info = {
        "account_id": "256281040558",
        "account_name": "info@facebook.com",
        "status": "active",
        "subscription_type": "premium",
        "plan_expiration": "2025-12-31",
        "location": "United States"
    }

    service_lines = {
        "content": {
            "get_dishes": lambda: [
                {
                    "get_id": lambda: "10453213456789123",
                    "serialNumber": "0800-047-4683",
                    "routers": [{"id": "8.8.8.8"}]
                }
            ]
        }
    }

    return account_info, service_lines

# Simulação de status de roteador
def obter_status_roteador(router_id):
    return {
        "wifi_get_status": {
            "status": "active"
        }
    }

if __name__ == "__main__":
    # Lê cookies simulados
    if os.path.exists("cookie.json"):
        with open("cookie.json", "r") as f:
            cookie_json = f.read()
    else:
        cookie_json = "{}"  # fallback

    # Obtém informações simuladas
    acc, sl = obter_info_starlink(cookie_json)

    print(f"\n[INFO] Conta:")
    print(json.dumps(acc, indent=4))

    for dish in sl["content"]["get_dishes"]():
        print("\n[INFO] Antena:")
        print(f"  DISH_ID     : {dish['get_id']()}")
        print(f"  Serial      : {dish['serialNumber']}")

        dish_status = {"alerts": {"warning": "Dish is offline"}}
        alerts = MessageToDict(dish_status["alerts"])

        print("  Alertas:")
        for key, value in alerts.items():
            print(f"    - {key.upper()}: {value}")

        print("  Satélite:")
        print(f"    Versão        : {satellitetle.get_version()}")
        print(f"    Info          : {satellitetle.get_satellite_info(dish['get_id']())}")

        for router in dish["routers"]:
            status = {
                "device_info": {
                    "id": router.get("id", "router_id_123"),
                    "software_version": "v1.0"
                },
                "config": {
                    "networks": [
                        {
                            "basic_service_sets": [
                                {"band": 0, "ssid": "SSID_2.4GHz"},
                                {"band": 1, "ssid": "SSID_5GHz"}
                            ]
                        }
                    ]
                },
                "clients": [
                    {"name": "Client1", "ip_address": "192.168.1.2"},
                    {"name": "Client2", "ip_address": "192.168.1.3"}
                ]
            }

            print("\n  [ROTEADOR]")
            print(f"    ID       : {status['device_info']['id']}")
            print(f"    Versão   : {status['device_info']['software_version']}")
            print("    Redes:")
            for n in status["config"]["networks"]:
                for bss in n["basic_service_sets"]:
                    banda = "2.4GHz" if bss["band"] == 0 else "5GHz"
                    print(f"      - {banda}: {bss['ssid']}")

            print("    Clientes:")
            for client in status["clients"]:
                print(f"      - {client['name']} | {client['ip_address']}")

    # Status de um roteador específico
    print("\n[CHECK] Status do Roteador Externo:")
    router_id = "ec2-44-241-66-173.us-west-2.compute.amazonaws.com"
    print(f"  {router_id} => {obter_status_roteador(router_id)['wifi_get_status']}")
