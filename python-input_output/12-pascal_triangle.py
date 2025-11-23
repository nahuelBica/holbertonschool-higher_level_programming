#!/usr/bin/python3
"""
Generates pascal triangle with n lines
"""


def pascal_triangle(n):
    
    if n <= 0:
        return []

    pascal_triangle = []
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            else:
                line.append(
                    pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]
                )

        pascal_triangle.append(line)

    return pascal_triangle