KEY = "8531487774:AAGIfstKLBrPOz4zrWfwgX7hHxshcIanZgE"
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

# Bot tokeningizni BotFather'dan olib, BU_YERGA_TOKEN_YOZING o'rniga qo'ying
TOKEN = "8531487774:AAGIfstKLBrPOz4zrWfwgX7hHxshcIanZgE"

# Bot va Dispatcher (xabarlarni qabul qiluvchi)ni sozlaymiz
dp = Dispatcher()

# /start buyrug'iga javob beruvchi funksiya
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Salom, {html.bold(message.from_user.full_name)}! \nBot muvaffaqiyatli ishga tushdi.")

@dp.message(Command("help"))
async def help_handler(message: Message) -> None:
    text = (
        "Bot buyruqlari:\n"
        "/start - Botni ishga tushirish\n"
        "/help - Yordam ko'rsatish\n"
        "Shunchaki matn yozsangiz, bot uni qaytaradi."
    )
    await message.answer(text)

# Har qanday boshqa matnli xabarni qaytaruvchi (echo) funksiya
@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        # Foydalanuvchi nima yozsa, o'ziga qaytaradi
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Kechirasiz, buni qaytara olmayman!")

async def main() -> None:
    # Bot obyektini yaratamiz
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    
    print("Bot yoqildi...")
    # Botni yangi xabarlarni kutish rejimiga o'tkazamiz
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main()) 