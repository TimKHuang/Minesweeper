# -*- coding:utf-8 -*-
"""
@author: timkhuang
@contact: timkhuang@icloud.com
@software: PyCharm
@file: TerminalView.py
@time: 07/07/2020 09:38
@description: Provides a terminal view showing the board with characters.
"""

from src.View import View
from src.constants import COLOUR


class TerminalView(View):
    """
    Showing the board in terminal with characters.
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
            # print the y-axis"
            print(y, end="\t")
            # print the board
            for x in range(self.cols):
                point = board[y][x]
                if point.is_opened:
                    if point.is_bomb:
                        print(COLOUR["B"] + "B", end=" ")
                        continue
                    print(COLOUR[point.bomb_around % 10] + str(point.bomb_around), end=" ")
                    continue
                if point.is_flagged:
                    print(COLOUR["F"] + "f", end=" ")
                    continue
                print(COLOUR["*"] + "*", end=" " if x < 9 else "  ")
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
        operation = self._input_check({"y", "n"}, "Flag a point? Please type y or n: \t")
        result["flag"] = operation == 'y'
        # Get x
        x = self._input_check(self._generate_string_collection(self.cols), "Type the x coordinate: \t")
        result["x"] = int(x)
        # Get y
        y = self._input_check(self._generate_string_collection(self.rows), "Type the y coordinate: \t")
        result["y"] = int(y)

        return result

    def get_board_size(self):
        """
        This function is used to get user wanted board size
        Returns:
            board ({"mine_count": int, "width": int, "height": int}): The dimension of the board
        """
        board = {}
        # Get operation
        operation = self._input_check({"y", "n"}, "Custom board? Please type y or n: \t")
        if operation == 'n':
            return board
        # Get mine_count
        mine_count = self._input_check(self._generate_string_collection(99), "Type the mine_count: \t")
        board["mine_count"] = int(mine_count)
        # Get width
        width = self._input_check(self._generate_string_collection(99), "Type the board's width: \t")
        board["width"] = int(width)
        # Get height
        height = self._input_check(self._generate_string_collection(99), "Type the board's height: \t")
        board["height"] = int(height)

        return board

    def fail(self):
        """
        Deal with the situation when game fails.
        Returns:
            continue (bool): True is restart. False otherwise.
        """
        print("Sorry, you've met a bomb.")
        operation = self._input_check({"y", "n"}, "Restart the game? Please type y or n: \t")
        return operation == "y"

    def win(self):
        """
        Deal with the situation when game wins.
        Returns:
            continue (bool): True is restart. False otherwise.
        """
        print("Wow excellent!")
        operation = self._input_check({"y", "n"}, "Restart the game? Please type y or n: \t")
        return operation == "y"

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


# Section below is for test use

def test():
    from src.Board import Board
    view = TerminalView()
    result = view.run(Board().get_board())
    print(result)


if __name__ == '__main__':
    test()
