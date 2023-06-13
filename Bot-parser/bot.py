import logging
import datetime
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import os
from dotenv import load_dotenv

from keyboards import *
from parse_news import parse_default_news, parse_economic_news


load_dotenv()

TOKEN=os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())



@dp.message_handler(commands='start')
async def start_process(message: types.Message):
    await message.answer('Привіт! Щоб переглянути останні новини, натисни кнопку:', reply_markup=news)


@dp.message_handler()
async def get_news(message:types.Message, state: FSMContext):
    if message.text == 'Політичні новини':
        await message.answer('Новини були отримані. Обирай їх за допомогою кнопки:', reply_markup=choise)
        await state.set_state('read_default_news')
    elif message.text == 'Економічні новини':
        await message.answer('Новини були отримані. Обирай їх за допомогою кнопки:', reply_markup=choise)
        await state.set_state('read_economic_news')


@dp.callback_query_handler(state='*', text='0')
async def end_reading(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('Перегляд завершено. Щоб прочитати новини ще раз - напишіть /start')
    await state.finish()


@dp.callback_query_handler(state='read_default_news')
async def read_default_news(callback: types.CallbackQuery, state: FSMContext):
    news = parse_default_news()
    if callback.data == '1':
        title = news[0]['title']
        articles = news[0]['text']
        source = news[0]['link']
        await callback.message.answer(
            f'<b>{title}</b>\n'
            f'{articles}\n'
            f'Джерело: {source}\n'
            f'Чи бажаєте прочитати щось інше?', reply_markup=choise, parse_mode='html'
        )
    elif callback.data == '2':
        title = news[1]['title']
        articles = news[1]['text']
        source = news[1]['link']
        await callback.message.answer(
            f'<b>{title}</b>\n'
            f'{articles}\n'
            f'Джерело: {source}\n'
            f'Чи бажаєте прочитати щось інше?', reply_markup=choise, parse_mode='html'
        )
    elif callback.data == '3':
      title = news[2]['title']
      articles = news[2]['text']
      source = news[2]['link']
      await callback.message.answer(
          f'<b>{title}</b>\n'
          f'{articles}\n'
          f'Джерело: {source}\n'
          f'Чи бажаєте прочитати щось інше?', reply_markup=choise, parse_mode='html'
      )
    elif callback.data == '4':
      title = news[3]['title']
      articles = news[3]['text']
      source = news[3]['link']
      await callback.message.answer(
          f'<b>{title}</b>\n'
          f'{articles}\n'
          f'Джерело: {source}\n'
          f'Чи бажаєте прочитати щось інше?', reply_markup=choise, parse_mode='html'
      )
    elif callback.data == '5':
      title = news[4]['title']
      articles = news[4]['text']
      source = news[4]['link']
      await callback.message.answer(
          f'<b>{title}</b>\n'
          f'{articles}\n'
          f'Джерело: {source}\n'
          f'Чи бажаєте прочитати щось інше?', reply_markup=choise, parse_mode='html'
      )


@dp.callback_query_handler(state='read_economic_news')
async def read_economic_news(callback: types.CallbackQuery):
    news = parse_economic_news()
    if callback.data == '1':
        title = news[0]['title']
        articles = news[0]['text']
        source = news[0]['link']
        await callback.message.answer(
            f'<b>{title}</b>\n'
            f'{articles}\n'
            f'Джерело: {source}\n'
            f'Чи бажаєте прочитати щось інше?', reply_markup=choise, parse_mode='html'
        )
    elif callback.data == '2':
        title = news[1]['title']
        articles = news[1]['text']
        source = news[1]['link']
        await callback.message.answer(
            f'<b>{title}</b>\n'
            f'{articles}\n'
            f'Джерело: {source}\n'
            f'Чи бажаєте прочитати щось інше?', reply_markup=choise, parse_mode='html'
        )
    elif callback.data == '3':
      title = news[2]['title']
      articles = news[2]['text']
      source = news[2]['link']
      await callback.message.answer(
          f'<b>{title}</b>\n'
          f'{articles}\n'
          f'Джерело: {source}\n'
          f'Чи бажаєте прочитати щось інше?', reply_markup=choise, parse_mode='html'
      )
    elif callback.data == '4':
      title = news[3]['title']
      articles = news[3]['text']
      source = news[3]['link']
      await callback.message.answer(
          f'<b>{title}</b>\n'
          f'{articles}\n'
          f'Джерело: {source}\n'
          f'Чи бажаєте прочитати щось інше?', reply_markup=choise, parse_mode='html'
      )
    elif callback.data == '5':
      title = news[4]['title']
      articles = news[4]['text']
      source = news[4]['link']
      await callback.message.answer(
          f'<b>{title}</b>\n'
          f'{articles}\n'
          f'Джерело: {source}\n'
          f'Чи бажаєте прочитати щось інше?', reply_markup=choise, parse_mode='html'
      )
      
    
        
        
        
        

  
if __name__ == '__main__':
    executor.start_polling(dp)