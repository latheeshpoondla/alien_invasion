import pygame


class Ship:
    """Class to manage the ship"""

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # Make sure to give the correct path to the image
        img = pygame.image.load(
            "D:/Latheesh/Projects/py_projects/alien_invasion/images/ship.bmp"
        )
        self.image = pygame.transform.scale(img, (100, 120))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.move_right = False
        self.move_left = False

    def blitship(self):
        self.screen.blit(self.image, self.rect)

    def _update_ship(self):
        if self.move_right and self.rect.centerx <= self.screen_rect.right:
            self.rect.x += self.ai_game.settings.ship_speed
        if self.move_left and self.rect.centerx >= 0:
            self.rect.x -= self.ai_game.settings.ship_speed