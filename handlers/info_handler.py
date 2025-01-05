from aiogram.types import InputFile
from pathlib import Path
from keyboards.start_keyboard import start_keyboard


# Данный хендлер реагирует на кнопку "Информация" чтобы получить информацию о боте
def info_handler_1(dp):
    @dp.message_handler(text="Информация")
    async def info_handler(message):
        photo_info = InputFile(Path('pictures/инфо.jpg'))
        await message.answer_photo(
            photo_info,
            caption=(
                "🌍 **TravelBuddy — найди попутчика мечты!** ✈️\n\n"
                "Ищешь компанию для следующего путешествия? TravelBuddy соединяет "
                "искателей приключений со всего мира! 🗺️\n\n"
                "✨ **Что может бот?**\n"
                "- Поможет найти попутчика с похожими интересами.\n"
                "- Подберёт людей для совместного отдыха. 🚗\n"
                "- Упростит организацию совместных поездок.\n\n"
                "💬 **Общайся, планируй и отправляйся в путь с новыми друзьями!**\n"
                "TravelBuddy — твой путеводитель в мир дружбы и открытий. 🚀"
            ),
            parse_mode="Markdown",  # Указываем режим Markdown для форматирования
            reply_markup=start_keyboard
        )
