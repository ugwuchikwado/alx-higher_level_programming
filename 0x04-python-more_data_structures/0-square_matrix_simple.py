def square_matrix_simple(matrix=[]):
    temp_matrix = []
    for x in range(len(matrix)):
        new_matrix = []
        for y in range(len(matrix[0])):
            new_matrix.append(matrix[x][y] ** 2)
        temp_matrix.append(new_matrix)
    return temp_matrix

