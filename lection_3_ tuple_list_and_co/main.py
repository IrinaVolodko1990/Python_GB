# # Дан список чисел. Определите, сколько в нем встречается различных чисел.
# # Input: [1, 1, 2, 0, -1, 3, 4, 4]
# # Output: 6

# import random

# initial_list = [1, 1, 2, 0, -1, 3, 4, 4]
# unique_list = []

# for number in initial_list:
#     if number not in unique_list:
#         unique_list.append(number)
# print(len(unique_list))

# print(len(set(initial_list)))

# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.

# Input: [1, 2, 3, 4, 5] k = 3

# Output: [3, 4, 5, 1, 2]

import random

# initial_list = [1, 2, 3, 4, 5]
number = int(input('Input k for replace: '))
size = random.randint(0,9)
initial_list = [random.randint(-100,100) for i in range (size)]
new_list = [] 
print(initial_list)

if number >= len(initial_list):
    print('Impossible for replace')
else:
    for index in range(size):
        if index >= number - 1:
            new_list.append(initial_list[index])
    for index in range (number - 1): # не работает при number = 1
        new_list.append(initial_list[index])
       
print(new_list)
# print ((initial_list[-number:] + initial_list[: -number]))

