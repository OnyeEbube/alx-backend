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

from queue import PriorityQueue


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """_summary_
    """

    def __init__(self):
        """_summary_
        """
        super().__init__()
        self.frequency_map = {}
        self.pq = PriorityQueue()

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
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                while self.pq.qsize() > 0:
                    freq, lfu_key = self.pq.get()
                    if self.frequency_map[lfu_key] == freq:
                        del self.cache_data[lfu_key]
                        print("DISCARD: {}".format(lfu_key))
                        del self.frequency_map[lfu_key]
                        break
            self.cache_data[key] = item
            self.frequency_map[key] = 0
            self.pq.put((0, key))

    def get(self, key):
        """return the value in self.cache_data linked to key

        Args:
                        key (_type_): _description_
        """
        if key is None or key not in self.cache_data.keys():
            return None

        self.frequency_map[key] += 1
        self.pq.put((self.frequency_map[key], key))
        return self.cache_data[key]
