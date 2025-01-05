from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_keyboard_without_verification = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text="Информация")
button_2 = KeyboardButton(text='Связь с администратором')
button_3 = KeyboardButton(text='Поддержка разработчиков')
button_4 = KeyboardButton(text='Найти друга')
start_keyboard_without_verification.row(button_1, button_2)
start_keyboard_without_verification.row(button_3, button_4)
