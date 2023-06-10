from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

colors = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🔴Red'),
            KeyboardButton(text='💚Green'),
            KeyboardButton(text='🟦Blue')
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)


request_contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Share my contact.', request_contact=True),
            KeyboardButton(text='Share my location.', request_location=True)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)