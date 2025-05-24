import pygame
import os

class Ship:
    """Class to manage the ship"""

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        # Make sure to give the correct path to the image
        self.img = pygame.image.load(os.path.join("images", "ship.bmp"))
        self.image = pygame.transform.scale(self.img, (self.ai_game.settings.screen_width//12, self.ai_game.settings.screen_height*3//20))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.move_right = False
        self.move_left = False
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)

    def blitship(self):
        self.screen.blit(self.image, self.rect)

    def _update_ship(self):
        if self.move_right and self.rect.centerx <= self.screen_rect.right:
            self.x += self.ai_game.settings.ship_speed
        if self.move_left and self.rect.centerx >= 0:
            self.x -= self.ai_game.settings.ship_speed
        self.rect.centerx = self.x