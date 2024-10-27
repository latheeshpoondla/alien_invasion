import pygame
import sys


class Alien_Invasion:
<<<<<<< HEAD
    """Master class of the game"""

=======
    '''Master class of the game'''
>>>>>>> d59f340172a02916f316b1835a33273f05ca3eab
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien_Invasion")
        self.bg_color = (180, 255, 190)
        self.clock = pygame.time.Clock()
<<<<<<< HEAD

    def run_game(self):
        """Main Loop - display loop"""
        while True:
            for event in pygame.event.get():
                """Event loop"""
=======
    def rungame(self):
        '''Main Loop - display loop'''
        while True:
            for event in pygame.event.get():
                '''Event loop'''
>>>>>>> d59f340172a02916f316b1835a33273f05ca3eab
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()
            self.clock.tick(60)

<<<<<<< HEAD

if __name__ == "__main__":
    ai = Alien_Invasion()
    ai.run_game()
=======
if __name__ == '__main__':
    ai = Alien_Invasion()
    ai.rungame()
>>>>>>> d59f340172a02916f316b1835a33273f05ca3eab
