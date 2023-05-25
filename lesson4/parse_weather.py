import requests
import logging
from aiogram import Dispatcher, executor, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Command


TOKEN = '5991419295:AAEYklQPfg2wTaEx8zXZfkrrwQnUOuWQsXI'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)


dp = Dispatcher(bot, storage=MemoryStorage())



async def parse_weather(city: str):
    api_key = '9fab472534148617ca02942ffad3c402'
    url = f'https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}'
    response = requests.get(url)
    return response.json()




@dp.message_handler(Command('start'))
async def start(message: types.Message):
    await message.answer("Привіт! Введи назву міста, щоб дізнатися погоду.")



@dp.message_handler()
async def info(message: types.Message):
    city = message.text
    weather = await parse_weather(city)
    if 'main' in weather:
        temp = round(weather['main']['temp'] - 273, 2)
        temp_min = round(weather['main']['temp_min'] - 273, 2)
        temp_max = round(weather['main']['temp_max'] - 273, 2)
        await message.answer(f'Місто - {city}\nТемпература - {temp} °C\nМінімальна температура - {temp_min}\nМаксимальна температура - {temp_max}')
    else:
        await message.answer('Ти увів назву міста не правильно. Спробуй ще раз.')

    


if __name__ == '__main__':
    executor.start_polling(dp)