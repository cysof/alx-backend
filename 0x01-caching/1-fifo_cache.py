#!/usr/bin/env python3

""" FIFO cache module that inherits from BasicCache and is a caching system
Must use self.cache_data - dictionary from the parent class BaseCaching
FIFO algorithm must be used to manage the cache
"""
BaseCaching = __import__('base_caching').BaseCaching

class FIFOCache(BaseCaching):
    
    def __init__(self):
        super().__init__()
        self.cache_keys = []
    
    def put(self, key, item):
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:

            first_item = self.cache_keys.pop(0)
            del self.cache_data[first_item]
            print(f"DISCARD: {first_item}")
        self.cache_keys.append(key)
        self.cache_data[key] = item
    
    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
