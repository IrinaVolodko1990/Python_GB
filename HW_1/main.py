# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.

# number = int (input ("Input number: "))
# hundreds = number // 100
# digits = number % 10
# tens = number % 100 // 10
# print(hundreds)
# print (tens)
# print (digits)
# res = hundreds + digits + tens
# print (f"Sum of all elements = {res}")

# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, 
# чем Петя и Сережа вместе?
# Выведите через пробел количество журавликов, сделанных Петей, Катей и Сережей.
# n = 60
# p_s = n // 6
# k = p_s * 4
# print (p_s, k, p_s)

# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна 
# сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета с 
# номером n и выводит на экран yes или no.

# number = int (input("Input 6-digits number: "))
# num_1 = number // 100000
# print (num_1)
# num_2 = number // 10000 % 10
# print (num_2)
# num_3 = number // 1000 % 10 
# print (num_3)
# num_4 = number // 100 % 10
# print (num_4)
# num_5 = number // 10 % 10 
# print (num_5)
# num_6 = number % 10
# print (num_6) 
# if num_1 + num_2 + num_3 == num_4 + num_5 + num_6:
#     print ("yes")
# else:
#     print("no")

# Определите, можно ли от шоколадки размером a × b долек отломить c долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# Выведите yes или no соответственно.

a = 3
b = 2
c = 4

if c <= a * b and (c % a == 0 or c % b == 0):
    print ('yes')
else:
    print ('no')


