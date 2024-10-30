#!/usr/bin/env python3
""" FIFO cache. """
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """ First-In-First-Out Cache class
        - Uses an OrderedDict to maintain the order of insertion
        - When capacity is exceeded, the first item is discarded
    """

    def __init__(self):
        """ Init superclass """
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        """ Assigned key: item to the cache
        using FIFO algorithm
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= self.MAX_ITEMS:
                first_key = next(iter(self.order))
                print("DISCARD: {}".format(first_key))
                del self.cache_data[first_key]
                del self.order[first_key]

        self.cache_data[key] = item
        self.order[key] = None

    def get(self, key):
        """ Return the value linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
