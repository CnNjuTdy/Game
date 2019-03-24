# -*- coding: utf-8 -*-
# Time       : 2019/2/26 8:23 PM
# Author     : tangdaye
# Description: 测试

import pygame  # 导入pygame库
from pygame.locals import *  # 导入pygame库中的一些常量
from sys import exit  # 导入sys库中的exit函数

if __name__ == '__main__':
    # 定义窗口的分辨率
    SCREEN_WIDTH = 960
    SCREEN_HEIGHT = 640

    # 初始化游戏
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption('This is my first pygame program')

    # 事件循环(main loop)
    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
