# -*- coding:utf-8 -*-
"""
@author: timkhuang
@contact: timkhuang@icloud.com
@software: PyCharm
@file: TkinterView.py
@time: 07/08/2020 14:14
@description: This is the GUI Part using the python module tkinter.
"""
from tkinter import Tk

from src.view.View import View

class TkinterView(View):

    def __init__(self):
        super().__init__()