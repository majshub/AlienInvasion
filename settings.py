class Settings:
    """stores the setting of the game"""

    def __init__(self):
        self.screen_width = 1300
        self.screen_height = 650
        self.bg_color = (230, 230, 230)

        # ship setting
        self.ship_speed = 1.5
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien setting
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet _direction -> 1 : right , -1 : left .
        self.fleet_direction = 1
