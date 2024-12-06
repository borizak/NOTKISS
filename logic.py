import pygame
import random

from NOTKISS.context import Context

class Logic:
    def __init__(self, _ : Context):
        self._ = _

        self.player = {"x": self._.settings.grid_pixels_WIDTH // 2,
                       "y": self._.settings.grid_pixels_HEIGHT - self._.settings.grid_SCALE}
        self.bullets = []
        self.enemies = []
        self.score = 0
        self.game_over = False
        self.clock = pygame.time.Clock()


    def spawn_enemy(self):

        x = (random.randint(0,
                            (self._.settings.grid_pixels_WIDTH // self._.settings.grid_SCALE) -
                            (self._.settings.enemy_SIZE // self._.settings.grid_SCALE)) *
             self._.settings.grid_SCALE
             )
        #TODO: y = (random.randint(0,
        #                (self._.settings.grid_pixels_WIDTH // self._.settings.GRID_SIZE) -
        #                (self._.settings.ENEMY_SIZE // self._.settings.GRID_SIZE)) *
        #                self._.settings.GRID_SIZE
        # )
        y = 0
        self.enemies.append({"x": x, "y": y})

    def move_bullets(self):
        for bullet in self.bullets:
            bullet["y"] -= self._.settings.grid_SCALE
            if bullet["y"] < 0:
                self.bullets.remove(bullet)

    def move_enemies(self):
        for enemy in self.enemies[:]:
            enemy["y"] += self._.settings.grid_SCALE
            if enemy["y"] >= self._.settings.grid_pixels_HEIGHT:
                self.enemies.remove(enemy)
            if (
                self.player["x"] < enemy["x"] + self._.settings.enemy_SIZE
                and self.player["x"] + self._.settings.grid_SCALE > enemy["x"]
                and self.player["y"] < enemy["y"] + self._.settings.enemy_SIZE
                and self.player["y"] + self._.settings.grid_SCALE > enemy["y"]
            ):
                self.game_over = True

    def check_collisions(self):
        for bullet in self.bullets[:]:
            for enemy in self.enemies[:]:
                if (
                    bullet["x"] >= enemy["x"]
                    and bullet["x"] < enemy["x"] + self._.settings.enemy_SIZE
                    and bullet["y"] >= enemy["y"]
                    and bullet["y"] < enemy["y"] + self._.settings.enemy_SIZE
                ):
                    self.bullets.remove(bullet)
                    self.enemies.remove(enemy)
                    self.score += 1
                    self._.flags.hit_detected = True
                    break