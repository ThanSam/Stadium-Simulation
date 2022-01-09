import time
import random


class Server:

    def __init__(self, ServerID, Zone):
        self.ServerID = ServerID
        self.Zone = Zone
        self.Queue = []

    def SpectatorService(self, spectator):
        if len(self.Queue) < 3:
            self.Queue.append(spectator)
            time.sleep(random.randint(2, 4))
            self.Queue.remove(spectator)
            spectator.served = True
        return spectator.served
