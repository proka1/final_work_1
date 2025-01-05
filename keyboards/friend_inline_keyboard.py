from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

friend_inline_keyboard = InlineKeyboardMarkup()
button = InlineKeyboardButton(text='Найти друзей 👫✈️', callback_data='finding')
button_2 = InlineKeyboardButton(text='Найти совпадение', callback_data='Find_people')
friend_inline_keyboard.row(button, button_2)
