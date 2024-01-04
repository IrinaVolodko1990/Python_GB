# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.
# Пример ввод

# transformation = lambda x: x
# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')


# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна


# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10


# s = lambda cur_tuple: cur_tuple[0] * cur_tuple[1]
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# index_max_orbit = 0
# max_elipse = s(orbits[0])


# for cur_orbit in orbits:
#     if cur_orbit[0] != cur_orbit[1]:
#         cur_elipse = s(cur_orbit)
#         if cur_elipse > max_elipse:
#             max_elipse = cur_elipse
#             index_max_orbit = cur_orbit

# print(index_max_orbit)

# 2nd option


# def find_farthest_orbit(list_of_orbits):
#     filter_list = list(
#         filter(lambda cur_tuple: cur_tuple[0] != cur_tuple[1], list_of_orbits)
#     )
#     s_list = list(map(lambda cur_tuple: cur_tuple[0] * cur_tuple[1], filter_list))
#     max_s = max(s_list)
#     index_max_orbit = s_list.index(max_s)
#     return filter_list[index_max_orbit]


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так. Если значение характеристики для
# разных объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True.
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод:                                              Вывод:
# values = [0, 2, 10, 6]                             same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

#1th option

def same_by(characteristic, objects):
    if not objects:
        return True
    list_1 = list(map(characteristic, objects))
    return all(list_1) == any(list_1)                  #1st option
    # if all(list_1) == True or all(list_1) == False:    #alternative return
    #     return True
    # else:
    #     return False
    
#2nd option

def same_by(characteristic, objects):
    if not objects:
        return True
    list_1 = set(map(characteristic, objects))
    return len(list_1) == 1

#3th option

def same_by(characteristic, objects):
    list_1 = list(filter(characteristic, objects))
    return list_1 == objects or not list_1



values = [1, 21, 101, 61]
if same_by(lambda x: x % 2 == 0, values):
    print("same")
else:
    print("different")
