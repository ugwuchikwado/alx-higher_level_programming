#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    matrix_len = len(matrix[0])
    if matrix_len == 0:
        print()
    else:
        count = 0
        for num1 in matrix:
            for num2 in num1:
                count += 1
                if count == matrix_len:
                    print("{:d}".format(num2), end="\n")
                else:
                    print("{:d} ".format(num2), end="")
            count = 0
