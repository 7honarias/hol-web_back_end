#!/usr/bin/env python3

""" Python Generator """

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Gener Async comprehension """
    x = [i async for i in async_generator()]
    return x
