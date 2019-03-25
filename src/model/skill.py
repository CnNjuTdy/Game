# -*- coding: utf-8 -*-
# Time       : 2019/3/22 19:17
# Author     : tangdaye
# Description: 技能
from model.items import ItemList
from config import damage_config
from config import level_up_config
from config import game_config
from model.role import Mage, Warrior


# from abc import abstractmethod


class Skill:
    _config_name = 'skill_name'

    def __init__(self, fit_roles):
        self._damage = damage_config(self._config_name)
        self._max_level = game_config('skill_max_level')
        self._level = 0
        self._fit_roles = fit_roles

    def level_up(self):
        if self._level == self._max_level:
            return 'already full level'
        self._damage += level_up_config(self._config_name)

    def is_suitable_weapon(self, role_class):
        return role_class in self._fit_roles


class Sprint(Skill):
    _config_name = 'sprint'

    def __init__(self):
        super().__init__([Warrior])


class Trample(Skill):
    _config_name = 'trample'

    def __init__(self):
        super().__init__([Warrior])


class Combat(Skill):
    _config_name = 'combat'

    def __init__(self):
        super().__init__([Warrior])


class Thunder(Skill):
    _config_name = 'thunder'

    def __init__(self):
        super().__init__([Mage])


class Wind(Skill):
    _config_name = 'wind'

    def __init__(self):
        super().__init__([Mage])


class Fire(Skill):
    _config_name = 'fire'

    def __init__(self):
        super().__init__([Mage])


class SkillList(ItemList):
    def __init__(self):
        super().__init__(game_config('max_skill_length'))
