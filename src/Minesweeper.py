# -*- coding:utf-8 -*-
"""
@author: timkhuang
@contact: timkhuang@icloud.com
@software: PyCharm
@file: Minesweeper.py
@time: 09/07/2020 10:28
@description: This can be seen as a launcher of the game or controller.
"""
from src.Board import Board
from src.TerminalView import TerminalView
from src.Point import Point


class Minesweeper:

    def __init__(self, mode=None):
        """
        Initialise the game.
        Args:
            mode (str): The string of the mode. default "terminal".
        """
        self.view = TerminalView()

    def one_turn(self):
        """
        Run one turn of the game.
        Returns:
            continue (bool): whether restart the game
        """
        # initiate the board
        board_size = self.view.get_board_size()
        if board_size == {}:
            board = Board()
        else:
            board = Board(mine_count=board_size["mine_count"], width=board_size["width"], height=board_size["height"])

        while not board.is_game_finish():
            operation = self.view.run(board.get_board())
            if not board.update(Point(operation["x"], operation["y"]), operation["flag"]):
                self.view.draw(board.get_board())
                return self.view.fail()
        return self.view.win()

    def run(self):
        while self.one_turn():
            pass


if __name__ == '__main__':
    Minesweeper().run()
