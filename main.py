import random
import numpy
from Classes import Gate as G, Spectator as Sp, TrafficZone as Tz

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

simTime = 0
endTime = 300  # 5 hours before the match

stadiumCapacity = 25000

count = 0  # number of spectators arriving

while simTime <= endTime:
    simTime += numpy.random.exponential(0.013)
    newSpectator = Sp.Spectator(count, random.randint(1, 6), int(simTime))
    tZone = newSpectator.EnterTheStadium(zones)
    tZone.EnterTheTrafficZone(newSpectator)
    tZone.CheckSpectators(simTime)
    #  ***** tZone.CheckForTheWaitingSpectators()
    print(count, int(simTime), " arrived.")  # The arrival of each spectator
    count += 1
print(count)
