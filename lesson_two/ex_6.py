fraction_one = list(input("Введите первую дробь: "))
fraction_two = list(input("Введите вторую дробь: "))
x_1 = ''
x_2 = ''
y_1 = ''
y_2 = ''


def fraction(x, y, fraction):
    i = 0
    position = 0
    while fraction[i] != "/":
        x = fraction[i] + x[position:]
        i += 1
    else:
        i += 1
        while i < len(fraction):
            y = fraction[i] + y[position:]
            i += 1
    return x, y


x_1, y_1 = fraction(x_1, y_1, fraction_one)
x_2, y_2 = fraction(x_2, y_2, fraction_two)

x_1 = int(x_1)
y_1 = int(y_1)
x_2 = int(x_2)
y_2 = int(y_2)

numerator_sum = x_1 * y_2 + x_2 * y_1
denominator_sum = y_2 * y_1

numerator_mul = x_1 * y_2
denominator_mul = x_2 * y_1

print("Сумма дробей: ", numerator_sum, "/", denominator_sum)
print("Произведение дробей: ", numerator_mul, "/", denominator_mul)
