class Settings:
    """stores the setting of the game"""

    def __init__(self):
        self.screen_width = 1300
        self.screen_height = 650
        self.bg_color = (0, 0, 0)

        # ship setting
        self.ship_limit = 3

        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3

        # Alien setting
        self.fleet_drop_speed = 12.2

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.is_mute = -1

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.2

        # fleet _direction -> 1 : right , -1 : left .
        self.fleet_direction = 1

        # scoring
        self.alien_points = 50


    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)