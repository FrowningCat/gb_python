age = int(input("Введите год: "))

if age < 0:
    print("Введено некоректное число")
elif age == 0:
    print("Год не весекосный")
elif age % 400 == 0:
    print("Год весекосный")
elif age % 100 == 0:
    print("Год не весекосный")
elif age % 4 == 0:
    print("Год весекосный")
else:
    print("Год не весекосный")
