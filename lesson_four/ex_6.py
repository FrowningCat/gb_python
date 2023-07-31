list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
index_1 = 11
index_2 = -2

def fun(list, index_1, index_2):
    sum = 0
    if index_1 > index_2:
        a = index_2
        index_2 = index_1
        index_1 = a
    if index_1 > len(list):
        index_1 = list[-1]
    if index_2 > len(list):
        index_2 = list[-1]
    for i in range(list[index_1], list[index_2] + 1):
        sum = sum + list[index_1]
    print(sum)


fun(list, index_1, index_2)
