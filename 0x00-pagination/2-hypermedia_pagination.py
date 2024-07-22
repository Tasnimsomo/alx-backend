#!/usr/bin/env python3
"""1. Simple pagination"""

import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Write a function named index_range that takes two
    integer arguments page and page_size.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

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
        """
        Implement a method named get_page that takes two integer arguments
        page with default value 1 and page_size with default value 10."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start_index:end_index]

        def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """returns a dictionary containing the following key-value pairs
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        start, end = index_range(page, page_size)

        # estimating the next page
        if (page < total_pages):
            next_page = page + 1
        else:
            next_page = None

        # estimating the previous page
        if (page == 1):
            prev_page = None
        else:
            prev_page = page - 1

        return {'page_size': len(data),
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
                }
