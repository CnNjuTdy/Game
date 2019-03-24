# -*- coding: utf-8 -*-
# Time       : 2019/3/22 16:46
# Author     : tangdaye
# Description: 武器
from model.attribute_owner import AttributeOwner


class Weapon(AttributeOwner):
    _config_name = 'weapon'
    _weapon_parts = []

    def get_attribute(self, name):
        t = 0
        for weapon_part in self._weapon_parts:
            t += weapon_part.get_attribute(name)
        m = self._attributes.get(name)
        return m + t if m is not None else t

    def __str__(self):
        return '武器'


class Shield(Weapon):
    _config_name = 'shield'

    def __init__(self):
        super().__init__()

    def __str__(self):
        return '盾牌'


class Sword(Weapon):
    _config_name = 'sword'

    def __init__(self):
        super().__init__()

    def __str__(self):
        return '大剑'


class MagicTome(Weapon):
    _config_name = 'magic_tome'

    def __init__(self):
        super().__init__()

    def __str__(self):
        return '法典'


class Scepter(Weapon):
    _config_name = 'scepter'

    def __init__(self):
        super().__init__()

    def __str__(self):
        return '法杖'


class NoWeapon(Weapon):
    """空的武器"""
    _config_name = 'no_weapon'

    def get_attribute(self, name):
        return 0

    def __str__(self):
        return '没有武器'


class WeaponPart(AttributeOwner):
    _config_name = 'weapon_part'

    def __str__(self):
        return '武器配件'


class VitalityShield(WeaponPart):
    _config_name = 'vitality_shield'

    def __str__(self):
        return '精力护盾'


class XuanWuShield(WeaponPart):
    _config_name = 'xuanwu_shield'

    def __str__(self):
        return '玄武护盾'


class SwordCase(WeaponPart):
    _config_name = 'sword_case'

    def __str__(self):
        return '剑格'


class SwordTassel(WeaponPart):
    _config_name = 'sword_tassel'

    def __str__(self):
        return '剑穗'


class SwordBlade(WeaponPart):
    _config_name = 'sword_blade'

    def __str__(self):
        return '剑刃'


class Feather(WeaponPart):
    _config_name = 'feather'

    def __str__(self):
        return '羽毛'


class IcePiece(WeaponPart):
    _config_name = 'ice_piece'

    def __str__(self):
        return '冰片'


class ImperfectSheet(WeaponPart):
    _config_name = 'imperfect_sheet'

    def __str__(self):
        return '残页'


class Cover(WeaponPart):
    _config_name = 'cover'

    def __str__(self):
        return '封面'


if __name__ == '__main__':
    s = Shield()
