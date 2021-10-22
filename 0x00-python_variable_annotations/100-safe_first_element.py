#!/usr/bin/env python3
"""The type of elements are not know"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of a list of elements"""
    if lst:
        return lst[0]
    else:
        return None