import os
import sqlite3


def check_db(db_name, request):
    """Функция проверки существование БД, при необходимости БД создается"""
    db_filename = f'{db_name}.db'  # Составляем имя БД
    if os.path.exists(db_filename):  # проверяем существование пути
        print(f'БД с имененм {db_name} существует')  # Подтверждение в консоле
    else:
        con = sqlite3.connect(db_name + '.db')  # Обращаемся к БД , создастся автоматически
        cur = con.cursor()  # открываем курсор

        # Создание таблицы с динамически определенными полями
        cur.execute(request)

        con.commit()  # отправка в БД
        con.close()  # Закрываем курсор БД

        print(f'БД {db_name} создали')  # Подтверждение в консоле










