#!/usr/bin/env python3
""" Least Frequently used cache
"""
from collections import defaultdict, OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ Implementation of an LSU cache
        - tracks the frequency of gets for data
        - del the record with the lowest freq.
    """
    def __init__(self):
        super().__init__()
        self.order = OrderedDict()
        self.freq = defaultdict(int)
        self.min_freq = 0

    def put(self, key, item):
        """ Add item using LRU """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.move_to_end(key)
            self.freq[key] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                self._evict()
            self.cache_data[key] = item
            self.order[key] = None
            self.freq[key] = 1
            self.min_freq = 1

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        self.order.move_to_end(key)
        self.freq[key] += 1
        return self.cache_data.get(key)

    def _evict(self):
        """ Evict the least frequently used item, using LRU for ties
        """
        # Find the minimum frequency
        self.min_freq = min(self.freq.values())

        lfu_keys = [k for k, v in self.freq.items() if v == self.min_freq]

        if lfu_keys:
            lru_key = lfu_keys[0]
            for k in lfu_keys:
                if list(self.order.keys()
                        ).index(k) < list(self.order.keys()).index(lru_key):
                    lru_key = k

            print("DISCARD: {}".format(lru_key))
            del self.cache_data[lru_key]
            del self.order[lru_key]
            del self.freq[lru_key]
