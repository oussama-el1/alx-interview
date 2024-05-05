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


def canUnlockAll(boxes):
    """
    Checks if all boxes can be unlocked by keys in each box.

    :param boxes: List of lists, where each inner list.
    :type boxes: List[List[int]]
    :return: True if all boxes can be unlocked, False otherwise.
    :rtype: bool
    """
    num_boxes: int = len(boxes)
    visited: bool = [False] * num_boxes
    queue = [0]
    visited[0] = True

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if 0 <= key < num_boxes and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
