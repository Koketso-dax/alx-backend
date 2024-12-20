#!/usr/bin/env python3
""" Hypermedia pagination """
import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for the
    given pagination parameters
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
        """Returns the requested page of the dataset
        """
        assert isinstance(page, int) and page > 0,\
            "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0,\
            "Page size must be a positive integer"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returns a dictionary containing the requested page of the dataset
        along with pagination metadata
        """
        data = self.get_page(page, page_size)
        total_pages = len(self.dataset()) // page_size + \
            (len(self.dataset()) % page_size > 0)
        return {
            "page": page,
            "page_size": page_size,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
