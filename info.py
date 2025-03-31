def display_satellite_data(data):
    print("Informações do Satélite:")
    for key, value in data.items():
        print(f"{key}: {value}")

# Função para acessar informações específicas
def get_specific_data(data, keys):
    specific_data = {}
    for key in keys:
        if key in data:
            specific_data[key] = data[key]
    return specific_data

# Dados do satélite STARLINK-1017
satellite_data = {
    "OBJECT_NAME": "STARLINK-1017",
    "OBJECT_ID": "2019-074L",
    "EPOCH": "2025-03-31T12:04:58.880064",
    "MEAN_MOTION": 15.063932749999999,
    "ECCENTRICITY": 0.0001504,
    "INCLINATION": 53.052399999999999,
    "RA_OF_ASC_NODE": 287.23809999999997,
    "ARG_OF_PERICENTER": 91.679299999999998,
    "MEAN_ANOMALY": 268.43680000000001,
    "EPHEMERIS_TYPE": 0,
    "CLASSIFICATION_TYPE": "U",
    "NORAD_CAT_ID": 44723,
    "ELEMENT_SET_NO": 999,
    "REV_AT_EPOCH": 29719,
    "BSTAR": 6.4657000000000001E-5,
    "MEAN_MOTION_DOT": 6.8199999999999999E-6,
    "MEAN_MOTION_DDOT": 0
}

# Exibindo todos os dados
display_satellite_data(satellite_data)

# Acessando informações específicas
specific_keys = ["MEAN_MOTION", "INCLINATION", "EPOCH"]
specific_data = get_specific_data(satellite_data, specific_keys)

print("\nValores Específicos:")
for key, value in specific_data.items():
    print(f"{key}: {value}")
