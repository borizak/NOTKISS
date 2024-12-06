import sys
import pygame

from NOTKISS.context import Context


class Interrupts:

    def __init__(self, _ : Context):
        self._ = _
    def propagate_keyboard_to_context(self):

        def propagate_keyboard_to_context_THREAD_():
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] and self._.logic.player["x"] > 0:
                self._.logic.player["x"] -= self._.settings.grid_SCALE
            if keys[pygame.K_d] and self._.logic.player["x"] < self._.settings.grid_pixels_WIDTH - self._.settings.grid_SCALE:
                self._.logic.player["x"] += self._.settings.grid_SCALE
            if keys[pygame.K_w] and self._.logic.player["y"] > 0:
                self._.logic.player["y"] -= self._.settings.grid_SCALE
            if keys[pygame.K_s] and self._.logic.player["y"] < self._.settings.grid_pixels_HEIGHT - self._.settings.grid_SCALE:
                self._.logic.player["y"] += self._.settings.grid_SCALE

            # Shooting bullets
            if keys[pygame.K_SPACE]:
                if not any(
                        bullet["y"] == self._.logic.player["y"] - self._.settings.grid_SCALE
                        and
                        bullet["x"] == self._.logic.player["x"]
                        for bullet in self._.logic.bullets):
                    self._.logic.bullets.append(
                        {"x": self._.logic.player["x"],
                         "y": self._.logic.player["y"] - self._.settings.grid_SCALE
                        }
                    )

        self._.threads.spawn(propagate_keyboard_to_context_THREAD_)

