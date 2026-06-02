from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
import os

TOKEN = os.environ.get("TOKEN")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ربات فعال است ✅")

app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, reply))

app.run_polling()
