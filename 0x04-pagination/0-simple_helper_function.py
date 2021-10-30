#!/usr/bin/python3
""" simple helper function"""


def index_range(page, page_size):
    """ range index function """
    return ((page * page_size)-page_size, (page * page_size))
