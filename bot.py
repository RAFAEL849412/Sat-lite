import json
import subprocess
import sys
from datetime import datetime, timedelta
import os

# Variáveis globais
TLE_FILE = "starlink.tle"
COMMANDS = {"starlink": "!starlink"}
VERBOSE = "-v" in sys.argv

# Função para log de depuração
def log(msg):
    if VERBOSE:
        print(msg)

# Função para converter string de data para objeto datetime
def strtotime(string):
    return datetime.strptime(string, "%Y-%m-%d %H:%M")

# Função para converter datetime para string
def timetostr(time):
    return time.strftime("%Y-%m-%d %H:%M")

# Função para ler o arquivo starlink.tle
def read_tle():
    if not os.path.exists(TLE_FILE):
        log("Arquivo starlink.tle não encontrado.")
        return None
    with open(TLE_FILE, "r") as f:
        return f.readlines()

# Classe que representa um SMS
class SMS:
    def __init__(self, sms):
        self.body = sms["body"]
        self.number = sms["number"]
        self.received = sms["received"]
        self.time = strtotime(sms["received"])

# Classe principal do bot
class Bot:
    def __init__(self):
        log("Inicializando bot...")
        self.tle_data = read_tle()
        log("Bot pronto.")

    # Função para processar o comando !starlink
    def handle_starlink(self, sms):
        log("Processando comando Starlink...")
        latitude = "XX.XXXXX"  # Substitua pela latitude real
        longitude = "YY.YYYYY"  # Substitua pela longitude real

        if not self.tle_data:
            response = "Erro: Dados de Starlink TLE não disponíveis."
        else:
            result = subprocess.run(
                ["python", "starlink_match.py", "--latitude", latitude, "--longitude", longitude],
                capture_output=True, text=True
            )
            response = result.stdout.strip()

        self.reply(sms, response)

    # Função para processar mensagens SMS
    def process_smses(self, smses):
        if not smses:
            log("Nenhuma nova mensagem.")
            return

        for sms_data in smses:
            sms = SMS(sms_data)
            log(f"Lendo SMS: {sms.body[:80]}")
            if COMMANDS["starlink"] in sms.body:
                self.handle_starlink(sms)

    # Função para responder ao SMS
    def reply(self, sms, text):
        log(f"Enviando resposta para {sms.number}")
        subprocess.run(["termux-sms-send", "-n", sms.number, text])

# Obtendo dados do starlink_match.py
sms_json = subprocess.check_output(["python", "starlink_match.py"])
sms_list = json.loads(sms_json)

# Executando o bot
bot = Bot()
bot.process_smses(sms_list)
