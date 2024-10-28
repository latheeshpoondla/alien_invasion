import pygame
class Ship:
    """Class to manage the ship"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        #Make sure to give the correct path to the image
        img = pygame.image.load('D:/Latheesh/Projects/py_projects/alien_invasion/images/ship.bmp')
        self.image = pygame.transform.scale(img, (100, 120))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
    def blitship(self):
        self.screen.blit(self.image, self.rect)