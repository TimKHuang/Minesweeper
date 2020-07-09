# -*- coding:utf-8 -*-
"""
@author: victorvv
@contact: wengvictor5@gmail.com
@software: PyCharm
@file: GenerateBoard.py
@time: 04/07/2020 18:03
@description: This file is used to generate a mine board
"""
import random
import time

from src.Point import Point
from src.exceptions import TooManyMineException


class Board:
    def __init__(self, mine_count=40, width=16, height=None):
        """
        This function is used to generate a mine board. Default size is 16*16
        Default mine_count is 40
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
            Randomly allocate mine in the board
            Number each square
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
            x = r // self.height
            y = r % self.width
            self.chessboard[x][y].set_bomb(True)
        for x in range(self.height):
            for y in range(self.width):
                mine = self.check(x, y)
                if mine == -1:
                    pass
                else:
                    self.chessboard[x][y].set_bomb(False, mine)
        # output_board = [[self.chessboard[x][y] for x in range(self.height)] for y in range(self.width)]
        # return output_board

    def update(self, x, y, flag=False):
        """
        This function is used to update a board after user selects a square
        Args:
            flag (boolean): This value determines if user flags a square
            x (int): This is the x-value of the square
            y (int): This is the y-value of the square
        Returns:
            void
        """
        """
        When GameOver, player can see the real board
        Player can flag any squares
        Updating the board
        """
        if self.isGameOver(x, y):
            print("Game Over! Try again!")
            for row in self.chessboard:
                for val in row:
                    val.open()
            # output_board = [[self.chessboard[x][y] for x in range(self.height)] for y in range(self.width)]
            # output_board = self.chessboard
        elif flag:
            self.chessboard[x][y].flag()
            # output_board = [[self.chessboard[x][y] for x in range(self.height)] for y in range(self.width)]
            # output_board = self.chessboard
        else:
            if not self.chessboard[x][y].open():
                pass
                # output_board = [[self.chessboard[x][y] for x in range(self.height)] for y in range(self.width)]
                # output_board = self.chessboard
            else:
                self.checkZero(x, y)
                # output_board = [[self.chessboard[x][y] for x in range(self.height)] for y in range(self.width)]
                # output_board = self.chessboard
        # return output_board

    # Auxiliary functions
    def check(self, x, y):
        """
        This function is used to number each square in the mine board.
        The value of a box is the number of mines around the square.
        Or the value is -1 if the square is mine.
        Args:
            x (int): This is the x-value of the square while iterating
            y (int): This is the y-value of the square while iterating
        Returns:
            mine (int): This returns the value of the square
        """
        mine = 0
        if self.chessboard[x][y].is_bomb():
            mine = -1
        elif not self.chessboard[x][y].is_bomb():
            res = self.surround(x, y)
            for ele in res:
                if self.chessboard[ele[0]][ele[1]].is_bomb():
                    mine += 1
        return mine

    def checkZero(self, x, y):
        """
        This function is used to update the board when a 0-value
        point is opened
        Args:
            x (int): This is the x-value of the box
            y (int): This is the y-value of the box
        Returns:
            void
        """
        self.chessboard[x][y].open()
        for p in self.surround(x, y):
            point = self.chessboard[p[0]][p[1]]
            if point.is_bomb():
                continue
            if point.open():
                self.checkZero(point.point_data.x, point.point_data.y)

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
        return res

    def isGameOver(self, x, y):
        """
        This function is used to determine if the user selects a mine
        Args:
            x (int): This is the x-value of the selected square
            y (int): This is the y-value of the selected square

        Returns:
            True, if it is a bomb
            False, otherwise
        """
        return self.chessboard[x][y].is_bomb()


# Section below is for test use

def test():
    mineboard = Board()
    for row in mineboard.chessboard:
        for val in row:
            if val.point_data.is_bomb:
                val.point_data.bomb_around = '*'
            print(val.point_data.bomb_around, end=' ')
        print()
    mineboard.update(5, 5)
    for row in mineboard.chessboard:
        for val in row:
            print(val.point_data.is_opened, end=' ')
        print()


if __name__ == '__main__':
    test()
