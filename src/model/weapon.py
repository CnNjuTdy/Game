# -*- coding: utf-8 -*-
# Time       : 2019/3/22 16:46
# Author     : tangdaye
# Description: 武器
from model.attribute_owner import AttributeOwner
from model.role import Mage, Warrior


class Weapon(AttributeOwner):
    _config_name = 'weapon'

    def __init__(self, fit_roles):
        super().__init__()
        self._weapon_parts = []
        self._fit_roles = fit_roles

    def get_attribute(self, name):
        t = 0
        for weapon_part in self._weapon_parts:
            t += weapon_part.get_attribute(name)
        m = self._attributes.get(name)
        return m + t if m is not None else t

    def is_suitable_weapon(self, role_class):
        return role_class in self._fit_roles

    def add_weapon_part(self, weapon_part):
        if weapon_part.is_suitable_weapon_part(type(self)):
            self._weapon_parts.append(weapon_part)
            return True
        return False

    def __str__(self):
        return '武器'


class Shield(Weapon):
    _config_name = 'shield'

    def __init__(self):
        super().__init__([Warrior])

    def __str__(self):
        return '盾牌'


class Sword(Weapon):
    _config_name = 'sword'

    def __init__(self):
        super().__init__([Warrior])

    def __str__(self):
        return '大剑'


class MagicTome(Weapon):
    _config_name = 'magic_tome'

    def __init__(self):
        super().__init__([Mage])

    def __str__(self):
        return '法典'


class Scepter(Weapon):
    _config_name = 'scepter'

    def __init__(self):
        super().__init__([Mage])

    def __str__(self):
        return '法杖'


class NoWeapon(Weapon):
    """空的武器"""
    _config_name = 'no_weapon'

    def __init__(self):
        super().__init__([Mage, Warrior])

    def get_attribute(self, name):
        return 0

    def __str__(self):
        return '没有武器'


class WeaponPart(AttributeOwner):
    _config_name = 'weapon_part'

    def __init__(self, fit_weapon):
        super().__init__()
        self.fit_weapon = fit_weapon

    def is_suitable_weapon_part(self, weapon_class):
        return weapon_class in self.fit_weapon

    def __str__(self):
        return '武器配件'


class VitalityShield(WeaponPart):
    _config_name = 'vitality_shield'

    def __init__(self):
        super().__init__([Shield])

    def __str__(self):
        return '精力护盾'


class XuanWuShield(WeaponPart):
    _config_name = 'xuanwu_shield'

    def __init__(self):
        super().__init__([Shield])

    def __str__(self):
        return '玄武护盾'


class SwordCase(WeaponPart):
    _config_name = 'sword_case'

    def __init__(self):
        super().__init__([Sword])

    def __str__(self):
        return '剑格'


class SwordTassel(WeaponPart):
    _config_name = 'sword_tassel'

    def __init__(self):
        super().__init__([Sword])

    def __str__(self):
        return '剑穗'


class SwordBlade(WeaponPart):
    _config_name = 'sword_blade'

    def __init__(self):
        super().__init__([Sword])

    def __str__(self):
        return '剑刃'


class Feather(WeaponPart):
    _config_name = 'feather'

    def __init__(self):
        super().__init__([Scepter])

    def __str__(self):
        return '羽毛'


class IcePiece(WeaponPart):
    _config_name = 'ice_piece'

    def __init__(self):
        super().__init__([Scepter])

    def __str__(self):
        return '冰片'


class ImperfectSheet(WeaponPart):
    _config_name = 'imperfect_sheet'

    def __init__(self):
        super().__init__([MagicTome])

    def __str__(self):
        return '残页'


class Cover(WeaponPart):
    _config_name = 'cover'

    def __init__(self):
        super().__init__([MagicTome])

    def __str__(self):
        return '封面'


if __name__ == '__main__':
    s = Shield()
