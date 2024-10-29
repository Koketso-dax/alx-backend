#!/usr/bin/env python3
""" LRU Cache """
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ Caching system using LRU algorithm """
    def __init__(self):
        """ Init Superclass & add order """
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        """ Add an item using LRU algorithm """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= self.MAX_ITEMS:
                lru_key = next(iter(self.order))
                print("DISCARD: {}".format(lru_key))
                del self.cache_data[lru_key]
                del self.order[lru_key]

        self.cache_data[key] = item
        self.order[key] = None

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        # Move the key to the end to mark it as most recently used
        self.order.move_to_end(key)
        return self.cache_data.get(key)
