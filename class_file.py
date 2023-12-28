from work_db import create_request, insert_data, check_db


class OrmModel:

    def __init__(self, **kwargs):
        self.fields = kwargs
        self.name_table = str(self.__class__.__name__)
        self.data_base_name = 'Test_DB'

        self.key_list = []
        self.value_list = []

    def create_query(self):
        """класс метод для составления запроса к БД"""

        for key, value in self.fields.items():
            self.key_list.append(key)
            self.value_list.append(value)
        # Вызываем функцию для составления запроса
        request_for_db = insert_data(self.key_list, self.value_list, self.name_table)
        # Вызываем функцию для отправки запроса в БД
        check_db(self.data_base_name, request_for_db)

    def __str__(self):
        return ', '.join(f'{key}={value}' for key, value in self.fields.items())


class SomeTable(OrmModel):

    def __init__(self, **kwargs):
        super().__init__()
        self.fields = kwargs
        self.primary_key_id = 0
        self.name_table = 'OrmModel'

        for key, value in kwargs.items():

            if isinstance(value, OrmInteger):

                if value.primary_key:
                    self.name_table = 'OrmInteger'
                    self.key_list.append(f'{key} INTEGER PRIMARY KEY')
                else:
                    self.primary_key_id += 1
                    self.key_list.append(f'{key} INTEGER')

            elif isinstance(value, OrmText):
                if value.primary_key:
                    self.name_table = 'OrmText'
                    self.key_list.append(f'{key} TEXT PRIMARY KEY')
                else:
                    self.primary_key_id += 1
                    self.key_list.append(f'{key} TEXT')

            elif isinstance(value, OrmFloat):
                if value.primary_key:
                    self.name_table = 'OrmFloat'
                    self.key_list.append(f'{key} REAL PRIMARY KEY')
                else:
                    self.primary_key_id += 1
                    self.key_list.append(f'{key} REAL')

        if self.primary_key_id == len(self.key_list):
            self.key_list.insert(0, f'id INTEGER PRIMARY KEY AUTOINCREMENT')
        # Вызываем функцию для составления запроса
        request_for_db = create_request(self.key_list, self.name_table)
        # Вызываем функцию для отправки запроса в БД
        check_db(self.data_base_name, request_for_db)


class OrmText(OrmModel):
    def __init__(self, primary_key=False, **kwargs):
        super().__init__(**kwargs)
        self.primary_key = primary_key

    # def __str__(self):
    #     return f'{self.value}, primary_key={self.primary_key}'


class OrmInteger(OrmModel):
    def __init__(self, primary_key=False, **kwargs):
        super().__init__(**kwargs)
        self.primary_key = primary_key

    # def __str__(self):
    #     return f'{self.value}, primary_key={self.primary_key}'


class OrmFloat(OrmModel):
    def __init__(self, primary_key=False, **kwargs):
        super().__init__(**kwargs)
        self.primary_key = primary_key

    # def __str__(self):
    #     return f'{self.value}, primary_key={self.primary_key}'
