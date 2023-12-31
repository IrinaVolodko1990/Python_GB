# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2


# user_str = str(input("Input some string: "))

# user_str = "a a a b c a a d c d d"
# list_symbols = user_str.split()
# uniq_symbols = dict()
# result = ""

# for symbol in list_symbols:
#     if symbol not in uniq_symbols:
#         uniq_symbols[symbol] = 0
#         result += f"{symbol} "
#         print(symbol, end=" ")
#     else:
#         uniq_symbols[symbol] += 1
#         result += f"{symbol}_{uniq_symbols[symbol]} "
#         print(f"{symbol}_{uniq_symbols[symbol]}", end=" ")
# print()
# print(result.strip())

# # 2nd option

# for symbol in list_symbols:
#     if symbol not in uniq_symbols:
#         result += f"{symbol} "
#     else:
#         result += f"{symbol}_{uniq_symbols[symbol]} "
#     uniq_symbols[symbol] = uniq_symbols.get(symbol, 0) + 1
# print(result.strip())


# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.

# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# user_str = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# edit_str_list = user_str.lower().split()
# str_set = set(edit_str_list)
# size = len(str_set)

# print (size)

# solution in 1 string
# print(len(set(user_str.lower().split())))

# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить значение наибольшего элемента
# последовательности, которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. 
# Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание.
# Они решили так: у кого  будет меньше ошибок в коде, тот и выиграл спор. За помощью товарищи обратились к Вам,
# студентам.

# Ваня:
n = int(input()) 
max_number = n            #1 некорректное число max_number = 1000
while n != 0:
    n = int(input())
    if max_number < n:     #2 было: max_number < n
        max_number = n
print(max_number)

# Петя:

# n = int(input())
# max_number = -1
# while n > 0:             #1 натуральные числа только положительные , было: while n < 0:
#     if max_number < n:
#         max_number = n   #3 было: n = max_number
#     n = int(input())     #2 эта строка была выше, перед циклом if
# print(max_number)        #4 было prtint(n)