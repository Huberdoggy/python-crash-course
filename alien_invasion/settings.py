class Settings:
    """A class to store all settings for Kyle's Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen stuff..
        self.screen_width = 1280
        self.screen_height = 1024
        self.bg_color = (255, 255, 204)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (232, 70, 49)
        self.bullets_allowed = 5