#!/usr/bin/env python3
"""1-fifo_cache"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
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
        if key is not None or item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data:
                first_key = self.keys_order.pop(0)
                del self.cache_data[first_key]
                print("DISCARD: {}". format(first_key))
            self.cache_data[key] = item
            self.keys_order.append(key)
        else:
            pass

    def get(self, key):
        """return the value in self.cache_data linked to key

        Args:
                        key (_type_): _description_
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
