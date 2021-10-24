#!/usr/bin/env python3

""" Python Async """

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """ Measure Async """
    start = time()
    task = [async_comprehension() for i in range(4)]
    await gather(*task)
    end = time()
    return (end - start)
