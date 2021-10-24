#!/usr/bin/env python3

"""Python Async"""

from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generate Async generator."""
    for _ in range(0, 10) :
        await sleep(1)
        yield uniform(0, 10)
