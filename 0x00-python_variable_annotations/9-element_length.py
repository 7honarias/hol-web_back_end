#!/usr/bin/env python3
"""funtion parameters for the command line"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """length of the element in the list"""
    return [(i, len(i)) for i in lst]
