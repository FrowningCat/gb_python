matrix = [[1, 2, 3], [4, 5, 6]]


def fun(matrix):
    matrix_0 = matrix[0]
    matrix_1 = matrix[1]
    i = 0
    new_matrix = []
    while i < len(matrix_0):
        new_matrix.append((matrix_0[i], matrix_1[i]))
        i += 1
    print(new_matrix)


fun(matrix)
