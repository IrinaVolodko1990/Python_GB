# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

import random

initial_list = [1, 50, 2, 0, -1, 3, 4, 4]
unique_list = []

for number in initial_list:
    if number not in unique_list:
        unique_list.append(number)
print(len(unique_list))

