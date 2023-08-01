a = str(input("Введите числа"))
list = a.split("/")
dict = {}

if len(list) < 4:
    print(False)
else:
    a, b, c, *d = list
    dict[b] = a
    dict[c] = d
    print(dict)
