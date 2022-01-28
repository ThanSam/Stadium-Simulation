from Classes import Server as S


class TrafficZone:
    WaitingSpectators = []
    WaitingTimes = []
    crowdNow = 0

    def __init__(self, ZoneID, gates):

        self.ZoneID = ZoneID
        self.gates = gates
        self.server1 = S.Server(1, self)
        self.server2 = S.Server(2, self)
        self.server3 = S.Server(3, self)
        self.additionalServers = []
        self.serverCount = 3

    def getQueue(self):

        return self.QueueZone

    def CheckSpectators(self, simTime):

        for spec in self.server1.Queue:
            if simTime >= spec.endTime:
                self.server1.Queue.remove(spec)
                # print("Spectator with id #", spec.id, "has been served.") #for debugging reasons
                TrafficZone.crowdNow -= 1
        for spec in self.server2.Queue:
            if simTime >= spec.endTime:
                self.server2.Queue.remove(spec)
                # print("Spectator with id #", spec.id, "has been served.")
                TrafficZone.crowdNow -= 1
        for spec in self.server3.Queue:
            if simTime >= spec.endTime:
                self.server3.Queue.remove(spec)
                # print("Spectator with id #", spec.id, "has been served.")
                TrafficZone.crowdNow -= 1
        for extraServer in self.additionalServers:
            for spec in extraServer.Queue:
                if simTime >= spec.endTime:
                    extraServer.Queue.remove(spec)
                    # print("Spectator with id #", spec.id, "has been served.")
                    TrafficZone.crowdNow -= 1

    @staticmethod
    def checkForTheWaiting(zones, gates, simTime):
        for spec in TrafficZone.WaitingSpectators:
            specTrafficZone = spec.EnterTheStadium(zones, gates)
            specTrafficZone.EnterTheTrafficZone(spec, simTime)
            TrafficZone.WaitingSpectators.remove(spec)

            spec.waitingTime = simTime - spec.waitingTime
            TrafficZone.WaitingTimes.append(spec.waitingTime)

    def EnterTheTrafficZone(self, spectator, simTime):

        if self.server1.SpectatorService(spectator, simTime):
            TrafficZone.crowdNow += 1
        elif self.server2.SpectatorService(spectator, simTime):
            TrafficZone.crowdNow += 1
        elif self.server3.SpectatorService(spectator, simTime):
            TrafficZone.crowdNow += 1
        elif self.additionalServers:  # not empty
            for server in self.additionalServers:
                server.SpectatorService(spectator, simTime)
                TrafficZone.crowdNow += 1
                break
        else:
            if TrafficZone.crowdNow > S.Server.serviceLimit:
                self.AddServer()
                self.additionalServers[len(self.additionalServers) - 1].SpectatorService(spectator, simTime)
                TrafficZone.crowdNow += 1
            else:
                TrafficZone.WaitingSpectators.append(spectator)
                spectator.waitingTime = simTime

    def AddServer(self):

        self.additionalServers.append(S.Server(self.serverCount + 1, self))
        self.serverCount += 1
