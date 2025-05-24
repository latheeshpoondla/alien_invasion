import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
import os


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
        self.bullets = pygame.sprite.Group()
        self.aliens_no = 0
        self.alien_speed = 0
        

    def run_game(self):
        """Main Loop - display loop"""
        while True:
            if self.aliens_no == 0:
                self.alien_speed += 0.02
                self._set_fleet()
            self._event_checker()
            self.ship._update_ship()
            self.aliens.update()
            self._update_bullet()
            self._update_screen()
            if self._check_game_over():
                self._end_game()
            self.clock.tick(500)

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
        if event.key == pygame.K_SPACE:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _check_event_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        if event.key == pygame.K_LEFT:
            self.ship.move_left = False
    
    def _update_bullet(self):
        self.bullets.update()
        for bullet in self.bullets.sprites():
            if bullet.y <= 0:
                bullet.kill()
        self._strike_alien()
    
    def _strike_alien(self):
        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    def _set_fleet(self):
        self.aliens_no = self.settings.screen_width//self.settings.alien_width - 5
        inc = (self.settings.screen_width-self.aliens_no*self.settings.alien_width)/(self.aliens_no + 1) + self.settings.alien_width
        y = self.settings.alien_height/2
        for _ in range(3):
            x = inc-self.settings.alien_width/2
            for _ in range(self.aliens_no):
                new_alien = Alien(self)
                new_alien.alien_speed = self.alien_speed
                new_alien._set_position(x, y)
                self.aliens.add(new_alien)
                x += inc
            y += self.settings.alien_height
        self.aliens_no *= 3
        
    def _check_game_over(self):
        wa = self.settings.alien_width/2
        ws = self.ship.rect.width/2
        for alien in self.aliens.sprites():
            if alien.y+wa >  self.ship.y-ws:
                return True
    
    def _update_screen(self):
        """manages changes on screen"""
        self.screen.fill(self.bg_colour)
        self.ship.blitship() # make sure that these are in correct order
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for alien in self.aliens.sprites():
            alien.blit()
        pygame.display.flip()
        
    def _end_game(self):
        go_img = pygame.image.load(os.path.join("images", "game_over.bmp"))
        go_img = pygame.transform.scale(go_img, (self.settings.screen_width, self.settings.screen_height))
        go_rect = go_img.get_rect()
        for _ in range(700):
            self.screen.blit(go_img, go_rect)
            pygame.display.flip()
        sys.exit()

if __name__ == "__main__":
    ai = Alien_Invasion()
    ai.run_game()