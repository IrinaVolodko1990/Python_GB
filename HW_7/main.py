# Напишите функцию print_operation_table(operation, num_rows, num_columns), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# По умолчанию номер столбца и строки = 9.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
# Между элементами должен быть 1 пробел, в конце строки пробел не нужен.


table_list = [1,2,3],[1,2,3]
for row in table_list:
    for column in table_list:
        table_list[row][column] = (row + 1) * (column + 1)
for row in table_list:
    for column in table_list:
        print(table_list[row][column])
        print('\t')
