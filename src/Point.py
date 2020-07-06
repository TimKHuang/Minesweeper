# -*- coding:utf-8 -*-
"""
@author: timkhuang
@contact: timkhuang@icloud.com
@software: PyCharm
@file: Point.py
@time: 05/07/2020 21:18
@description: Contains the class PointData.
"""


class Point:
    """
    PointData is the data structure of each point on the board.

    Attributes:
        point_data (PointData): the data of the point
    """

    def __init__(self, x, y):
        """
        Constructor of PointData

        Args:
            x (int): x-coordinate of the point
            y (int): y-coordinate of the point
        """
        self.point_data = PointData(x, y)

    def set_bomb_around(self, number):
        """
        set the number of bombs around the current point.

        Args:
            number (int): number of bombs around
        """
        self.point_data.bomb_around = number

    def continue_game(self):
        """
        True if the game continues.
        False if meet a bomb and game over.
        """
        return not self.point_data.is_bomb

    def open(self):
        """
        True if other points should be opened as well.
        False if open should stop.
        """
        self.point_data.is_opened = True
        return self.point_data.bomb_around == 0

    def __str__(self):
        """ be able to print the point info. """
        return str(self.point_data)


class PointData:
    """
    PointData stores the information of a point.

    Attributes:
        x (int): x-coordinate of the point
        y (int): y-coordinate of the point
        is_bomb (bool): whether the point is a bomb
        is_opened (bool): whether the point has been opened
        is_flagged (bool): whether the user has flagged the point
        bomb_around (int): number of bombs around
    """

    def __init__(self, x, y):
        """
        Constructor of PointData

        Args:
            x (int): x-coordinate of the point
            y (int): y-coordinate of the point
        """
        self.x = x
        self.y = y
        self.is_bomb = False
        self.is_opened = False
        self.is_flagged = False
        self.bomb_around = 0

    def hide(self):
        """
        Hide the information based on the current status.
        Should only be called when copy the data and pass it to the user.

        Returns:
            result (PointData): a point with only necessary point.
        """
        self.is_bomb = None
        if self.is_opened:
            self.is_flagged = None
        else:
            self.bomb_around = None

    def clone(self):
        """
        Get a copy of the point.

        Returns:
            copy (PointData): The copied result
        """
        copy = PointData(self.x, self.y)
        copy.is_bomb = self.is_bomb
        copy.is_opened = self.is_opened
        copy.is_flagged = self.is_flagged
        copy.is_bomb = self.is_bomb
        return copy

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
