import json
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart, Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode
from aiogram.utils.token import TokenValidationError
from aiohttp import web

# Load env vars
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

logging.basicConfig(level=logging.INFO)

try:
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
except TokenValidationError:
    print("Invalid bot token")
    exit()

dp = Dispatcher(storage=MemoryStorage())

# User language state (simple in-memory storage)
user_lang = {}

# Load channels from file
CHANNELS_FILE = "channels.json"
def load_channels():
    with open(CHANNELS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# Keyboards
def get_main_keyboard(lang='ua'):
    channels = load_channels()
    keyboard = InlineKeyboardBuilder()
    for ch in channels:
        btn_text = f"{ch['emoji']} {ch['name']} — {ch['description']}"
        keyboard.add(InlineKeyboardButton(text=btn_text, url=ch['link']))
    support_text = "💸 Підтримати проєкт" if lang == 'ua' else "💸 Support project"
    support_btn = InlineKeyboardButton(text=support_text + " / Support", url="https://bit.ly/freedomechoes")
    keyboard.add(support_btn)
    keyboard.adjust(2)
    return keyboard.as_markup()

# Handlers
@dp.message(CommandStart())
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    lang = user_lang.get(user_id, 'ua')
    text = "📡 <b>EchoTenderBot активний</b>\n\nОбери канал:" if lang == 'ua' else "📡 <b>EchoTenderBot is live</b>\n\nChoose a channel:"
    await message.answer(text, reply_markup=get_main_keyboard(lang))

@dp.message(Command("lang"))
async def lang_handler(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Українська 🇺🇦", callback_data="lang_ua")],
        [InlineKeyboardButton(text="English 🇬🇧", callback_data="lang_en")]
    ])
    await message.answer("🌐 Обери мову / Choose your language:", reply_markup=keyboard)

@dp.callback_query(F.data.startswith("lang_"))
async def set_lang(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    lang_code = callback.data.split("_")[1]
    user_lang[user_id] = lang_code
    await callback.message.edit_text("✅ Мову змінено / Language updated.")
    await callback.answer()

@dp.message(Command("about"))
async def about_handler(message: types.Message):
    lang = user_lang.get(message.from_user.id, 'ua')
    text = "Цей бот об'єднує всі наші канали для зручного доступу." if lang == 'ua' else "This bot unites all our channels for easy access."
    await message.answer(text)

@dp.message(Command("broadcast"))
async def broadcast_handler(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return await message.answer("⛔️ Тільки для адміна / Admin only.")
    await message.answer("Відправ свій текст для розсилки / Send your message for broadcast.")

@dp.message(F.reply_to_message, F.from_user.id == ADMIN_ID)
async def broadcast_text(message: types.Message):
    users = []  # список користувачів, які писали боту
    text = message.text
    for user_id in users:
        try:
            await bot.send_message(user_id, text)
        except:
            pass
    await message.answer("✅ Розсилка завершена / Broadcast completed.")

# Webhook endpoint (опціонально для Railway)
async def handle(request):
    return web.Response(text="Bot is running")

app = web.Application()
app.router.add_get("/", handle)

if __name__ == "__main__":
    import asyncio
    from aiogram import executor

    async def main():
        await dp.start_polling(bot)

    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped")
