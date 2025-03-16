import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.ai_game = ai_game
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.img = pygame.image.load("D:/Latheesh/Projects/py_projects/alien_invasion/images/alienship.bmp")
        self.image = pygame.transform.scale(self.img, (self.settings.screen_width//24, self.settings.screen_height*3//40))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.screen_rect.topleft
        
    def blit(self):
        self.screen.blit(self.image, self.rect)