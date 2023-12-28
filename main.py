from class_file import SomeTable, OrmInteger, OrmText, OrmFloat, OrmModel

# 1 Экземплаяр для создания таблицы с нужными столбиками Определите primary_key или не указывайте
# table_instance = SomeTable(
#     some_field_1=OrmText(primary_key=True),
#     some_field_2=OrmInteger(),
#     some_field_3=OrmFloat(),
#     some_field_4=OrmText())

# 2 Экземпляр класс где id primary_key - True
# model1 = OrmModel(
#     some_field_1='значение_поля_1-1',
#     some_field_2=43,
#     some_field_3=3.15,
#     some_field_4='значение_поля_4-1')
# #
# #  # Вызов метода класса для загрузки данных
# model1.create_query()

# 2 Экземпляры класса OrmText перед созданием не забудьте создать таблицу
# model2 = OrmText(
#     some_field_1='значение_поля_11',
#     some_field_2=424,
#     some_field_3=3.1444,
#     some_field_4='значение_поля_44')
#
# model2.create_query()

# model3 = OrmText(
#     some_field_1='значение_поля_11-3',
#     some_field_2=423,
#     some_field_3=3.1443,
#     some_field_4='значение_поля_44-3')
#
# model3.create_query()



