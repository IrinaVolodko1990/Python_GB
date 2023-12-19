# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ...,
# где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

# num = int(input("Input some number: "))


# def fib(num):
#     if num in [1, 2]:
#         return 1
#     return fib(num - 1) + fib(num - 2)


# print(fib(num))

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.

# from random import randint
# import time

# size = int(input("Input size: "))

# mark_list = [randint(1, 5) for mark_list in range(size)]
# print(mark_list)
# start_1 = time.time()
# max_mark = max(set(mark_list))
# min_mark = min(set(mark_list))
# end_1 = time.time()
# print(end_1 - start_1)

# # 2nd option for search max-min на больших числах короче по времени
# # start_2 = time.time()
# # max_mark = mark_list[0]
# # min_mark = mark_list[0]

# # for mark in set(mark_list):
# #     if  mark > max_mark:
# #         max_mark = mark
# #     if  mark < min_mark:
# #         min_mark = mark


# # end_2 = time.time()
# # print(end_2 - start_2)
# #######

# print(max_mark, min_mark)


# for index in range(size):
#     if mark_list[index] == max_mark:
#         mark_list[index] = min_mark

# print(mark_list)


# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым.
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)

# number = int(input("Input some number: "))


# def simple_num(num):
#     for div in range(2, num):
#         if num % div == 0:
#             return "No"
#         return "Yes"


# print(simple_num(number))


# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы
# (даже для ввода и вывода).

# Input: 2 -> 3 4
# Output: 4 3


# def reverse_nums(size):
#     if size == 0:
#         return ''
#     rev_num = int(input('Input some number: '))
#     return f'{reverse_nums(size - 1)} {rev_num}'



# size = int(input('Input size of collection: '))
# print(reverse_nums(size))

def reverse_nums(n):
    if n == 1:
        return input("Введите число последовательности: ")
    k = input("Введите число последовательности: ")
    return f'{reverse_nums(n-1)} {k}'


num = int(input('Введите количество чисел '))
print(reverse_nums(num))