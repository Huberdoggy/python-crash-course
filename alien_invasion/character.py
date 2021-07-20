import pygame

class Character:
    """A class to manage my .BMP guy"""

    def __init__(self, ai_game):
        """Init the character and set his starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the character .BMP and get its rect
        self.image = pygame.image.load('images/doomguy_green2_large.png')
        self.rect = self.image.get_rect()

        # Start the new character at the bottom left each time screen is redrawn
        self.rect.bottomleft = self.screen_rect.midbottom

    def blitme(self):
        """Draw the man at his current location"""
        self.screen.blit(self.image, self.rect)
