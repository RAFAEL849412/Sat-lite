import os
import subprocess
import sys
import logging
import robots as bot
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

def instalar_e_importar_dotenv():
    """Verifica se dotenv está instalado e importa corretamente."""
    try:
        import dotenv  # Importa diretamente como dotenv
    except ImportError:
        print("Instalando dotenv...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "python-dotenv"])
        print("Instalação concluída!")

        # Agora, importamos dotenv corretamente
        import dotenv

    return dotenv

# Garantindo que dotenv está instalado e carregado
dotenv = instalar_e_importar_dotenv()
dotenv.load_dotenv()

# Configuração do logging
logging.basicConfig(level=logging.INFO)

# Substitua pelos seus dados
TELEGRAM_TOKEN = "5986172966:AAHTLBf4VDaB8b1Bbx_ZZnc0_IPmwS5N0mM"
ADMIN_CHAT_ID = "5671962308"  # Seu ID do Telegram

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

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_admin))

    print("Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()
    
