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
import time

from src.view.assets.datas.constants import RGB
from src.view.PygameView.Button import Button
from src.view.View import View
from src.view.PygameView.TextBox import TextBox


class PygameView(View):
    """
    This class is used to generate the GUI View
    This class is built by PygameView
    """

    def __init__(self, screen_width=400, screen_height=600):
        """
        Constructor for PygameView
        Args:
            screen_width: default value for screen width is 400
            screen_height: default value for screen height is 600
        """
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.board_rows = None
        self.board_cols = None
        self.time_width = 0
        self.time_height = 0
        # Set up the screen
        self.screen = None
        # Generate the event
        self.event = None
        # Initialise pygame
        pygame.init()

    def get_board_size(self):
        """
        This function is used initialise the game
        And get the board size of the game
        Returns:
            game_level(dictionary): This determines the dimension of the board
        """
        # Dimension of button
        board = {}
        BUTTON_WIDTH = 200
        BUTTON_HEIGHT = 50
        MESSAGE_SIZE = 20
        all_button_height = BUTTON_HEIGHT * 3 + 200

        # The get board size window has a fixed dimension
        self.screen_width = 400
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Minesweeper")
        icon = pygame.image.load('view/assets/images/icon.jpg').convert_alpha()
        pygame.display.set_icon(icon)

        # Each iteration needs to refill the screen
        bg = pygame.image.load('view/assets/images/bg-galaxy.jpg').convert_alpha()
        bg = pygame.transform.smoothscale(bg, (self.screen_width, self.screen_height))
        self.screen.blit(bg, (0, 0))

        # Set up beginner button
        beginner_button = Button(
            (self.screen_width // 2 - BUTTON_WIDTH // 2, (self.screen_height - all_button_height) // 2 + 50,
             BUTTON_WIDTH,
             BUTTON_HEIGHT),
            RGB["VIOLET"], "Beginner", RGB["WHITE"], MESSAGE_SIZE)
        beginner_button.draw_button(self.screen)

        # Set up intermediate button
        intermediate_button = Button(
            (self.screen_width // 2 - BUTTON_WIDTH // 2, (self.screen_height - all_button_height) // 2 + 150,
             BUTTON_WIDTH, BUTTON_HEIGHT),
            RGB["VIOLET"], "Intermediate", RGB["WHITE"], MESSAGE_SIZE)
        intermediate_button.draw_button(self.screen)

        # Set up customise button
        customise_button = Button(
            (self.screen_width // 2 - BUTTON_WIDTH // 2, (self.screen_height - all_button_height) // 2 + 250,
             BUTTON_WIDTH, BUTTON_HEIGHT),
            RGB["VIOLET"], "Customise", RGB["WHITE"], MESSAGE_SIZE)
        customise_button.draw_button(self.screen)

        # First time set up the screen
        pygame.display.flip()

        # Get the game level
        while True:
            self.event = pygame.event.wait()
            if beginner_button.within_bound(pygame.mouse.get_pos()):
                if beginner_button.update_button(self.event, self.screen):
                    pygame.display.update()
                    board = beginner_button.get_board_size()

            if intermediate_button.within_bound(pygame.mouse.get_pos()):
                if intermediate_button.update_button(self.event, self.screen):
                    pygame.display.update()
                    board = intermediate_button.get_board_size()

            if customise_button.within_bound(pygame.mouse.get_pos()):
                if customise_button.update_button(self.event, self.screen):
                    self.screen.fill(RGB["WHITE"])
                    bg = pygame.image.load('view/assets/images/bg-galaxy.jpg').convert_alpha()
                    bg = pygame.transform.smoothscale(bg, (self.screen_width, self.screen_height))
                    self.screen.blit(bg, (0, 0))
                    beginner_button.set_alpha(self.screen, 50)
                    intermediate_button.set_alpha(self.screen, 50)
                    customise_button.set_alpha(self.screen, 50)
                    pygame.display.update()
                    board = self._draw_text_box(MESSAGE_SIZE)

            if len(board) == 3:
                return board

            elif self.event.type == pygame.QUIT:
                raise SystemExit

    def _draw_text_box(self, size):
        """
        This function is used to demand for user's input
        And it draws the text boxes out
        Args:
            size(int): determines the size of the message
        Returns:
            board(dictionary): determines the dimension of the board
        """
        board = {}
        BUTTON_WIDTH = 200
        BUTTON_HEIGHT = 50
        MESSAGE_SIZE = 20
        all_button_height = BUTTON_HEIGHT * 3 + 200

        font = pygame.font.Font('view/assets/fonts/Trinity.ttf', size)
        mine_text = font.render('Mine count ', True, RGB["VIOLET"])
        mine_tw, mine_th = mine_text.get_size()
        mine_tx = (self.screen_width - mine_tw) // 6
        mine_ty = (self.screen_height - mine_th) // 6
        self.screen.blit(mine_text, (mine_tx, mine_ty + 50))
        mine_count_box = TextBox(
            (mine_tx + mine_tw + 20, mine_ty + 40, self.screen_width - mine_tw - mine_tx - 40, mine_th * 2), size,
            RGB["VIOLET"])
        mine_count_box.draw(self.screen)

        width_text = font.render('Width ', True, RGB["VIOLET"])
        width_tw, width_th = width_text.get_size()
        width_tx = mine_tx
        width_ty = mine_ty + 100
        self.screen.blit(width_text, (width_tx, width_ty + 50))
        width_box = TextBox(
            (mine_tx + mine_tw + 20, width_ty + 40, self.screen_width - mine_tw - mine_tx - 40, width_th * 2),
            size, RGB["VIOLET"])
        width_box.draw(self.screen)

        height_text = font.render('Height ', True, RGB["VIOLET"])
        height_tw, height_th = height_text.get_size()
        height_tx = mine_tx
        height_ty = width_ty + 100
        self.screen.blit(height_text, (height_tx, height_ty + 50))
        height_box = TextBox(
            (mine_tx + mine_tw + 20, height_ty + 40, self.screen_width - mine_tw - mine_tx - 40, height_th * 2),
            size, RGB["VIOLET"])
        height_box.draw(self.screen)

        # Create a submit button allows user to submit the dimension of the board
        submit_button = Button(
            (self.screen_width // 2 - BUTTON_WIDTH // 2, (self.screen_height - all_button_height) // 2 + 350,
             BUTTON_WIDTH,
             BUTTON_HEIGHT),
            RGB["VIOLET"], "Submit", RGB["WHITE"], MESSAGE_SIZE)
        submit_button.draw_button(self.screen)

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if mine_count_box.within_bound(pygame.mouse.get_pos()):
                    if event.type == pygame.KEYDOWN:
                        self.event = event
                        mine_count_box.update(self.event)

                if width_box.within_bound(pygame.mouse.get_pos()):
                    if event.type == pygame.KEYDOWN:
                        self.event = event
                        width_box.update(self.event)

                if height_box.within_bound(pygame.mouse.get_pos()):
                    if event.type == pygame.KEYDOWN:
                        self.event = event
                        height_box.update(self.event)

                if submit_button.within_bound(pygame.mouse.get_pos()):
                    self.event = event
                    if submit_button.update_button(self.event, self.screen):
                        pygame.display.update()
                        board["mine_count"] = int(mine_count_box.text)
                        board["width"] = int(width_box.text)
                        board["height"] = int(height_box.text)
                        return board

                elif event.type == pygame.QUIT:
                    raise SystemExit

            pygame.time.delay(33)
            mine_count_box.draw(self.screen)
            width_box.draw(self.screen)
            height_box.draw(self.screen)
            pygame.display.update()

    def draw(self, board, remaining):
        """
        This function is used to draw the board, and update the board
        Args:
            board: the selected board
            remaining (int): The number of remained mine on the board
        """
        # Dimension of cell
        CELL_WIDTH = 30
        CELL_HEIGHT = 30
        NUMBER_SIZE = 20
        LINE_WIDTH = 0

        # Set up the new screen
        self.board_rows = len(board)
        self.board_cols = len(board[0])
        max_width = (self.board_cols + 1) * CELL_WIDTH
        max_height = (self.board_rows + 1) * CELL_HEIGHT
        self.screen_width = max_width + 100 * 2
        self.screen_height = max_height + 100 * 2
        startpos_x = (self.screen_width - max_width) // 2
        startpos_y = (self.screen_height - max_height) // 2
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # During each iteration the prev screen is refilled
        bg = pygame.image.load('view/assets/images/bg-yourname.jpg').convert_alpha()
        bg = pygame.transform.smoothscale(bg, (self.screen_width, self.screen_height))
        bg.set_alpha(10)
        self.screen.blit(bg, (0, 0))

        for y in range(self.board_rows):
            # Draw the x axis
            pygame.draw.line(self.screen, RGB["BLACK"], (startpos_x, CELL_HEIGHT * y + startpos_y),
                             (max_width, CELL_HEIGHT * y + startpos_y),
                             LINE_WIDTH)

        for x in range(self.board_cols):
            # Draw the y axis
            pygame.draw.line(self.screen, RGB["BLACK"], (CELL_WIDTH * x + startpos_x, startpos_y),
                             (CELL_WIDTH * x + startpos_x, max_height),
                             LINE_WIDTH)

        font = pygame.font.Font('view/assets/fonts/digital-7 (mono italic).ttf', 35)
        text = "Mine remained: " + str(remaining)
        remained_mine = font.render(text, True, RGB["PALE_PURPLE"])
        remained_mine_w, remained_mine_h = remained_mine.get_size()
        self.screen.blit(remained_mine, (0, remained_mine_h))

        # Draw the board out
        for y in range(self.board_rows):
            for x in range(self.board_cols):
                point = board[y][x]
                bx = x * CELL_WIDTH + startpos_x
                by = y * CELL_HEIGHT + startpos_y
                bw = CELL_WIDTH - 2
                bh = CELL_HEIGHT - 2
                if point.is_opened:
                    # Load the image of mine to the screen
                    if point.is_bomb:
                        pygame.draw.rect(self.screen, RGB["WHITE"], (bx, by, bw, bh), 1)
                        bomb = pygame.image.load('view/assets/images/mine.png')
                        bomb = pygame.transform.smoothscale(bomb, (CELL_WIDTH - 5, CELL_HEIGHT - 5))
                        self.screen.blit(bomb, (x * CELL_WIDTH + startpos_x, y * CELL_HEIGHT + startpos_y))
                        continue

                    else:
                        # Draw the point out
                        pygame.draw.rect(self.screen, RGB["WHITE"], (bx, by, bw, bh), 1)
                        if point.bomb_around == 0:
                            continue
                        else:
                            number_font = pygame.font.Font('view/assets/fonts/number.ttf', NUMBER_SIZE)
                            number = number_font.render(str(point.bomb_around), True, RGB[str(point.bomb_around)])
                            tw, th = number.get_size()
                            # Centralise the number
                            tx = bx + bw / 2 - tw / 2
                            ty = by + bh / 2 - th / 2
                            self.screen.blit(number, (tx, ty))
                            continue

                if point.is_flagged:
                    # Load the image of flag to the screen
                    pygame.draw.rect(self.screen, RGB["WHITE"], (bx, by, bw, bh), 1)
                    flag = pygame.image.load('view/assets/images/flag.png')
                    flag = pygame.transform.smoothscale(flag, (CELL_WIDTH - 5, CELL_HEIGHT - 5))
                    self.screen.blit(flag, (x * CELL_WIDTH + startpos_x, y * CELL_HEIGHT + startpos_y))
                    continue

                else:
                    # Draw squares for unopened point on the board
                    pygame.draw.rect(self.screen, RGB["SAKURA"], (bx, by, bw, bh))
                    continue

        # Update the screen after changing
        pygame.display.update()

    def _centralise(self, text, dim):
        """
        This function is used to centralise the text on a given screen
        Args:
            text(String): message to be displayed
            dim(Tuple): the dimension of the screen or
        """
        tw, th = text.get_size()
        bx, by, bw, bh = dim
        tx = bx + bw / 2 - tw / 2
        ty = by + bh / 2 - th / 2
        self.screen.blit(text, (tx, ty))

    def _get_continue(self, message):
        """
        This function is used get if user wants to continue the game
        Args:
            message: The message to be displayed
        Returns:
            continue (boolean): if user wants to continue the game
        """
        """
                Deal with the situation when game fails
                Returns:
                    continue(boolean): True is start. False otherwise
                """
        # Dimension of the button
        DEMAND_SIZE = 30
        MESSAGE_SIZE = 20

        # Let the user to view the game
        time.sleep(3)

        # The dimension of this window is fixed:
        self.screen_width = 600
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.reset_timer()

        # Refill the screen
        bg = pygame.image.load('view/assets/images/bg-space.jpg').convert_alpha()
        bg = pygame.transform.smoothscale(bg, (self.screen_width, self.screen_height))
        self.screen.blit(bg, (0, 0))

        bx, by, bw, bh = (
            self.screen_width / 6, self.screen_height / 4, self.screen_width * 2 / 3, self.screen_height / 6)
        # Get the font
        font = pygame.font.Font('view/assets/fonts/Trinity.ttf', DEMAND_SIZE)
        text = font.render(message, True, RGB["PALE_PURPLE"])
        self._centralise(text, (bx, by, bw, bh))

        # Create two buttons
        restart_button = Button(
            (self.screen_width / 6, self.screen_height / 2, self.screen_width / 6, self.screen_height / 10),
            RGB["VIOLET"],
            "RESTART", RGB["WHITE"], MESSAGE_SIZE)
        quit_button = Button(
            (self.screen_width * 2 / 3, self.screen_height / 2, self.screen_width / 6, self.screen_height / 10),
            RGB["VIOLET"],
            "QUIT", RGB["WHITE"], MESSAGE_SIZE)
        restart_button.draw_button(self.screen)
        quit_button.draw_button(self.screen)
        pygame.display.update()

        # Get user's choice
        while True:
            self.event = pygame.event.wait()
            if restart_button.within_bound(pygame.mouse.get_pos()):
                if restart_button.update_button(self.event, self.screen):
                    pygame.display.update()
                    return restart_button.get_choice()

            if quit_button.within_bound(pygame.mouse.get_pos()):
                if quit_button.update_button(self.event, self.screen):
                    pygame.display.update()
                    return quit_button.get_choice()

            if self.event.type == pygame.QUIT:
                raise SystemExit

    def fail(self):
        """
        Deal with the situation when game fails
        Returns:
            continue(boolean): True is start. False otherwise
        """
        return self._get_continue("You've met a bomb")

    def win(self):
        """
        Deal with the situation when game wins
        Returns:
            continue(boolean): True is start. False otherwise
        """
        return self._get_continue("Wow! Excellent!")

    def _get_board_coordinates(self, pos):
        """
        This function is used to return the x, y coordinate of the updated point on the board
        Args:
            pos(int, int): event's pos
        Returns:
            coordinates(int, int): the x, y value of the point on the board
        """
        # Dimension of cell
        CELL_WIDTH = 30
        CELL_HEIGHT = 30
        max_width = (self.board_cols + 1) * CELL_WIDTH
        max_height = (self.board_rows + 1) * CELL_HEIGHT
        startpos_x = (self.screen_width - max_width) // 2
        startpos_y = (self.screen_height - max_height) // 2

        x, y = pos
        for r in range(self.board_rows):
            for c in range(self.board_cols):
                bx = c * CELL_WIDTH + startpos_x
                by = r * CELL_HEIGHT + startpos_y
                bw = CELL_WIDTH - 2
                bh = CELL_HEIGHT - 2
                if bx <= x <= bx + bw and by <= y <= by + bh:
                    return c, r
                else:
                    pass

    def _update_time(self):
        """
        This function is used to update the time
        """
        time_passed = "TIME: " + str(int(self.time_running())) + " SEC"
        font = pygame.font.Font('view/assets/fonts/digital-7 (mono italic).ttf', 35)
        text = font.render(time_passed, True, RGB["PALE_PURPLE"])
        self.screen.blit(text, (0, 0))
        self.time_width, self.time_height = text.get_size()

    def _reload_screen(self):
        """
        This function is used to reload the screen
        """
        bg = pygame.image.load('view/assets/images/bg-yourname.jpg').convert_alpha()
        bg = pygame.transform.smoothscale(bg, (self.screen_width, self.screen_height))
        select_area = pygame.Rect(0, 0, self.time_width, self.time_height)
        snapshot = bg.subsurface(select_area).copy()
        self.screen.blit(snapshot, (0, 0))

    def input(self):
        """
        This function return user's move
        Returns:
            user_move{"POS": (int, int), "OPEN": boolean, "FLAG": bool}
        """
        user_move = {}
        while True:
            for event in pygame.event.get():
                self.event = event
                if self.event.type == pygame.QUIT:
                    raise SystemExit
                elif self.event.type == pygame.MOUSEBUTTONUP and self.event.button == 1:
                    coordinates = self._get_board_coordinates(self.event.pos)
                    if coordinates is not None:
                        user_move["flag"] = False
                        user_move["x"] = coordinates[0]
                        user_move["y"] = coordinates[1]
                        return user_move
                elif self.event.type == pygame.MOUSEBUTTONUP and self.event.button == 3:
                    coordinates = self._get_board_coordinates(self.event.pos)
                    if coordinates is not None:
                        user_move["flag"] = True
                        user_move["x"] = coordinates[0]
                        user_move["y"] = coordinates[1]
                        return user_move

            # Update the time taken
            self._reload_screen()
            self._update_time()
            pygame.display.update()


# The section below is for test purposes

def check_stop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit


def test():
    from src.Board import Board
    view = PygameView(800, 800)
    view.run(Board().get_board(), Board().remaining())
    while True:
        check_stop()


if __name__ == '__main__':
    test()
