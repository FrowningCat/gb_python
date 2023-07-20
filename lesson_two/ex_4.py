import decimal
import math

di = int(input("Ввелите диаметр окружности: "))
decimal.getcontext().prec = 42
pi = math.pi

print("Длина окружноссти = ", pi*di)
print("Диаметр окружноссти = ", (pi*di**2)/4)
