from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

passport_inline_keyboard = InlineKeyboardMarkup()
button_1 = InlineKeyboardButton(text='Верифицироваться', callback_data='passport')
passport_inline_keyboard.add(button_1)
