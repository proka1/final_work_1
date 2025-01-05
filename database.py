import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Включаем поддержку внешних ключей
cursor.execute("PRAGMA foreign_keys = 1")

# Таблица для верификации
cursor.execute('''
CREATE TABLE IF NOT EXISTS Verification (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE NOT NULL,
    photo_passport TEXT NOT NULL,
    photo_selfie TEXT NOT NULL,
    verification INTEGER NOT NULL
)
''')

# Таблица для поиска
cursor.execute('''
CREATE TABLE IF NOT EXISTS Find (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,  -- Это поле для связи с Verification
    name TEXT NOT NULL,
    country TEXT NOT NULL,
    city TEXT NOT NULL,
    hotel TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    date_in DATE NOT NULL,
    date_out DATE NOT NULL,
    telegram TEXT UNIQUE NOT NULL,
    FOREIGN KEY(user_id) REFERENCES Verification(user_id) ON DELETE CASCADE
)
''')

# Добавление индексов для ускорения запросов (выполняем по одному запросу)
cursor.execute('CREATE INDEX IF NOT EXISTS idx_user_id_verification ON Verification(user_id);')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_user_id_find ON Find(user_id);')

connection.commit()
connection.close()
