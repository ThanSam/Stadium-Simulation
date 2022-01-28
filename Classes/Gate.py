class Gate:

    def __init__(self, gateID, capacity, trafficZoneID):
        self.gateID = gateID
        self.capacity = capacity
        self.trafficZoneID = trafficZoneID
        self.crowd = 0
