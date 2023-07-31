def fun(**kwargs):
    result = {}
    for k, v in kwargs.items():
        try:
            result[v] = k
        except TypeError:
            result[str(v)] = k

    print(result)


fun(res=1, reverse=[1, 2, 3])
