import Server


class TrafficZone:

    WaitingSpectators = []

    def __init__(self, ZoneID, gates, crowdNow):
        self.ZoneID = ZoneID
        self.gates = gates
        self.crowdNow = crowdNow
        server1 = Server(1, self)
        server2 = Server(2, self)
        server3 = Server(3, self)

    def getQueue(self):
        return self.QueueZone

    def EnterTheTrafficZone(self, spectator):

        if len(self.server1) < 3:
            self.server1.append(spectator)
        elif len(self.server2) < 3:
            self.server2.append(spectator)
        elif len(self.server3) < 3:
            self.server3.append(spectator)
        else:
            self.WaitingSpectators.append(spectator)

