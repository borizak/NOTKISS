class _Flag:
    def __init__(self):
        self._frames_left = 0

    def set(self, life_span_in_frames :  int = 1):
        self._frames_left = life_span_in_frames

    def is_up(self):
        return self._frames_left > 0

    def tick(self):
        self._frames_left -= self._frames_left and 1 # decrease 1 only when any left to decrease


class Flags:
    def __init__(self):

        # general
        self.player_lost = _Flag()
        self.player_won = _Flag()
        # enemy hit
        self.hit_detected = _Flag()
        self.combo_detected = _Flag()

        # audio
        self.music_started = _Flag()
        self.music_stopped = _Flag()

        self._all : list[_Flag] = list(self.__dict__.values())


    def tick(self):
        for flag in self._all:
            flag.tick()

    def ups(self):
        return [_ for _ in self._all if _.is_up()]
