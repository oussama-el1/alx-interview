#!/usr/bin/python3
"""
  Prototype: def minOperations(n)
  Returns an integer
  If n is impossible to achieve, return 0
"""


def isprime(n: int) -> bool:
    """ is odd """
    for i in range(2, int(n / 2)):
        if n % i == 0:
            return False
    return True


def min_operations(n: int) -> int:
    """Returns the minimum number of operations to reach n characters"""

    if n < 1:
        return 0

    prime_factors = []

    for i in range(2, int(n / 2)):
        if n % i == 0 and isprime(i):
            prime_factors.append(i)
            r = n / i
            if isprime(r):
                prime_factors.append(int(r))
                break
            else:
                n = r

    return sum(prime_factors)
