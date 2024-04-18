#!/usr/bin/env python3
""" complex types functions """
from typing import Callable


def make_multiplier(multiplayer: float) -> Callable[[float], float]:
    """complex types functions"""
    return lambda x: multiplayer ** 2
