leng_a = int(input("Введите длину стороны A: "))
leng_b = int(input("Введите длину стороны B: "))
leng_c = int(input("Введите длину стороны C: "))

if (leng_a + leng_b < leng_c) | (leng_c + leng_b < leng_a) | (leng_a + leng_c < leng_b):
    print("Треугольник не сушествует")
elif (leng_a == leng_b) | (leng_a == leng_c) | (leng_b == leng_c):
    print("Треугольник равнобедренный")
elif leng_a == leng_b == leng_c:
    print("Треугольник равносторонний")
else:
    print("Треугольник разносторонний")