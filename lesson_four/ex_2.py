string = str(input("Введите строку: "))


def func(str):
    unitlist = []
    str = list(str)
    str.sort(reverse=True)
    for i in str:
        unitlist.append(ord(i))
    return unitlist


print(func(string))
