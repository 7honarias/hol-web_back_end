#!/usr/bin/env python3
"""sum mixed list int and float"""
from typing import Union, List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """sum mixed list int and float"""
    return float(sum(mxd_list))
