#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially
from 0 to n - 1 and each box may
contain keys to the other boxes.

    -Prototype: def canUnlockAll(boxes)
    -boxes is a list of lists
    -A key with the same number as a box opens that box
    -You can assume all keys will be positive integers
    -There can be keys that do not have boxes
    -The first box boxes[0] is unlocked
    -Return True if all boxes can be opened, else return False
"""
from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Check if all boxes can be unlocked by using their keys.
    Boxes are represented as a list of lists, where each inner list contains
    the keys to unlock the corresponding box.

    Args:
    boxes (List[List[int]]): List of lists, where each inner list contains
    the keys to unlock the corresponding box.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.
    """
    num_boxes: int = len(boxes)
    visited: List[bool] = [False] * num_boxes
    queue: List = [0]
    visited[0] = True

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if key < num_boxes and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
