import numpy
import random

from Classes import Gate as G, Spectator as Sp, TrafficZone as Tz

Gate1 = G.Gate(1, 4000, 1)
Gate2 = G.Gate(2, 2000, 2)
Gate3 = G.Gate(3, 4000, 3)
Gate4 = G.Gate(4, 7000, 4)
Gate5 = G.Gate(5, 3000, 5)
Gate6 = G.Gate(6, 5000, 6)

gates = [Gate1, Gate2, Gate3, Gate4, Gate5, Gate6]

Zone1 = Tz.TrafficZone(1, [Gate1, Gate2])
Zone2 = Tz.TrafficZone(2, [Gate3, Gate4])
Zone3 = Tz.TrafficZone(3, [Gate5, Gate6])

zones = [Zone1, Zone2, Zone3]

simTime = 0
endTime = 360  # 6 hours before the match starts, spectators can enter the stadium

stadiumCapacity = 20000

count = 0  # number of spectators arriving

print("\n------------- Arrivals -------------\n")

while simTime <= endTime and count < stadiumCapacity:
    simTime += numpy.random.exponential(0.018)  # = endTime/StadiumCapacity
    newSpectator = Sp.Spectator(count, gates[random.randint(0, 5)], int(simTime))
    tZone = newSpectator.EnterTheStadium(zones, gates)
    tZone.EnterTheTrafficZone(newSpectator, int(simTime))
    tZone.CheckSpectators(simTime)
    Tz.TrafficZone.checkForTheWaiting(zones, gates, simTime)
    print("Spectator with id #", count, "arrived in time:", int(simTime))  # The arrival of each spectator
    count += 1

print("\nTotal spectators arrived: ", count)
print("\nSpectators who couldn't be served: ", Tz.TrafficZone.crowdNow)

print("\nZone's 1 servers:", Zone1.serverCount)
print("Zone's 2 servers:", Zone2.serverCount)
print("Zone's 3 servers:", Zone3.serverCount)
print("\nExtra servers:", len(Zone1.additionalServers) + len(Zone2.additionalServers) + len(Zone3.additionalServers))


print("\nSpectators in Gate 1:", Gate1.crowd)
print("Spectators in Gate 2:", Gate2.crowd)
print("Spectators in Gate 3:", Gate3.crowd)
print("Spectators in Gate 4:", Gate4.crowd)
print("Spectators in Gate 5:", Gate5.crowd)
print("Spectators in Gate 6:", Gate6.crowd)
