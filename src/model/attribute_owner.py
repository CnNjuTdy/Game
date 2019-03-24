# -*- coding: utf-8 -*-
# Time       : 2019/3/22 17:19
# Author     : tangdaye
# Description: 所有有属性的父类
from config import attribute_config


class AttributeOwner:
    # 'hp': None, 'speed': None, 'attack': None, 'critical': None, 'defense': None, 'power': None ,
    # 'exp':None, 'level':None
    _config_name = 'attribute_owner'

    def __init__(self):
        self._attributes = attribute_config(self._config_name)

    def get_attribute(self, name):
        t = self._attributes.get(name)
        return t if t is not None else 0
