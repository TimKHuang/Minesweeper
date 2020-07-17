# -*- coding:utf-8 -*-
"""
@author: victorvv
@contact: wengvictor5@gmail.com
@software: PyCharm
@file: PygameView.py
@time: 2020/7/14 上午10:46
@description: This builds the general GUI for minesweeper
"""
import pygame

from src.constants import RGB
from src.Button import Button
from src.View import View


class PygameView:
    """
    Showing the board as GUI
    Attributes:
        width = width of the screen
        height = height of the screen
        screen = the screen to display the game
    """

    def __init__(self, width=400, height=600):
        """
        Constructor for the GUI
        Args:
            width: the width of the screen
            height: the height of the screen
        """
        self.width = width
        self.height = height
        screen = pygame.display.set_mode((self.width, self.height))
        self.screen = screen

    def get_board_size(self, event):
        """
        This function is used initialise the game
        And get the board size of the game
        Args:
            event:

        Returns:

        """
        # Initialise the game
        pygame.init()

        # Set up window and background
        self.screen.fill(RGB["WHITE"])
        pygame.display.set_caption('MineSweeper')

        # Dimension of button
        font_size = 20
        button_width = 200
        button_height = 50
        all_button_height = 350
        # Set up the option buttons
        beginner_button = Button(
            (self.width // 2 - button_width // 2, (self.height - all_button_height) // 2, button_width, button_height),
            RGB["PALE_GREEN"], "Beginner", RGB["WHITE"], font_size)
        beginner_button.draw_button(self.screen)
        intermediate_button = Button((self.width // 2 - button_width // 2, (self.height - all_button_height) // 2 + 100,
                                      button_width, button_height),
                                     RGB["PALE_GREEN"], "Intermediate", RGB["WHITE"], font_size)
        intermediate_button.draw_button(self.screen)
        customise_button = Button((self.width // 2 - button_width // 2, (self.height - all_button_height) // 2 + 200,
                                   button_width, button_height),
                                  RGB["PALE_GREEN"], "Customise", RGB["WHITE"], font_size)
        customise_button.draw_button(self.screen)
        pygame.display.flip()

        # Get the game level
        while True:
            if beginner_button.update_button(event, self.screen):
                pygame.display.update()
                board_size = beginner_button.update_button(event, self.screen)
                return board_size
                break
            elif intermediate_button.update_button(event, self.screen):
                pygame.display.update()
                board_size = intermediate_button.update_button(event, self.screen)
                return board_size
            else:
                pygame.display.update()
                board_size = customise_button.update_button(event, self.screen)
                return board_size

    def draw(self, board):
        """
        This function is used to draw the board, and update the board
        Args:
            board: the mine board
        Returns:
            void
        """
        # Get the dimension of the board
        rows = len(board)
        cols = len(board[0])
        # square dimension
        sqr_width = self.width / cols
        sqr_height = self.height / rows
        for y in range(rows):
            # Draw the y axis
            pygame.draw.line(self.screen, RGB["CYANINE"], (0, sqr_height * y), (self.width, sqr_height * y), 5)
            for x in range(cols):
                # Draw the x axis
                pygame.draw.line(self.screen, RGB["CYANINE"], (sqr_width * x, 0), (sqr_width * x, self.height), 5)
                # Draw the square
                square = Button((x * sqr_width + 5, y * sqr_height + 5, sqr_width - 5, sqr_height - 5), RGB["HAZE"])
                square.draw_square(self.screen)
        pygame.display.update()

    def detect_event(self, event):
        """
        This function is used to update the GUI according to the event
        Args:
            event(Event): user's event

        Returns:
            void
        """
        if event.type == pygame.QUIT:
            exit()

        # Choose the buttons

    def run(self):
        """
        A function runs the game
        Returns:

        """


#
# while True:
#
#         # elif event.type == material.VIDEORESIZE:
#         #     size = width, height = event.size[0], event.size[1]
#         #     screen = material.display.set_mode(size, material.RESIZABLE)
#         #     screen.blit(material.transform.scale(img, size), (0, 0))
#         #     material.display.flip()
#
#         board_size = beginner_button.update_button(event, window)
#         # print(board_size)
#         intermediate_button.update_button(event, window)
#         customise_button.update_button(event, window)


# The section below is for test purposes

def test():
    from src.Board import Board
    view = PygameView()
    board_size = None
    while True and board_size is None:
        for event in pygame.event.get():
            view.detect_event(event)
            if view.get_board_size(event):
                print(view.get_board_size(event))
                board_size = view.get_board_size(event)
                break
    view.screen.fill(RGB["WHITE"])
    board = Board(1, 2, 2).get_board()
    view.draw(board)
    while True:
        for event in pygame.event.get():
            view.detect_event(event)


if __name__ == '__main__':
    test()
