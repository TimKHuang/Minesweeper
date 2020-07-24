# -*- coding:utf-8 -*-
"""
@author: timkhuang
@contact: timkhuang@icloud.com
@software: PyCharm
@file: View.py
@time: 06/07/2020 21:24
@description: This is the abstract class for all the rendering/visualisation of the game/board.
"""
from abc import ABC, abstractmethod
import timeit


class View(ABC):
    """
    An Abstract class for all kinds of GUI.
    Provide a run() function to draw the GUI and get the user input.
    """
    def __init__(self):
        self.time = None

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
           result ({"flag": bool, "x": int, "y": int}): The coordinate of the user input.
        """
        pass
    
    @abstractmethod
    def get_board_size(self):
        """
        Get the board dimension at start of game
        Returns:
            board ({"mine_count": int, "width": int, "height": int}): The dimension of the board
        """
        pass

    @abstractmethod
    def fail(self):
        """
        Deal with the situation when game fails.
        The function should reset the time.
        Returns:
            continue (bool): True is restart. False otherwise.
        """
        pass

    @abstractmethod
    def win(self):
        """
        Deal with the situation when game wins.
        The function should reset the timer.
        Returns:
            continue (bool): True is restart. False otherwise.
        """
        pass

    def run(self, board, ai=None):
        """
        To run the view, showing the board and get an input from the player.
        Args:
            board (matrix of PointData): The processed board with key info hidden
            ai (AI): The AI object.
        Returns:
            result ({"flag": bool, "x": int, "y": int}): The coordinate of the user input.
        """
        if self.time is None:
            self.time = timeit.default_timer()
        self.draw(board)
        if ai:
            return ai.make_decision(board)
        return self.input()

    def time_running(self):
        """
        get how long the game has run. The Board size part is not included.
        Returns:
            time (int): the time in seconds
        """
        if self.time is None:
            return 0
        return timeit.default_timer() - self.time

    def reset_timer(self):
        """
        reset the time to zero.
        """
        self.time = None
