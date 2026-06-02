import os
import requests
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = os.environ.get("TOKEN")
HF_TOKEN = os.environ.get("HF_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct"

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def ask_ai(text):
    r = requests.post(API_URL, headers=headers, json={"inputs": text})
    try:
        return r.json()[0]["generated_text"]
    except:
        return "AI جواب نداد"

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    answer = ask_ai(user_text)
    await update.message.reply_text(answer)

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, reply))
app.run_polling()
