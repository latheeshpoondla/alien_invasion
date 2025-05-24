class Settings:
    """settings for Alien Invasion"""

    def __init__(self):
        self.win_screen_width = 1200
        self.win_screen_height = 800
        self.screen_width = 1200
        self.screen_height = 800
        self.bgcolor = (25, 20, 30)
        self.ship_speed = 1
        self.bullet_speed = 2
        self.bullet_color = (255, 255, 255)
        self.alien_width = self.screen_width//24
        self.alien_height = self.screen_width//24
        self.ship_limit = 3