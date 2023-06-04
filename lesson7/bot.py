from aiogram import types, Dispatcher, Bot, executor
from inline import first
from default import colors as c
import asyncio



TOKEN = "5991419295:AAEYklQPfg2wTaEx8zXZfkrrwQnUOuWQsXI"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(text = "Hello!")



@dp.message_handler(content_types='text')
async def echo(message: types.Message):
    await message.answer(text='Press this button!', reply_markup=first)

# @dp.callback_query_handler(text='first')
# async def second_step(Callback: types.CallbackQuery):
#     await Callback.message.answer('1**3')

# @dp.callback_query_handler(text='second')
# async def second_step(Callback: types.CallbackQuery):
#     await Callback.message.answer('8**')


# @dp.callback_query_handler(text='third')
# async def second_step(Callback: types.CallbackQuery):
#     await Callback.message.answer('27')









if __name__ == "__main__":
    executor.start_polling(dp)
