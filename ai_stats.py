import pygame
class Stats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.high_score = 0
        self.reset_stats()
    
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0