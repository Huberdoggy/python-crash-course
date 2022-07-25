import pygame


class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Init the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship .BMP and get its rect
        self.image = pygame.image.load("images/alienblaster.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag. Using 'if' instead of 'elif' in case the player
        holds both keys at the same time, resulting in the ship standing in place, otherwise
        'right' would take priority here"""
        # Update the ship's x value, not the rect (to keep the float portion of our 1.5x speed)
        if (
            self.moving_right and self.rect.right < self.screen_rect.right
        ):  # the ship hasn't reached right edge of scr
            self.x += self.settings.ship_speed
        if (
            self.moving_left and self.rect.left > 0
        ):  # the ship hasn't reached left edge of screen
            self.x -= self.settings.ship_speed

        # Update rect object from self.x - only the int portion will be stored here for displaying the ship,
        # but that's okay
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
