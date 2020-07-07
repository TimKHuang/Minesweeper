# -*- coding:utf-8 -*-
"""
@author: victorvv
@contact: wengvictor5@gmail.com
@software: PyCharm
@file: exceptions.py
@time: 2020/7/7 下午3:57
@description:
"""
class TooManyMineException:
    def __init__(self):
        super().__init__("Number of mines exceeds the board size")