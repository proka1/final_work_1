from aiogram.dispatcher.filters.state import State, StatesGroup


# Классы для собра информации от человека из чат бота


class VerificationState(StatesGroup):
    selfi = State()
    passport = State()


class FriendState(StatesGroup):
    name = State()
    country = State()
    city = State()
    hotel = State()
    phone_number = State()
    date_in = State()
    date_out = State()
    telegram = State()
