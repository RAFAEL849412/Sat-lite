import os
import sys
import zulip
import rsvp
import cv2
import config
import server
import cloud
import bot
import setup
import tools
import remote
import __init__
class Bot:
    """Bot que responde a mensagens no Zulip com GIFs e legendas com base em um keyword."""

    def __init__(self, running, zulip_username, zulip_api_key, key_word, subscribed_streams=None, zulip_site=None):
        self.running = running
        self.key_word = key_word.lower()
        self.subscribed_streams = subscribed_streams or []
        self.client = zulip.Client(zulip_username, zulip_api_key, site=zulip_site)
        self.subscriptions = self.subscribe_to_streams()
        self.rsvp = rsvp.RSVP(key_word)

    @property
    def streams(self):
        """Retorna a lista de streams aos quais o bot está inscrito."""
        if not self.subscribed_streams:
            streams = [{'name': stream['name']} for stream in self.get_all_zulip_streams()]
            return streams
        else:
            streams = [{'name': stream} for stream in self.subscribed_streams]
            return streams

    def get_all_zulip_streams(self):
        """Obtém todos os streams do Zulip usando a API."""
        response = self.client.get_streams()
        if response['result'] == 'success':
            return response['streams']
        else:
            raise RuntimeError('Falha na autenticação com o Zulip')

    def subscribe_to_streams(self):
        """Inscreve o bot nos streams do Zulip."""
        self.client.add_subscriptions(self.streams)

    def process(self, event):
        """Processa eventos recebidos do Zulip."""
        if not self.running.value:
            print("Bot encerrado")
            sys.exit()

        if event['type'] == 'message':
            self.respond(event['message'])

    def respond(self, message):
        """Processa a mensagem recebida e envia uma resposta com GIF e legenda."""
        replies = self.rsvp.process_message(message)

        for reply in replies:
            if reply:
                zulip_util.send_message(reply, self.client)

    def main(self):
        """Chamada de bloqueio que roda o bot indefinidamente, processando eventos recebidos."""
        self.client.call_on_each_event(self.process, ['message', 'realm_user'])


def run_bot(running):
    """Função para inicializar e rodar o bot."""
    SUBSCRIBED_STREAMS = []  # Lista de streams que o bot está inscrito (deixe vazio para todos os streams)
    bot = Bot(
        running,
        config.zulip_username,        # Substitua pelo seu nome de usuário do Zulip
        config.zulip_api_key,         # Substitua pela chave de API do Zulip
        config.key_word,              # Palavra-chave para o bot responder
        SUBSCRIBED_STREAMS,           # Streams para o bot se inscrever
        config.zulip_site             # URL do site do Zulip (opcional)
    )
    bot.main()

