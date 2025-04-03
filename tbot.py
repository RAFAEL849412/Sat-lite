import os
import subprocess
import sys
import logging                                                                                                                                                                        
# Função para instalar pacotes utilizando subprocess
def instalar_pacote(pacote):
    """Verifica se o pacote está instalado, caso contrário, instala usando pip."""
    try:
        __import__(pacote)
        print(f"{pacote} já está instalado.")
    except ImportError:
        print(f"{pacote} não encontrado. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pacote])
        print(f"{pacote} instalado com sucesso!")

# Garantindo que python-dotenv e python-telegram-bot estão instalados
instalar_pacote('python-dotenv')
instalar_pacote('python-telegram-bot')

# Importar dotenv após garantir que está instalado
import dotenv
import robots
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Carregar as variáveis de ambiente do .env
dotenv.load_dotenv()

# Configuração do logging
logging.basicConfig(level=logging.INFO)

# Definição direta dos dados de configuração
TELEGRAM_TOKEN = "5986172966:AAHTLBf4VDaB8b1Bbx_ZZnc0_IPmwS5N0mM"  # Substitua pelo token do seu bot
ADMIN_CHAT_ID = "5671962308"  # Substitua pelo seu ID de chat do administrador

async def start(update: Update, context: CallbackContext) -> None:
    """Responde ao comando /start"""
    chat_id = update.message.chat_id
    await update.message.reply_text(f"Olá! Seu ID é {chat_id}. Envie uma mensagem e eu reencaminharei ao admin.")

async def forward_to_admin(update: Update, context: CallbackContext) -> None:
    """Reencaminha mensagens para o admin"""
    chat_id = update.message.chat_id
    message_text = f"📩 Nova mensagem de {chat_id}:\n\n{update.message.text}"

    # Enviar mensagem ao admin
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=message_text)

    # Confirmar ao usuário
    await update.message.reply_text("Mensagem enviada ao administrador!")

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Adiciona os handlers de comando
    app.add_handler(CommandHandler("start", start))

    # Adiciona o handler para mensagens de texto
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_admin))

    print("Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()
