import os
import sqlite3


def create_request(column_name_list, name_table):
    """Функция для создания запроса в БД для создания таблицы """
    # print('зашли в функцию для создания таблицы ')

    field_definitions = ', '.join(column_name_list)
    query = f'CREATE TABLE {name_table} ({field_definitions})'
    # Чекпоинт для проверки запроса
    # print(query)
    return query


def insert_data(key_list, value_list, name_table):
    """Для создания запроса заполнения\дописывания БД"""
    print('зашли в функцию для заполнения таблиц ')
    tab_key_list = ', '.join(key_list)
    query_insert = f'INSERT INTO {name_table} ({tab_key_list}) VALUES{tuple(value_list)}'
    # Чекпоинт для проверки запроса
    # print(query_insert)
    return query_insert


def check_db(db_name, request):
    """Функция отправки запросов в БД, при необходимости БД создается"""

    con = sqlite3.connect(db_name + '.db')  # Обращаемся к БД , создастся автоматически
    cur = con.cursor()  # открываем курсор

    cur.execute(request)

    con.commit()  # отправка в БД
    con.close()  # Закрываем курсор БД

    # Отправляем команду в БД c обработкой ошибки
    # try:
    #     cur.execute(request)
    #
    #     con.commit()  # отправка в БД
    #     con.close()  # Закрываем курсор БД
    # except sqlite3.OperationalError:
    #     print('Что то не то передаем')

    # Чек поинт Подтверждение в консоле что прошло без ошибок
    print(f'Вышли из БД')










