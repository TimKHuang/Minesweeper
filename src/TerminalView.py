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

    Attributes:
        rows (int): The row number of the board.
        cols (int): The col number of the board.
    """

    def __init__(self):
        self.rows = -1
        self.cols = -1

    def draw(self, board):
        """
        Show the board. Provide a GUI.

        Args:
            board (matrix of PointData): The processed board with key info hidden
        """
        self.rows = len(board)
        self.cols = len(board[0])
        # print the x-axis
        print("\t", end="")
        for x in range(self.cols):
            print(x, end=" ")
        print("\n")
        # print the rest lines
        for y in range(self.rows):
            # print the y-axis
            print(y, end="\t")
            # print teh board
            for x in range(self.cols):
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
            result ({"flag": bool, "x": int, "y": int}): The coordinate of the user input.
        """
        result = {}
        # Get operation.
        while True:
            user_type = input("Flag a point or Open a point?\n"
                              "y for yes and n for no:")
            if user_type == "y":
                result["flag"] = True
                break
            if user_type == "n":
                result["flag"] = False
                break
            print("Please only type y or n!")
        # Get x

    def _input_check(self, checklist, message):
        """
        Ask for input until required is given.
        Message should show the accepted characters clearly.

        Args:
            checklist (List of str): All the accepted strings
            message (str): A message asking for input.

        Returns:
            user_input (str): accepted input
        """
        while True:
            user_input = input(message)
            if user_input in checklist:
                return user_input
            print("Please only type Accepted Characters")

    def _generate_string_collection(self, maximum, minimum=0):
        """
        This will generate a list of strings.
        The strings are all the numbers in the range.

        Args:
            maximum (int): The maximum number.
            minimum (int): The minimum number. default 0

        Returns:
            collections (List of str): The string collection generated
        """
        collection = []
        for i in range(minimum, maximum):
            collection.append(str(i))

        return collection
