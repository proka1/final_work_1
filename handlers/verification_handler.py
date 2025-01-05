from aiogram.types import InputFile, ContentType
from pathlib import Path
from keyboards.verification_inline_keyboard import passport_inline_keyboard
from keyboards.start_keyboard_without_verification import start_keyboard_without_verification
from keyboards.start_keyboard import start_keyboard
from states import VerificationState
import asyncio
import sqlite3


def verification_handler_1(dp):
    @dp.message_handler(text="Верификация")
    async def verification_handler(message):
        user_id = message.from_user.id

        # Проверяем статус верификации
        verification_status = get_verification_status(user_id)

        if verification_status:
            # Пользователь уже верифицирован
            await message.answer(
                "Вы уже прошли верификацию!\n"
                "Теперь вы можете искать друзей для путешествий.",
                reply_markup=start_keyboard_without_verification  # Клавиатура для верифицированных
            )
        else:
            # Пользователь не верифицирован
            photo_info = InputFile(Path('pictures/verif.png'))
            await message.answer_photo(
                photo_info,
                caption="Пожалуйста, пройдите верификацию, чтобы получить доступ к нашему сервису по поиску партнеров "
                        "для путешествий",
                reply_markup=passport_inline_keyboard  # Клавиатура для начала процесса верификации
            )


def passport_1(dp):
    @dp.callback_query_handler(text='passport')
    async def passport(call):
        photo_info = InputFile(Path('pictures/passport.png'))
        await call.message.answer_photo(
            photo_info,
            caption='Пожалуйста, загрузите фото паспорта в соответствии с описанием на фотографии',
        )
        # Устанавливаем состояние для ожидания фото паспорта
        await VerificationState.passport.set()


def collect_passport(dp):
    @dp.message_handler(content_types=[ContentType.PHOTO, ContentType.DOCUMENT], state=VerificationState.passport)
    async def collect_passport_photo(message, state):
        # Проверяем, что это фото
        if message.content_type == ContentType.PHOTO:
            passport_photo = message.photo[-1]  # Берём последнее фото (наибольшего разрешения)
        elif message.content_type == ContentType.DOCUMENT:
            passport_photo = message.document  # Обрабатываем документ как файл
        else:
            # Если тип не фото и не документ, то просто игнорируем
            return

        # Сохраняем file_id в FSMContext
        photo_file_id = passport_photo.file_id
        await state.update_data(passport_photo_id=photo_file_id)

        # Переходим к следующему шагу
        photo_info = InputFile(Path('pictures/selfi.jpg'))
        await message.answer_photo(
            photo_info,
            caption='Пожалуйста, загрузите селфи в соответствии с описанием на фотографии',
        )
        await VerificationState.selfi.set()


def selfi_1(dp):
    @dp.message_handler(content_types=[ContentType.PHOTO, ContentType.DOCUMENT], state=VerificationState.selfi)
    async def collect_selfie(message, state):
        # Проверяем, что это фото
        if message.content_type == ContentType.PHOTO:
            selfie_photo = message.photo[-1]
        elif message.content_type == ContentType.DOCUMENT:
            selfie_photo = message.document  # Обрабатываем документ как файл
        else:
            # Если тип не фото и не документ, то просто игнорируем
            return

        # Сохраняем file_id в FSMContext
        photo_file_id = selfie_photo.file_id
        await state.update_data(selfie_photo_id=photo_file_id)

        photo_info_wait = InputFile(Path('pictures/wait.jpg'))
        photo_success_wait = InputFile(Path('pictures/verif.jpg'))
        await message.answer_photo(
            photo_info_wait,
            caption='Пожалуйста, ожидайте проверки документов! Это займет не больше 10 секунд!'
        )
        await asyncio.sleep(3)
        data = await state.get_data()
        # Формируем строку с данными, которые мы собрали
        passport_photo_id = data.get('passport_photo_id')
        selfie_photo_id = data.get('selfie_photo_id')
        # Получаем user_id из message
        user_id = message.from_user.id

        # Сохраняем данные в базу данных
        save_verification_data(user_id, passport_photo_id, selfie_photo_id)

        await state.finish()
        keyboard = get_keyboard_for_user(user_id)
        await message.answer_photo(
            photo_success_wait,
            caption='Верификация успешно пройдена!\n'
                    'Вы можете продолжить поиск друзей по путешествию!',
            reply_markup=keyboard
        )


def save_verification_data(user_id, passport_photo_id, selfie_photo_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    try:
        cursor.execute('''
        INSERT INTO Verification (user_id, photo_passport, photo_selfie, verification)
        VALUES (?, ?, ?, ?)
        ''', (user_id, passport_photo_id, selfie_photo_id, 1))
    except sqlite3.IntegrityError:
        # Если запись уже существует, просто обновляем данные
        cursor.execute('''
        UPDATE Verification
        SET photo_passport = ?, photo_selfie = ?, verification = ?
        WHERE user_id = ?
        ''', (passport_photo_id, selfie_photo_id, 1, user_id))

    connection.commit()
    connection.close()


def get_verification_status(user_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # Проверяем статус верификации пользователя
    cursor.execute('SELECT verification FROM Verification WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()

    connection.close()

    # Если запись существует и значение verification == 1, пользователь верифицирован
    return result and result[0] == 1


def get_keyboard_for_user(user_id):
    # Проверяем статус верификации
    verification_status = get_verification_status(user_id)

    if verification_status:
        # Пользователь верифицирован, показываем клавиатуру с кнопкой "Найти друга"
        return start_keyboard_without_verification
    else:
        # Пользователь не верифицирован, показываем клавиатуру с кнопкой "Верификация"
        return start_keyboard
