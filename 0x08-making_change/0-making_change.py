#!/usr/bin/python3
""" 0-making_change.py """
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    function: makeChange
    args: coins -> List[int], total: int
    """
    if total <= 0:
        return 0

    sorted_coins = sorted(coins, reverse=True)
    counter = 0
    copy_total = total

    for coin in sorted_coins:
        if coin <= copy_total:
            count = copy_total // coin
            copy_total -= coin * count
            counter += count
        if copy_total == 0:
            break

    if copy_total != 0:
        return -1

    return counter
