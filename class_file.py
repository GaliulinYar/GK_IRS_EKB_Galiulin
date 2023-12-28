from work_db import create_request, insert_data, check_db, search_filter_request


class OrmModel:
    """Основной родительский класс"""

    def __init__(self, **kwargs):
        self.fields = kwargs  # все поступающие значения в переменной
        self.name_table = str(self.__class__.__name__)  # Имя для таблицы
        self.data_base_name = 'Test_DB'  # Имя для базы данных

        self.key_list = []  # пустой список для формирования ключей для БД
        self.value_list = []  # пустой список для формирования значений для БД

    def create_query(self):
        """класс метод для составления запроса к БД"""
        for key, value in self.fields.items():  # перебор поступающих данных
            # меняем имя таблица, если нужно  обратится к таблице SomeTable (primary_key - id)
            if self.name_table == 'OrmModel':
                self.name_table = 'SomeTable'
            # заполняем списки
            self.key_list.append(key)
            self.value_list.append(value)
        # Вызываем функцию для составления запроса
        request_for_db = insert_data(self.key_list, self.value_list, self.name_table)
        # Вызываем функцию для отправки запроса в БД
        check_db(self.data_base_name, request_for_db)

    @classmethod
    def search_filter(cls, column_name, query_name):
        """Метод для вызова функции search_filter_request. Работаем с фильтрацией данных из БД"""

        # меняем имя таблица, если нужно  обратится к таблице SomeTable (primary_key - id)
        if cls().name_table == 'OrmModel':
            name_table = 'SomeTable'
        else:  # или оставляем имя согласно классу
            name_table = cls().name_table
        # Формируем запрос с использованием данных объекта и отправляем в БД
        search_filter_request(cls().data_base_name, name_table, column_name, query_name)

    def __str__(self):
        """Строковый вывод класса OrmModel"""
        return ', '.join(f'{key}={value}' for key, value in self.fields.items())


class SomeTable(OrmModel):
    """Класс для создания таблиц"""

    def __init__(self, **kwargs):
        super().__init__()
        self.fields = kwargs  # все поступающие значения в переменной
        self.primary_key_id = 0  # учет primary_key изначально 0

        for key, value in kwargs.items():  # перебираем значения

            if isinstance(value, OrmInteger):  # проверка на тип "число"

                if value.primary_key:
                    self.name_table = 'OrmInteger'  # Задаем имя таблицы в зависимости от primary_key
                    self.key_list.append(f'{key} INTEGER PRIMARY KEY')  # готовим значение для запроса в БД
                else:
                    self.primary_key_id += 1  # считаем primary_key-False
                    self.key_list.append(f'{key} INTEGER')  # готовим значение для запроса в БД

            elif isinstance(value, OrmText):  # проверка на тип "текст"
                if value.primary_key:
                    self.name_table = 'OrmText'  # Задаем имя таблицы в зависимости от primary_key
                    self.key_list.append(f'{key} TEXT PRIMARY KEY')  # готовим значение для запроса в БД
                else:
                    self.primary_key_id += 1  # считаем primary_key-False
                    self.key_list.append(f'{key} TEXT')  # готовим значение для запроса в БД

            elif isinstance(value, OrmFloat):  # проверка на тип "число с точкой"
                if value.primary_key:
                    self.name_table = 'OrmFloat'  # Задаем имя таблицы в зависимости от primary_key
                    self.key_list.append(f'{key} REAL PRIMARY KEY')  # готовим значение для запроса в БД
                else:
                    self.primary_key_id += 1  # считаем primary_key-False
                    self.key_list.append(f'{key} REAL')  # готовим значение для запроса в БД

        if self.primary_key_id == len(self.key_list):  # сравниваеим кол-во primary_key-False
            self.key_list.insert(0, f'id INTEGER PRIMARY KEY AUTOINCREMENT')   # готовим значение для запроса в БД
        # Вызываем функцию для составления запроса
        request_for_db = create_request(self.key_list, self.name_table)
        # Вызываем функцию для отправки запроса в БД
        check_db(self.data_base_name, request_for_db)


class OrmText(OrmModel):
    """Класс для типа полей TEXT"""
    def __init__(self, primary_key=False, **kwargs):
        super().__init__(**kwargs)  # наследуем значения от родителя
        self.primary_key = primary_key

    def __str__(self):
        """Строковый вывод класса OrmText"""
        return f'primary_key={self.primary_key}'


class OrmInteger(OrmModel):
    """Класс для типа полей INTEGER"""
    def __init__(self, primary_key=False, **kwargs):
        super().__init__(**kwargs)   # наследуем значения от родителя
        self.primary_key = primary_key

    def __str__(self):
        """Строковый вывод класса OrmInteger"""
        return f'primary_key={self.primary_key}'


class OrmFloat(OrmModel):
    """Класс для типа полей REAL"""
    def __init__(self, primary_key=False, **kwargs):
        super().__init__(**kwargs)   # наследуем значения от родителя
        self.primary_key = primary_key

    def __str__(self):
        """Строковый вывод класса OrmFloat"""
        return f'primary_key={self.primary_key}'
