#!/usr/bin/env python3
import asyncio
import random

"""
wait random function gets a random float number and sleeps
"""


async def wait_random(max_delay: int = 10) -> float:
    """
        Defintion of wait_random
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
