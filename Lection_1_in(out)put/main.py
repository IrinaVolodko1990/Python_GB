#За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут
#длиной m километров? При решении этой задачи нельзя пользоваться условной конструкцией if и циклами.


# from math import ceil 

# speed = int(input("Input speed of car: "))
# distance = int(input("Input distance: "))
# days = ceil(distance/speed)
# print (f"{days} days for this destination")

#В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них 
#новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из 
#трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.

from math import ceil 

first_class_pupils = int(input("Pupils of first class: "))
second_class_pupils = int(input("Pupils of second class: "))
third_class_pupils = int(input("Pupils of third class: "))

table1 = ceil(first_class_pupils/2);
table2 = ceil(second_class_pupils/2)
table3 = ceil(third_class_pupils/2)

print (f'Sum of tables for 3 classes: {table1+table2+table3}')