import random
from Classes import Server as S, Spectator as Sp, Gate as G


class TrafficZone:

    WaitingSpectators = []

    def __init__(self, ZoneID, gates, crowdNow):

        self.ZoneID = ZoneID
        self.gates = gates
        self.crowdNow = crowdNow
        self.server1 = S.Server(1, self, 5)
        self.server2 = S.Server(2, self, 5)
        self.server3 = S.Server(3, self, 5)
        self.additionalServers = []
        self.serverCount = 3

    def getQueue(self):

        return self.QueueZone

    def CheckSpectators(self, simTime):

        for spec in self.server1.Queue:
            if simTime >= spec.endTime:
                self.server1.Queue.remove(spec)
        for spec in self.server2.Queue:
            if simTime >= spec.endTime:
                self.server2.Queue.remove(spec)
        for spec in self.server3.Queue:
            if simTime >= spec.endTime:
                self.server3.Queue.remove(spec)
        for extraServer in self.additionalServers:
            for spec in extraServer:
                if simTime >= spec.endTime:
                    extraServer.Queue.remove(spec)

    def EnterTheTrafficZone(self, spectator):

        if self.server1.SpectatorService(spectator):
            self.crowdNow += 1

        elif self.server2.SpectatorService(spectator):
            self.crowdNow += 1

        elif self.server3.SpectatorService(spectator):
            self.crowdNow += 1

        elif self.additionalServers:  # not empty
            for server in self.additionalServers:
                server.SpectatorService(spectator)
                self.crowdNow += 1
                break
        else:
            TrafficZone.WaitingSpectators.append(spectator)

    def AddServer(self):

        self.additionalServers.append(S.Server(self.serverCount + 1, self))
        self.serverCount += 1
