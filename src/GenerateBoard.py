# -*- coding:utf-8 -*-
"""
@author: Victor
@contact: wengvictor5@gmail.com
@software: PyCharm
@file: GenerateBoard.py
@time: 04/07/2020 18:03
@description: This file is used to generate a mineboard
"""
import sys
import random
import time


class Generateboard:
    def __init__(self, mine_count=25, width=16, height=None):
        """
        This function is used to generate a mine board. Default size is 16*16

        Args:
            mine_count (int): This determines the total number of mines in a board
            width (int): This determines the width of the board
            height (int): This determines the height of the board
        """

        if height == None:
            height = width
        if mine_count > height * width:
            print('More mines than the max size of the board')
            sys.exit()
        self.height = height
        self.width = width
        self.minecount = mine_count
        self.chessboard = [[0 for x in range(height)] for y in range(width)]
        self.mines = [0 for z in range(mine_count)]
        self.initialise()

    def initialise(self):
        """
        This function is used to initialise the board
        Returns:
            void
        """

        random.seed(time.time())  # set seed, to generate distinct random number
        size = self.height * self.width - 1
        for i in range(self.minecount):
            randnum = int(random.random() * size + 1)
            if self.mines[:i].__contains__(randnum):
                randnum = int(random.random() * size + 1)
            self.mines[i] = randnum
            del randnum
        for r in self.mines:
            x = r // self.width
            y = r % self.height
            self.chessboard[x][y] = -1
        mines = 0
        for x in range(self.height):
            for y in range(self.width):
                mine = self.check(x, y)
                if mine == -1:
                    mines += 1
                self.chessboard[x][y] = mine
        self.mine_count = mines

    # Auxilary functions
    def check(self, x, y):
        """
        This function is used to number each boxes in the mine board.
        The value of a box is the number of mines around the box.
        Or the value is -1 if the box is mine.
        Args:
            x (int): This is the x-value of the box while iterating
            y (int): This is the y-value of the box while iterating
        Returns:
            mine (int): This returns the value of the box.
        """

        mine = 0
        if self.chessboard[x][y] == -1:
            mine = -1
        elif x == 0 and y == 0 and self.chessboard[x][y] != -1:
            if self.chessboard[x + 1][y] == -1:
                mine += 1
            if self.chessboard[x + 1][y + 1] == -1:
                mine += 1
            if self.chessboard[x][y + 1] == -1:
                mine += 1
        elif x == self.height - 1 and y == self.width - 1 and self.chessboard[x][y] != -1:
            if self.chessboard[x - 1][y] == -1:
                mine += 1
            if self.chessboard[x - 1][y - 1] == -1:
                mine += 1
            if self.chessboard[x][y - 1] == -1:
                mine += 1
        elif x == 0 and self.chessboard[x][y] != -1:
            if self.chessboard[x][y - 1] == -1:
                mine += 1
            if self.chessboard[x + 1][y - 1] == -1:
                mine += 1
            if self.chessboard[x + 1][y] == -1:
                mine += 1
            if y < self.width - 1:
                if self.chessboard[x + 1][y + 1] == -1:
                    mine += 1
                if self.chessboard[x][y + 1] == -1:
                    mine += 1
        elif y == 0 and self.chessboard[x][y] != -1:
            if self.chessboard[x - 1][y] == -1:
                mine += 1
            if self.chessboard[x - 1][y + 1] == -1:
                mine += 1
            if self.chessboard[x][y + 1] == -1:
                mine += 1
            if x < self.height - 1:
                if self.chessboard[x + 1][y + 1] == -1:
                    mine += 1
                if self.chessboard[x + 1][y] == -1:
                    mine += 1
        elif x == self.height - 1 and self.chessboard[x][y] != -1:
            if self.chessboard[x][y - 1] == -1:
                mine += 1
            if self.chessboard[x - 1][y - 1] == -1:
                mine += 1
            if self.chessboard[x - 1][y] == -1:
                mine += 1
            if self.chessboard[x - 1][y + 1] == -1:
                mine += 1
            if self.chessboard[x][y + 1] == -1:
                mine += 1
        elif y == self.width - 1 and self.chessboard[x][y] != -1:
            if self.chessboard[x - 1][y] == -1:
                mine += 1
            if self.chessboard[x - 1][y - 1] == -1:
                mine += 1
            if self.chessboard[x][y - 1] == -1:
                mine += 1
            if self.chessboard[x + 1][y - 1] == -1:
                mine += 1
            if self.chessboard[x + 1][y] == -1:
                mine += 1
        elif self.chessboard[x][y] != -1:
            if self.chessboard[x - 1][y] == -1:
                mine += 1
            if self.chessboard[x - 1][y - 1] == -1:
                mine += 1
            if self.chessboard[x][y - 1] == -1:
                mine += 1
            if self.chessboard[x + 1][y - 1] == -1:
                mine += 1
            if self.chessboard[x + 1][y] == -1:
                mine += 1
            if self.chessboard[x + 1][y + 1] == -1:
                mine += 1
            if self.chessboard[x][y + 1] == -1:
                mine += 1
            if self.chessboard[x - 1][y + 1] == -1:
                mine += 1
        return mine

# mineboard = Mineboard(40,16)
# for row in mineboard.chessboard:
#     for val in row:
#         if val == -1:
#             val = '*'
#         print (val, end = ' ')
#     print()
