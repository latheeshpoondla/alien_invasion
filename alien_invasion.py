import pygame
import sys
from settings import Settings
from ship import Ship


class Alien_Invasion:
    '''Master class of the game'''

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien_Invasion")
        self.bg_colour = (25, 20, 30)
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)

    def run_game(self):
        '''Main Loop - display loop'''
        while True:
            self._event_checker()
            self._update_screen()

            self.clock.tick(60)
    
    def _event_checker(self):
        '''Checks for events (user input)'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
    def _update_screen(self):
        '''manages changes on screen'''
        self.screen.fill(self.bg_colour)
        self.ship.blitship()#make sure that these are in correct order
        pygame.display.flip()

if __name__ == "__main__":
    ai = Alien_Invasion()
    ai.run_game()