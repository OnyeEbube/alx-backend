#!/usr/bin/env python3
"""Write a function named index_range that takes two integer
arguments page and page_size."""

import csv
import math
from typing import List, Dict


def index_range(page, page_size):
    """Returns a tuple(start_ind, end_ind)"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


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
        """returns dataset list
        """
        assert isinstance(
                page, int), "raised when page and/or page_size are not ints"
        assert page != 0, "raised with 0"
        assert page > 0, "raised with negative values"
        assert type(
            page_size) is int, "raised when page and/orpage_size are not ints"

        assert page_size != 0, "raised with 0"
        assert page_size > 0, "raised with negative values"
        dataset = self.dataset()

        start_index, end_index = index_range(page, page_size)
        return dataset[start_index:end_index]

        if start_index >= len(dataset) or start_index < 0:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Return hyper
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        hyper_metadata = {
                "page_size": len(data),
                "page": page,
                "data": data,
                "next_page": page + 1 if page < total_pages else None,
                "prev_page": page - 1 if page > 1 else None,
                "total_pages": total_pages
            }
        return hyper_metadata
