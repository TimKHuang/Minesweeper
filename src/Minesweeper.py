# -*- coding:utf-8 -*-
"""
@author: timkhuang
@contact: timkhuang@icloud.com
@software: PyCharm
@file: Minesweeper.py
@time: 09/07/2020 10:28
@description: This can be seen as a launcher of the game or controller.
"""
import sys

from src.Board import Board
from src.view.ViewFactory import ViewFactory
from src.AI import AI


class Minesweeper:

    def __init__(self, mode="terminal"):
        """
        Initialise the game.
        Args:
            mode (str): The string of the mode. default "terminal".
        """
        self.view = ViewFactory.get_view(mode)

    def one_turn(self, use_ai):
        """
        Run one turn of the game.
        Returns:
            continue (bool): whether restart the game
            ai (bool): true if there is a script that can run.
        """
        # initiate the board
        board_size = self.view.get_board_size()
        if board_size == {}:
            board = Board()
        else:
            board = Board(mine_count=board_size["mine_count"], width=board_size["width"], height=board_size["height"])
        # initiate the ai
        if use_ai:
            ai = AI()

        while not board.is_game_finish():
            if use_ai:
                operation = self.view.run(board.get_board(), ai=ai)
            else:
                operation = self.view.run(board.get_board())
            if not board.update(operation["x"], operation["y"], operation["flag"]):
                self.view.draw(board.get_board())
                return self.view.fail()
        return self.view.win()

    def run(self, ai):
        """
        Run the game.
        Args:
            ai (bool): true if there is a script that can run.
        """
        while self.one_turn(ai):
            pass

    @staticmethod
    def display_help_menu():
        # TODO add helper menu
        pass


def main():
    arguments = sys.argv[1:]
    # help menu
    if "-h" in arguments or "--help" in arguments:
        Minesweeper.display_help_menu()
        return

    minesweeper = None
    # terminal run
    if "-t" in arguments or "--terminal" in arguments:
        minesweeper = Minesweeper(mode="terminal")
    # pygame run
    if "-p" in arguments or "--pygame" in arguments:
        if minesweeper:
            raise Exception("Cannot specify more than one visual type")
        minesweeper = Minesweeper(mode="pygame")
    # tkinter run
    if "-tk" in arguments or "--tkinter" in arguments:
        if minesweeper:
            raise Exception("Cannot specify more than one visual type")
        minesweeper = Minesweeper(mode="tkinter")
    # default
    if minesweeper is None:
        minesweeper = Minesweeper()

    # ai option
    if "-ai" in arguments:
        minesweeper.run(ai=True)
    else:
        minesweeper.run(ai=False)


if __name__ == '__main__':
    main()
