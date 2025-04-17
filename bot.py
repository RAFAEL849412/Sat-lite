import argparse
import json
import os
import sys
from datetime import datetime

# Função para carregar os dados TLE
def load_tle():
    tle_file = "starlink.tle"
    if not os.path.exists(tle_file):
        print(f"Erro: Arquivo {tle_file} não encontrado. Certifique-se de que o arquivo está no diretório correto.", file=sys.stderr)
        sys.exit(1)
    
    try:
        with open(tle_file, "r") as f:
            tle_data = f.readlines()
    except Exception as e:
        print(f"Erro ao abrir o arquivo {tle_file}: {e}", file=sys.stderr)
        sys.exit(1)

    return tle_data

# Função para calcular uma posição simulada do satélite
def calculate_position(latitude, longitude):
    # Validar latitude e longitude
    if not (-90 <= latitude <= 90):
        raise ValueError("A latitude deve estar entre -90 e 90 graus.")
    if not (-180 <= longitude <= 180):
        raise ValueError("A longitude deve estar entre -180 e 180 graus.")
    
    # Simulação de cálculo de posição
    altitude = 45.2  # Exemplo de altitude em graus
    azimuth = 135.4  # Exemplo de azimute em graus

    return altitude, azimuth

# Função para gerar a resposta com a posição calculada
def generate_response(latitude, longitude):
    try:
        altitude, azimuth = calculate_position(latitude, longitude)
    except ValueError as e:
        return {
            "status": "error",
            "message": str(e)
        }
    
    return {
        "status": "success",
        "altitude": altitude,
        "azimuth": azimuth,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

# Função principal
def main():
    parser = argparse.ArgumentParser(description="Calcula a posição de satélites Starlink")
    parser.add_argument('--latitude', type=float, required=True, help="Latitude do observador (entre -90 e 90)")
    parser.add_argument('--longitude', type=float, required=True, help="Longitude do observador (entre -180 e 180)")

    args = parser.parse_args()

    # Gerar resposta com a posição do satélite
    response = generate_response(args.latitude, args.longitude)

    # Imprimir a resposta em formato JSON
    print(json.dumps(response, indent=4))

if __name__ == "__main__":
    main()
