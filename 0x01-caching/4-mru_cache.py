#!/usr/bin/env python3
""" MRU Cache """
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ Caching system using MRU algorithm.
    """

    def __init__(self):
        """ Init Superclass & add order """
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        """ Add an item using MRU algorithm """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= self.MAX_ITEMS:
                mru_key = next(reversed(self.order))
                print("DISCARD: {}".format(mru_key))
                del self.cache_data[mru_key]
                del self.order[mru_key]

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
