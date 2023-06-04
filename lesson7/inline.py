from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

first = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text = '1', callback_data='first')],
        [InlineKeyboardButton(text = '2', callback_data='second')],
        [InlineKeyboardButton(text = '3', callback_data='third')]

    ]
)