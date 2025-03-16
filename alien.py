import pygame
import os
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.ai_game = ai_game
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.img = pygame.image.load(os.path.join("images", "alienship.bmp"))
        self.image = pygame.transform.scale(self.img, (self.settings.alien_width, self.settings.alien_height))
        self.rect = self.image.get_rect()
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)
        self.alien_speed = 0
        
    def blit(self):
        self.screen.blit(self.image, self.rect)
    
    def _set_position(self, x, y):
        self.x = x
        self.y = y
        self.rect.centerx = x
        self.rect.centery = y
    
    def update(self):
        self.y += self.alien_speed
        self.rect.centery = self.y