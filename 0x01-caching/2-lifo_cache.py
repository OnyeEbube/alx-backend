#!/usr/bin/env python3
"""
Create a class LIFOCache that inherits from BaseCaching and is a
caching system"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """_summary_
    """
    def __init__(self):
        """_summary_
        """
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """_summary_
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                last_key = self.keys_order.pop(-1)
                del self.cache_data[last_key]
                print("DISCARD: {}".format(last_key))
            self.cache_data[key] = item
            self.keys_order.append(key)

    def get(self, key):
        """_summary_
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
