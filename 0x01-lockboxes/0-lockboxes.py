#!/usr/bin/python3
"""
Solution to lockboxes problem
"""


def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for index in range(len(boxes)):
            boxes_checked = k in boxes[index] and k != index
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
