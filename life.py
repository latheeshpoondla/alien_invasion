import pygame
import os
from pygame.sprite import Sprite

class Life(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.ai_game = ai_game
        self.stats = ai_game.stats
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.img = pygame.image.load(os.path.join("images", "heart.bmp"))
        self.image = pygame.transform.scale(self.img, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.bottomright = self.screen_rect.bottomright

    def blit(self):
        self.screen.blit(self.image, self.rect)