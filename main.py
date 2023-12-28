from class_file import SomeTable, OrmInteger, OrmText, OrmFloat, OrmModel

# Экземплаяр для создания таблицы с нужными столбиками
# table_instance = SomeTable(
#     some_field_1=OrmText(primary_key=True),
#     some_field_2=OrmInteger(),
#     some_field_3=OrmFloat(),
#     some_field_4=OrmText())

# Экземпляр класс где id primary_key - True
# model1 = OrmModel(
#     some_field_1='значение_поля_1',
#     some_field_2=42,
#     some_field_3=3.14,
#     some_field_4='значение_поля_4')
# #
# #  # Вызов метода класса для загрузки данных
# model1.create_query()


model2 = OrmText(
    some_field_1='значение_поля_11',
    some_field_2=424,
    some_field_3=3.1444,
    some_field_4='значение_поля_44')

model2.create_query()



