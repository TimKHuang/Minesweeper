# coding=gbk
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

from .Point import Point


class Board:

    def __init__(self, mine_count=25, width=16, height=None):
        """
        This function is used to generate a mine board. Default size is 16*16
        Args:
            mine_count (int): This determines the total number of mines in a board
            width (int): This determines the width of the board
            height (int): This determines the height of the board
        """
        if height is None:
            height = width
        if mine_count > height * width:
            raise Exception('The board is too small to hold those mines.')
        self.height = height
        self.width = width
        self.mine_count = mine_count
        self.chessboard = [[Point(x,y) for x in range(height)] for y in range(width)]
        self.mines = [0 for z in range(mine_count)]
        self.initialise()

    def initialise(self):
        """
        This function is used to initialise the board:
            Randomly allocate bomb in the board
            Number each boxes
        Returns:
            void
        """
        random.seed(time.time())  # set seed, to generate distinct random number
        size = self.height * self.width - 1
        for i in range(self.mine_count):
            randnum = int(random.random() * size + 1)
            if self.mines[:i].__contains__(randnum):
                randnum = int(random.random() * size + 1)
            self.mines[i] = randnum
            del randnum
        for r in self.mines:
            x = r // self.width
            y = r % self.height
            self.chessboard[x][y].set_bomb(True)
        mines = 0
        for x in range(self.height):
            for y in range(self.width):
                mine = self.check(x, y)
                if mine == -1:
                    mines += 1
                    self.chessboard[x][y].set_bomb(True)
                else:
                    self.chessboard[x][y].set_bomb(False, mine)
        self.mine_count = mines

    def update(self, x, y, flag=False):
        """
        This function is used to update a board after user selects a box
        Args:
            x (int): This is the x-value of the box
            y (int): This is the y-value of the box
        Returns:
            void
        """
        output_board = None
        # When GameOver, player can see the real board
        if self.isGameOver(x, y):
            print("Game Over! Try again!")
            output_board = [[self.chessboard[x][y] for x in range(self.height)]for y in range(self.width)]
        elif flag:
            self.chessboard[x][y].point_data.is_flagged = True
        else:
            if self.chessboard[x][y].point_data.bomb_around != 0:
                self.chessboard[x][y].point_data.is_opened = True
                output_board = [[self.chessboard[x][y] for x in range(self.height)]for y in range(self.width)]



    # Auxiliary functions
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
        if self.chessboard[x][y].point_data.is_bomb:
            mine = -1
        # elif x == 0 and y == 0 and self.chessboard[x][y] != -1:
        #     if self.chessboard[x + 1][y] == -1:
        #         mine += 1
        #     if self.chessboard[x + 1][y + 1] == -1:
        #         mine += 1
        #     if self.chessboard[x][y + 1] == -1:
        #         mine += 1
        # elif x == self.height - 1 and y == self.width - 1 and self.chessboard[x][y] != -1:
        #     if self.chessboard[x - 1][y] == -1:
        #         mine += 1
        #     if self.chessboard[x - 1][y - 1] == -1:
        #         mine += 1
        #     if self.chessboard[x][y - 1] == -1:
        #         mine += 1
        # elif x == 0 and self.chessboard[x][y] != -1:
        #     if self.chessboard[x][y - 1] == -1:
        #         mine += 1
        #     if self.chessboard[x + 1][y - 1] == -1:
        #         mine += 1
        #     if self.chessboard[x + 1][y] == -1:
        #         mine += 1
        #     if y < self.width - 1:
        #         if self.chessboard[x + 1][y + 1] == -1:
        #             mine += 1
        #         if self.chessboard[x][y + 1] == -1:
        #             mine += 1
        # elif y == 0 and self.chessboard[x][y] != -1:
        #     if self.chessboard[x - 1][y] == -1:
        #         mine += 1
        #     if self.chessboard[x - 1][y + 1] == -1:
        #         mine += 1
        #     if self.chessboard[x][y + 1] == -1:
        #         mine += 1
        #     if x < self.height - 1:
        #         if self.chessboard[x + 1][y + 1] == -1:
        #             mine += 1
        #         if self.chessboard[x + 1][y] == -1:
        #             mine += 1
        # elif x == self.height - 1 and self.chessboard[x][y] != -1:
        #     if self.chessboard[x][y - 1] == -1:
        #         mine += 1
        #     if self.chessboard[x - 1][y - 1] == -1:
        #         mine += 1
        #     if self.chessboard[x - 1][y] == -1:
        #         mine += 1
        #     if self.chessboard[x - 1][y + 1] == -1:
        #         mine += 1
        #     if self.chessboard[x][y + 1] == -1:
        #         mine += 1
        # elif y == self.width - 1 and self.chessboard[x][y] != -1:
        #     if self.chessboard[x - 1][y] == -1:
        #         mine += 1
        #     if self.chessboard[x - 1][y - 1] == -1:
        #         mine += 1
        #     if self.chessboard[x][y - 1] == -1:
        #         mine += 1
        #     if self.chessboard[x + 1][y - 1] == -1:
        #         mine += 1
        #     if self.chessboard[x + 1][y] == -1:
        #         mine += 1
        # elif self.chessboard[x][y] != -1:
        #     if self.chessboard[x - 1][y] == -1:
        #         mine += 1
        #     if self.chessboard[x - 1][y - 1] == -1:
        #         mine += 1
        #     if self.chessboard[x][y - 1] == -1:
        #         mine += 1
        #     if self.chessboard[x + 1][y - 1] == -1:
        #         mine += 1
        #     if self.chessboard[x + 1][y] == -1:
        #         mine += 1
        #     if self.chessboard[x + 1][y + 1] == -1:
        #         mine += 1
        #     if self.chessboard[x][y + 1] == -1:
        #         mine += 1
        #     if self.chessboard[x - 1][y + 1] == -1:
        #         mine += 1
        elif not self.chessboard[x][y].point_data.is_bomb:
            res = self.surround(x, y)
            for ele in res:
                if self.chessboard[ele[0]][ele[1]].point_data.is_bomb:
                    mine +=1
        return mine

    def checkZero(self, x, y):
        """
        This function finds out coordinates of boxes having value 0
        that are next to each other.
        Box (x, y) must have value 0
        Args:
            x (int): This is the x-value of the box
            y (int): This is the y-value of the box
        Returns:
            s (set((int,int))): This contains boxes' coordinates needed to be open
        """
        s = set([])
        res = self.surround(x, y)
        s.update(res) #all ele in res needs to be opened
        temp = self.hasZero(res)
        while len(temp) > 0:
            for ele in temp:
                t = self.surround(ele[0], ele[1]) #it is a set contains coordinates of boxes around box ele
                s.update(t) #all ele in t needs to be opened
                self.checkZero(ele[0], ele[1])



    def hasZero(self, s):
        """
        This function checks if boxes in a set has value 0 or not
        Args:
            s (set((int, int))): This is a set contains boxes' coordinates

        Returns:
            zero (set((int,int))): This contains the coordinates of boxes
            having value 0 in set s
        """
        zero = set([])
        for ele in s:
            if self.chessboard[ele[0]][ele[1]].point_data.bomb_around == 0:
                zero.add(ele)
        return zero


    def surround(self, x, y):
        """
        This function is used to visit boxes around (x, y)
        It would return a set of boxes' coordinates
        Args:
            x (int): This is the x-value of the box
            y (int): This is the y-value of the box

        Returns:
            res(set((int,int))): This is a set of coordinates of all nearby boxes
        """
        res = set([])
        if x == 0 and y == 0:
            res.add((x+1, y))
            res.add((x+1, y+1))
            res.add((x, y+1))
        elif x == self.height - 1 and y == self.width - 1:
            res.add((x-1, y))
            res.add((x-1, y-1))
            res.add((x, y-1))
        elif x == 0:
            res.add((x, y-1))
            res.add((x+1, y-1))
            res.add((x+1, y))
            if y < self.width -1:
                res.add((x+1, y+1))
                res.add((x, y+1))
        elif y == 0:
            res.add((x-1, y))
            res.add((x-1, y+1))
            res.add((x, y+1))
            if x < self.height - 1:
                res.add((x+1, y+1))
                res.add((x+1, y))
        elif x == self.height -1:
            res.add((x, y-1))
            res.add((x-1, y-1))
            res.add((x-1, y))
            res.add((x-1, y+1))
            res.add((x, y+1))
        elif y == self.width - 1:
            res.add((x-1, y))
            res.add((x-1, y-1))
            res.add((x, y-1))
            res.add((x+1, y-1))
            res.add((x+1, y))
        else:
            res.add((x-1, y))
            res.add((x-1, y-1))
            res.add((x, y-1))
            res.add((x+1, y-1))
            res.add((x+1, y))
            res.add((x+1, y+1))
            res.add((x, y+1))
            res.add((x-1, y+1))
        return res

    def isGameOver(self, x, y):
        """
        This function is used to determine if the user selects a mine
        Args:
            x (int): This is the x-value of the selected box
            y (int): This is the y-value of the selected box

        Returns:
            GameOver (boolean): This value determines if the game is over
        """
        GameOver = False
        if self.chessboard[x][y].point_data.is_bomb:
            GameOver = True
        return GameOver







# mineboard = Mineboard(40,16)
# for row in mineboard.chessboard:
#     for val in row:
#         if val == -1:
#             val = '*'
#         print (val, end = ' ')
#     print()
