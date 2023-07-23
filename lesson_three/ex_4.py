list = [1, 1, 1, 1, 4, 4, 5, 6, 6]
i = 0

while i < len(list):
    q = list[i]
    x = 0
    while x < len(list):
        if q == list[x]:
            list.pop(x)
        x += 1
    i += 1

print(list)
