# -*- coding: utf-8 -*-
# Time       : 2019/3/22 16:39
# Author     : tangdaye
# Description: 观察者模式实现
from abc import abstractmethod


class Subject:
    """观察者模式"""
    _observers = []

    def notify_all(self):
        for observer in self._observers:
            observer.update(self)

    def register(self, observer):
        self._observers.append(observer)


class Observer:
    @abstractmethod
    def update(self, subject):
        pass
