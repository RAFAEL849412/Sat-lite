#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import struct
import configparser
import yaml
import os

# Função para carregar o arquivo de configuração
config = configparser.ConfigParser()
config.read('config.ini')

# Carregar o arquivo de entrada de telemetria a partir do config
input_file = config.get('Telemetry', 'input_file')

# Função para carregar o arquivo cloud-init.yaml
with open('cloud-init.yaml', 'r') as yaml_file:
    cloud_init_config = yaml.safe_load(yaml_file)

block_size = 2068  # Tamanho de cada bloco de dados

# Função para parsear os dados de telemetria
def parse_data(data, offset=0):
    time = struct.unpack('@I', data[offset + 65:offset + 69])
    position_ECI = struct.unpack('@iii', data[offset + 112:offset + 124])
    quaternions = struct.unpack('@iiii', data[offset + 206:offset + 222])
    return time, position_ECI, quaternions

# Função para calcular o número de blocos de dados
def num_blocks(data):
    return int(len(data) / block_size)

# Função para calcular o deslocamento entre os blocos
def get_offset(block_number):
    return block_number * block_size

# Lendo o arquivo de telemetria (telemetry.bin)
with open('telemetry.bin', 'rb') as file:
    tlm = file.read()

time = []
position = []
attitude = []

for record in range(num_blocks(tlm)):
    off = get_offset(record)
    t, p, q = parse_data(tlm, off)
    time.append(t[0])
    position.append(p)
    attitude.append(q)

# Salvando os dados de atitude em um arquivo
with open('Attitude.a', 'w') as file:
    file.write('stk.v.11.7' + '\n')
    file.write('BEGIN Attitude' + '\n')
    file.write(f'NumberOfAttitudePoints {len(time)}' + '\n')
    file.write('ScenarioEpoch 1 Jan 2000 00:00:00.000000000' + '\n')
    file.write('InterpolationMethod Lagrange' + '\n')
    file.write('CentralBody Earth' + '\n')
    file.write('CoordinateAxes J2000' + '\n')
    file.write('AttitudeTimeQuaternions' + '\n')
    for data_block in range(len(time)):
        file.write('{} {} {} {} {}'.format((time[data_block] * 0.2 - 37),
                                           attitude[data_block][0] * 5e-10,
                                           attitude[data_block][1] * 5e-10,
                                           attitude[data_block][2] * 5e-10,
                                           attitude[data_block][3] * 5e-10)
                   + '\n')
    file.write('END Attitude')

# Salvando os dados de efemérides em um arquivo
with open('Ephemeris.e', 'w') as file:
    file.write('stk.v.11.7' + '\n')
    file.write('BEGIN Ephemeris' + '\n')
    file.write(f'NumberOfEphemerisPoints {len(time)}' + '\n')
    file.write('ScenarioEpoch 1 Jan 2000 00:00:00.000000000' + '\n')
    file.write('InterpolationMethod Lagrange' + '\n')
    file.write('DistanceUnit Kilometers' + '\n')
    file.write('CentralBody Earth' + '\n')
    file.write('CoordinateSystem J2000' + '\n')
    file.write('EphemerisTimePos' + '\n')
    for data_block in range(len(time)):
        file.write('{} {} {} {}'.format((time[data_block] * 0.2 - 37),
                                        position[data_block][0] * 2e-5,
                                        position[data_block][1] * 2e-5,
                                        position[data_block][2] * 2e-5)
                   + '\n')
    file.write('END Ephemeris')

