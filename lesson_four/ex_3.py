string = str(input("Введите строку с 2 числами через пробел: "))

def fun(str):
    uni = {}
    str = list(str)
    for i in str:
        uni[ord(i)] = i
    print(uni)


fun(string)
