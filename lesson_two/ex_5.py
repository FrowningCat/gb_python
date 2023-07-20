import math

a = int(input("Ввелите переменную A: "))
b = int(input("Ввелите переменную B: "))
c = int(input("Ввелите переменную C: "))

dis = b ** 2 - 4 * a * c

if dis < 0:
    print("Корней нет")
elif dis == 0:
    x = -b / 2 * a
    print("Корень = ", x)
else:
    x_1 = (-b + math.sqrt(dis)) / (2 * a)
    x_2 = (-b - math.sqrt(dis)) / (2 * a)
    print("Корени = ", x_1, "и", x_2)
