#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from datetime import datetime

# Dados a serem salvos
data = [
    {
        "measurement": "spacex.starlink.user_terminal.status",
        "tags": {
            "id": "256281040558",
            "hardware": "V1",
            "software": "1.0"
        },
        "time": datetime.utcnow().isoformat(),
        "fields": {
            "state": "active",
            "uptime": 5000,
            "downlink_mbps": 1.0,
            "uplink_mbps": 0.5,
            "azimuth": 45,
            "elevation": 30
        }
    }
]

satellite_info = {
    "satellite_info": {
        "number_of_records": 100,
        "attitude_data": [
            {
                "time": 1609459200,
                "quaternions": [1, 0, 0, 0]
            },
            {
                "time": 1609459260,
                "quaternions": [0, 1, 0, 0]
            }
        ],
        "position_data": [
            {
                "time": 1609459200,
                "position": [500000, 200000, 300000]
            },
            {
                "time": 1609459260,
                "position": [500100, 200200, 300300]
            }
        ]
    }
}

# Nome do arquivo alterado para satellite_status.json
with open('satellite_status.json', 'w') as f:
    json.dump(data, f, indent=4)
    f.write("\n")  # adiciona nova linha entre os blocos
    json.dump(satellite_info, f, indent=4)

print("Arquivo satellite_status.json criado com sucesso!")
