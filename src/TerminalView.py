# -*- coding:utf-8 -*-
"""
@author: timkhuang
@contact: timkhuang@icloud.com
@software: PyCharm
@file: TerminalView.py
@time: 07/07/2020 09:38
@description: Provides a terminal view showing the board with characters.
"""


from .View import View


class TerminalView(View):
    """
    Showing the board in terminal withe characters.
    * means not opened.
    f means flagged.
    number is the bomb around.
    """

    def draw(self, board):
        """
        Show the board. Provide a GUI.

        Args:
            board (matrix of PointData): The processed board with key info hidden
        """
        rows = len(board)
        cols = len(board[0])
        # print the x-axis
        print("\t", end="")
        for x in range(cols):
            print(x, end=" ")
        print("\n")
        # print the rest lines
        for y in range(rows):
            # print the y-axis
            print(y, end="\t")
            # print teh board
            for x in range(cols):
                point = board[y][x]
                if point.is_opened:
                    if point.is_bomb:
                        print("B", end="")
                        continue
                    print(point.bomb_around, end=" ")
                    continue
                if point.is_flagged:
                    print("f", end=" ")
                    continue
                print("*", end="")
            print()

    def input(self):
        """
        Get the the next step of the player.
        By typing the coordinate.

        Returns:
            input (tuple of int): The coordinate of the user input.
        """
        print("Flag a point or Open a point?")

