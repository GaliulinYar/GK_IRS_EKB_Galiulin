from main import create_request, insert_data
from work_db import check_db


class OrmModel:

    def __init__(self, **kwargs):
        self.fields = kwargs
        self.name_table = str(self.__class__.__name__)
        self.check_key = False  # Проверка на то что primary_key нигде не указан

        for key, value in self.fields.items():  # перебираем ключи и значения

            if key and value.primary_key:  # проверяем pk на значение primary key true
                self.check_key = True
                if key == 'pk':
                    # Вызываем функцию для создания запроса
                    query = create_request(self)
                    print(query)
                    # Создаем БД и отправляем запрос на создание таблицы
                    check_db('SomeDB', query)
                    # создаем запрос на добавление данных таблицы
                    query_list = insert_data(self)
                    print(query_list)
        """почему выводится 5 раз"""
        if self.check_key is False:
            print('check_key None')

    def __str__(self):
        return ', '.join(f'{key}={value}' for key, value in self.fields.items())


class SomeTable(OrmModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Итерируемся по переданным аргументам и создаем атрибуты для просмотрав строке
        for key, value in kwargs.items():
            setattr(self, key, value)


class OrmText(OrmModel):
    def __init__(self, value=None, primary_key=False, **kwargs):
        super().__init__(**kwargs)
        self.value = value
        self.primary_key = primary_key

        if self.primary_key:
            print('primary_key true')

    def __str__(self):
        return f'{self.value}, primary_key={self.primary_key}'


class OrmInteger(SomeTable):
    def __init__(self, value=None, primary_key=False, **kwargs):
        super().__init__(**kwargs)
        self.value = value
        self.primary_key = primary_key

        if self.primary_key:
            print(self.primary_key, self.value)

            for key, value in self.__dict__.items():  # перебираем ключи и значения
                # print(key, value)

                """код ниже из класса OrmModel не работает, если переношу сюда"""

                # if key and value.primary_key:  # проверяем pk на значение primary key true
                #
                #     if key == 'pk':
                #         # Вызываем функцию для создания запроса
                #         query = create_request(self)
                #         print(query)
                #         # Создаем БД и отправляем запрос на создание таблицы
                #         check_db('SomeDB', query)
                #         # создаем запрос на добавление данных таблицы
                #         query_list = insert_data(self)
                #         print(query_list)

    def __str__(self):
        return f'{self.value}, primary_key={self.primary_key}'


class OrmFloat(OrmModel):
    def __init__(self, value=None, primary_key=False, **kwargs):
        super().__init__(**kwargs)
        self.value = value
        self.primary_key = primary_key

    def __str__(self):
        return f'{self.value}, primary_key={self.primary_key}'


table_instance = SomeTable(
    pk=OrmInteger(),
    some_field_1=OrmText(value='some text'),
    some_field_2=OrmInteger(value=4),
    some_field_3=OrmFloat(value=3.44))


# table_instance2 = SomeTable(
#     pk=OrmInteger(primary_key=True),
#     some_field_1=OrmText(value='some text'),
#     some_field_2=OrmInteger(value=4),
#     some_field_3=OrmFloat(value=3.44),
#     some_field_4=OrmFloat(value=54.44, primary_key=True)
# )

# print(table_instance)
# print(table_instance2)
# print(table_instance)
# CREATE TABLE YourTableName (
#     id INTEGER PRIMARY KEY,
#     column1 TEXT,
#     column2 INTEGER,
#     column3 REAL
# );