from aiogram.types import InputFile
from pathlib import Path
from keyboards.friend_inline_keyboard import friend_inline_keyboard
from keyboards.check_inline_keyboard import find_people_keyboard
from states import FriendState
import sqlite3



# Данный хендлер реагирует на кнопку "Найти друга" чтобы получить основной функционал поиска
def find_friend_handler_1(dp):
    @dp.message_handler(text="Найти друга")
    async def find_friend_handler(message):
        photo_info = InputFile(Path('pictures/friend.jpeg'))
        await message.answer_photo(
            photo_info,
            caption="🌍✨ Найди друзей для путешествий! 👫✈️ Осталось совсем немного действий! 📝 "
                    "Заполни данные, и ты точно найдешь крутых друзей для своего путешествия! 🚀🙌",
            reply_markup=friend_inline_keyboard
        )


def name_1(dp):
    @dp.callback_query_handler(text='finding')
    async def name(call):
        await call.message.answer(
            "Как ваше имя?\n"
            'Пример: Иван'
        )
        await FriendState.name.set()


def country_1(dp):
    @dp.message_handler(state=FriendState.name)
    async def country(message, state):
        await state.update_data(name=message.text)
        await message.answer(
            "В какую страну вы отправялетесь?\n"
            "Пример: Турция"
        )
        await FriendState.country.set()


def city_1(dp):
    @dp.message_handler(state=FriendState.country)
    async def city(message, state):
        await state.update_data(country=message.text)
        await message.answer(
            "В какой город вы отправляетесь?\n"
            'Пример: Стамбул'
        )
        await FriendState.city.set()


def hotel_1(dp):
    @dp.message_handler(state=FriendState.city)
    async def hotel(message, state):
        await state.update_data(city=message.text)
        await message.answer(
            "В каком отеле вы будете проживать?\n"
            'Пример: Hotel Plaza'
        )
        await FriendState.hotel.set()


def phone_number_1(dp):
    @dp.message_handler(state=FriendState.hotel)
    async def phone_number(message, state):
        await state.update_data(hotel=message.text)
        await message.answer(
            'Пожалуйста укажите ваш номер телефона:\n'
            'Формат номера: 89222222222'
        )
        await FriendState.phone_number.set()


def date_in_1(dp):
    @dp.message_handler(state=FriendState.phone_number)
    async def date_in(message, state):
        await state.update_data(phone_number=message.text)
        await message.answer(
            'Пожалуйста, укажите число прибытия:\n'
            'Формат даты: гггг-мм-дд'
        )
        await FriendState.date_in.set()


def date_out_1(dp):
    @dp.message_handler(state=FriendState.date_in)
    async def date_out(message, state):
        await state.update_data(date_in=message.text)
        await message.answer(
            'Пожалуйста, укажите число отбытия:\n'
            'Формат даты: гггг-мм-дд'
        )
        await FriendState.date_out.set()


def telegram_1(dp):
    @dp.message_handler(state=FriendState.date_out)
    async def telegram(message, state):
        await state.update_data(date_out=message.text)
        await message.answer(
            'Пожалуйста, укажите ваш Telegramm\n'
            'Формат: @example'
        )
        await FriendState.telegram.set()


def finish_1(dp):
    @dp.message_handler(state=FriendState.telegram)
    async def finish(message, state):
        await state.update_data(telegram=message.text)

        data = await state.get_data()

        user_id = message.from_user.id
        name = data.get('name')
        country = data.get('country')
        city = data.get('city')
        hotel = data.get('hotel')
        phone_number = data.get('phone_number')
        date_in = data.get('date_in')
        date_out = data.get('date_out')
        telegram = data.get('telegram')

        # Сохраняем данные в базу
        save_find_data(user_id, name, country, city, hotel, phone_number, date_in, date_out, telegram)

        # Завершаем состояние
        await state.finish()

        # Отправляем ответ пользователю
        await message.answer(
            text=f'Ваше имя: {name}\n'
                 f'Страна: {country}\n'
                 f'Город: {city}\n'
                 f'Отель: {hotel}\n'
                 f'Ваш номер телефона: {phone_number}\n'
                 f'Дата заезда: {date_in}\n'
                 f'Дата выезда: {date_out}\n'
                 f'Telegram для связи: {telegram}',
            reply_markup=find_people_keyboard
        )



# Функция сохранения в БД баланса информации об человеке
def save_find_data(user_id, name, country, city, hotel, phone_number, date_in, date_out, telegram):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('''
    INSERT INTO Find (user_id, name, country, city, hotel, phone_number, date_in, date_out, telegram)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (user_id, name, country, city, hotel, phone_number, date_in, date_out, telegram))

    connection.commit()
    connection.close()
