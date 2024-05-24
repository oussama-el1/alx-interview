#!/usr/bin/python3
"""
TODO:
    - Iterate through the data: Loop through each integer in the data list.
    - Check the first byte of each character:
        -For a single-byte character, the first byte must start with 0.
        -For multi-byte characters, the first byte must
         match one of the following patterns:
        -110xxxxx for two-byte characters.
        -1110xxxx for three-byte characters.
        -11110xxx for four-byte characters.
    -Check continuation bytes:
        - For multi-byte characters, the following bytes
          (continuation bytes) must start with 10.
          Validate the sequence:
    - Ensure that the sequence of bytes conforms to the UTF-8 encoding rules.
    - Return True or False:
        - If the sequence is valid UTF-8 encoding, return True.
        - Otherwise, return False.
    - Handle edge cases:
    - Consider edge cases such as invalid input or incomplete byte sequences.
    Hints:
        Use bitwise operations (&, |, >>, <<, etc.) to extract and manipulate
        individual bits of each integer.
        Maintain a state machine or flags to keep track of the current
        state of the UTF-8 encoding.
        Utilize masking and bit manipulation to check the
        patterns of each byte.
        Handle different byte lengths (1 to 4 bytes) based
        on the UTF-8 encoding rules.
"""
from typing import List


def check_continuation_bytes(data, start_index, expected_bytes):
    """ check_continuation_bytes """
    if start_index + expected_bytes >= len(data):
        return False
    for j in range(start_index + 1, start_index + 1 + expected_bytes):
        if data[j] & 0b11000000 != 0b10000000:
            return False
    return True


def validUTF8(data: List[int]):
    """ validUTF8 """
    i = 0
    while i < len(data):
        byte = data[i]
        if byte & 0b10000000 == 0 and byte <= 0b01111111:
            i += 1
        elif byte & 0b11100000 == 0b11000000:
            if not check_continuation_bytes(data, i, 1):
                return False
            i += 2
        elif byte & 0b11110000 == 0b11100000:
            if not check_continuation_bytes(data, i, 2):
                return False
            i += 3
        elif byte & 0b11111000 == 0b11110000:
            if not check_continuation_bytes(data, i, 3):
                return False
            i += 4
        else:
            return False
    return True
