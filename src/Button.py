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
