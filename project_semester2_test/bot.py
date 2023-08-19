import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage


import os
from dotenv import load_dotenv

from utils import check_query
from parse import get_vacancies

load_dotenv()

TOKEN=os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())



@dp.message_handler(commands='start')
async def start_process(message: types.Message):
  await message.answer('Привіт! Введи свій пошуковий запит.')
  
  
@dp.message_handler(content_types='text')
async def get_jobs(message: types.Message):
  if not check_query(message.text):
    await message.answer('Будь ласка, введи пошуковий запит через пробіл.')
  else:
    query = message.text.lower().strip()
    vacancies = get_vacancies(query)
    print(vacancies)
    for vacancy in vacancies:
      title = vacancy['title']
      company = vacancy['company']
      url = vacancy['url']
      description = vacancy['description']
      
      msg = f"<b>Вакансія:</b> {title}\n<b>Компанія:</b> {company}\n<b>Опис:</b> {description}\n\n<b>Посилання:</b> {url}"
      await message.answer(text=msg, parse_mode='html', disable_web_page_preview=True)

  
  
  
if __name__ == "__main__":
  executor.start_polling(dp)