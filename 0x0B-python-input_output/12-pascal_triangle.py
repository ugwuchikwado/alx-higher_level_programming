#!/usr/bin/python3
"""
Defines a Pascal's Triangle function.
"""


def pascal_triangle(n):
    """
    Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        trian = triangles[-1]
        tempo = [1]
        for i in range(len(tri) - 1):
            tempo.append(trian[i] + trian[i + 1])
        tempo.append(1)
        triangles.append(tempo)
    return triangles
