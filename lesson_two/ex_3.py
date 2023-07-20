number: int = int(input("Введите число: "))

print(bin(number))
print(oct(number))


def number_system(number_system, numberr):
    i = ""
    position = 0
    while numberr > 0:
        i = str(numberr % number_system) + i[position:]
        numberr //= number_system
    print(i)


number_system(2, number)
number_system(8, number)
