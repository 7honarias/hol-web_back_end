#!/usr/bin/python3
""" simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ range index function """
    return ((page * page_size)-page_size, (page * page_size))
