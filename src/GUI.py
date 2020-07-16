# -*- coding:utf-8 -*-
"""
@author: victorvv
@contact: wengvictor5@gmail.com
@software: PyCharm
@file: GUI.py
@time: 2020/7/14 上午10:46
@description: This builds the general GUI for minesweeper
"""
import pygame

from src.constants import RGB
from src.Button import Button
from src.View import View


class GUI:
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

    def initialise(self):
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
        # Update the screen the first time
        pygame.display.flip()

    # def draw(self, board):
    #     """
    #     This function is used to draw the board, and update the board
    #     Args:
    #         board: the mine board
    #     Returns:
    #         void
    #     """
    #     # Get the dimension of the board
    #     rows = len(board)
    #     cols = len(board[0])
    #     # square dimension
    #     sqr_width = 400 / cols
    #     sqr_height = 600 / rows
    #     for y in range(rows):
    #         # Draw the y axis
    #         pygame.draw.line(self.screen, RGB["CYANINE"] (0, sqr_height * y), (self.width, sqr_height * y), 5)
    #         for x in range(cols):
    #             # Draw the x axis
    #             pygame.draw.line(self.screen, RGB["CYANINE"], (sqr_width * x, 0), (sqr_width * x, self.height), 5)
    #             square = Button(())
    #             point = board[y][x]
    #             if point.is_opened:
    #                 if


#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
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
#
#
# # Draw the board
# def display_board(board):
#     rows = len(board)
#     cols = len(board[0])
#     sqr_width = 400 / cols
#     sqr_height = 600 / rows
#     # Draw the x, y axis
#     for y in range(rows):
#         pygame.draw.line(window, (92, 167, 186), (0, sqr_height * y), (400, sqr_height * y), 5)
#         for x in range(cols):
#             pygame.draw.line(window, (92, 167, 186), (sqr_width * x, 0), (sqr_width * x, 600), 5)
#     # Create the mine_board
#     mine_board = [[Button((x * sqr_width + 5, y * sqr_height + 5, sqr_width - 5, sqr_height - 5), (199, 237, 233), None,
#                           None, None) for x in range(cols)] for y in range(rows)]
#     # Display the board
#     for row in mine_board:
#         for val in row:
#             val.draw_square(window)

# The section below is for test purposes


def test():
    view = GUI()
    GUI.initialise(view)


if __name__ == '__main__':
    test()
