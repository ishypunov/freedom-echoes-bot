
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

pause_mode = False
TOKEN = os.getenv("TOKEN")

# /start — головне меню з усіма кнопками
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if pause_mode:
        return
    keyboard = [
        [InlineKeyboardButton("🎙️ /tunein", callback_data='tunein')],
        [InlineKeyboardButton("🇺🇦 /ua", callback_data='ua')],
        [InlineKeyboardButton("🗺 /bandmap", callback_data='bandmap')],
        [InlineKeyboardButton("📡 /signal", callback_data='signal')],
        [InlineKeyboardButton("📖 /static", callback_data='static')],
        [InlineKeyboardButton("🛰 /relay", callback_data='relay')],
        [InlineKeyboardButton("🎛 /pulse", callback_data='pulse')],
        [InlineKeyboardButton("🎚 /drift", callback_data='drift')],
        [InlineKeyboardButton("🔌 /uplink", callback_data='uplink')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "📡 Transmission connected.\nWelcome to the Resistance Frequency.\n\nChoose your signal:",
        reply_markup=reply_markup
    )

# /tunein
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

# /ua
async def ua(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📄 Project Doc", url="https://docs.google.com/document/d/1QY_kXlGk7ble4QTzPcJdNYtW6skksF5wz_ILEtHg82E/edit?usp=drivesdk")],
        [InlineKeyboardButton("🇺🇦 Tymko's HQ", url="https://t.me/tymkoshelban")],
        [InlineKeyboardButton("🌞 Sunshine Reggae", url="https://t.me/sunshinereggaee")],
        [InlineKeyboardButton("📡 Freedom Echoes", url="https://t.me/freedomechoes")],
        [InlineKeyboardButton("🌱 Tender Ukrainisation", url="https://t.me/tenderukrainisation")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🇺🇦 Ukrainian Frequency:\n\n"
        "Signals from cultural frontlines. Projects, voices, resistance.\nChoose your channel:",
        reply_markup=reply_markup
    )

# /bandmap
async def bandmap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎙️ /tunein", callback_data='tunein')],
        [InlineKeyboardButton("📡 /signal", callback_data='signal')],
        [InlineKeyboardButton("📖 /static", callback_data='static')],
        [InlineKeyboardButton("🛰 /relay", callback_data='relay')],
        [InlineKeyboardButton("🎛 /pulse", callback_data='pulse')],
        [InlineKeyboardButton("🎚 /drift", callback_data='drift')],
        [InlineKeyboardButton("🔌 /uplink", callback_data='uplink')],
        [InlineKeyboardButton("🇺🇦 /ua", callback_data='ua')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "📻 Resistance Bandmap\n\nChoose your frequency. Tune wisely.",
        reply_markup=reply_markup
    )

# /signal
async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🧾 Decode the message", url="https://bit.ly/freedomechoes")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "📡 Signal received:\n\n"
        "Fragments from the frontline.\nEchoes etched in silence.\n\n"
        "Explore the archive below.",
        reply_markup=reply_markup
    )

# /static
async def static(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🛰 Apply to join", url="https://forms.gle/xob4piEzFbLKAuSP9")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "📖 Static on the line:\n\n"
        "— Is this anonymous?\nYes. The air doesn’t remember.\n\n"
        "— Can I share this?\nOnly with those who listen between the waves.\n\n"
        "— Who are you?\nA signal. A shimmer. A shadow of resistance.\n\n"
        "— Want to join?\nTap the satellite.",
        reply_markup=reply_markup
    )

# /relay
async def relay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛰 Relay stations online:\n\n"
        "🔗 Telegram: https://t.me/tymkoshelban\n"
        "📸 Instagram: https://instagram.com/echosoffreedomua\n"
        "🌐 Linktree: https://linktr.ee/freedomechoes\n"
        "📘 Facebook: https://www.facebook.com/EchoesOfUAFreedom/\n"
        "▶️ YouTube: https://youtube.com/@freedomechoesua"
    )

# /pulse
async def pulse(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🎛 Send a Pulse", url="https://ngl.link/quantumcurls")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🎛 Transmit your anonymous pulse:\n\n"
        "Whisper into the void. Let the signal find its shape.\n\n"
        "📧 Email: dod29022000@gmail.com\n"
        "💬 Telegram: https://t.me/tenderwhip",
        reply_markup=reply_markup
    )

# /drift
async def drift(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎚 Drift into the encrypted zone:\n\n"
        "This frequency transmits adult content.\n"
        "Soft, wild, visual — always intimate.\n"
        "My partner is aware and cool with it.\n\n"
        "Suggested donations:\n"
        "• 150 UAH — vanishing photo 📸\n"
        "• 300 UAH — vanishing video 🎥\n"
        "• 300 UAH — photo file 🖼\n"
        "• 500 UAH — video file 🔥\n\n"
        "No faces. No noise. Only signal.\n"
        "DM for access: @tenderwhip"
    )

# /uplink
async def uplink(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("❤️ Donate via Donorbox", url="https://donorbox.org/echoes-of-freedom")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🔌 Uplink your energy to the signal:\n\n"
        "💸 PayPal / Wise: iishypunov@gmail.com\n"
        "🌐 Linktree: https://linktr.ee/freedomechoes\n\n"
        "This transmission is powered by shared intention.\n"
        "Every coin, a wave.\nEvery wave, a whisper.",
        reply_markup=reply_markup
    )

# Обробка callback-кнопок
async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    handler_map = {
        'tunein': tunein,
        'ua': ua,
        'bandmap': bandmap,
        'signal': signal,
        'static': static,
        'relay': relay,
        'pulse': pulse,
        'drift': drift,
        'uplink': uplink
    }
    if data in handler_map:
        await handler_map[data](update, context)

# Запуск бота
if __name__ == "__main__":
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

    app.add_handler(CallbackQueryHandler(handle_callback))

    print("Radio Resistance Bot is live.")
    app.run_polling()
