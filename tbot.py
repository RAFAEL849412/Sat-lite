import os
import subprocess
import sys
import logging
import robots
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# 📌 Instalar dependências automaticamente
def instalar_dependencias():
    pacotes = ["python-telegram-bot[webhooks]"]
    for pacote in pacotes:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", pacote])
        print(f"✅ Pacote '{pacote}' instalado com sucesso!")

# ✅ Instalar pacotes necessários
instalar_dependencias()

# ✅ Configuração do logging
logging.basicConfig(level=logging.INFO)

# ✅ Configuração dos tokens
TELEGRAM_TOKEN = "5986172966:AAHTLBf4VDaB8b1Bbx_ZZnc0_IPmwS5N0mM"
ADMIN_CHAT_ID = "5671962308"
WEBHOOK_URL = "https://webhook.site"  # Substitua por um URL HTTPS válido

# =======================
# 🤖 BOT DO TELEGRAM
# =======================
async def start(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    await update.message.reply_text(f"Olá! Seu ID é {chat_id}. Envie uma mensagem e eu encaminharei ao admin.")

async def forward_to_admin(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    message_text = f"📩 Nova mensagem de {chat_id}:\n\n{update.message.text}"
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=message_text)
    await update.message.reply_text("Mensagem enviada ao administrador!")

def iniciar_telegram_bot():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_admin))
    print("🤖 Bot do Telegram rodando...")
    app.run_webhook(listen="0.0.0.0", port=8443, url_path=TELEGRAM_TOKEN, webhook_url=WEBHOOK_URL)

# =======================
# 🔥 EXECUTAR O BOT
# =======================
if __name__ == "__main__":
    iniciar_telegram_bot()
