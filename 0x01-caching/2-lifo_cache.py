#!/usr/bin/env python3
""" LIFO cache """
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """ Cache that uses LIFO algorithm
        - Uses OrderedDict to maintain order of insertion
        - When capacity is exceeded, the last item is discarded
    """

    def __init__(self):
        """ Init superclass """
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        """ inserts item at key and deletes last inserted
        record if Max is reached.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= self.MAX_ITEMS:
                last_key = next(reversed(self.order))
                print("DISCARD: {}".format(last_key))
                del self.cache_data[last_key]
                del self.order[last_key]

        self.cache_data[key] = item
        self.order[key] = None

    def get(self, key):
        """ Return the value linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
