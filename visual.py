import pygame

from NOTKISS.context import Context

class Visual:
    def __init__(self, _ : Context):
        self._ = _
        self.screen = pygame.display.set_mode((self._.settings.grid_pixels_WIDTH, self._.settings.grid_pixels_HEIGHT))
        pygame.display.set_caption("Simple Grid Game")


    def clear(self):
        pygame.display.flip()
        self._.front.screen.fill(self._.settings.color_BLACK)

    def draw_player(self):
        pygame.draw.rect(
            self._.front.screen,
            self._.settings.color_BLUE,
            (self._.logic.player["x"], self._.logic.player["y"], self._.settings.grid_SCALE, self._.settings.grid_SCALE)
        )

    def draw_bullet(self,bullet):
        pygame.draw.rect(
            self._.front.screen,
            self._.settings.color_WHITE,
            (bullet["x"], bullet["y"], self._.settings.grid_SCALE, self._.settings.grid_SCALE)
        )

    def draw_enemy(self,enemy):
        pygame.draw.rect(
            self._.front.screen,
            self._.settings.color_RED,
            (enemy["x"], enemy["y"], self._.settings.enemy_SIZE, self._.settings.enemy_SIZE)
        )

    def draw_game_over(self):
        self._.front.screen.fill(self._.settings.color_BLACK)
        font = pygame.font.SysFont(None, self._.settings.text_game_over_FONT_SIZE)
        game_over_text = font.render("GAME OVER", True, self._.settings.color_RED)
        self._.front.screen.blit(game_over_text, self._.settings.text_game_over_LOCATION_ON_SCREEN)

    def draw_score(self):
        font = pygame.font.SysFont(None, self._.settings.text_score_FONT_SIZE)
        score_text = font.render(f"Score: {self._.logic.score}",
                                 True,
                                 self._.settings.color_WHITE if not self._.flags.hit_detected else self._.settings.color_RED)
        self._.front.screen.blit(score_text, self._.settings.text_score_LOCATION_ON_SCREEN)