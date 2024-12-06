class Context:
    def __init__(self):
        from game_loop import GameLoop
        from settings import Settings
        from logic import Logic
        from visual import Visual
        from flags import Flags
        from audio import Audio
        from interrupts import Interrupts
        from threads import Threads

        from lib_wrap import PyGameWrap
        from video import Video

        self.lib = PyGameWrap() # an api to whatever game library lies underneath, for all the other modules to use
        self.settings   = Settings() # adjustable values
        self.flags = Flags() # booleans with variable life spans
        self.threads = Threads() # managed thread pool

        self.game_loop  = GameLoop(self)    # main loop
        self.logic      = Logic(self)       # game logic
        self.front       = Visual(self)     # ui
        self.audio      = Audio(self)       # sound control
        self.video      = Video(self)       # video control
        self.interrupts = Interrupts(self)  # managed io interrupts
