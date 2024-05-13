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


def minOperations(n: int):
    """ minOperations : function """
    if n < 1:
        return 0

    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return sum(factors)
