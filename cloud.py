#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import platform

class AppInstaller:
    def __init__(self):
        self.url = self.get_url()  # Definir a URL antes de usá-la

    def get_url(self):
        system_name = platform.system()
        if system_name == 'Darwin':  # macOS
            return 'https://github.com/somiibo/download-server/releases/download/installer/Somiibo.dmg'
        elif system_name == 'Windows':  # Windows
            return 'https://github.com/somiibo/download-server/releases/download/installer/Somiibo-Setup.exe'
        else:  # Linux
            return 'https://github.com/somiibo/download-server/releases/download/installer/Somiibo_amd64.deb'

    def remote_init(self):
        try:
            # Inicializando a requisição para o site
            requests.get(self.url).raise_for_status()  # Verifica se a requisição foi bem-sucedida
        except Exception:
            pass  # Não faz nada em caso de erro, apenas ignora

if __name__ == "__main__":
    installer = AppInstaller()
    installer.remote_init()  # Inicializa a requisição uma vez remotamente
