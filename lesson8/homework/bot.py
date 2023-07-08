import os
import logging
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

load_dotenv()

TOKEN=os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
  await message.answer("Привіт! Для реєстрації зробіть декілька кроків.")
  
  
@dp.message_handler()
async def echo(message: types.Message):
  await message.answer(message.text)



if __name__ == "__main__":
  executor.start_polling(dp)