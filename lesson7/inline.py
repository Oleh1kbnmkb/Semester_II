from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

first = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1', callback_data='1'),
            InlineKeyboardButton(text='2', callback_data='2'),
            InlineKeyboardButton(text='3', callback_data='3')
        ],
        [
            InlineKeyboardButton(text='😡BIG AGGRESSIVE BUTTON', callback_data='0')
        ],
        [
            InlineKeyboardButton(text='4', callback_data='4'),
            InlineKeyboardButton(text='5', callback_data='5'),
            InlineKeyboardButton(text='6', callback_data='6')
        ]
    ]
)


social_networks = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Facebook', url='https://facebook.com')
        ],
        [
            InlineKeyboardButton(text='Instagram', url='https://instagram.com')
        ],
        [
            InlineKeyboardButton(text='Twitter', url='https://twitter.com')
        ]
    ]
)
