import os
import subprocess
import sys
import logging
import robots
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# 📌 Instalar dependências automaticamente
def instalar_dependencias():
    pacotes = ["python-telegram-bot[webhooks]"]
    for pacote in pacotes:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", pacote])
            print(f"✅ Pacote '{pacote}' instalado com sucesso!")
        except subprocess.CalledProcessError:
            print(f"❌ Erro ao instalar '{pacote}'.")

# ✅ Instalar pacotes necessários
instalar_dependencias()

# ✅ Configuração do logging
logging.basicConfig(level=logging.INFO)

# ✅ Configuração dos tokens
TELEGRAM_TOKEN = "5986172966:AAHTLBf4VDaB8b1Bbx_ZZnc0_IPmwS5N0mM"
ADMIN_CHAT_ID = "5671962308"

# ✅ Configuração do bot Telegram
async def start(update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    await update.message.reply_text(f"Olá! Seu ID é {chat_id}. Envie uma mensagem e eu encaminharei ao admin.")

async def forward_to_admin(update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    message_text = f"📩 Nova mensagem de {chat_id}:\n\n{update.message.text}"
    try:
        await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=message_text)
        await update.message.reply_text("Mensagem enviada ao administrador!")
    except Exception as e:
        logging.error(f"Erro ao encaminhar mensagem: {e}")
        await update.message.reply_text("Erro ao enviar a mensagem. Tente novamente mais tarde.")

def iniciar_telegram_bot():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_admin))
    print("🤖 Bot do Telegram rodando...")
    try:
        app.run_polling()
    except OSError as e:
        logging.error(f"Erro ao iniciar o bot: {e}")
        print("⚠️ O bot já pode estar em uso. Certifique-se de que nenhuma outra instância está rodando.")

# ✅ Iniciar bot
if __name__ == "__main__":
    iniciar_telegram_bot()
