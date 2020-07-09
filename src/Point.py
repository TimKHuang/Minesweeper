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

    def set_bomb(self, is_bomb, number=0):
        """
        set the number of bombs around the current point.

        Args:
            is_bomb (bool): if this is a bomb
            number (int): number of bombs around
        """
        if is_bomb:
            self.point_data.is_bomb = True
            return
        self.point_data.bomb_around = number

    def is_bomb(self):
        """
        True if it is a bomb.
        """
        return self.point_data.is_bomb

    def is_correct_state(self):
        """
        To check if the point is in the correct state to end.

        Returns:
            True if correct.
            False otherwise.
        """
        if self.is_bomb() and self.point_data.is_flagged:
            return True
        if self.point_data.is_opened:
            return True
        return False

    def open(self):
        """
        True if other points should be opened as well.
        False if open should stop.
        """
        if self.point_data.is_opened:
            return False
        self.point_data.is_opened = True
        self.point_data.is_flagged = None
        return self.point_data.bomb_around == 0

    def flag(self):
        """ Flag the point"""
        if self.point_data.is_opened:
            return
        self.point_data.is_flagged = not self.point_data.is_flagged

    def output(self):
        """
        Generate an output that can be passed to the user

        Returns:
            output (PointData): The processed data of the pointData
        """
        output = self.point_data.clone()
        output.hide()
        return output

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
        bomb_around (int): number of bombs around.
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
        return "Coordinate: ({}, {})\n" \
               "is_bomb: {}\n" \
               "is_opened: {}\n" \
               "is_flagged: {}\n" \
               "bomb_around: {}\n" \
            .format(self.x, self.y,
                    self.is_bomb,
                    self.is_opened,
                    self.is_flagged,
                    self.bomb_around)


# Section below is for test use

def test():
    point1 = Point(1, 2)
    point1.set_bomb(is_bomb=False, number=2)
    # Basic Point
    print("The point itself:")
    print(point1)
    # Output Point
    print("The output point:")
    print(point1.output())
    # Opened Point
    point1.open()
    print("Opened Output:")
    print(point1.output())


if __name__ == '__main__':
    test()
