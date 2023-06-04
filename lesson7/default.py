from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

colors = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = 'Red')
        ],
        [
            KeyboardButton(text = 'Blue')
        ],
        [
            KeyboardButton(text = 'Black')
        ]
    ]
)


request_contact = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Share my contact.', request_contact=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)