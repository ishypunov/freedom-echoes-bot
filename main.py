
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

    if context.args:
        command = context.args[0].lower()
        command_map = {
            "tunein": tunein,
            "ua": ua,
            "bandmap": bandmap,
            "signal": signal,
            "static": static,
            "relay": relay,
            "pulse": pulse,
            "drift": drift,
            "uplink": uplink
        }
        if command in command_map:
            return await command_map[command](update, context)

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

async def ua(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🇺🇦 Ukrainian front links coming soon...")

async def bandmap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🗺 Full bandmap coming soon...")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📡 Archive signal detected...")

async def static(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📖 Static: FAQ & Join form coming soon...")

async def relay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🛰 Relay stations: socials coming soon...")

async def pulse(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎛 Anonymous pulse ready soon...")

async def drift(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎚 Drift mode: encrypted zone coming soon...")

async def uplink(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔌 Uplink: donate link coming soon...")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("tunein", tunein))
    app.add_handler(CommandHandler("ua", ua))
    app.add_handler(CommandHandler("bandmap", bandmap))
    app.add_handler(CommandHandler("signal", signal))
    app.add_handler(CommandHandler("static", static))
    app.add_handler(CommandHandler("relay", relay))
    app.add_handler(CommandHandler("pulse", pulse))
    app.add_handler(CommandHandler("drift", drift))
    app.add_handler(CommandHandler("uplink", uplink))
    print("EchoTenderBot is running.")
    app.run_polling()
