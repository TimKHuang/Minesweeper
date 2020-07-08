# -*- coding:utf-8 -*-
"""
@author: victorvv
@contact: wengvictor5@gmail.com
@software: PyCharm
@file: GenerateBoard.py
@time: 04/07/2020 18:03
@description: This file is used to generate a mine board
"""
import sys
import random
import time

from src.Point import Point
from src.exceptions import TooManyMineException


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
            raise TooManyMineException
        self.height = height
        self.width = width
        self.mine_count = mine_count
        self.chessboard = [[Point(x, y) for y in range(width)] for x in range(height)]
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
            while randnum in self.mines:
                randnum = int(random.random() * size + 1)
            self.mines[i] = randnum
            del randnum
        for r in self.mines:
            x = r // self.width
            y = r % self.height
            # print("bomb", (x, y))
            self.chessboard[x][y].set_bomb(True)
        mines = 0
        for x in range(self.height):
            for y in range(self.width):
                mine = self.check(x, y)
                if mine == -1:
                    mines += 1
                    # self.chessboard[x][y].set_bomb(True)
                else:
                    self.chessboard[x][y].set_bomb(False, mine)
        self.mine_count = mines
        output_board = [[self.chessboard[x][y] for x in range(self.height)] for y in range(self.width)]
        return output_board

    def update(self, x, y, flag=False):
        """
        This function is used to update a board after user selects a box
        Args:
            flag (boolean): This value determines if user flags a box
            x (int): This is the x-value of the box
            y (int): This is the y-value of the box
        Returns:
            void
        """
        """
        When GameOver, player can see the real board
        Player can flag any boxes
        Updating the board
        """
        if self.isGameOver(x, y):
            print("Game Over! Try again!")
            for row in self.chessboard:
                for val in row:
                    val.point_data.is_opened = True
            # output_board = [[self.chessboard[x][y] for x in range(self.height)] for y in range(self.width)]
            # output_board = self.chessboard
        elif flag:
            self.chessboard[x][y].point_data.is_flagged = True
            # output_board = [[self.chessboard[x][y] for x in range(self.height)] for y in range(self.width)]
            # output_board = self.chessboard
        else:
            if self.chessboard[x][y].point_data.bomb_around != 0:
                self.chessboard[x][y].point_data.is_opened = True
                # output_board = [[self.chessboard[x][y] for x in range(self.height)] for y in range(self.width)]
                # output_board = self.chessboard
            else:
                self.checkZero(x, y)
                # res = self.checkZero(x, y)
                # for ele in res:
                #     self.chessboard[ele[0]][ele[1]].point_data.is_opened = True
                # output_board = [[self.chessboard[x][y] for x in range(self.height)] for y in range(self.width)]
                # output_board = self.chessboard
        # return output_board

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
        elif not self.chessboard[x][y].point_data.is_bomb:
            res = self.surround(x, y)
            for ele in res:
                # print ((ele[0],ele[1]))
                if self.chessboard[ele[0]][ele[1]].point_data.is_bomb:
                    mine += 1
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
        self.chessboard[x][y].point_data.is_opened = True
        res = self.surround(x, y)
        while self.hasZero(res):
            for ele in res:
                point = self.chessboard[ele[0]][ele[1]]
                if point.point_data.bomb_around == 0 and not point.point_data.is_opened:
                    point.point_data.is_opened = True
                    s.add((point.point_data.x, point.point_data.y))
                    self.checkZero(point.point_data.x, point.point_data.y)

    def hasZero(self, s):
        """
        This function checks if boxes in a set has value 0 or not
        If so, the coordinates of the box will be returned
        Args:
            s (set((int, int))): This is a set contains boxes' coordinates
        Returns:
            True or False: This contains the coordinates of boxes
            having value 0 in set s
        """
        for ele in s:
            if self.chessboard[ele[0]][ele[1]].point_data.bomb_around == 0:
                return True
        return False

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
        if x + 1 < self.height:
            res.add((x + 1, y))
            if y + 1 < self.width:
                res.add((x + 1, y + 1))
                res.add((x, y + 1))
            if y - 1 >= 0:
                res.add((x + 1, y - 1))
                res.add((x, y - 1))
        if x - 1 >= 0:
            res.add((x - 1, y))
            if y + 1 < self.width:
                res.add((x - 1, y + 1))
                res.add((x, y + 1))
            if y - 1 >= 0:
                res.add((x - 1, y - 1))
                res.add((x, y - 1))
        # print("visit",(x,y))
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


def test():
    mineboard = Board()
    for row in mineboard.chessboard:
        for val in row:
            if val.point_data.is_bomb:
                val.point_data.bomb_around = '*'
            print(val.point_data.bomb_around, end=' ')
        print()
    # print (mineboard.mine_count)
    mineboard.update(5, 5)
    for row in mineboard.chessboard:
        for val in row:
            print(val.point_data.is_opened, end="")
        print()

if __name__ == '__main__':
    test()
