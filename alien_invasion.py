import pygame
import sys
from settings import Settings
from ship import Ship


class Alien_Invasion:
    """Master class of the game"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien_Invasion")
        #Make sure to change the diretory to the correct path
        self.bg_colour = (27, 40, 45)
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)

    def run_game(self):
        """Main Loop - display loop"""
        while True:
            for event in pygame.event.get():
                """Event loop"""
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            self.ship.blitship()
            self.screen.fill(self.bg_colour)
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    ai = Alien_Invasion()
    ai.run_game()