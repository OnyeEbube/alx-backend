#!/usr/bin/env python3
"""Create a class MRUCache that inherits
from BaseCaching and is a caching system:

You must use self.cache_data - dictionary
from the parent class BaseCaching
You can overload def __init__(self): but don’t
forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the
item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher
that BaseCaching.MAX_ITEMS:
you must discard the most recently used item
(MRU algorithm)
you must print DISCARD: with the key discarded and
following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in
self.cache_data, return None.
"""

from collections import defaultdict


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """_summary_
    """

    def __init__(self):
        """_summary_
        """
        super().__init__()
        self.frequency_map = defaultdict(int)
        self.frequencies = defaultdict(list)
        self.min_frequency = 0

    def put(self, key, item):
        """_summary_

        Args:
                        key (_type_): _description_
                        item (_type_): _description_
        """
        if key is None or item is None:
            pass
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency_map[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                while not self.frequencies[self.min_frequency]:
                    self.min_frequency += 1
                lfu_key = self.frequencies[self.min_frequency].pop(0)
                del self.cache_data[lfu_key]
                print("DISCARD: {}".format(lfu_key))
                del self.frequency_map[lfu_key]

            self.cache_data[key] = item
            self.frequency_map[key] = 1
            self.frequencies[1].append(key)
            self.min_frequency = 1

    def get(self, key):
        """return the value in self.cache_data linked to key

        Args:
                        key (_type_): _description_
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency_map[key] += 1
        freq = self.frequency_map[key]

        if key in self.frequencies[freq - 1]:
            self.frequencies[freq - 1].remove(key)
        self.frequencies[freq].append(key)

        if not self.frequencies[self.min_frequency]:
            self.min_frequency += 1

        return self.cache_data[key]
