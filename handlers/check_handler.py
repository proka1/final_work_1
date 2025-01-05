import sqlite3



def check_overlapping_trips(user_id):
    """
    Проверка пересечений поездок.
    Возвращает список совпадений, если есть совпадения, иначе пустой список.
    """
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # SQL-запрос для поиска всех пересечений поездок, исключая самого пользователя
    query = """
    SELECT t2.user_id, t2.name, t2.phone_number, t2.telegram
    FROM Find t1
    JOIN Find t2
      ON t1.user_id != t2.user_id
      AND t1.country = t2.country
      AND t1.city = t2.city
      AND t1.date_in <= t2.date_out
      AND t1.date_out >= t2.date_in
    WHERE t1.user_id = ?
    """

    cursor.execute(query, (user_id,))
    results = cursor.fetchall()  # Получаем все записи
    conn.close()  # Закрываем соединение с БД

    overlaps = []
    for row in results:
        overlaps.append({
            'user_id': row[0],
            'name': row[1],
            'phone_number': row[2],
            'telegram': row[3]
        })

    return overlaps  # Возвращаем список совпадений


def check_trips_1(dp):
    @dp.callback_query_handler(text='Find_people')
    async def check_trips(callback_query):
        user_id = callback_query.from_user.id  # Получаем user_id из callback_query

        # Проверяем наличие совпадений
        overlaps = check_overlapping_trips(user_id)

        if overlaps:
            # Если есть совпадения, отправляем информацию о каждом человеке
            for user_info in overlaps:
                await callback_query.message.answer(
                    text=f"Найдено совпадение.\n"
                         f"Имя: {user_info['name']}\n"
                         f"Телеграм: {user_info['telegram']}\n"
                         f"Номер для связи: {user_info['phone_number']}"
                )
        else:
            # Если совпадений нет
            await callback_query.message.answer(
                text="К сожалению, совпадений не найдено.\nПожалуйста, подождите и повторите попытку позже."
            )
