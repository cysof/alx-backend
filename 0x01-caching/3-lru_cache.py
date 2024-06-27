#!/usr/bin/env python3
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):

    def __init__(self):
        super().__init__()
        self.access_order = []
    
    def put(self, key, item):

        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            recent_item = self.access_order.pop(0)
            del self.cache_data[recent_item]
            print(f"DISCARD: {recent_item}")

        self.cache_data[key] = item
        self.access_order.append(key)
    
    def get(self, key):
        """ Return value in self.cache_data linked to key
        If key is None or key does not exist in self.cache_data, return None
        """
        # if key is None or key not in self.cache_data:
        #     return None
        # return self.cache_data.get(key)
        if key is not None:
            if key in self.cache_data:
                # update access order
                self.access_order.remove(key)
                self.access_order.append(key)
                return self.cache_data[key]  # return value associated with key
        return None