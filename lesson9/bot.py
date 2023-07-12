import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from state import *
from aiogram.dispatcher import FSMContext
from config import token

logging.basicConfig(level=logging.INFO)


bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)



@dp.message_handler(commands=['start'])
async def start_command(message: types.Message, state: FSMContext):
    if user(message.from_user.id):
        await message.reply("Ви вже зареєстровані!")
    else:
        await RegistrationStates.step1.set()
        await message.answer("Привіт! Я бот для реєстрацій. Щоб зареєструватися виконай наступні вказівки. \nВведіть своє ім'я:")


@dp.message_handler(state=RegistrationStates.step1)
async def process_step1(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    
    await RegistrationStates.step2.set()
    await message.reply("Добре! Тепер введіть свій вік:")


@dp.message_handler(state=RegistrationStates.step2)
async def process_step2(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    
    await RegistrationStates.step3.set()
    await message.reply("Супер! Наступним кроком поділися своєю адресою:")

@dp.message_handler(state=RegistrationStates.step3)
async def process_step3(message: types.Message, state: FSMContext):
    await state.update_data(address=message.text)
    
    user_data = await state.get_data()
    
    file = open("C:/Python_1y_15_22/lessons_semester II/lesson9/users.txt", "a", encoding='utf-8')
    file.write(f"User ID: {message.from_user.id}\n")
    file.write(f"Name: {user_data['name']}\n")
    file.write(f"Age: {user_data['age']}\n")
    file.write(f"Address: {user_data['address']}\n\n\n")
    
    await state.finish()
    await message.reply("Реєстрація завершена!")

def user(user_id):
    with open('C:/Python_1y_15_22/lessons_semester II/lesson9/users.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip() == f"User ID: {user_id}":
                return True
    return False


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


