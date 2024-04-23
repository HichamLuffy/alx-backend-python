#!/usr/bin/env python3
"""Async Comprehension"""
from typing import List
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List:
    """async comprehension"""
    result = []
    async for i in async_generator():
        result.append(i)
    return result
