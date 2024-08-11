#!/usr/bin/python3

"""
calculates the minimum number of operations needed to achieve
exactly n characters using the most optimal series of
Copy All and Paste operations.
"""


def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
