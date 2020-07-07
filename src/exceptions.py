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
    """
    This is the exception called when trying to add to many exceptions.
    """

    def __init__(self):
        super().__init__("Number of mines exceeds the board size")