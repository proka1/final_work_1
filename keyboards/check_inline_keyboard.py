from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


find_people_keyboard = InlineKeyboardMarkup()
button_3 = InlineKeyboardButton(text='Найти совпадение', callback_data='Find_people')
find_people_keyboard.add(button_3)
