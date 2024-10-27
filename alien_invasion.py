import pygame
import sys
from settings import Settings


class Alien_Invasion:
    """Master class of the game"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien_Invasion")
        self.bg_color = self.settings.bg_color
        self.clock = pygame.time.Clock()

    def run_game(self):
        """Main Loop - display loop"""
        while True:
            for event in pygame.event.get():
                """Event loop"""
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    ai = Alien_Invasion()
    ai.run_game()