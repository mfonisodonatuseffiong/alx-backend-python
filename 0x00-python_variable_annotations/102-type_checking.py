#!/usr/bin/env python3
"""
Task 12: Type Checking
"""

from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Creates multiple copies of items in a tuple.

    Args:
        lst (Tuple[int, ...]): The tuple to be copied.
factor (int): The number of times each item will be repeated. Default is 2.

    Returns:
        List[int]: A list with items repeated 'factor' times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
