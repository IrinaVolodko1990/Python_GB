# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.

number = int (input ("Input number: "))
hundreds = number // 100
digits = number % 10
tens = number % 100 // 10
print(hundreds)
print (tens)
print (digits)
res = hundreds + digits + tens
print (f"Sum of all elements = {res}")
