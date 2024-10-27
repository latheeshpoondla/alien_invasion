import pygame
class Ship:
    """Class to manage the ship"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('D:/Latheesh/Projects/py_projects/alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
    def blitship(self):
        self.screen.blit(self.image, self.rect)