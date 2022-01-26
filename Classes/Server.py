import random


class Server:

    def __init__(self, ServerID, Zone, limit):
        self.ServerID = ServerID
        self.Zone = Zone
        self.Queue = []
        self.serviceLimit = limit

    def SpectatorService(self, spectator):
        if len(self.Queue) < self.serviceLimit:
            self.Queue.append(spectator)
            spectator.endTime = spectator.arrival + random.randint(1, 3)
            return True
        else:
            return False
