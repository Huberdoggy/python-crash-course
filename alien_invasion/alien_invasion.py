import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from character import Character


class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize the game, create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        # Note, argument for screen size is a tuple, therefore,
        # nest the dimensions inside the parentheses for the method call
        pygame.display.set_caption("Kyle's Alien Invasion")
        self.ship = Ship(
            self
        )  # Remember, requires 1 argument in the Ship module - (ai_game) to inherit the screen resources, etc
        # When imported here, this corresponds to an instance of 'AlienInvasion' which we're passing to it
        self.bullets = (
            pygame.sprite.Group()
        )  # manage bullets that have already been fired using this built-in
        self.character = Character(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Helper methods use the '_' prefix. Differences - they are not meant to be called through and instance
            self._check_events()
            # After check_events, update the position of ship each pass based on identified key events...
            self.ship.update()
            # And redraw the screen accordingly
            self._update_bullets()
            self._update_screen()

    def _update_bullets(self):
        """Update the pos of bullets and get rid of old bullets"""
        self.bullets.update()  # will update each bullet in the sprite Group
        # Get rid of bullets that have disappeared off screen
        # Python expects a list will stay the same while a loop is running, so we need to make a copy to modify,
        # bullets inside the loop
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            # print(len(self.bullets)) Only needed to test that they ARE being removed from memory

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right based on the bool in 'ship'
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        # Opposite. set the flags false
        # Here, we can use 'elif' because each event is only connected to 1 key
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.character.blitme()

        pygame.display.flip()


# If file is directly called, make an instance of AlienInvasion class and run the main loop

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
