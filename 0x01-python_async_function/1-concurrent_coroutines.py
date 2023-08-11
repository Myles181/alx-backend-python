#!/usr/bin/env python3
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

"""
wait n function
"""


async def wait_n(n: int, max_delay: int):
    """
    Definittion of wait n
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delay = await asyncio.gather(*tasks)
    return sorted(delay)

