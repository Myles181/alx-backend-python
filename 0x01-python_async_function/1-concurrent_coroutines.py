#!/usr/bin/env python3
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

"""
wait n function
"""


async def wait_n(n: int, max_delay: int) -> List[int]:
    """
    Definittion of wait n
    """
    tasks: List[int] = [wait_random(max_delay) for _ in range(n)]
    delay: List[int] = await asyncio.gather(*tasks)
    return sorted(delay)
