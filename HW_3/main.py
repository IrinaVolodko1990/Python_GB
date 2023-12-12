# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.


# from random import randint


# size = int(input("Input list size: "))

# list_1 = [randint(-5, 5) for item in range(size)]
# print(list_1)

# k = int(input("Input some k: "))
# count = 0

# for num in list_1:
#     if num == k:
#         count += 1

# print(count)

# Требуется найти в массиве list_1 самый близкий по значению элемент
# к заданному числу k и вывести его.Считать, что такой элемент может быть только один.
# Если значение k совпадает с этим элементом - выведите его.

# from random import randint
# import math

# size = int(input("Input list size: "))

# list_1 = [randint(-10, 10) for item in range(size)]
# print(list_1)
# k = int(input("Input some k: "))

# diff = abs(list_1[0] - k)
# search_num = list_1[0]

# for index in range(1, len(list_1) - 1):
#     if abs(list_1[index] - k) < diff:
#         diff = abs(list_1[index] - k)
#         search_num = list_1[index]

# print(search_num)


# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

# В случае с английским алфавитом очки распределяются так:

# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:

# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k
# и выводит его. Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.


letters_dict = {
    (
        "A",
        "E",
        "I",
        "O",
        "U",
        "L",
        "N",
        "S",
        "T",
        "R",
        "А",
        "В",
        "Е",
        "И",
        "Н",
        "О",
        "Р",
        "С",
        "Т",
    ): 1,
    ("D", "G", "Д", "К", "Л", "М", "П", "У"): 2,
    ("B", "C", "M", "P", "Б", "Г", "Ё", "Ь", "Я"): 3,
    ("F", "H", "V", "W", "Y", "Й", "Ы"): 4,
    ("K", "Ж", "З", "Х", "Ц", "Ч"): 5,
    ("J", "X", "Ш", "Э", "Ю"): 8,
    ("Q", "Z", "Ф", "Щ", "Ъ"): 10,
}

str_1 = str(input("Input some string: "))
sum = 0

for key, value in letters_dict.items():
    for letter_index in range(len(str_1)):
        for letter in range(len(key)):
            if str_1[letter_index].upper() == key[letter]:
                sum += value

print(sum)
