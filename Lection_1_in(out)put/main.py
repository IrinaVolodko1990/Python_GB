#За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут
#длиной m километров? При решении этой задачи нельзя пользоваться условной конструкцией if и циклами.
import math

n = int(input("Input speed of car: "))
m = int(input("Input destination: "))
days = math.ceil(m/n)
print (f"{days} days for this destination")