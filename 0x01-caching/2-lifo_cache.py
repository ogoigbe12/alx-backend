#!/usr/bin/python3

'''
LIFO Caching
'''

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Initialize
        """
        self.last_item = ""
        super().__init__()

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data
        the item value for the key key.
        """
        if key and item:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.last_item)
            print('DISCARD:', self.last_item)
        if key:
            self.last_item = key

    def get(self, key):
        """
        Return value of cache_data linked to key
        """
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        else:
            return None
