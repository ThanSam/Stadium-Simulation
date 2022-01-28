import numpy


class Server:

    serviceLimit = 8

    def __init__(self, ServerID, Zone):
        self.ServerID = ServerID
        self.Zone = Zone
        self.Queue = []

    def SpectatorService(self, spectator, simTime):
        if len(self.Queue) < Server.serviceLimit:
            self.Queue.append(spectator)
            spectator.endTime = simTime + numpy.random.randint(1, 4, 1, int)[0]
            return True
        else:
            return False
