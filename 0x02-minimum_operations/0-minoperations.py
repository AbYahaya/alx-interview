#!/#!/usr/bin/python3
"""
By Ab yahaya
"""


def minOperations(n: int) -> int:
    """
    Calculates the minimum number of operations to result in exactly n H char
    using Copy All and Paste operations.
    
    Args:
        n (int): The target number of H characters.
    
    Returns:
        int: The minimum number of operations needed to reach exactly n H char
             If n is impossible to achieve, return 0.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        # Divide n by the current factor as much as possible
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
