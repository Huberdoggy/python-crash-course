import sys
import pygame
from settings import Settings
from ship import Ship
from character import Character

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
        self.character = Character(self)


    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Helper methods use the '_' prefix. Differences - they are not meant to be called through and instance
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.character.blitme()


        pygame.display.flip()

# If file is directly called, make an instance of AlienInvasion class and run the main loop

if __name__ == '__main__':
        ai = AlienInvasion()
        ai.run_game()
