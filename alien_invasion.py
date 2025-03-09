import pygame
import sys
from settings import Settings
from ship import Ship


class Alien_Invasion:
    """Master class of the game"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien_Invasion")
        self.bg_colour = self.settings.bgcolor
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)
        self.fullscreen = 0

    def run_game(self):
        """Main Loop - display loop"""
        while True:
            self._event_checker()
            self.ship._update_ship()
            self._update_screen()

            self.clock.tick(300)

    def _event_checker(self):
        """Checks for events (user input)"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_event_keydown(event)
            elif event.type == pygame.KEYUP:
                self.check_event_keyup(event)

    def check_event_keydown(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        if event.key == pygame.K_LEFT:
            self.ship.move_left = True
        if event.key == pygame.K_f:
            if self.fullscreen == 0:
                self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                self.fullscreen = 1
            elif self.fullscreen == 1:
                self.screen = pygame.display.set_mode((self.settings.win_screen_width, self.settings.win_screen_height))
                self.fullscreen = 0
            self.settings.screen_height = self.screen.get_height()
            self.settings.screen_width = self.screen.get_width()
            self.ship.resize_screen()
    
    def check_event_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        if event.key == pygame.K_LEFT:
            self.ship.move_left = False
    
    def _update_screen(self):
        """manages changes on screen"""
        self.screen.fill(self.bg_colour)
        self.ship.blitship()  # make sure that these are in correct order
        pygame.display.flip()


if __name__ == "__main__":
    ai = Alien_Invasion()
    ai.run_game()