import os
import logging
import psycopg2
from database import*
from dotenv import load_dotenv
from aiogram.dispatcher import FSMContext as FSM
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage



load_dotenv()


logging.basicConfig(level=logging.INFO)


TOKEN = os.getenv('TOKEN')



connection = psycopg2.connect(
    host='ep-empty-sea-524845.eu-central-1.aws.neon.tech',
    port='5432',
    database='neondb',
    user='op663246',
    password='5ELlvIaWx3JK'
)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
db = Database()







async def login_user(username: str, password: str) -> bool:
    try:
        connection = psycopg2.connect(
            host='ep-empty-sea-524845.eu-central-1.aws.neon.tech',
            port='5432',
            database='neondb',
            user='op663246',
            password='5ELlvIaWx3JK'
        )

        cursor = connection.cursor()

        query = 'SELECT * FROM users WHERE username = %s AND password = %s'
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        cursor.close()
        connection.close()

        if user:
            return True
        else:
            return False

    except Exception as error:
        print('Error occurred while checking login credentials:', error)
        return False





@dp.message_handler(commands=['start'])
async def login_command(message: types.Message):
    await message.answer("Вітаємо! Введіть своє ім'я:")
    await Login.set_username.set()



@dp.message_handler(state=Login.set_username)
async def process_login(message: types.Message, state: FSM):
    async with state.proxy() as data:
      data['username'] = message.text
    await message.answer('Добре. Тепер введіть свій пароль: ')
    await Login.set_password.set()
    


@dp.message_handler(state=Login.set_password)
async def process_password(message: types.Message, state: FSM):
    async with state.proxy() as data:
        username = data['username']
        password = message.text
    if await login_user(username, password):
        await message.answer("Ви увійшли в систему!")
    else:
        await message.answer("Такого користувача не існує в базі даних, просимо вас зареєструватися по команді /register")
    await state.finish()
    
    
    
    
@dp.message_handler(commands=['register'])
async def start(message: types.Message):
    await message.answer('Welcome!\nPlease enter your name.')
    await Registration.set_name.set()


@dp.message_handler(state=Registration.set_name)
async def set_name(message: types.Message, state: FSM):
    async with state.proxy() as data:
        data['username'] = message.text
    await message.answer('Nice!\nNow enter your password.')
    await Registration.set_age.set()


@dp.message_handler(state=Registration.set_age)
async def set_age(message: types.Message, state: FSM):
    async with state.proxy() as data:
        data['password'] = message.text
    await message.answer('Good!\nNow enter your email.')
    await Registration.set_email.set()


@dp.message_handler(state=Registration.set_email)
async def set_email(message: types.Message, state: FSM):
    async with state.proxy() as data:
        name = data['username']
        age = data['password']
        email = message.text
    await db.register_student(name, age, email)
    await message.answer('You have been successfully registered.')
    await state.finish()





if __name__ == "__main__":
  executor.start_polling(dp, skip_updates=True)
