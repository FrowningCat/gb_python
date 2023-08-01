max = 100


def fun(max):
    a, b = 0, 1
    print(a)
    while b < max:
        a, b = b, a + b
        print(a)


fun(max)
