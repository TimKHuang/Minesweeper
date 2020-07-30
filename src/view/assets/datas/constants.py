# -*- coding:utf-8 -*-
"""
@author: victorvv
@contact: wengvictor5@gmail.com
@software: PyCharm
@file: datas.py
@time: 2020/7/9 下午6:45
@description: This file contains datas value for minesweeper
"""
BOARD_DIM = {"MINE_COUNT": 40,
             "BOARD_WIDTH": 16,
             "BOARD_HEIGHT": None
             }

# The dictionary below denotes the colour for each square's value
COLOUR = {"B": "\033[1m",
          "F": "\033[4m",
          "*": "\033[0m",
          0: "\033[0m",
          1: "\033[30m",
          2: "\033[31m",
          3: "\033[32m",
          4: "\033[33m",
          5: "\033[34m",
          6: "\033[35m",
          7: "\033[36m",
          8: "\033[37m",
          }

# The dictionary defines the RGB value for different colours
RGB = {"PALE_GREEN": (199, 237, 233),
       "WHITE": (255, 255, 255),
       "HAZE": (175, 215, 237),
       "CYANINE": (92, 167, 186),
       "BLACK": (0, 0, 0),
       "VIOLET": (137, 157, 192),
       "PALE_PURPLE": (225, 220, 252),
       "SAKURA": (246, 214, 255),
       "1": (225, 238, 210),
       "2": (219, 208, 167),
       "3": (230, 155, 3),
       "4": (209, 73, 78),
       "5": (18, 53, 85),
       "6": (227, 179, 37),
       "7": (119, 52, 96),
       "8": (78, 29, 76)
}

# The dictionary defines the dimension of the board for Intermediate
INTERMEDIATE_BOARD = {
    "mine_count": 40,
    "width": 16,
    "height": 16
}

BEGINNER_BOARD = {
    "mine_count": 10,
    "width": 8,
    "height": 8
}

# The dictionary defines the level of the game
GAME_LEVEL = {
    "B": "Beginner",
    "I": "Intermediate",
    "C": "Customise"
}
