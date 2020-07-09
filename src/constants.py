# -*- coding:utf-8 -*-
"""
@author: victorvv
@contact: wengvictor5@gmail.com
@software: PyCharm
@file: constants.py
@time: 2020/7/9 下午6:45
@description: This file contains constants value for minesweeper
"""

# The values below are used to initialise a mine board
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
