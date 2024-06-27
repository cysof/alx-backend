#!/usr/bin/env python3

""" LIFO cache module that inherits from BaseCaching and is a caching system
Must use self.cache_data - dictionary from the parent class BaseCaching
LIFO algorithm must be used to manage the cache
"""
BaseCaching = __import__('base_caching').BaseCaching

class LIFOCache(BaseCaching):

    def __init__(self):
        super().__init__()
        self.cache_keys = []

    def put(self, key, item):

        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_item = self.cache_keys.pop()
            del self.cache_data[last_item]
            print(f"DISCARD: {last_item}")
        self.cache_keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)

