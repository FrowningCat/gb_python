number = int(input("Введите число: "))
summand_one = None
summand_two = None
summand_three = None
degree = 2

if number < 0:
    print("Введите другое число")
elif number < 10:
    print(number**degree)
elif number < 100:
    summand_one = number % 10
    summand_two = number // 10
    print(summand_one * summand_two)
elif number < 1000:
    summand_one = number % 10
    summand_two = (number // 10) % 10
    summand_three = number // 100
    print(summand_one, summand_two, summand_three, sep='')
else:
    print("Введите другое число")