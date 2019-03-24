# -*- coding: utf-8 -*-
# Time       : 2019/3/21 23:43
# Author     : tangdaye
# Description: 职业
from model.attribute_owner import AttributeOwner
from model.equipment import EquipmentList
from model.skill import SkillList
from model.state import DefaultState
from model.weapon import NoWeapon
from pattern.observer import Subject


class Role(Subject, AttributeOwner):
    """职业基类
    """

    _config_name = 'role'

    def __init__(self):
        super().__init__()
        self._weapon = NoWeapon()
        self._equipments = EquipmentList()
        self._skills = SkillList()
        self._state = DefaultState()

    def get_attribute(self, name):
        attribute = self._attributes.get(name)
        if attribute is not None:
            return attribute + self._weapon.get_attribute(name) + self._equipments.get_attribute(name)
        return self._weapon.get_attribute(name) + self._equipments.get_attribute(name)

    # def attack(self):
    #     self._state.attack(self)
    #
    # def be_attacked(self, attack_instance):
    #     self._state.be_attacked(self, attack_instance)

    def __str__(self):
        return '职业'


class Mage(Role):
    _config_name = 'mage'

    def __init__(self):
        super().__init__()

    def __str__(self):
        return '法师'


class Warrior(Role):
    _config_name = 'warrior'

    def __init__(self):
        super().__init__()

    def __str__(self):
        return '战士'


class NPC(Role):
    _config_name = 'npc'

    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'NPC'


if __name__ == '__main__':
    role = Mage()
