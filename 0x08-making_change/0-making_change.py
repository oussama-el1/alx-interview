#!/usr/bin/python3
"""
The coin change problem
"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    makeChange Function
    """

    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for i in range(coin, total + 1):
        for coin in coins:
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
