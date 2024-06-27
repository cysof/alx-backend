#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize the Server class.

        This method initializes the Server class by setting the __dataset and __indexed_dataset attributes to None.

        Parameters:
            None

        Returns:
            None
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get the hypermedia index for a given dataset.

        Args:
            index (int, optional): The index of the dataset. Defaults to None.
            page_size (int, optional): The size of the page. Defaults to 10.

        Returns:
            dict: A dictionary containing the following key-value pairs:
                - index (int): The index of the dataset.
                - next_index (int): The index of the next dataset.
                - page_size (int): The size of the page.
                - data (list): The data at the given index, or None if the index is not present.

        Raises:
            AssertionError: If the index is not within the range of the dataset.
        """
        # Check if index is within the range of dataset
        assert index in range(len(self.dataset()))
        index_dict = self.indexed_dataset()

        # Check if index is 0 and page_size is 10
        if index == 0 and page_size == 10:
            # Get the first 10 elements from index_dict
            data = index_dict[0:10]
        elif index is None:  # Check if index is None
            index = index  # Assign index to itself (redundant statement?)
        # Get the data at the given index from index_dict,
        # or None if index is not present
        data = [index_dict[index] if index in index_dict else None]

        return {
            "index": index,  # Return the index
            "next_index": index + 1,  # Return the next index
            "page_size": page_size,  # Return the page size
            "data": data  # Return the data
        }