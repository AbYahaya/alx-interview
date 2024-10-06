#!/usr/bin/pyhton3
"""
Pascals's triangle
"""

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row of Pascal's Triangle

    for i in range(1, n):
        row = [1]  # First element is always 1
        # Calculate the intermediate values of the row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # Last element is always 1
        triangle.append(row)

    return triangle
