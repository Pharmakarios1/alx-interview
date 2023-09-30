#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """

    if n <= 0:
        return []
    p_triangle = [[1]]
    for i in range(1, n):
        row = [1]
        prev_row = p_triangle[i - 1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        p_triangle.append(row)
    return p_triangle
