# -*- coding:utf-8 -*-
"""
@author: timkhuang
@contact: timkhuang@icloud.com
@software: PyCharm
@file: View.py.py
@time: 06/07/2020 21:24
@description: This is the abstract class for all the rendering/visualisation of the game/board.
"""


from abc import ABC, abstractmethod


class View(ABC):
    """
    An Abstract class for all kinds of GUI.
    Provide a run() function to draw the GUI and get the user input.
    """

    @abstractmethod
    def draw(self, board):
        """
        Show the board. Provide a GUI.
        Args:
            board (matrix of PointData): The processed board with key info hidden
        """
        pass

    @abstractmethod
    def input(self):
        """
        Get the the next step of the player.
        Returns:
            input (tuple of int): The coordinate of the user input.
        """
        pass
    
    @abstractmethod
    def get_board_size(self):
        """
        Get the board dimension at start of game
        Returns:
            int (tuple of int): The dimensions of user's board
        """
        pass

    def run(self, board):
        """
        To run the view, showing the board and get an input from the player.
        Args:
            board (matrix of PointData): The processed board with key info hidden
        Returns:
            result ({"flag": bool, "x": int, "y": int}): The coordinate of the user input.
        """
        self.draw(board)
        return self.input()
