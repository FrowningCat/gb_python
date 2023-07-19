number = int(input("Введите число: "))
i = 2

if number < 0:
    number *= -1
elif number > 100000:
    print("Введите другое число")
    exit()
else:
    while i < number:
        if number % i == 0:
            print("Число составное")
            exit()
        i += 1

print("Число простое")
