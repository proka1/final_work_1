from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import *
from handlers.start_handler import *
from handlers.info_handler import info_handler_1
from handlers.admin_handler import admin_handler_1
from handlers.deposit_handler import *
from handlers.verification_handler import *
from handlers.find_friend_handler import *
from handlers.check_handler import *

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

start_message_1(dp)
info_handler_1(dp)
admin_handler_1(dp)
deposit_handler_1(dp)
verification_handler_1(dp)
crypto_deposit_1(dp)
sbp_deposit_1(dp)
umoney_deposit_1(dp)
tinkoff_deposit_1(dp)
sberbank_deposit_1(dp)
passport_1(dp)
selfi_1(dp)
collect_passport(dp)
start_message(dp)
find_friend_handler_1(dp)
name_1(dp)
country_1(dp)
city_1(dp)
hotel_1(dp)
phone_number_1(dp)
date_in_1(dp)
date_out_1(dp)
telegram_1(dp)
finish_1(dp)
check_trips_1(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
