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
    cp = n
    if cp < 1:
        return 0

    primes = []

    if cp == 4:
        end = 3
    else:
        end = int(cp / 2)

    for i in range(2, end):
        if isprime(i) and cp % i == 0:
            primes.append(i)
            r = cp / i
            if isprime(r):
                primes.append(int(r))
                break
            else:
                cp = r

    s = 0
    for prime in primes:
        s = s + prime

    return s
