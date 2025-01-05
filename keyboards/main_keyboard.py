from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text="Найти друга")
button_2 = KeyboardButton(text='Вернуться в основное меню')
main_keyboard.row(button_1, button_2)