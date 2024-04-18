#!/usr/bin/env python3
"""complex types mixed list"""
from typing import List


def sum_mixed_list(mxd_lst: List[float | int]) -> float:
    """mixed sum"""
    return sum(mxd_lst)
