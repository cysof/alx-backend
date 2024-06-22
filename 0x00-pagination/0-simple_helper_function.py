#!/usr/bin/env python3

""" Python script that contains function named index_range
that takes two integer arguments page and page_size.
Function returns a tuple of size two containing a start index
and an end index corresponding to the range of indexes to return
in a list for those particular pagination parameters.
Page numbers are 1-indexed, i.e. the first page is page 1.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices for a given page and page size.

    Args:
        page (int): The page number. Page numbers are 1-indexed, i.e. the first page is page 1.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index.
            The start index is calculated as (page - 1) * page_size.
            The end index is calculated as start_index + page_size.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)