import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import random

TOKEN = os.getenv("TOKEN")

responses = [
    "Bro wtf are you even saying 💀",
    "That sounds like a bad decision already, i am in",
    "I’m judging you silently, also having lewd thoughts about you",
    "Continue… this is getting interesting, I am ovulating",
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm alive. Unfortunately for you.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()

    if "sad" in user_message:
        reply = "Life is tough, but so are you… kinda"
    else:
        reply = random.choice(responses)

    await update.message.reply_text(reply)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
