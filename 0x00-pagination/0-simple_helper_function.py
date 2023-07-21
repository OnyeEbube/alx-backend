#!/usr/bin/env python3
"""Write a function named index_range that takes two integer
arguments page and page_size."""


def index_range(page, page_size):
    """Returns a tuple(start_ind, end_ind)"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
