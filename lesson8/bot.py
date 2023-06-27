import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from steps import TrafficLights, Flow
from keyboards import lights, redkb, yellowkb, greenkb, traffic_off_kb, request_contact
from config import TOKEN


logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands='start')
async def start_process(message: types.Message):
    await message.answer('Привіт! Я бот - із машинами станів. Для реєстрації - поширь свій контакт.', reply_markup=request_contact)


@dp.message_handler(commands='start', state=Flow.RegisterState)
async def start_processor(message: types.Message):
    await message.answer('Ви уже зареєстровані')



@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def registration(message: types.Message):
    if message.from_user != message.contact.user_id:
        await message.answer('Ви надіслали не ваш контакт')

    full_name  = message.contact.full_name
    phone = message.contact.phone_number
    await Flow.RegisterState.set()
        
    await message.answer(f"{full_name}, Тепер напишіть Ваше ім'я\nВаш номер - {phone}")
    
    
@dp.message_handler(content_types='text', state=Flow.RegisterState)
async def get_name(message: types.Message):
    await message.answer(f"{message.text}, дякую за реєстрацію")



@dp.message_handler(commands='traffic_light_on')
async def traffic_light_on(message: types.Message):
    await TrafficLights.StateOn.set()
    await message.answer('Ви увімкнули світлофор🚦\n'
                         'Тепер ви можете увімкнути будь-яке світло:',
                         reply_markup=lights)


@dp.message_handler(text='Червоний 🔴', state=TrafficLights.StateOn)
async def traffic_red(message: types.Message):
    await TrafficLights.StateRed.set()
    await message.answer('Ви увімкнули червоне світло 🔴\n'
                         'Тепер ви можете увімкнути жовте:',
                         reply_markup=yellowkb)
    

@dp.message_handler(text='Жовтий 🟡', state=TrafficLights.StateRed)
async def traffic_yellow(message: types.Message):
    await TrafficLights.StateYellow.set()
    await message.answer('Ви увімкнули жовте світло 🟡\n'
                         'Тепер ви можете увімкнути зелене:',
                         reply_markup=greenkb)


@dp.message_handler(text='Зелений 🟢', state=TrafficLights.StateYellow)
async def traffic_green(message: types.Message):
    await TrafficLights.StateGreen.set()
    await message.answer('Ви увімкнули зелене світло 🟢\n'
                         'Тепер ви можете вимкнути світлофор:',
                         reply_markup=traffic_off_kb)
    

@dp.message_handler(text='Вимкнути', state=TrafficLights.StateGreen)
async def traffic_off(message: types.Message):
    await dp.current_state().reset_state()
    await message.answer('Ви вимкнули світлофор.\n'
                         'Щоб увімкнути - /traffic_light_on')


if __name__=='__main__':
    executor.start_polling(dp)