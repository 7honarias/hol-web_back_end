#!/usr/bin/env python3
"""write an asynchronous command to a file"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random number of seconds to complete"""
    num = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
