import typing
from threading import Thread


from context import Context

class Threads:

    def __init__(self):
        self.all : dict[str ,Thread] = {}

    def purge(self):

        while len(self.all):
            for thread_id, thread in self.all.items():
                try:
                    thread.join()
                    self.all.__delitem__(thread_id)
                except Exception as e:
                    print(f"THREADS PURGE PROCESS ENCOUNTERED ERROR {e}:{e.args} WHILE ATTEMPTING TO KILL THREAD {thread_id}:{thread}. WILL RETRY. ")


    def spawn(self, target : typing.Callable) -> str:
        thread = Thread(target=target, daemon=True)
        try:
            thread.start()
        except Exception as e:
            print(f"EXCEPTION {e}:{e.args} WHEN STARTING THREAD FROM [{target=}]")
            return ""

        thread_id = str(thread)
        self.all[thread_id] = thread
        return thread_id

    def kill(self, thread_id : str) -> tuple[bool,typing.Union[Exception, None]]:
        thread = self.all.get(thread_id, None)
        success = False
        error = None

        if thread:
            try:
                thread.join()
                success = True
            except Exception as e:
                print(f"FAILED TO KILL THREAD {thread}, DUE TO ERROR : {e}:{e.args}")
                error = e

        return success, error


    def is_alive(self, thread_id : str):
        thread = self.all.get(thread_id)
        return False if not thread else thread.is_alive()

