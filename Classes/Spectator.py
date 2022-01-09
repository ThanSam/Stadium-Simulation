class Spectator:

    def __init__(self, id, gate, arrival):
        self.id = id
        self.gate = gate
        self.arrival = arrival
        self.trafficZone = 0
        self.served = False

    def EnterTheStadium(self, zones):
        if self.gate == 1 or self.gate == 2:
            self.trafficZone = zones[0]
        elif self.gate == 3 or self.gate == 4:
            self.trafficZone = zones[1]
        else:
            self.trafficZone = zones[2]
        return self.trafficZone
