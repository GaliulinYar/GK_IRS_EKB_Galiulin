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
    tab_key_list = ', '.join(key_list)  # Собираем название столбцов
    query_insert = f'INSERT INTO {name_table} ({tab_key_list}) VALUES{tuple(value_list)}'
    # Чекпоинт для проверки запроса
    # print(query_insert)
    return query_insert


def check_db(db_name, request):
    """Функция отправки запросов в БД, при необходимости БД создается"""

    con = sqlite3.connect(db_name + '.db')  # Обращаемся к БД , создастся автоматически
    cur = con.cursor()  # открываем курсор

    # Отправляем команду в БД c обработкой ошибки
    try:
        cur.execute(request)

        con.commit()  # отправка в БД
        con.close()  # Закрываем курсор БД
    except sqlite3.OperationalError:
        print('Что то не так, обратитесь к разработчику')

    # Чек поинт Подтверждение в консоле что прошло без ошибок
    print(f'Вышли из БД')


def search_filter_request(db_name, table_name, column_name, query_name):
    """Функция для вывода определенных значений таблицы, фильтрация"""
    con = sqlite3.connect(db_name + '.db')
    cur = con.cursor()
    if column_name:  # Если имя колонки есть
        search_request = f'SELECT * FROM {table_name} WHERE {column_name} = ?'
        res = cur.execute(search_request, (query_name,))
    else:  # Если имя колонки None
        search_request = f'SELECT * FROM {table_name}'
        res = cur.execute(search_request)
    print(res.fetchall())  # вывода результат в консоль
    con.close()

    return print('Вот ваш результат поиска')  # чек поинт что все прошло





