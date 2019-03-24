# -*- coding: utf-8 -*-
# Time       : 2019/3/22 16:51
# Author     : tangdaye
# Description: 状态类


class State:
    def __str__(self):
        return '基本状态'

    # @abstractmethod
    # def attack(self, role):
    #     pass
    #
    # @abstractmethod
    # def be_attacked(self, role, attack_instance):
    #     pass


class DefaultState(State):
    def __str__(self):
        return '默认状态'


class EruptState(State):
    """爆发状态：血量低于30"""

    def __str__(self):
        return '爆发状态'
