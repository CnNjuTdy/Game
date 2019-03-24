# -*- coding: utf-8 -*-
# Time       : 2019/3/21 23:38
# Author     : tangdaye
# Description: 配置
import threading


def attribute_config(name):
    try:
        return AttributeConfig.instance().__getattribute__(name)
    except AttributeError:
        return {}


def game_config(name):
    try:
        return GameConfig.instance().__getattribute__(name)
    except AttributeConfig:
        return 0


class GameConfig:
    """单例模式"""
    _instance_lock = threading.Lock()

    max_skill_length = 2
    max_equipment_length = 3

    @classmethod
    def instance(cls):
        with AttributeConfig._instance_lock:
            if not hasattr(AttributeConfig, "_instance"):
                AttributeConfig._instance = AttributeConfig()
        return AttributeConfig._instance


class AttributeConfig:
    """单例模式"""
    _instance_lock = threading.Lock()

    mage = {}
    warrior = {}
    npc = {}

    shield = {'defense': 50}
    sword = {'attack': 40}
    magic_tome = {'hp': 200}
    scepter = {'power': 40}

    vitality_shield = {'hp': 80}
    xuanwu_shield = {'defense': 30}
    sword_case = {'critical': 15}
    sword_tassel = {'speed': 70}
    feather = {'power': 20}
    ice_piece = {'defense': 20}
    imperfect_sheet = {'power': 15}
    cover = {'hp': 100}

    @classmethod
    def instance(cls):
        with AttributeConfig._instance_lock:
            if not hasattr(AttributeConfig, "_instance"):
                AttributeConfig._instance = AttributeConfig()
        return AttributeConfig._instance


if __name__ == '__main__':
    a = AttributeConfig()

    pass
