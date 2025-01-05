from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

deposit_inline_keyboard = InlineKeyboardMarkup()
button_1 = InlineKeyboardButton(text="Криптовалюта", callback_data="Cryptocurrency")
button_2 = InlineKeyboardButton(text="СБП", callback_data="SBP")
button_3 = InlineKeyboardButton(text='Юмани', callback_data='Umoney')
button_4 = InlineKeyboardButton(text='Тинькофф', callback_data='Tinkoff')
button_5 = InlineKeyboardButton(text='Сбербанк', callback_data='Sberbank')
deposit_inline_keyboard.add(button_1)
deposit_inline_keyboard.add(button_2)
deposit_inline_keyboard.add(button_3)
deposit_inline_keyboard.add(button_4)
deposit_inline_keyboard.add(button_5)
