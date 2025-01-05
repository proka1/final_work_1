from keyboards.start_keyboard import start_keyboard
from aiogram.types import InputFile
from pathlib import Path


# Данный хендлер реагирует на команду "/start" чтобы начать работу с ботом
def start_message_1(dp):
    @dp.message_handler(commands=['start'])
    async def start_message(message):
        photo_start = InputFile(Path("pictures/111.jpg"))
        await message.answer_photo(
            photo_start,
            caption="**🌟 Добро пожаловать!**\n\n"
                    "Если вы мечтаете найти надёжного попутчика для увлекательного путешествия, то этот бот — именно то, что вам нужно! 🚀\n\n"
                    "Вместе планировать поездки проще, интереснее и веселее. Давайте искать приключения вместе! 🌍✈️",
            parse_mode='Markdown',
            reply_markup=start_keyboard
        )


def start_message(dp):
    @dp.message_handler(text='Вернуться в основное меню')
    async def start_message_2(message):
        photo_start = InputFile(Path("pictures/111.jpg"))
        await message.answer_photo(
            photo_start,
            caption="Если вы в поиске партнера для совместного путешествия, этот бот для вас!",
            reply_markup=start_keyboard)
