from sys import getsizeof

data = [1, 1.2, "Hello", False, 1]
i = 0

while i < len(data):
    x = data[i]
    i += 1
    if isinstance(data[i - 1], int):
        print(i, x, id(x), getsizeof(x), hash(x), isinstance(data[i - 1], int))
    elif isinstance(data[i - 1], str):
        print(i, x, id(x), getsizeof(x), hash(x), isinstance(data[i - 1], str))
    else:
        print(i, x, id(x), getsizeof(x), hash(x))