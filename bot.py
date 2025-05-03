#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
import asyncio
import requests
import threading
from telegram import Bot as tbot
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Token do bot Telegram
TOKEN = "968019501:AAHTsOYy26wr-n4f_3XBk_o78-gcPtbB8SA"
bot = tbot(token=TOKEN)

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
            send_telegram_message("256281040558", f"O arquivo Alpha.txt foi modificado: {event.src_path}")

async def start_file_monitor():
    event_handler = FileMonitorHandler()
    observer = Observer()
    observer.schedule(event_handler, path="./", recursive=False)
    observer.start()
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def main():
    logging.info("Monitoramento de arquivos iniciado...")
    file_monitor_thread = threading.Thread(target=lambda: asyncio.run(start_file_monitor()), daemon=True)
    file_monitor_thread.start()
    while True:
        pass  # Coloque aqui o que deseja executar continuamente

if __name__ == "__main__":
    main()
