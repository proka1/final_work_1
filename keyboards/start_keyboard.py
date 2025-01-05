from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text="Информация")
button_2 = KeyboardButton(text='Связь с администратором')
button_3 = KeyboardButton(text='Поддержка разработчиков')
button_4 = KeyboardButton(text='Верификация')
start_keyboard.row(button_1, button_2)
start_keyboard.row(button_3, button_4)
