# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b
# с помощью рекурсии.

# Функция не должна ничего выводить, только возвращать значение.


# def f(num, pow):
#     if pow == 1:
#         return num
#     return num * f(num, pow - 1)


# num = int(input("Input some number: "))
# pow = int(input("Input pow of number: "))
# print(f(num, pow))

# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
# неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# Функция не должна ничего выводить, только возвращать значение.


def sum(num1, num2):
    if num2 == 0:
        return num1
    return sum(num1 + 1, num2 - 1)


num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))
print(sum(num1, num2))
