# -*- coding: utf-8 -*-
# Time       : 2019/3/22 19:17
# Author     : tangdaye
# Description: 技能
from model.items import ItemList
from config import damage_config
from config import level_up_config
from config import game_config

from abc import abstractmethod


class Skill:
    _config_name = 'skill_name'

    def __init__(self, max_level):
        self._damage = damage_config(self._config_name)

    @abstractmethod
    def level_up(self):
        pass


class Sprint(Skill):
    _config_name = 'sprint'

    def level_up(self):
        self._damage += level_up_config(self._config_name)


class Trample(Skill):
    _config_name = 'trample'

    def level_up(self):
        self._damage += level_up_config(self._config_name)


class Combat(Skill):
    _config_name = 'combat'

    def level_up(self):
        self._damage += level_up_config(self._config_name)


class Thunder(Skill):
    _config_name = 'thunder'

    def level_up(self):
        self._damage += level_up_config(self._config_name)


class Wind(Skill):
    _config_name = 'wind'

    def level_up(self):
        self._damage += level_up_config(self._config_name)


class Fire(Skill):
    _config_name = 'fire'

    def level_up(self):
        self._damage += level_up_config(self._config_name)


class SkillList(ItemList):
    def __init__(self):
        super().__init__(game_config('max_skill_length'))
