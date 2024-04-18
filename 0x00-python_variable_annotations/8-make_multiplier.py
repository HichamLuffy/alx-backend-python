#!/usr/bin/env python3
""" complex types functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """complex types functions"""
    return lambda x: x * multiplier
