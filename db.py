import sqlite3


def init_db():
    # Подключаемся к базе данных (или создаем ее)
    conn = sqlite3.connect('dogs.db')
    cursor = conn.cursor()

    # Создаем таблицу, если она еще не создана
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dogs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')

    # Сохраняем изменения и закрываем соединение
    conn.commit()
    conn.close()

init_db()