import random
import numpy
import Gate as G
import Spectator as Sp
import Stadium as S
import TrafficZone as Tz

Gate1 = G.Gate("G1", 4000, 1, 0)
Gate2 = G.Gate("G2", 2000, 1, 0)
Gate3 = G.Gate("G3", 4000, 2, 0)
Gate4 = G.Gate("G4", 7000, 2, 0)
Gate5 = G.Gate("G5", 3000, 3, 0)
Gate6 = G.Gate("G6", 5000, 3, 0)

gates = [Gate1, Gate2, Gate3, Gate4, Gate5, Gate6]

Zone1 = Tz.TrafficZone(1, [Gate1, Gate2], 0)
Zone2 = Tz.TrafficZone(2, [Gate3, Gate4], 0)
Zone3 = Tz.TrafficZone(3, [Gate5, Gate6], 0)

zones = [Zone1, Zone2, Zone3]

startTime = simTime = 0
endTime = 300  # 5 hours before the match
stadiumCapacity = 25000
stadium = S.Stadium(stadiumCapacity, zones, gates)

count = 0  # number of spectators arriving

while simTime <= endTime:
    simTime += numpy.random.exponential(0.013)
    newSpectator = Sp.Spectator(count, random.randint(1, 6), simTime)
    tZone = newSpectator.EnterTheStadium(zones)
    tZone.EnterTheTrafficZone(newSpectator)
    print()
    count += 1
print(count)
