#!/usr/bin/env python3
""" Type Checking """
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """type checking advenced"""
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple[int, ...] = (12, 72, 91)

zoom_2x: List[int] = zoom_array(array)

zoom_3x: List[int] = zoom_array(array, int(3.0))
