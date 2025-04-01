from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

pause_mode = False
TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if pause_mode:
        return
    await update.message.reply_text(
        "🫧 Ласкаво просимо в Tender Echoes\n\n"
        "Цей бот створено українським військовим. Поки багато хто бʼється руками — я працюю мозком у підвалі.\n"
        "Тут — трохи життя, трохи краси, трохи прямоти.\n"
        "Без сорому. Без фільтрів. І трохи еротики теж.\n\n"
        "📌 Команди:\n"
        "🗣️ /smalltalk – чому я це роблю\n"
        "🤝 /justhelp – як підтримати\n"
        "❓ /faq – відповіді на дивні питання\n"
        "📸 /touch – ціни та формати контенту\n"
        "🔥 /tenderwhip – залишити анонімне побажання\n"
        "🎴 /random – одна мила думка\n"
        "▶️ /hi – увімкнути бот\n"
        "⏸️ /bye – поставити на паузу\n\n"
        "Анонімно написати: https://ngl.link/quantumcurls\n"
        "Моя дівчина в курсі і не проти. Все цивільно. Все анонімно."
    )

async def smalltalk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Цей бот — мій спосіб говорити про життя, не мовчати про ніжність і залишатися собою, навіть під землею.")

async def justhelp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Підтримати можна добрим словом або донатом:\n@tenderwhip")

async def faq(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("FAQ:\n– Так, усе анонімно\n– Ні, в TikTok я не йду\n– Так, моя дівчина в курсі")

async def touch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Ціни за емоції:\n\n"
        "150 грн — зникаюче фото 📸\n"
        "300 грн — зникаюче відео 🎥\n"
        "300 грн — фото файлом 🖼\n"
        "500 грн — відео файлом 🔥\n\n"
        "Спочатку — донат. Потім — бажання.\n"
        "Контент — ніжний, дикий, домашній, з мотузками чи без.\n"
        "Фото — без обличчя. Бо ми не в TikTok.\n\n"
        "Мій гаманець: https://t.me/tenderwhip"
    )

async def tenderwhip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Ця команда — для побажань.\n\n"
        "Пиши сюди анонімно:\nhttps://ngl.link/quantumcurls\n\n"
        "Або на email:\ndod29022000@gmail.com"
    )

async def random(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from random import choice
    thoughts = [
        "Навіть після вибуху приходить тиша. І в тиші — життя.",
        "Кожна ніжність — маленька перемога над темрявою.",
        "Справжня сила — це залишатися добрим, коли маєш право ламати.",
        "Ти маєш право бути вразливим. І цим ти сильний.",
        "Сонце сходить завжди. Навіть над окопами."
    ]
    await update.message.reply_text(choice(thoughts))

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

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("smalltalk", smalltalk))
    app.add_handler(CommandHandler("justhelp", justhelp))
    app.add_handler(CommandHandler("faq", faq))
    app.add_handler(CommandHandler("touch", touch))
    app.add_handler(CommandHandler("tenderwhip", tenderwhip))
    app.add_handler(CommandHandler("random", random))
    app.add_handler(CommandHandler("bye", bye))
    app.add_handler(CommandHandler("hi", hi))
    app.add_handler(CommandHandler("kitsun", kitsun))
    print("Бот запущено.")
    app.run_polling()
