# Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).
# На вход подается список с элементамиlist_1 и границы диапазона в виде 
# чисел min_number, max_number.

# from random import randint

# list_1 = [randint(-10, 10) for _ in range(randint(10, 20))]

# print(list_1)

# max_number = int(input('Input max number: '))
# min_number = int(input('Input min number: '))

# for index in range(len(list_1)):
#     if min_number <= list_1[index] <= max_number:
#         print(index)


# Заполните массив элементами арифметической прогрессии. Её первый элемент a1 , 
# разность d и количество элементов n будет задано автоматически. Формула для 
# получения n-го члена прогрессии: an = a1 + (n-1) * d.


start_num = int(input('Input first number: '))
step_num = int (input('Input step: '))
size = int(input('Input size of list: '))

for i in range(1, size + 1):
    print(start_num)
    start_num +=step_num

#2nd option 

# a1 = 2
# d = 3
# n = 4

# for i in range(1, n + 1):
#     print(a1)
#     a1 += d

#3th option 

# a1 = 2
# d = 3
# n = 4

# for i in range(n):
#   print(a1 + i * d)
    
