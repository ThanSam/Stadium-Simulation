class TrafficZone:

    def __init__(self, gates, crowdNow, queue):
        self.gates = gates
        self.crowdNow = crowdNow
        self.queue = queue

    def addSpectator(self):
        self.crowdNow += 1