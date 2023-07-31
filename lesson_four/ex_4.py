list = list(input("Введите список из чисел: "))


def fun(list):
    for i in range(1, len(list)):
        item = list[i]
        j = i - 1
        while j >= 0 and list[j] > item:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = item
    print(list)


fun(list)
