import logging
import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage


import os
from dotenv import load_dotenv
from threading import Thread
import schedule


from utils import check_query
from parse import get_vacancies
from database import Database

load_dotenv()

TOKEN = os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
db = Database()


loop = asyncio.get_event_loop()


@dp.message_handler(commands='start')
async def start_process(message: types.Message):
    user = await db.check_user(message.from_id)
    if not user:
        await db.register_user(
            message.from_user.first_name,
            message.from_user.last_name,
            message.from_user.username,
            message.from_id
        )
        await message.answer('Дякую за реєстрацію!')
    else:
        await message.answer('Ви уже зареєстровані.')
    await message.answer('Введи свій пошуковий запит.')


@dp.message_handler(content_types='text')
async def get_jobs(message: types.Message):
    if not check_query(message.text):
        await message.answer('Будь ласка, введи пошукий запит через пробіли.')
    else:
        query = message.text.lower().strip()
        await db.insert_search_query(message.from_id, query)
        vacancies = get_vacancies(query)
        for vacancy in vacancies:
            title = vacancy['title']
            company = vacancy['company']
            url = vacancy['url']
            description = vacancy['description']

            msg = (f'<b>Вакансія:</b> {title}\n<b>Компанія:</b> {company}\n<b>Опис:</b> {description}\n\n<b'
                   f'>Посилання:</b> {url}')
            await message.answer(text=msg, parse_mode='html', disable_web_page_preview=True)


async def send_notifications():
    users = await db.get_users()
    for user in users:
        last_search = user['search_query']
        notification_title = f'<b>Розсилка</b>\nЗа вашим останнім пошуковим запитом - <b>{last_search}</b> з\'явилися нові вакансії:\n\n'
        await bot.send_message(user['telegram_id'], text=notification_title, parse_mode='html')
        vacancies = get_vacancies(user['search_query'])
        for vacancy in vacancies:
            title = vacancy['title']
            company = vacancy['company']
            url = vacancy['url']
            description = vacancy['description']

            msg = (f'<b>Вакансія:</b> {title}\n<b>Компанія:</b> {company}\n<b>Опис:</b> {description}\n\n<b'
                   f'>Посилання:</b> {url}')
            await bot.send_message(chat_id=user['telegram_id'], text=msg, parse_mode='html', disable_web_page_preview=True)


def notify():
    send_not = asyncio.run_coroutine_threadsafe(send_notifications(), loop)
    send_not.result()


def run_schedule():
    schedule.every().day.at('11:35').do(notify)
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    executor_notifications = Thread(target=run_schedule, args=())
    executor_notifications.start()
    executor.start_polling(dp)