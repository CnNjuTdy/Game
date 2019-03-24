# -*- coding: utf-8 -*-
# Time       : 2019/3/22 19:21
# Author     : tangdaye
# Description: 一系列数据的集合


class ItemList:
    def __init__(self, max_size):
        self._max_size = max_size
        self._items = []

    def get(self, index):
        if index < len(self._items):
            return self._items[index]
        return None

    def swap(self, index, new_item):
        self._items[index] = new_item

    def add(self, new_item):
        if len(self._items) < self._max_size:
            self._items.append(new_item)
            return 1
        else:
            return 0
