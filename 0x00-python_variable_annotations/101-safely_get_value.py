#!/usr/bin/env python3
"""task 11"""
from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """typevar :TypeVar is used to create a generic type
    that can change based on the input. This function looks
    up key in dct and returns the corresponding
    value or the default if the key is not found."""
    if key in dct:
        return dct[key]
    else:
        return default
