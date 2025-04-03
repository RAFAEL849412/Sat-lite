import os
import logging
import robots as bot  # Importa o módulo robots como "bot"
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Carregar variáveis do arquivo .env
load_dotenv()
TELEGRAM_TOKEN = os.getenv("5986172966:AAHTLBf4VDaB8b1Bbx_ZZnc0_IPmwS5N0mM")
ADMIN_CHAT_ID = os.getenv("5671962308")

# Configuração do logging
logging.basicConfig(level=logging.INFO)

# Instancia um "Robot" com o ID do admin
robot = bot.Robot(ADMIN_CHAT_ID)

async def start(update: Update, context: CallbackContext) -> None:
    """Responde ao comando /start"""
    chat_id = update.message.chat_id
    await update.message.reply_text(f"Olá! Seu ID é {chat_id}. Envie uma mensagem e eu reencaminharei ao admin.")

async def forward_to_admin(update: Update, context: CallbackContext) -> None:
    """Reencaminha mensagens para o admin"""
    chat_id = update.message.chat_id
    message_text = update.message.text

    # Processa a mensagem usando o "robot"
    processed_message = robot.process_message(message_text)

    # Enviar mensagem ao admin
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=f"📩 Nova mensagem de {chat_id}:\n\n{processed_message}")

    # Confirmação ao usuário
    await update.message.reply_text("Mensagem enviada ao administrador!")

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_admin))

    print("Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()
    
