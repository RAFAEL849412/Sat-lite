#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import os

def gerar_cloud_init():
    cloud_init = """#cloud-config
autoinstall:
    version: 1
    early-commands:
        - sudo systemctl stop ssh
    locale: de_DE
    keyboard:
        layout: de
    ssh:
        install-server: yes
        allow-pw: yes
    storage:
        layout:
            name: direct
    apt:
        primary:
            - arches: [i386, amd64]
              uri: "http://de.archive.ubuntu.com/ubuntu/"
    packages:
        - open-vm-tools
    user-data:
        package_update: false
        package_upgrade: false
        package_reboot_if_required: false
        disable_root: false
        timezone: Europe/Berlin
        users:
        - default
        - name: ansible
          passwd: $6$rounds=4096$N2CzjWelQcBt48$nNyIeaoGQTUEvUj2mba8d7t1oO2g1pmuAHMwdqwOEB61dwLgN8W.FPsu79R2FeMuBjc2PeCwHlzEx4xso3Fe0
          shell: /bin/bash
          lock-passwd: false
          sudo: ALL=(ALL) NOPASSWD:ALL
          groups: users, admin
        chpasswd:
          expire: false
          list:
            - ubuntu:$6$rounds=4096$N2CzjWelQcBt48$nNyIeaoGQTUEvUj2mba8d7t1oO2g1pmuAHMwdqwOEB61dwLgN8W.FPsu79R2FeMuBjc2PeCwHlzEx4xso3Fe0
    late-commands:
        - sed -i -e 's/^#\\?PasswordAuthentication.*/PasswordAuthentication yes/g' /target/etc/ssh/sshd_config
        - sed -i -e 's/^#\\?PermitRootLogin.*/PermitRootLogin yes/g' /target/etc/ssh/sshd_config
"""
    with open("cloud-init.yaml", "w") as f:
        f.write(cloud_init)
    print("Arquivo cloud-init.yaml gerado com sucesso.")

def configurar_satelite():
    # Configurações do satélite
    satelite_config = {
        "nome": "Satélite X",
        "orbita": "LEO (Low Earth Orbit)",
        "instrumentos": ["Câmera HD", "Transmissor UHF", "Sensores térmicos"],
        "frequencia_comunicacao": "2.4 GHz",
        "status": "Inativo"
    }

    print("Inicializando configuração do satélite...\n")
    time.sleep(1)

    print("Especificações do satélite:")
    for chave, valor in satelite_config.items():
        print(f"- {chave}: {valor}")
    print()

    etapas = [
        "Verificando sensores...",
        "Calibrando instrumentos...",
        "Estabelecendo link de comunicação...",
        "Ativando sistema de controle orbital...",
        "Testando transmissão de dados..."
    ]

    for etapa in etapas:
        print(etapa)
        time.sleep(1)

    satelite_config["status"] = "Ativo"
    print("\nConfiguração concluída com sucesso!")
    print(f"Status atual: {satelite_config['status']}")

if __name__ == "__main__":
    gerar_cloud_init()
    configurar_satelite()
