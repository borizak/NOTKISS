import pygame
import random

from NOTKISS.context import Context


class GameLoop:
    
    def __init__(self, _ : Context):
        self._ = _
        pygame.init()

    def run(self):
        self._.audio.play_audio(song_name=self._.settings.audio_DEFAULT_SONG, start_time=0)

        while not self._.logic.game_over:
            self._.interrupts.propagate_keyboard_to_context()
            self._.front.clear()


            # Spawn enemies
            # TODO :  if self._.logic.is_time_to_spawn_enemy():
            if random.randint(*self._.settings.enemy_spawn_RANDOM_SEED) == self._.settings.enemy_spawn_RANDOM_CRITERIA:
                self._.logic.spawn_enemy()

            # Move objects
            self._.logic.move_bullets()
            self._.logic.move_enemies()
            self._.logic.check_collisions()

            # Show objects
            self._.front.draw_player()

            for bullet in self._.logic.bullets:
                self._.front.draw_bullet(bullet)

            for enemy in self._.logic.enemies:
                self._.front.draw_enemy(enemy)

            self._.front.draw_score()

            self._.logic.clock.tick(self._.settings.game_FPS)
        self.quit()

    def quit(self):
        self._.front.draw_game_over()
        # pygame.display.flip()
        self._.front.clear()
        pygame.time.wait(self._.settings.text_game_over_DISPLAY_TIME_MS)
        pygame.quit()