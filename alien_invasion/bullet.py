import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect from scratch (not based on a stored img) at (0, 0) and then set correct pos
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop # associate the bullet with the pos of ship's midtop

        # Store the bullet's pos as a decimal value (y axis for it's travel direction)
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        # Update the dec pos of the bullet...will move toward screen top, hence the subtraction below..
        self.y -= self.settings.bullet_speed
        # Update the rect pos. Similar to how we did with 'ship'
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect) # Fill the screen portion defined by bullet's rect with,
        # color stored in 'settings'

