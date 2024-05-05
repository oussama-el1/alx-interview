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
    :param boxes:
    :type boxes:
    :return:
    :rtype:
    """
    startbox = 0
    n = len(boxes)
    nodes_queue = []
    visited = [False] * n
    nodes_queue.append(startbox)
    visited[startbox] = True
    visited_nodes = [startbox]

    while len(nodes_queue) > 0:
        node = nodes_queue.pop(0)
        for neighbor in boxes[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                nodes_queue.append(neighbor)
                visited_nodes.append(neighbor)
    if n == len(visited_nodes):
        return True
    else:
        return False
