#!/usr/bin/env python3
"""takes a float """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a multiplier callable"""
    def multi(x: float) -> float:
        """returns a multiplier callable"""
        return float(multiplier * x)
    return multi
