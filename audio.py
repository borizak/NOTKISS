import os.path
import threading

import pygame
from context import Context
class Audio:
    def __init__(self, _ : Context):
        self._ = _
        pygame.mixer.init()

    def play_audio(self,  song_name : str, start_time : int):
        song_name = song_name or self._.settings.audio_DEFAULT_SONG
        file_path = os.path.join(self._.settings.audio_ASSET_DIR, song_name)
        def play_audio_THREAD_():
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play(start=start_time)
            print(f"Playing {song_name} from {start_time} seconds")
            self._.flags.music_started = True
            while pygame.mixer.music.get_busy():
                continue
            self._.flags.music_stopped = True

        self._.threads.spawn(play_audio_THREAD_)




    @staticmethod
    def get_current_playback_position() -> int:
        if pygame.mixer.music.get_busy():
            return pygame.mixer.music.get_pos() // 1000
        return -1
