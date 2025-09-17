import asyncio
import logging
from aiogram.filters.command import Command
from aiogram import Bot, Dispatcher, types
from db.database import create_table
from handlers import start, quiz, results


API_TOKEN = ""

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Регистрация хэндлеров
start.register_handlers(dp)
quiz.register_handlers(dp)
results.register_handlers(dp)


@dp.message(Command("myid"))
async def cmd_myid(message: types.Message):
    await message.answer(f"Ваш ID: {message.from_user.id}")

async def main():
    await create_table()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())