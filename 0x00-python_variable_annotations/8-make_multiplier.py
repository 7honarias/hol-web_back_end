#!/usr/bin/env python3
"""takes a float """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multi(x: float):
        return multiplier * x
    return multi