# -*- coding:utf-8 -*-
"""
@author: victorvv
@contact: wengvictor5@gmail.com
@software: PyCharm
@file: AI.py
@time: 2020/08/07 18:10
@description: This file contains the algorithm for AI
"""
# Feel free to change the Name of your AI and other details in the above sections
import random


# If not specified, please do not change any of the code below.
class AI:

    def make_decision(self, board):
        # TODO add the wiki page url
        """
        This is the function that your AI makes decision based on the current board.
        For more details about the types and APIs, please see the Wiki page on Github.
        Args:
            board (matrix of PointData): The board with all the information.
        Returns:
            result ({"flag": bool, "x": int, "y": int}): The coordinate of the user input.
        """

        # TODO Add you return statement here. Please make sure the return type is correct.

    def random_open(self, board):
        """
        This function is used to open a box when the game is initially set up
        Args:
            board (matrix of PointData): The board with all the information.
        Returns:
            result ({"flag": bool, "x": int, "y": int}): The coordinate of the user input.
        """
        rows = len(board)
        cols = len(board[0])

        while True:
            y = random.randint(0, rows - 1)
            x = random.randint(0, cols - 1)
            if not board[y][x].is_opened:
                return {"flag": False, "x": x, "y": y}

    def divide_board(self):
        """
        This function is used to divide the board into different blocks
        Returns:

        """

    def check_unopen_surround(self, board):
        """
        This function is used to check the unopened boxes around opened boxes
        Args:
            board (matrix of PointData): The board with all the information.
        Returns:

        """
        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                num = board[r][c].bomb_around
                if board[r][c].is_opened and num != 0:
                    res = self.unopen_surround((c, r), cols, rows)
                    unopen_surr = list([])
                    flag_surr = list([])
                    for coordinates in res:
                        point = board[coordinates[1]][coordinates[0]]
                        # Add coordinates of hidden boxes in the unopen_surr
                        if not point.is_opened:
                            unopen_surr.append(coordinates)
                        # Add coordinates of flagged boxes in the flag_surr
                        if point.is_flagged:
                            flag_surr.append(coordinates)
                    # when the number of unopened boxes equals to the number on the opened box
                    if num == len(unopen_surr):
                        # Confirmed that all unopened boxes are mines
                        # Flag those boxes
                        x = unopen_surr[0][0]
                        y = unopen_surr[0][1]
                        return {"flag": True, "x": x, "y": y}
                    # when the number 
                    


    def unopen_surround(self, p, width, height):
        """
        This function is used to visit boxes around p
        It would return a set of unopened boxes' coordinates
        Args:
            p (Point): The point being opened
            width (int): The width of the board
            height (int): The height of the board
        Returns:
            res(set((int,int))): This is a set of coordinates of all nearby boxes
        """
        res = set([])
        if p[0] + 1 < width:
            res.add((p[0] + 1, p[1]))
            if p[1] + 1 < height:
                res.add((p[0] + 1, p[1] + 1))
                res.add((p[0], p[1] + 1))
            if p[1] - 1 >= 0:
                res.add((p[0] + 1, p[1] - 1))
                res.add((p[0], p[1] - 1))
        if p[0] - 1 >= 0:
            res.add((p[0] - 1, p[1]))
            if p[1] + 1 < height:
                res.add((p[0] - 1, p[1] + 1))
                res.add((p[0], p[1] + 1))
            if p[1] - 1 >= 0:
                res.add((p[0] - 1, p[1] - 1))
                res.add((p[0], p[1] - 1))
        return res


# Section below is for test use


def test():
    from src.Board import Board
    user = AI()
    board = Board(1, 4)
    for row in board.chessboard:
        for val in row:
            if val.point_data.is_bomb:
                val.point_data.bomb_around = '*'
            print(val.point_data.bomb_around, end=' ')
        print()
    board.update(0, 0)
    board.update(1, 1)
    board.update(1, 0)
    for row in board.chessboard:
        for val in row:
            print(val)

    print(user.random_open(board.get_board()))


if __name__ == '__main__':
    test()
