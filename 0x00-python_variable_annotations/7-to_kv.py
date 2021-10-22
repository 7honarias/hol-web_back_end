#!/usr/bin/env python3
"""take string and a int return tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Take a string and a float return tuple"""
    return (k, v**2)
