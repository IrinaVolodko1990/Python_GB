# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

# from random import randint


# def input_list():
#     size = int(input("Input size of array: "))
#     user_list = list()
#     for item in range(size):
#         user_list.append(int(input("Input element of array: ")))
#     print(user_list)
#     return user_list


# def input_list2():
#     size = int(input("Input size of array: "))
#     user_list = [randint(1, 3) for item in range(size)]
#     print(user_list)
#     return user_list


# list1 = input_list()
# list2 = input_list2()
# # list2 = set(input_list2())

# for el in list1:
#     if el not in list2:
#         print(el, end=" ")


# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве. Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

# Ввод:                 Ввод:
# 5                      5
# 1 2 3 4 5              1 5 1 5 1

# Вывод:                   Вывод
#    0                           2

# from random import randint

# size = int(input("Input size of list: "))
# user_list = [randint(1, 11) for el in range(size)]

# print(user_list)

# count = 0

# for index in range(1, size - 1):
#     if user_list[index - 1] < user_list[index] > user_list[index + 1]:
#         count += 1

# print(count)

# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных строках.
# Ввод:                   Вывод:
# 1 2 3 2 3                 2

# from random import randint

# user_list = [randint(1, 10) for _ in range(randint(5, 10))]
# print(user_list)

# count = 0
# for i in range(len(user_list) - 1):
#     for j in range(i + 1, len(user_list)):
#         if user_list[i] == user_list[j]:
#             count += 1

# print(count)

# # 2nd option

# count = 0

# for i in range(len(user_list)):
#     count += user_list[i + 1 :].count(user_list[i])

# print(count)


# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести все
# пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую
# пару не дает).


# Ввод:        Вывод:
# 300          220 284

from random import randint 

# def div_sum(num):
#     sum_divs = 1
#     for item in range(2,num):
#         if num % item == 0:
#             sum_divs += item
#     return sum_divs


# size = int(input('Input limit of numbers: '))

# for num_1 in range(2, size):
#     for num_2 in range(2, size):
#         if num_1 < num_2 and div_sum(num_1) == num_2 and div_sum(num_2) == num_1:
#             print(num_1, num_2)


# # 2nd option loop for

# for num_1 in range(2,size):
#     num_2 = div_sum(num_1) 
#     if div_sum(num_2) == num_1 and num_1 < num_2:
#         print(num_1, num_2)


# # 3th option 

def div_sum(number):
    sum_divs = 1
    sq_num = number ** 0.5                     #берём корень от числа
    if sq_num == int(sq_num):
        sum_divs += sq_num
    for div in range(2, int(number ** 0.5)):
        if number % div == 0:
            sum_divs += div + number // div    #при нахождении делителя у сумме прибавляемое частное
    return sum_divs


size = int(input('Введите предельное число К: '))

for num_1 in range(2, size):
    num_2 = div_sum(num_1)
    if div_sum(num_2) == num_1 and num_1 < num_2:
        print(num_1, num_2)