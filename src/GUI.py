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

# Initialise the game
pygame.init()

# Set up window and background
window = pygame.display.set_mode((400, 600))
window.fill((255, 255, 255))
pygame.display.set_caption('MineSweeper')

beginner_button = Button((100, 100, 200, 50), "Beginner", RGB["PALE_GREEN"], RGB["WHITE"], 20)
beginner_button.draw_button(window)
intermediate_button = Button((100, 200, 200, 50), "Intermediate", RGB["PALE_GREEN"], RGB["WHITE"], 20)
intermediate_button.draw_button(window)
customise_button = Button((100, 300, 200, 50), "Customise", RGB["PALE_GREEN"], RGB["WHITE"], 20)
customise_button.draw_button(window)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        # elif event.type == material.VIDEORESIZE:
        #     size = width, height = event.size[0], event.size[1]
        #     screen = material.display.set_mode(size, material.RESIZABLE)
        #     screen.blit(material.transform.scale(img, size), (0, 0))
        #     material.display.flip()

        board_size = beginner_button.update_button(event, window)
        # print(board_size)
        intermediate_button.update_button(event, window)
        customise_button.update_button(event, window)


# Draw the board
def display_board(board):
    rows = len(board)
    cols = len(board[0])
    square_width = 400 // cols
    # Draw the x axis
    for i in range(cols - 1):
        pygame.draw.line(window, RGB["CYANINE"], (square_width * i, 0), (square_width * i, 600))
    # Draw the y axis
    for i in range(rows - 1):
        pygame.draw.line(window, RGB[""])
