class Spectator:

    def __init__(self, id, gate, arrival):
        self.id = id
        self.gate = gate
        self.arrival = arrival
        self.trafficZone = 0
        self.served = False
        self.endTime = 0
        self.waitingTime = 0

    def EnterTheStadium(self, zones, gates):

        if self.gate.crowd >= self.gate.capacity:
            if not self.gate.gateID == 6:
                self.gate = gates[self.gate.gateID]  # Redirecting the spectator to the next gate.
            else:
                self.gate = gates[0]
            self.EnterTheStadium(zones, gates)
        else:
            self.gate.crowd += 1

        if self.gate.gateID == 1 or self.gate.gateID == 2:  # Crossing the right traffic zone.
            self.trafficZone = zones[0]
        elif self.gate.gateID == 3 or self.gate.gateID == 4:
            self.trafficZone = zones[1]
        else:
            self.trafficZone = zones[2]

        return self.trafficZone
