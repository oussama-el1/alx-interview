#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange


# Test case 5: Multiple denominations, greedy optimal
print(makeChange([1, 3, 4], 6))  # Expected output: 2 -------- Error case
# Test case 9: Total is a multiple of the smallest coin
print(makeChange([2, 5, 10], 6))  # Expected output: 3 ----- Error case
