import os
import requests
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

# توکن تلگرام
TOKEN = os.environ.get("TOKEN")

# کلید OpenRouter
OPENROUTER_KEY = os.environ.get("OPENROUTER_KEY")


# تابع هوش مصنوعی
def ask_ai(text):
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-4o-mini",
                "messages": [
                    {"role": "user", "content": text}
                ]
            },
            timeout=30
        )

        data = response.json()

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return "مشکلی در اتصال به AI پیش آمد."


# هندلر پیام‌ها
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    answer = ask_ai(user_text)

    await update.message.reply_text(answer)


# ساخت اپلیکیشن
app = Application.builder().token(TOKEN).build()

# گرفتن همه پیام‌های متنی
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

# اجرا
app.run_polling()
