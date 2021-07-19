import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize the game, create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))  # Note, argument for screen size is a tuple, therefore,
        # nest the dimensions inside the parentheses for the method call
        pygame.display.set_caption("Kyle's Alien Invasion")
        self.ship = Ship(self) # Remember, requires 1 argument in the Ship module - (ai_game) to inherit the screen resources, etc
        # When imported here, this corresponds to an instance of 'AlienInvasion' which we're passing to it

        # Set the B/G color as an RGB value...
        # self.bg_color = (0, 128, 255)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Redraw the screen during each pass through the loop, using my defined B/G color
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Make the most recently drawn screen visible
            pygame.display.flip()

# If file is directly called, make an instance of AlienInvasion class and run the main loop
if __name__ == '__main__':
        ai = AlienInvasion()
        ai.run_game()
