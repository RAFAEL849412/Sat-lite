#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
import asyncio
import requests
import telegram
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Telegram Bot Configuration
TOKEN = "968019501:AAHTsOYy26wr-n4f_3XBk_o78-gcPtbB8SA"  # Define our Bot's token that we need to authenticate with the Telegram API
bot = telegram.Bot(token=TOKEN)

# Função para enviar mensagem pelo Telegram Bot
def send_telegram_message(chat_id: str, message: str):
    try:
        bot.send_message(chat_id=chat_id, text=message)
        logging.info(f"Mensagem enviada para o Telegram: {message}")
    except Exception as e:
        logging.error(f"Erro ao enviar mensagem: {str(e)}")

# Configuração de logging
logging.basicConfig(level=logging.INFO)

# Monitoramento de arquivos com Watchdog
class FileMonitorHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("Alpha.txt"):
            logging.info(f"Arquivo modificado: {event.src_path}")
            # Exemplo de envio de mensagem para Telegram quando o arquivo é modificado
            send_telegram_message("256281040558", f"O arquivo Alpha.txt foi modificado: {event.src_path}")

async def start_file_monitor():
    event_handler = FileMonitorHandler()
    observer = Observer()
    observer.schedule(event_handler, path="./", recursive=False)
    observer.start()
    try:
        while True:
            await asyncio.sleep(1)  # Aguarda corretamente dentro de uma corrotina
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Iniciando o monitoramento de arquivos em um thread separado
file_monitor_thread = threading.Thread(target=lambda: asyncio.run(start_file_monitor()), daemon=True)
file_monitor_thread.start()

# Executando o servidor ou outras lógicas principais (se necessário)
if __name__ == "__main__":
    logging.info("Monitoramento de arquivos iniciado...")
    # O código principal do servidor ou execução pode ser colocado aqui se necessário
