from aiogram.types import InputFile
from pathlib import Path
from keyboards.start_keyboard import start_keyboard

# Данный хендлер реагирует на кнопку "Связь с администратором" чтобы получить информацию об админе
def admin_handler_1(dp):
    @dp.message_handler(text="Связь с администратором")
    async def admin_handler(message):
        photo_info = InputFile(Path('pictures/admin.jpeg'))
        await message.answer_photo(
            photo_info,
            caption="📩 **Связь с администратором**\n"
            "Если у вас возникли вопросы, предложения или нужна помощь — напишите администратору! 👇\n\n"
            "👨‍💻 **Админ:** [@sane4ek24](https://t.me/sane4ek24)\n\n"
            "Мы всегда готовы помочь и сделать ваше путешествие лучше! 🌟",
            parse_mode="Markdown",
            reply_markup=start_keyboard
        )