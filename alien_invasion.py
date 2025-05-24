import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from ai_stats import Stats
from life import Life
from button import Button
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
        self.stats = Stats(self)
        self.aliens_no = 0
        self.alien_speed = 0
        self.life_list = []
        self.play_button = Button(self, "Play")
        self.lives = pygame.sprite.Group()
        self.game_status = False
        self._create_lives()
        

    def run_game(self):
        """Main Loop - display loop"""
        while True:
            self._event_checker()
            if self.game_status:
                if self.aliens_no == 0:
                    self.alien_speed += 0.1
                    self._set_fleet()
                self.ship._update_ship()
                self._update_alien()
                self._update_bullet()
            self._update_screen()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)

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
        if event.key == pygame.K_ESCAPE:
            self.reset_game()
    
    def reset_game(self):
        """Reset the game to initial state"""
        self.stats.reset_stats()
        self.aliens.empty()
        self.bullets.empty()
        self.ship.center_ship()
        self.alien_speed = 0
        self.game_status = False
        pygame.mouse.set_visible(True)
        self.aliens_no = 0
        self.life_list.clear()
        self.lives.empty()
    
    def _check_event_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        if event.key == pygame.K_LEFT:
            self.ship.move_left = False
    
    def check_play_button(self, mouse_pos):
        """Start the game when the player clicks Play"""
        if self.play_button.rect.collidepoint(mouse_pos) and not self.game_status:
            self.game_status = True
            self._create_lives()
            pygame.mouse.set_visible(False)
    
    def _update_bullet(self):
        self.bullets.update()
        for bullet in self.bullets.sprites():
            if bullet.y <= 0:
                bullet.kill()
        self._strike_alien()
    
    def _create_lives(self):
        if self.game_status:
            for i in range(self.stats.ships_left):
                new_life = Life(self)
                new_life.rect.centerx -= (i*40)
                self.lives.add(new_life)
                self.life_list.append(new_life)
                
    def _strike_alien(self):
        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        self.aliens_no = len(self.aliens)

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
        
    def _update_alien(self):
        self.aliens.update()
        self._check_alien_hit()
        
    def _check_alien_hit(self):
        """Check if the ship has been hit by an alien"""
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break
        
    def _ship_hit(self):
        last_life = self.life_list.pop()
        last_life.kill()
        if self.stats.ships_left > 1:
            self.stats.ships_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            self.alien_speed = 0
            self.ship.center_ship()
            sleep(0.5)
        else:
            self._end_game()
    
    def _update_screen(self):
        """manages changes on screen"""
        self.screen.fill(self.bg_colour)
        self.ship.blitship() # make sure that these are in correct order
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for alien in self.aliens.sprites():
            alien.blit()
        for life in self.lives.sprites():
            life.blit()
        if not self.game_status:
            self.play_button.draw_button()
        pygame.display.flip()
        
    def _end_game(self):
        go_img = pygame.image.load(os.path.join("images", "game_over.bmp"))
        go_img = pygame.transform.scale(go_img, (self.settings.screen_width, self.settings.screen_height))
        go_rect = go_img.get_rect()
        for _ in range(700):
            self.screen.blit(go_img, go_rect)
            pygame.display.flip()
        self.reset_game()

if __name__ == "__main__":
    ai = Alien_Invasion()
    ai.run_game()