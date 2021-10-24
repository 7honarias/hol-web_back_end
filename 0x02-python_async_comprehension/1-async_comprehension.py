#!/usr/bin/env python3
"""Python Generator"""

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """Gener Async comprehension"""
    return [i async for i in async_generator()]
