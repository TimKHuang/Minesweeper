# -*- coding:utf-8 -*-
"""
@author: timkhuang
@contact: timkhuang@icloud.com
@software: PyCharm
@file: PointData.py
@time: 05/07/2020 21:18
@description: Contains the class PointData.
"""


class PointData:
    """
    PointData is the data structure of each point on the board.

    Attributes:
        x (int): x-coordinate of the point
        y (int): y-coordinate of the point
        is_bomb (bool): whether the point is a bomb
        is_opened (bool): whether the point has been opened
        is_flagged (bool): whether the user has flagged the point
        bomb_around (int): number of bombs around
    """

    def __init__(self, x, y, is_bomb):
        """
        Constructor of PointData

        Args:
            x (int): x-coordinate of the point
            y (int): y-coordinate of the point
            is_bomb (bool): whether the point is a bomb
        """
        self.x = x
        self.y = y
        self.is_bomb = is_bomb
        self.is_opened = False
        self.is_flagged = False
        self.bomb_around = 0

    def set_bomb_around(self, number):
        """
        set the number of bombs around the current point.

        Args:
            number (int): number of bombs around
        """
        self.bomb_around = number

    def continue_game(self):
        """
        True if the game continues.
        False if meet a bomb and game over.
        """
        return not self.is_bomb

    def open(self):
        """
        True if other points should be opened as well.
        False if open should stop.
        """
        self.is_opened = True
        return not self.is_bomb

    def __str__(self):
        """ be able to print the point info. """
        return "Coordinate: ({}, {})" \
               "is_bomb: {}" \
               "is_opened: {}" \
               "is_flagged: {}" \
               "bomb_around: {}" \
            .format(self.x, self.y,
                    self.is_bomb,
                    self.is_opened,
                    self.is_flagged,
                    self.bomb_around)
