class TrafficZone:

    server1 = []
    server2 = []
    server3 = []
    WaitingSpectators = []

    def __init__(self, ZoneID, gates, crowdNow):
        self.ZoneID = ZoneID
        self.gates = gates
        self.crowdNow = crowdNow

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

