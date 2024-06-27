#!/usr/bin/env python3
BaseCaching = __import__('base_caching').BaseCaching
""" BaseCaching module: that inherits from BaseCaching and is a caching system:

    You must use self.cache_data - dictionary from the parent class BaseCaching
    This caching system doesn’t have limit
"""

class BasicCache(BaseCaching):
    """ BasicCache class that inherits from BaseCaching
    No limits on number of items it can store.
    """

    def __init__(self):
        """ Initialize BasicCache
        """
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)