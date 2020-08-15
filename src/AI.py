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
        if self.check_surround(board) is None:
            print("random open")
            print("---" * 10)
            random_open = self.random_open(board)
            print(random_open)
            return random_open
        else:
            print("ordinary open")
            print("---" * 10)
            ordinary_open = self.check_surround(board)
            print(ordinary_open)
            return ordinary_open

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
        unopened_box = list([])

        # Add the current unopened boxes on the board to the list -- unopened
        for y in range(rows):
            for x in range(cols):
                if not board[y][x].is_opened:
                    unopened_box.append((x, y))

        x, y = random.choice(unopened_box)
        return {"flag": False, "x": x, "y": y}

    def divide_board(self):
        """
        This function is used to divide the board into smaller boards
        Returns:

        """

    # This is implemented by using the ordinary algorithm
    def check_surround(self, board):
        """
        This function is used to check the unopened boxes around opened boxes
        Args:
            board (matrix of PointData): The board with all the information.
        Returns:
            result ({"flag": bool, "x": int, "y": int}): The coordinate of the user input.
        """
        rows = len(board)
        cols = len(board[0])

        for y in range(rows):
            for x in range(cols):
                point = board[y][x]
                if point.is_opened and point.bomb_around != 0:
                    surr = self.unopen_surround((x, y), board)
                    unopen_surr = list([])
                    flag_surr = list([])
                    for coordinates in surr:
                        box = board[coordinates[1]][coordinates[0]]
                        # Add coordinates of hidden boxes to the unopen_surr
                        if not box.is_opened and not box.is_flagged:
                            unopen_surr.append(coordinates)
                        # Add coordinates of flagged boxes to the flag_surr
                        if box.is_flagged and not box.is_opened:
                            flag_surr.append(coordinates)
                    # when the number of flagged boxes equals to the number of the box
                    if point.bomb_around == len(flag_surr) and point.bomb_around != 0:
                        # Confirmed that all unopen boxes are safe
                        # Open those boxes
                        if len(unopen_surr) == 0:
                            continue
                        p_x = unopen_surr[0][0]
                        p_y = unopen_surr[0][1]
                        return {"flag": False, "x": p_x, "y": p_y}
                    # when the number of unopened boxes equals to the number on the opened box
                    if point.bomb_around is None:
                        continue
                    if point.bomb_around - len(flag_surr) == len(unopen_surr):
                        # Confirmed that all unopened boxes are mines
                        # Flag those boxes
                        p_x = unopen_surr[0][0]
                        p_y = unopen_surr[0][1]
                        return {"flag": True, "x": p_x, "y": p_y}

    def unopen_surround(self, p, board):
        """
        This function is used to visit boxes around p
        It would return a set of unopened boxes' coordinates
        Args:
            p ((int, int): The point being opened
            board (matrix of PointData): The board with all the information.
        Returns:
            res(set((int,int))): This is a set of coordinates of all nearby boxes
        """
        rows = len(board)
        cols = len(board[0])

        res = set([])
        if p[0] + 1 < cols:
            res.add((p[0] + 1, p[1]))
            if p[1] + 1 < rows:
                res.add((p[0] + 1, p[1] + 1))
                res.add((p[0], p[1] + 1))
            if p[1] - 1 >= 0:
                res.add((p[0] + 1, p[1] - 1))
                res.add((p[0], p[1] - 1))
        if p[0] - 1 >= 0:
            res.add((p[0] - 1, p[1]))
            if p[1] + 1 < cols:
                res.add((p[0] - 1, p[1] + 1))
                res.add((p[0], p[1] + 1))
            if p[1] - 1 >= 0:
                res.add((p[0] - 1, p[1] - 1))
                res.add((p[0], p[1] - 1))
        return res


# Section below is for test use


def test():
    from src.Board import Board
    board = Board(4, 4)
    user = AI()
    for row in board.chessboard:
        for val in row:
            if val.point_data.is_bomb:
                val.point_data.bomb_around = '*'
            print(val.point_data.bomb_around, end=' ')
        print()
    board.update(0, 0)
    # board.update(1, 1)
    # board.update(1, 0)
    for row in board.chessboard:
        for val in row:
            print(val)

    print(user.make_decision(board.get_board()))
    print(user.make_decision(board.get_board()))
    print(user.make_decision(board.get_board()))


if __name__ == '__main__':
    test()
