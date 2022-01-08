import random
import numpy
import Gate as G
import Spectator as Sp
import Stadium as S
import TrafficZone as Tz

Gate1 = G.Gate("G1", 4000, "Z1", 0)
Gate2 = G.Gate("G2", 2000, "Z1", 0)
Gate3 = G.Gate("G3", 4000, "Z2", 0)
Gate4 = G.Gate("G4", 7000, "Z2", 0)
Gate5 = G.Gate("G5", 3000, "Z3", 0)
Gate6 = G.Gate("G6", 5000, "Z3", 0)

gates = [Gate1, Gate2, Gate3, Gate4, Gate5, Gate6]

QueueZone1 = []
QueueZone2 = []
QueueZone3 = []

Zone1 = Tz.TrafficZone([Gate1, Gate2], 0, QueueZone1)
Zone2 = Tz.TrafficZone([Gate3, Gate4], 0, QueueZone2)
Zone3 = Tz.TrafficZone([Gate5, Gate6], 0, QueueZone1)

zones = [Zone1, Zone2, Zone3]

startTime = simTime = 0
endTime = 300  # 5 hours before the match
stadiumCapacity = 25000
spectators = []
stadium = S.Stadium(stadiumCapacity, zones, gates)

count = 0
while simTime <= endTime:
    simTime += numpy.random.exponential(0.013)
    newSpectator = Sp.Spectator(count, random.randint(1, 6), simTime)
    count += 1
    # print(newSpectator.id, newSpectator.gate, newSpectator.arrival)
print(count)
