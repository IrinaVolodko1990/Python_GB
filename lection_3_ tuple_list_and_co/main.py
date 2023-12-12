# # Дан список чисел. Определите, сколько в нем встречается различных чисел.
# # Input: [1, 1, 2, 0, -1, 3, 4, 4]
# # Output: 6

# import random

# initial_list = [1, 1, 2, 0, -1, 3, 4, 4]

# size = int(input("Input size of collection: "))
# initial_list = list()

# for _ in range(size):
#     initial_list.append(random.randint(-5, 5))


# initial_list = [random.randint(-5,5) for _ in range (size)]
# print(initial_list)

# 2nd option
# unique_list = []

# for number in initial_list:
#     if number not in unique_list:
#         unique_list.append(number)
# print(len(unique_list))

# alternative output
# print(len(set(initial_list)))


# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.

# Input: [1, 2, 3, 4, 5] k = 3

# Output: [3, 4, 5, 1, 2]

# import random

# initial_list = [1, 2, 3, 4, 5]

# number = int(input("Input k for replace: "))
# size = random.randint(0, 9)
# initial_list = [random.randint(-100, 100) for i in range(size)]
# print(initial_list)

# print ((initial_list[-number:] + initial_list[: -number]))
# 2nd option

# for _ in range(number):
#     last_number = initial_list.pop()
#     initial_list.insert(0, last_number)

# print(initial_list)


# INCORRECT
# new_list = []
# if number >= len(initial_list):
#     print('Impossible for replace')
# else:
#     for index in range(size):
#         if index >= number - 1:
#             new_list.append(initial_list[index])
#     for index in range (number - 1): # не работает при number = 1
#         new_list.append(initial_list[index])
# print(new_list)


# Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#         {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]


d = [
    {"V": "S001"},
    {"V": "S002"},
     {"VI": "S001", "VIII": "S00007"}, # здесь распаковка (*) не сработает
    {"VI": "S005"},
    {"VII": "S005"},
    {"V": "S009"},
    {"VIII": "S007"},
]

values_set = set()
for item in d:
    values_set.add(*item.values()) # * - распаковка объекта, но метод add не работает при наличии в словаре нескольких пар ключ-значение
# values_set.update(item.values())

# 2nd option
# for item in d:
#     for key in item:
#         values_set.add(item[key])


# код для работы с объединением union
# for item in d:
#     values_set |= set(item.values())


print(values_set)

# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает
# количество элементов массива, больших предыдущего (элемента с предыдущим номером)

# Input: [0, -1, 5, 2, 3]
# Output: 2
# Пояснение: (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения списка или список задан изначально.

# рандомное формирование списка
# from random import randint

# # initial_list = [0, -1, 5, 2, 3]
# size = int(input("Input list size: "))
# initial_list = [randint(-100, 100) for i in range(size)]
# print(initial_list)

# count = 0

# for index in range(len(initial_list) - 1):
#     if initial_list[index] < initial_list[index + 1]:
#         count += 1
# print(count)

# 2nd option
# new_list =[1 for index in range (len(initial_list)- 1)
#            if initial_list[index] < initial_list[index + 1]]
# print(len(new_list))
# идентично выводу выше
# print(sum(new_list))


# Решение задачи по замене элементов списка на новые значения
# new_list_2 =[0 if initial_list[index] % 2 == 0
#              else 1
#              for index in range (len(initial_list))
#            ]
# print(new_list_2)
