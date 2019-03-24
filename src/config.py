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


def damage_config(name):
    try:
        return DamageConfig.instance().__getattribute__(name)
    except AttributeConfig:
        return 0


def level_up_config(name):
    try:
        return LevelUpConfig.instance().__getattribute__(name)
    except AttributeConfig:
        return 0


class DamageConfig:
    """伤害设置 单例模式"""
    _instance_lock = threading.Lock()

    sprint = 60
    trample = 45
    combat = 30
    thunder = 50
    wind = 35
    fire = 20

    @classmethod
    def instance(cls):
        with DamageConfig._instance_lock:
            if not hasattr(DamageConfig, "_instance"):
                DamageConfig._instance = DamageConfig()
        return DamageConfig._instance


class AttributeConfig:
    """属性设置 单例模式"""
    _instance_lock = threading.Lock()

    # 角色属性
    mage = {'hp': 70, 'attack': 20, 'critical': 0, 'defense': 30, 'power': 10, 'speed': 100}
    warrior = {'hp': 100, 'attack': 40, 'critical': 20, 'defense': 40, 'power': 0, 'speed': 80}
    npc = {'hp': 100, 'attack': 10, 'critical': 10, 'defense': 10, 'power': 20, 'speed': 90}

    # 装备属性
    vitality_booster = {'hp': 200}
    attack_ring = {'attack': 60}
    critical_ring = {'critical': 30}
    armor = {'defense': 60}
    kaya = {'power': 50}
    power_treads = {'speed': 35, 'power': 5, 'critical': 5, 'attack': 20}
    crimson_guard = {'hp': 160, 'defense': 40}
    crystals = {'attack': 40, 'critical': 15}

    # 武器属性
    shield = {'defense': 50}
    sword = {'attack': 40}
    magic_tome = {'hp': 200}
    scepter = {'power': 40}

    # 武器配件
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


class GameConfig:
    """游戏设置 单例模式"""
    _instance_lock = threading.Lock()

    max_skill_length = 2
    max_equipment_length = 3
    role_max_level = 3
    skill_max_level = 3

    @classmethod
    def instance(cls):
        with GameConfig._instance_lock:
            if not hasattr(GameConfig, "_instance"):
                GameConfig._instance = GameConfig()
        return GameConfig._instance


class LevelUpConfig:
    """升级设置 单例模式"""
    _instance_lock = threading.Lock()

    sprint = 20
    trample = 25
    combat = 30
    thunder = 20
    wind = 30
    fire = 40

    warrior = {'hp': 50, 'attack': 10, 'critical': 5, 'defense': 20, 'power': 0, 'speed': 10}
    mage = {'hp': 50, 'attack': 5, 'critical': 2, 'defense': 10, 'power': 10, 'speed': 10}
    npc = {'hp': 10, 'attack': 3, 'critical': 5, 'defense': 5, 'power': 10, 'speed': 5}

    @classmethod
    def instance(cls):
        with LevelUpConfig._instance_lock:
            if not hasattr(LevelUpConfig, "_instance"):
                LevelUpConfig._instance = LevelUpConfig()
        return LevelUpConfig._instance


if __name__ == '__main__':
    pass
