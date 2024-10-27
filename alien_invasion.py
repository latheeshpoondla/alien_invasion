import pygame
import sys


class Alien_Invasion:
    """Master class of the game"""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien_Invasion")
        self.bg_color = (180, 255, 190)
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