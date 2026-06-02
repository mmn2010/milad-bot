from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN="8829174612:AAGqb_nhX7Z5eHU5jcSD5Dd3RC_vXUtw63U"

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text("سلام، پیام شما دریافت شد: " + text)

app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, reply))

app.run_polling()