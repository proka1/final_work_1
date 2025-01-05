from aiogram.types import InputFile
from pathlib import Path
from keyboards.deposit_inline_keyboard import deposit_inline_keyboard


# Данный хендлер реагирует на кнопку "Поддержка разработчиков" чтобы получить методы депозита через ссылку
def deposit_handler_1(dp):
    @dp.message_handler(text="Поддержка разработчиков")
    async def deposit_handler(message):
        photo_info = InputFile(Path('pictures/deposit.jpeg'))
        await message.answer_photo(
            photo_info,
            caption=(
                "🌟 **Дорогие друзья!** 🌟\n"
                "Ваши донаты — это не просто поддержка, это настоящая **инвестиция в развитие нашего проекта**. 🙌\n"
                "Благодаря вашей помощи мы сможем продолжать радовать вас новыми идеями, улучшениями"
                " и полезными функциями. 🚀✨\n\n"
                "💡 **Почему это важно?**\n"
                "Каждый ваш вклад помогает нам:\n"
                "- 🛠️ Развивать новые функции.\n"
                "- 📈 Улучшать качество сервиса.\n"
                "- 💬 Быть ближе к каждому из вас.\n\n"
                "🔗 **Выберите удобный способ поддержки**:\n"
                "💳 Карта / 📱 QR-код / 🌐 Онлайн-платежи — всё просто и быстро!\n\n"
                "❤️ **Мы ценим каждого из вас и благодарим за вашу щедрость!** Вместе мы "
                "сделаем этот проект ещё лучше. 💪✨"
            ),
            reply_markup=deposit_inline_keyboard
        )


def crypto_deposit_1(dp):
    @dp.callback_query_handler(text='Cryptocurrency')
    async def crypto_deposit(call):
        await call.message.answer(
            'Для пополнения криптовалютой пройдите по ссылке:<a href="https://example.com">ссылка</a>',
            parse_mode='HTML')
        await call.answer()


def sbp_deposit_1(dp):
    @dp.callback_query_handler(text='SBP')
    async def sbp_deposit(call):
        await call.message.answer(
            'Для пополнения по Системе Быстрых Платежей пройдите по ссылке:<a href="https://example.com">ссылка</a>',
            parse_mode='HTML')
        await call.answer()


def umoney_deposit_1(dp):
    @dp.callback_query_handler(text='Umoney')
    async def umoney_deposit(call):
        await call.message.answer(
            'Для пополнения с помощью Юмани пройдите по ссылке:<a href="https://example.com">ссылка</a>',
            parse_mode='HTML')
        await call.answer()


def tinkoff_deposit_1(dp):
    @dp.callback_query_handler(text='Tinkoff')
    async def tinkoff_deposit(call):
        await call.message.answer(
            'Для пополнения с помощью Tinkoff пройдите по ссылке:<a href="https://example.com">ссылка</a>',
            parse_mode='HTML')
        await call.answer()


def sberbank_deposit_1(dp):
    @dp.callback_query_handler(text='Sberbank')
    async def sberbank_deposit(call):
        await call.message.answer(
            'Для пополнения с помощью Sberbank пройдите по ссылке:<a href="https://example.com">ссылка</a>',
            parse_mode='HTML')
        await call.answer()
