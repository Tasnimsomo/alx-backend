#!/usr/bin/env python3
"""0. Basic dictionary"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """
    Create a class BasicCache that inherits from
    BaseCaching and is a caching system:
    """
    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data
        the item value for the key key.
        """
        if item is None or key is None:
            return None
        self.cache_data[key] = item

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
