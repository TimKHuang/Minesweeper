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

CELL_WIDTH = 20
CELL_HEIGHT = 20
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BOARD_WIDTH = 400
BOARD_HEIGHT = 600
MESSAGE_SIZE = BOARD_HEIGHT // BOARD_WIDTH * 20
NUMBER_SIZE = CELL_HEIGHT // CELL_WIDTH * 10
DEMAND_SIZE = BOARD_HEIGHT // BOARD_WIDTH * 30


def get_board_size(screen, event):
    """
    This function is used initialise the game
    And get the board size of the game
    Args:
        screen(String): the screen user wants to display
        event(Event): this is user's action
    Returns:
    game_level(dictionary): This determines the dimension of the board
        """
    # Set up window and background
    screen.fill(RGB["WHITE"])
    pygame.display.set_caption('MineSweeper')

    # Dimension of button
    all_button_height = 350
    # Set up the option buttons
    beginner_button = Button(
        (BOARD_WIDTH // 2 - BUTTON_WIDTH // 2, (BOARD_HEIGHT - all_button_height) // 2, BUTTON_WIDTH, BUTTON_HEIGHT),
        RGB["PALE_GREEN"], "Beginner", RGB["WHITE"], MESSAGE_SIZE)
    beginner_button.draw_button(screen)
    intermediate_button = Button((BOARD_WIDTH // 2 - BUTTON_WIDTH // 2, (BOARD_HEIGHT - all_button_height) // 2 + 100,
                                  BUTTON_WIDTH, BUTTON_HEIGHT),
                                 RGB["PALE_GREEN"], "Intermediate", RGB["WHITE"], MESSAGE_SIZE)
    intermediate_button.draw_button(screen)
    customise_button = Button((BOARD_WIDTH // 2 - BUTTON_WIDTH // 2, (BOARD_HEIGHT - all_button_height) // 2 + 200,
                               BUTTON_WIDTH, BUTTON_HEIGHT),
                              RGB["PALE_GREEN"], "Customise", RGB["WHITE"], MESSAGE_SIZE)
    customise_button.draw_button(screen)
    # First time set up the screen
    pygame.display.flip()

    # Get the game level
    while True:
        if beginner_button.update_button(event, screen):
            pygame.display.update()
            return beginner_button.update_button(event, screen)

        elif intermediate_button.update_button(event, screen):
            pygame.display.update()
            return intermediate_button.update_button(event, screen)

        else:
            pygame.display.update()
            return customise_button.update_button(event, screen)


def draw(screen, board):
    """
    This function is used to draw the board, and update the board
    Args:
        screen(String): the screen user wants to display
        board(matrix of pointdata): the mine board
    Returns:
        void
    """
    screen.fill(RGB["WHITE"])

    # Get the dimension of the board
    rows = len(board)
    cols = len(board[0])
    for y in range(rows):
        # Draw the y axis
        pygame.draw.line(screen, RGB["CYANINE"], (0, CELL_HEIGHT * y), (BOARD_WIDTH, CELL_HEIGHT * y), 5)
        for x in range(cols):
            # Draw the x axis
            pygame.draw.line(screen, RGB["CYANINE"], (CELL_WIDTH * x, 0), (CELL_WIDTH * x, BOARD_HEIGHT), 5)
            point = board[y][x]
            if point.is_opened:
                # Load the image of mine to the screen
                if point.is_bomb:
                    bomb = pygame.image.load('material/mine.jpg')
                    bomb = pygame.transform.smoothscale(bomb, (CELL_WIDTH, CELL_HEIGHT))
                    screen.blit(bomb, (x * CELL_WIDTH + 5, y * CELL_HEIGHT + 5))
                    continue
                # Draw the point out
                bx = x * CELL_WIDTH - 5
                by = y * CELL_HEIGHT - 5
                bw = CELL_WIDTH - 5
                bh = CELL_HEIGHT - 5
                pygame.draw.rect(screen, RGB["HAZE"], (bx, by, bw, bh), 5)
                number_font = pygame.font.Font('material/number.ttf', NUMBER_SIZE)
                number = number_font.render(point, True, RGB[str(point)])
                tw, th = number.get_size()
                # Centralise the number
                tx = bx + bw / 2 - tw / 2
                ty = by + bh / 2 - th / 2
                screen.blit(number, (tx, ty))

            if point.is_flagged:
                # Load the image of flag to the screen
                flag = pygame.image.load('material/flag.png')
                flag = pygame.transform.smoothscale(flag, (CELL_WIDTH, CELL_HEIGHT))
                screen.blit(flag, (x * CELL_WIDTH + 5, y * CELL_HEIGHT + 5))
                continue

            # Draw squares for unopened point on the board
            bx = x * CELL_WIDTH - 5
            by = y * CELL_HEIGHT - 5
            bw = CELL_WIDTH - 5
            bh = CELL_HEIGHT - 5
            pygame.draw.rect(screen, RGB["PALE_GREEN"], (bx, by, bw, bh))

    # Update the screen after changing
    pygame.display.update()


class UserPlayer:
    """
    A simple user player that reads moves
    """
    user_move = {
        "POS": (),
        "OPEN": False,
        "FLAG": False
    }

    def choose_action(self, board):
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                raise SystemExit
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.user_move["POS"] = event.pos
                self.user_move["OPEN"] = True
                self.user_move["FLAG"] = False
                return self.user_move
            elif event.type == pygame and event.button == 3:
                self.user_move["POS"] = event.pos
                self.user_move["OPEN"] = False
                self.user_move["FLAG"] = True
                return self.user_move


def fail(screen, event):
    """
    Deal with the situation when game fails
    Args:
        event(Event): user's event
        screen(String): the screen to display chanegs
    Returns:
        continune(boolean): True is start. False otherwise
    """
    screen.fill(RGB["WHITE"])
    (bx, by, bw, bh) = (BOARD_WIDTH / 4, BOARD_HEIGHT / 4, BOARD_WIDTH / 2, BOARD_HEIGHT / 6)
    pygame.draw.rect(screen, RGB["PALE_GREEN"], (bx, by, bw, bh))
    # Get the font
    font = pygame.font.Font('material/Trinity.ttf', DEMAND_SIZE)
    text = font.render("You've met a bomb", True, RGB["WHITE"])
    tw, th = text.get_size()
    # Centralise the text
    tx = bx + bw / 2 - tw / 2
    ty = by + bh / 2 - th / 2
    screen.blit(text, (tx, ty))

    # Create two buttons
    restart_button = Button((BOARD_WIDTH / 4, BOARD_HEIGHT / 2, BOARD_WIDTH / 3, BOARD_HEIGHT / 10), RGB["PALE_GREEN"],
                            "RESTART", RGB["WHITE"], MESSAGE_SIZE)
    quit_button = Button((BOARD_WIDTH * 2 / 3, BOARD_HEIGHT / 2, BOARD_WIDTH / 3, BOARD_HEIGHT / 10), RGB["PALE_GREEN"],
                         "QUIT", RGB["WHITE"], MESSAGE_SIZE)
    # Get user's choice
    while True:
        if restart_button.is_up(event.pos, screen):
            pygame.display.update()
            return restart_button.get_choice(event, screen)
        if quit_button.is_up(event.pos, screen):
            pygame.display.update()
            return quit_button.get_choice(event, screen)


def win(screen, event):
    """
    Deal with the situation when game wins
    Args:
        event(Event): user's event
        screen(String): the screen to display chanegs
    Returns:
        continune(boolean): True is start. False otherwise
    """
    screen.fill(RGB["WHITE"])
    (bx, by, bw, bh) = (BOARD_WIDTH / 4, BOARD_HEIGHT / 4, BOARD_WIDTH / 2, BOARD_HEIGHT / 6)
    pygame.draw.rect(screen, RGB["PALE_GREEN"], (bx, by, bw, bh))
    # Get the font
    font = pygame.font.Font('material/Trinity.ttf', DEMAND_SIZE)
    text = font.render("Wow! Excellent", True, RGB["WHITE"])
    tw, th = text.get_size()
    # Centralise the text
    tx = bx + bw / 2 - tw / 2
    ty = by + bh / 2 - th / 2
    screen.blit(text, (tx, ty))

    # Create two buttons
    restart_button = Button((BOARD_WIDTH / 4, BOARD_HEIGHT / 2, BOARD_WIDTH / 3, BOARD_HEIGHT / 10), RGB["PALE_GREEN"],
                            "RESTART", RGB["WHITE"], MESSAGE_SIZE)
    quit_button = Button((BOARD_WIDTH * 2 / 3, BOARD_HEIGHT / 2, BOARD_WIDTH / 3, BOARD_HEIGHT / 10), RGB["PALE_GREEN"],
                         "QUIT", RGB["WHITE"], MESSAGE_SIZE)
    # Get user's choice
    while True:
        if restart_button.is_up(event.pos, screen):
            pygame.display.update()
            return restart_button.get_choice(event, screen)
        if quit_button.is_up(event.pos, screen):
            pygame.display.update()
            return quit_button.get_choice(event, screen)


# To be added
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
    pass


if __name__ == '__main__':
    test()
