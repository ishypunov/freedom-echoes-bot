
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎙️ /tunein", url="https://t.me/EchoTenderBot?start=tunein"),
         InlineKeyboardButton("🇺🇦 /ua", url="https://t.me/EchoTenderBot?start=ua")],
        [InlineKeyboardButton("🗺 /bandmap", url="https://t.me/EchoTenderBot?start=bandmap"),
         InlineKeyboardButton("📡 /signal", url="https://t.me/EchoTenderBot?start=signal")],
        [InlineKeyboardButton("📖 /static", url="https://t.me/EchoTenderBot?start=static"),
         InlineKeyboardButton("🛰 /relay", url="https://t.me/EchoTenderBot?start=relay")],
        [InlineKeyboardButton("🎛 /pulse", url="https://t.me/EchoTenderBot?start=pulse"),
         InlineKeyboardButton("🎚 /drift", url="https://t.me/EchoTenderBot?start=drift")],
        [InlineKeyboardButton("🔌 /uplink", url="https://t.me/EchoTenderBot?start=uplink")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "📡 Transmission connected.\nWelcome to the Resistance Frequency.\n\nChoose your signal:",
        reply_markup=reply_markup
    )

async def tunein(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🎧 Tune it", url="https://youtu.be/nA-GnVrvFtw?si=fXDqtaTGCF7txWel")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🎙️ You’re tuned in.\n\n"
        "This is the clandestine frequency of free voices.\n"
        "The static hides truth, the silence screams louder.\n\n"
        "Use /bandmap to navigate the spectrum.",
        reply_markup=reply_markup
    )

async def placeholder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📡 This frequency is being tuned...")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("tunein", tunein))
    app.add_handler(CommandHandler("ua", placeholder))
    app.add_handler(CommandHandler("bandmap", placeholder))
    app.add_handler(CommandHandler("signal", placeholder))
    app.add_handler(CommandHandler("static", placeholder))
    app.add_handler(CommandHandler("relay", placeholder))
    app.add_handler(CommandHandler("pulse", placeholder))
    app.add_handler(CommandHandler("drift", placeholder))
    app.add_handler(CommandHandler("uplink", placeholder))
    print("EchoTenderBot is running.")
    app.run_polling()
