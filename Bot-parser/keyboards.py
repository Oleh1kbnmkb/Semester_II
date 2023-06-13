from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

news = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Політичні новини')],
        [KeyboardButton(text='Економічні новини')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

choise = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1', callback_data='1'),
            InlineKeyboardButton(text='2', callback_data='2'),
            InlineKeyboardButton(text='3', callback_data='3'),
            InlineKeyboardButton(text='4', callback_data='4'),
            InlineKeyboardButton(text='5', callback_data='5')
        ],
        [
            InlineKeyboardButton(text='Завершити перегляд', callback_data='0')
        ]
    ]
    
)