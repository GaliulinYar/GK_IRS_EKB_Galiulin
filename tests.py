# Проверка результатов
import sqlite3

from class_file import OrmModel, OrmText

db_name = 'Test_DB.db'
table_name = 'SomeTable'


# Проверка , какие таблицы созданы
# def get_table_names(db_name):
#     con = sqlite3.connect(db_name)
#     cur = con.cursor()
#
#     # Выполнение запроса
#     cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
#     # Извлечение результатов
#     table_names = cur.fetchall()
#     con.close()
#
#     return table_names
#
#
# print(get_table_names(db_name))


# Посмотреть информацию о столбиках таблицы
# def get_table_columns(table_name):
#     con = sqlite3.connect('Test_DB.db')
#     cur = con.cursor()
#     # Выполнение запроса для получения информации о столбцах таблицы
#     cur.execute(f"PRAGMA table_info({table_name});")
#
#     # Извлечение результатов
#     columns_info = cur.fetchall()
#     con.close()
#     # Возвращаем только имена столбцов
#     column_names = [column[1] for column in columns_info]
#
#     return column_names
#
#
# print(get_table_columns(table_name))


# # Вывод значений определенной таблицы
# def check_db_test(db_name, table_name):
#     con = sqlite3.connect(db_name)
#     cur = con.cursor()
#     res = cur.execute(f"SELECT * FROM {table_name}")
#     print(res.fetchall())
#     con.close()
#
#
# check_db_test(db_name, table_name)

# # тестирования поиска - фильтра
# OrmModel.search_filter(column_name='some_field_1', query_name='значение_поля_1')
# OrmText.search_filter(column_name='some_field_2', query_name=423)
#
# # тестирование вывода всей необходимой таблицы
# OrmModel.search_filter(column_name=None, query_name=None)
