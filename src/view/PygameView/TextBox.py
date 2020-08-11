# -*- coding:utf-8 -*-
"""
@author: victorvv
@contact: wengvictor5@gmail.com
@software: PyCharm
@file: TextBox.py
@time: 2020/7/22 11:23
@description: this file creates the textboxes
"""
import pygame

from src.view.assets.datas.constants import RGB


class TextBox:
    """
    This function is used to create textboxes
    Boxes are used to get user's input
    """

    def __init__(self, dim, message_size, colour, callback=None):
        """
        This is the constructor for the textbox
        Args:
            dim(Tuple of 4): dim[0], dim[1] denotes the top-left corner's coordinate;
                             dim[2], dim[3] denotes the width and height of the textbox
            message_size(int): it determines the size of the text in the box
        """
        self.x, self.y = dim[0], dim[1]
        self.width, self.height = dim[2], dim[3]
        self.text = ""
        self.message_size = message_size
        self.colour = colour
        self.callback = callback

    def draw(self, screen):
        """
        This function is used to draw the textbox out at expected position
        Args:
            screen: the screen user wants to display the box
        """
        surface = pygame.Surface((self.width, self.height))
        surface.fill(self.colour)
        # Get the font
        font = pygame.font.Font('view/assets/fonts/Trinity.ttf', self.message_size)
        text_surf = font.render(self.text, True, RGB["WHITE"])
        screen.blit(surface, (self.x, self.y))
        screen.blit(text_surf, (self.x, self.y + (self.height - text_surf.get_height())),
                    (0, 0, self.width, self.height))

    def update(self, event):
        """
        This function is used to get user's input
        Args:
            event(Event): This is user's event
        """
        if event.type == pygame.KEYDOWN:

            unicode = getattr(event, "unicode")
            key = getattr(event, "key")

            # DEL
            if key == 8:
                self.text = self.text[:-1]
                return

            # CAPS
            if key == 301:
                return

            # ENTER
            if key == 13:
                if self.callback:
                    self.callback(self.text)
                return True
            
            # Can only type in numbers
            if 48 <= key <= 57:
                char = chr(key)
                self.text += char

    def within_bound(self, pos):
        """
        This function is used to check if a user's event is within the text box or not
        Args:
            pos(int, int): determines the coordinates of the event
        Returns:
            True, if it is within the box
            False, otherwise
        """
        x, y = pos
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        return False
