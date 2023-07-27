#!/usr/bin/env python3
"""0-basic_cache"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    def __init__(self):
        """_summary_
        """
        super().__init__()

    def put(self, key, item):
        """_summary_"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """_summary_"""
        if key is not None or key in self.cache_data.keys():
            return self.cache_data.get(key)
        return None
