matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def fun(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        new_matrix.append(list())
        for j in range(len(matrix)):
            new_matrix[i].append(matrix[j][i])
    print(new_matrix)


fun(matrix)
