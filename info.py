def display_satellite_data(data):
    """Exibe todas as informações do satélite."""
    print("Informações do Satélite:")
    for key, value in data.items():
        print(f"{key}: {value}")

# Função para acessar informações específicas
def get_specific_data(data, keys):
    """Retorna um dicionário com dados específicos do satélite."""
    return {key: data[key] for key in keys if key in data}

# Dados do satélite STARLINK-1017
satellite_data = {
    "OBJECT_NAME": "STARLINK-1017",
    "OBJECT_ID": "2019-074L",
    "EPOCH": "2025-03-31T12:04:58.880064",
    "MEAN_MOTION": 15.06393275,
    "ECCENTRICITY": 0.0001504,
    "INCLINATION": 53.0524,
    "RA_OF_ASC_NODE": 287.2381,
    "ARG_OF_PERICENTER": 91.6793,
    "MEAN_ANOMALY": 268.4368,
    "EPHEMERIS_TYPE": 0,
    "CLASSIFICATION_TYPE": "U",
    "NORAD_CAT_ID": 44723,
    "ELEMENT_SET_NO": 999,
    "REV_AT_EPOCH": 29719,
    "BSTAR": 6.4657e-5,
    "MEAN_MOTION_DOT": 6.82e-6,
    "MEAN_MOTION_DDOT": 0,
}

# Exibindo todos os dados
display_satellite_data(satellite_data)

# Acessando informações específicas
specific_keys = ["MEAN_MOTION", "INCLINATION", "EPOCH"]
specific_data = get_specific_data(satellite_data, specific_keys)

print("\nValores Específicos:")
for key, value in specific_data.items():
    print(f"{key}: {value}")
