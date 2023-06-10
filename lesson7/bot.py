import logging
from aiogram import types, Dispatcher, Bot, executor
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from inline import first, social_networks 
from default import colors, request_contact

logging.basicConfig(level=logging.INFO)

bot = Bot('5991419295:AAEYklQPfg2wTaEx8zXZfkrrwQnUOuWQsXI')
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(text='Hello!')


@dp.message_handler(text='I wanna press button.')
async def echo(message: types.Message):
    await message.answer(text='Press this button!', reply_markup=first)


@dp.callback_query_handler()
async def second_step(callback: types.CallbackQuery):
    await callback.message.answer('You\'ve already pressed.')


@dp.message_handler(commands='choose_color')
async def choose_color(message: types.Message):
    await message.answer('Choose your color.', reply_markup=colors)


@dp.message_handler(commands='give-info')
async def get_contact(message: types.Message):
    await message.answer('Gimme your information!', reply_markup=request_contact)


@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def use_contact_info(message: types.Message):
    if message.contact.user_id != message.from_id:
        await message.answer('That is not your number.')
    else:
        await message.answer(f'Hello, {message.contact.phone_number}')


@dp.message_handler(commands='socials')
async def get_socials(message: types.Message):
    await message.answer('Available socials:', reply_markup=social_networks)


if __name__ == '__main__':
    executor.start_polling(dp)