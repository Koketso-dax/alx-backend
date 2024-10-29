#!/usr/bin/env python3
""" Basic cache using base_caching super """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache inherits from BaseCaching
        and implements a basic cache system
    """

    def __init__(self):
        super().__init__()
        del self.MAX_ITEMS

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
