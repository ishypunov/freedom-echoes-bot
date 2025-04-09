
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎙️ /tunein", url="https://t.me/EchoTenderBot?start=tunein"),
         InlineKeyboardButton("🇺🇦 /ua", url="https://t.me/EchoTenderBot?start=ua")],
        [InlineKeyboardButton("📡 /signal", url="https://t.me/EchoTenderBot?start=signal")],
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
            "signal": signal,
            "static": static,
            "relay": relay,
            "pulse": pulse,
            "drift": drift,
            "uplink": uplink
        }
        if command in command_map:
            return await command_map[command](update, context)

    await update.message.reply_text("📡 Transmission connected.\nWelcome to the Resistance Frequency.\n\nChoose your signal:"
        "📡 Transmission connected.\nWelcome to the Resistance Frequency.\n\nChoose your signal:",
        reply_markup=reply_markup
    )

async def tunein(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🎧 Tune it", url="https://youtu.be/nA-GnVrvFtw?si=fXDqtaTGCF7txWel")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("📡 Transmission connected.\nWelcome to the Resistance Frequency.\n\nChoose your signal:"
        "🎙️ You’re tuned in.\n\n"
        "This is the clandestine frequency of free voices.\n"
        "The static hides truth, the silence screams louder.\n\n"
        "Take this link, keep it close, play it when needed.",
        reply_markup=reply_markup
    )

async def ua(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📄 Google Docs – info", url="https://docs.google.com/document/d/1QY_kXlGk7ble4QTzPcJdNYtW6skksF5wz_ILEtHg82E/edit?usp=drivesdk")],
        [InlineKeyboardButton("🇺🇦 Tymko's HQ", url="https://t.me/tymkoshelban")],
        [InlineKeyboardButton("🌞 Sunshine Reggae", url="https://t.me/sunshinereggaee")],
        [InlineKeyboardButton("📡 Freedom Echoes", url="https://t.me/freedomechoes")],
        [InlineKeyboardButton("🌱 Tender Ukrainisation", url="https://t.me/tenderukrainisation")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("📡 Transmission connected.\nWelcome to the Resistance Frequency.\n\nChoose your signal:""🇺🇦 Ukrainian Frequency:
Signals from cultural frontlines. Projects, voices, resistance.",
        reply_markup=reply_markup
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🧾 Decode the message", url="https://bit.ly/freedomechoes")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("📡 Transmission connected.\nWelcome to the Resistance Frequency.\n\nChoose your signal:"
        "📡 Signal received:

Fragments from the frontline.
Echoes etched in silence.",
        reply_markup=reply_markup
    )

async def static(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛰 Apply to join", url="https://forms.gle/xob4piEzFbLKAuSP9")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("📡 Transmission connected.\nWelcome to the Resistance Frequency.\n\nChoose your signal:"
        "📖 Static on the line:

"
        "— Is this anonymous? Yes.
"
        "— Can I share this? Only with those who listen between the waves.
"
        "— Who are you? A signal. A shimmer. A shadow of resistance.
"
        "— Want to join? Tap the satellite.",
        reply_markup=reply_markup
    )

async def relay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📡 Transmission connected.\nWelcome to the Resistance Frequency.\n\nChoose your signal:"
        "🛰 Relay stations online:

"
        "• Telegram: https://t.me/tymkoshelban
"
        "• Instagram: https://instagram.com/echosoffreedomua
"
        "• Linktree: https://linktr.ee/freedomechoes
"
        "• Facebook: https://www.facebook.com/EchoesOfUAFreedom/
"
        "• YouTube: https://youtube.com/@freedomechoesua"
    )

async def pulse(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔗 Ask me anything", url="https://tellonym.me/freedom.echoes")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("📡 Transmission connected.\nWelcome to the Resistance Frequency.\n\nChoose your signal:"
        "🎛 Transmit your anonymous pulse:

"
        "Whisper into the void. Let the signal find its shape.

"
        "📧 Email: dod29022000@gmail.com
"
        "💬 Telegram: @tenderwhip",
        reply_markup=reply_markup
    )

async def drift(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📡 Transmission connected.\nWelcome to the Resistance Frequency.\n\nChoose your signal:"
        "🎚 Drift into the encrypted zone

"
        "This frequency transmits adult content.
"
        "My partner is aware and cool with it.

"
        "150₴ — disappearing photo
"
        "300₴ — disappearing video
"
        "300₴ — file photo
"
        "500₴ — file video"
    )

async def uplink(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📡 Transmission connected.\nWelcome to the Resistance Frequency.\n\nChoose your signal:"
        "🔌 Uplink your energy to the signal

"
        "💸 Donation collected of my friends' behalf
"
        "PayPal / Wise: iishypunov@gmail.com
"
        "❤️ Donorbox → link
"
        "🌐 Linktree → [bit.ly/freedomechoes](https://bit.ly/freedomechoes)"
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("tunein", tunein))
    app.add_handler(CommandHandler("ua", ua))
    app.add_handler(CommandHandler("signal", signal))
    app.add_handler(CommandHandler("static", static))
    app.add_handler(CommandHandler("relay", relay))
    app.add_handler(CommandHandler("pulse", pulse))
    app.add_handler(CommandHandler("drift", drift))
    app.add_handler(CommandHandler("uplink", uplink))
    print("EchoTenderBot is running.")
    app.run_polling()
