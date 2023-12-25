def create_request(self):
    """Функция для создания запроса в БД для создания таблицы где pk primary key"""
    create_list_db = []
    for name, value_field in zip(self.fields.keys(), self.fields.values()):
        if isinstance(value_field.value, str):
            create_list_db.append(f'{name} TEXT')
        elif isinstance(value_field.value, int):
            create_list_db.append(f'{name} INTEGER')
        elif isinstance(value_field.value, float):
            create_list_db.append(f'{name} REAL')

    field_definitions = ', '.join(create_list_db)
    query = f'CREATE TABLE {self.name_table} (pk INTEGER PRIMARY KEY AUTOINCREMENT, {field_definitions})'
    return query


def insert_data(self):
    """Для создания запроса заполнения\дописывание БД"""
    for name, value_field in zip(self.fields.keys(), self.fields.values()):
        print(name)
        print(value_field.value)
    query_insert = f'INSERT INTO {self.name_table} (значение) VALUES (Значение)'
    return query_insert


# def create_request_pk(name_table, **kwargs):
#     """Функция для создания запроса в БД для создания таблицы, где
#     primary key какое-то другое поле"""
#     create_list_db = []
#     for name, value_field in kwargs.items():
#         if isinstance(value_field.value, str):
#             create_list_db.append(f'{name} TEXT')
#         elif isinstance(value_field.value, int):
#             create_list_db.append(f'{name} INTEGER')
#         elif isinstance(value_field.value, float):
#             create_list_db.append(f'{name} REAL')
#
#     field_definitions = ', '.join(create_list_db)
#     query = f'CREATE TABLE {name_table} (pk INTEGER PRIMARY KEY AUTOINCREMENT, {field_definitions})'
#     return query
