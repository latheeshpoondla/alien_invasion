import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


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
        self.aliens = pygame.sprite.Group()
        new_alien = Alien(self)
        self.aliens.add(new_alien)
        self.bullets = pygame.sprite.Group()
        self.fullscreen = 0

    def run_game(self):
        """Main Loop - display loop"""
        while True:
            self._event_checker()
            self.ship._update_ship()
            self.bullets.update()
            self._delete_bullet()
            self._update_screen()

            self.clock.tick(300)

    def _event_checker(self):
        """Checks for events (user input)"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_event_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_event_keyup(event)

    def _check_event_keydown(self, event):
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
        if event.key == pygame.K_SPACE:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _check_event_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        if event.key == pygame.K_LEFT:
            self.ship.move_left = False
    
    def _delete_bullet(self):
        for bullet in self.bullets.sprites():
            if bullet.y <= 0:
                bullet.kill()
            
    def _update_screen(self):
        """manages changes on screen"""
        self.screen.fill(self.bg_colour)
        self.ship.blitship() # make sure that these are in correct order
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for alien in self.aliens.sprites():
            alien.blit()
        pygame.display.flip()


if __name__ == "__main__":
    ai = Alien_Invasion()
    ai.run_game()