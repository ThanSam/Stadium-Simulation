import random
from Classes import Server as S, Spectator as Sp


class TrafficZone:

    def __init__(self, ZoneID, gates, crowdNow):
        self.ZoneID = ZoneID
        self.gates = gates
        self.crowdNow = crowdNow
        self.WaitingSpectators = []
        self.server1 = S.Server(1, self)
        self.server2 = S.Server(2, self)
        self.server3 = S.Server(3, self)

    def getQueue(self):
        return self.QueueZone

    def CheckSpectators(self, simTime):
        for spec in self.server1.getQueue():
            if simTime >= spec.endTime:
                self.server1.getQueue().remove(spec)
        for spec in self.server2.getQueue():
            if simTime >= spec.endTime:
                self.server2.getQueue().remove(spec)
        for spec in self.server3.getQueue():
            if simTime >= spec.endTime:
                self.server3.getQueue().remove(spec)

    def CheckForTheWaitingSpectators(self):
        for spec in self.WaitingSpectators:
            self.EnterTheTrafficZone(spec)

    def EnterTheTrafficZone(self, spectator):

        if len(self.server1.getQueue()) < 3:
            self.server1.SpectatorService(spectator)
            spectator.endTime = spectator.arrival + random.randint(1, 3)
        elif len(self.server2.getQueue()) < 3:
            self.server2.SpectatorService(spectator)
            spectator.endTime = spectator.arrival + random.randint(1, 3)
        elif len(self.server3.getQueue()) < 3:
            self.server3.SpectatorService(spectator)
            spectator.endTime = spectator.arrival + random.randint(1, 3)
        else:
            self.WaitingSpectators.append(spectator)
