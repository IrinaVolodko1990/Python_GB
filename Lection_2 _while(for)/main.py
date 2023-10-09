# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while

# n = int(input("Input N: "))
# res = 1
# while n > 0:
#     res*=n
#     n-=1
# print (res)

# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Ряд чисел Фибоначчи:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, …

# number = int (input("Input some number > 1: "))
# first_F_number = 0
# second_F_number = 1
# index = 1
# temp = 0

# while second_F_number <= number:
#     temp = first_F_number + second_F_number
#     first_F_number = second_F_number
#     second_F_number = temp
#     index += 1
# print (index)

# Пользователь вводит число N (1 ≤ N ≤ 10). Далее построчно N чисел от -50 до 50. 
# Нужно вывести наибольшее количество идущих подряд положительных чисел.

import random

days = int(input("Input qty of days: "))
count = 0
max_pos_num = 0
for i in range (1, days):
    num = random.randint(-50, 50)
    print (num)
    if num > 0:
        count += 1
        if max_pos_num < count:
            max_pos_num = count
    else:
        count = 0
print (f"{max_pos_num} days in a row ")
    

