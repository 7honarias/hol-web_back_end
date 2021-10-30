#!/usr/bin/env python3
""" simple helper function"""
from typing import Tuple
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get page function """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        result = self.dataset()
        pageRange = index_range(page, page_size)
        if len(result) < pageRange[0]:
            return []
        return result[pageRange[0]: pageRange[1]]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ range index function """
    return ((page - 1) * page_size, (page * page_size))
