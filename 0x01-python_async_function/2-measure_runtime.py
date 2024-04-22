#!/usr/bin/env python3
"""measure runtime"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """calcul total execution time"""
    start_time = time.perf_counter()
    # print("i start at :", start_time)
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    # print("i end at :", end_time)
    execution_time = end_time - start_time
    return execution_time / n
