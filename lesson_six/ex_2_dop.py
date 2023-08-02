from random import randint


def fun(x, y, z):
    number = randint(x, y)
    while z > 0:
        t = int(input("Введите число: "))
        if t > number:
            print("Меньше")
        elif t < number:
            print("Больше")
        else:
            print(True)
            exit()
        z -= 1
    print(False)
