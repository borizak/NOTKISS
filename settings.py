import os.path

import pygame


class Settings:
    def __init__(self):

        # general
        self.paths_ROOT = os.path.join(os.path.dirname(__file__))
        self.game_FPS = 30

        # grid
        self.grid_WIDTH, self.grid_HEIGHT = 80, 80  # cells in the grid
        self.grid_SCALE = 10  # pixels in each grid cell
        self.grid_pixels_WIDTH, self.grid_pixels_HEIGHT = self.grid_WIDTH * self.grid_SCALE , self.grid_HEIGHT * self.grid_SCALE

        # enemies
        self.enemy_SIZE = 40

        self.enemy_spawn_RANDOM_SEED = (1, 20)
        self.enemy_spawn_RANDOM_CRITERIA = 1

        # displayed text
        self.text_score_FONT_SIZE = 30
        self.text_score_LOCATION_ON_SCREEN = (10,10)

        self.text_game_over_FONT_SIZE = 60
        self.text_game_over_DISPLAY_TIME_MS = 3000
        self.text_game_over_LOCATION_ON_SCREEN = (self.grid_pixels_WIDTH // 2 - 150, self.grid_pixels_HEIGHT // 2 - 30)

        # colors
        self.color_WHITE = (255, 255, 255)
        self.color_BLACK = (0, 0, 0)
        self.color_RED = (255, 0, 0)
        self.color_BLUE = (0, 0, 255)

        # audio
        self.audio_ASSET_DIR = os.path.join(self.paths_ROOT, "assets", "audio")
        self.audio_DEFAULT_SONG= "Jedi Mind Tricks Presents_Army Of The Pharaohs - Seven [Official Audio].mp3"



        self.key_FORWARD = pygame.K_w
        self.key_BACKWARD = pygame.K_s
        self.key_LEFT = pygame.K_a
        self.key_RIGHT = pygame.K_d
        self.key_FIRE = pygame.K_SPACE