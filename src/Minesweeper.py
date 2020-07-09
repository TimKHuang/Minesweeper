# -*- coding:utf-8 -*-
"""
@author: timkhuang
@contact: timkhuang@icloud.com
@software: PyCharm
@file: Minesweeper.py
@time: 09/07/2020 10:28
@description: This can be seen as a launcher of the game or controller.
"""
from src.Board import Board
from src.TerminalView import TerminalView


class Minesweeper:

    def __init__(self, mode):
        self.board = Board()
        if mode == "terminal":
            self.view = TerminalView()

