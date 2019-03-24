# -*- coding: utf-8 -*-
# Time       : 2019/3/22 17:16
# Author     : tangdaye
# Description: 装备
from model.attribute_owner import AttributeOwner
from model.items import ItemList
from config import game_config


class Equipment(AttributeOwner):
    _config_name = 'equipment'

    def __str__(self):
        return '装备'


class VitalityBooster(Equipment):
    _config_name = 'vitality_booster'

    def __str__(self):
        return '活力球'


class AttackRing(Equipment):
    _config_name = 'attack_ring'

    def __str__(self):
        return '攻击指环'


class CriticalRing(Equipment):
    _config_name = 'critical_ring'

    def __str__(self):
        return '暴击指环'


class Armor(Equipment):
    _config_name = 'armor'

    def __str__(self):
        return '板甲'


class Kaya(Equipment):
    _config_name = 'kaya'

    def __str__(self):
        return '辉光'


class PowerTreads(Equipment):
    _config_name = 'power_treads'

    def __str__(self):
        return '动力鞋'


class CrimsonGuard(Equipment):
    _config_name = 'crimson_guard'

    def __str__(self):
        return '赤红甲'


class Crystals(Equipment):
    _config_name = 'crystals'

    def __str__(self):
        return '水晶剑'


class EquipmentList(ItemList):
    def __init__(self):
        super().__init__(game_config('max_equipment_length'))

    def get_attribute(self, name):
        result = 0
        for equipment in self._items:
            result += equipment.get_attribute(name)
        return result

    def __str__(self):
        return '装备'
