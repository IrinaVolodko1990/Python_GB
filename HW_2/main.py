# На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом. 
#Ваша задача - определить минимальное количество монеток, которые нужно перевернуть, 
#чтобы все монетки лежали одной и той же стороной вверх.
# Входные данные:
# На вход программе подается список coins, где coins[i] равно 0, если i-я 
#монетка лежит гербом вверх, и равно 1, если i-я монетка лежит решкой вверх.
# Размер списка не превышает 1000 элементов.
# Выходные данные:
# Программа должна вывести одно целое число - минимальное количество монеток, которые нужно перевернуть.

import random

coins_size = random.randint(1, 1000)
print (coins_size)
coins = []
count_zero = 0
count_ones = 0
# coins = list()
# coins = [1, 0, 0, 1,0]
for item in range(coins_size):
    coins.append(random.randint(0,1))
    if coins[item] == 0:
        count_zero += 1
    elif coins[item] == 1:
        count_ones += 1

print(count_ones, count_zero)

print (coins)

if (count_zero >= count_ones):
    print(count_ones)
else:
    print(count_zero)
