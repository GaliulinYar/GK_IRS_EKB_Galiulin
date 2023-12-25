# Проверка результатов
import sqlite3

from work_db import check_db


# ТЕСТЫ СОЗДАНИЯ
def check_db_test():
    check_db('sometable', 'OrmModel', some_field_1='TEXT', some_field_2='INTEGER', some_field_3='REAL')

    con = sqlite3.connect('sometable.db')
    cur = con.cursor()
    res = cur.execute('SELECT * FROM OrmModel')
    res.fetchall()
    print(res.fetchall())


# # Вставка данных
# data_to_insert = {'some_field_1': 'Value1', 'some_field_2': 42, 'some_field_3': 3.14}
# insert_data('sometable', 'OrmModel', data_to_insert)
#
# Проверка результатов
def rezult():
    con = sqlite3.connect('SomeDB.db')
    cur = con.cursor()
    res = cur.execute('SELECT * FROM SomeTable')
    result = res.fetchall()

    con.close()
    return result



def get_table_names():
    con = sqlite3.connect('SomeDB.db')
    cur = con.cursor()

    # Выполнение запроса
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

    # Извлечение результатов
    table_names = cur.fetchall()

    con.close()

    return table_names


def get_table_columns(table_name):
    con = sqlite3.connect('SomeDB.db')
    cur = con.cursor()

    # Выполнение запроса для получения информации о столбцах таблицы
    cur.execute(f"PRAGMA table_info({table_name});")

    # Извлечение результатов
    columns_info = cur.fetchall()

    con.close()

    # Возвращаем только имена столбцов
    column_names = [column[1] for column in columns_info]

    return column_names


print(get_table_names())

print(get_table_columns('SomeTable'))
print(rezult())

