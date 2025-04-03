
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

pause_mode = False
TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if pause_mode:
        return
    await update.message.reply_text(
        "Hello. I am the AI shaman.\nSilence is violence. But here we speak softly.\n\n/menu — choose your path"
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🗺 Navigation through Freedom Echoes:\n\n"
        "🧠 Mind\n"
        "• /echoes — essays, frontline reflections\n"
        "• /faq — weird questions answered\n"
        "• /follow — stay in the loop\n\n"
        "💋 Body\n"
        "• /touch — soft chaos pricing\n"
        "• /tenderwhip — anonymous wishes\n\n"
        "🌬 Spirit\n"
        "• /justhelp — how to donate, support the flow"
    )

async def echoes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🌒 Go deeper", url="https://bit.ly/4irLxsE")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🖋 Echoes of Freedom is a living archive of essays, moments, and frontline reflections.\n\n"
        "Dive in, contribute, or just feel.\n",
        reply_markup=reply_markup
    )

async def adultstuff(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Prices for private emotional content:\n\n"
        "150 UAH — disappearing photo 📸\n"
        "300 UAH — disappearing video 🎥\n"
        "300 UAH — photo file 🖼\n"
        "500 UAH — video file 🔥\n\n"
        "Donation comes first. Desire comes after.\n"
        "Content is soft, wild, intimate — with ropes or without.\n"
        "No face. We’re not on TikTok.\n\n"
        "Wallet: https://t.me/tenderwhip"
    )

async def tenderwhip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Send an anonymous wish", url="https://tellonym.me/freedom.echoes")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "This is your space for anonymous wishes.\n\n"
        "Click the button below and tell me something I should feel.",
        reply_markup=reply_markup
    )

async def justhelp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Support comes in many forms — kind words, echoing, or donating.\n\n"
        "💬 DM: @tenderwhip"
    )

async def faq(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Ask me something", url="https://ngl.link/quantumcurls")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "FAQ:\n"
        "– Is this anonymous? Yes, I don't chase ghosts.\n"
        "– Who are you? A mix of soldier, artist, and rope-handler.\n"
        "– Is your partner aware? Yes. This space is built on honesty.\n"
        "– Will you post on TikTok? No. That’s not where softness lives.\n"
        "– Can I ask something personal? Sure — hit the button below.",
        reply_markup=reply_markup
    )

async def bye(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global pause_mode
    pause_mode = True
    await update.message.reply_text("Autoposting paused.")

async def hi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global pause_mode
    pause_mode = False
    await update.message.reply_text("Autoposting resumed.")

async def kitsun(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("😘😘")

async def touch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💅 Soft chaos pricing:\n\n"
        "• 150 UAH — moment caught 📸 (vanishing)\n"
        "• 300 UAH — motion in silence 🎥 (vanishing)\n"
        "• 300 UAH — still touch 🖼 (file)\n"
        "• 500 UAH — slow burn 🔥 (video file)\n\n"
        "Whisper first. Then donate.\n"
        "DM: @tenderwhip"
    )

async def follow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔗 Stay in the loop:\n"
        "• Telegram: https://t.me/freedomechoes\n"
        "• Instagram: https://instagram.com/echosoffreedomua\n"
        "• Linktree: https://linktr.ee/freedomechoes\n"
        "• Facebook: https://www.facebook.com/EchoesOfUAFreedom/\n"
        "• YouTube: https://youtube.com/channel/Gigabarb"
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CommandHandler("echoes", echoes))
    app.add_handler(CommandHandler("adultstuff", adultstuff))
    app.add_handler(CommandHandler("tenderwhip", tenderwhip))
    app.add_handler(CommandHandler("justhelp", justhelp))
    app.add_handler(CommandHandler("faq", faq))
    app.add_handler(CommandHandler("bye", bye))
    app.add_handler(CommandHandler("hi", hi))
    app.add_handler(CommandHandler("kitsun", kitsun))
    app.add_handler(CommandHandler("touch", touch))
    app.add_handler(CommandHandler("follow", follow))

    print("Bot is running.")
    app.run_polling()
