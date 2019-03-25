# -*- coding: utf-8 -*-
# Time       : 2019/3/25 00:43
# Author     : tangdaye
# Description: 战斗控制器


class BattleController:
    def __init__(self, player, npc):  # 控制器需要传入玩家参数和npc参数
        self._player = player
        self._npc = npc
