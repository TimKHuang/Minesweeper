# -*- coding:utf-8 -*-
"""
@author: timkhuang
@contact: timkhuang@icloud.com
@software: PyCharm
@file: ViewFactory.py
@time: 17/07/2020 10:18
@description: The Factory to produce a particular View instance.
"""
from src.view.TerminalView.TerminalView import TerminalView
from src.view.PygameView.PygameView import PygameView
from src.exceptions import NoModeException


class ViewFactory:
    @staticmethod
    def get_view(mode):
        """
        Can be seen as a factory of different views.
        Available views are: "terminal", "pygame"
        Args:
            mode (str): The chosen running mode
        Returns:
            view (View): instance of a particular view.
        """
        if mode == "terminal":
            return TerminalView()
        if mode == "pygame":
            return PygameView()
        raise NoModeException
