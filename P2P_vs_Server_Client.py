#!/usr/bin/python3

'''
20 Gbit file to N peers with downrate 5 Mbps u uprate:
    N = 10, u = 300 Kbps
    N = 100, u = 800Kbps
    N = 1000, u = 3Mbps

    Server uprate = 50Mbps
'''
def downtime(N, u, P2P = True):
    F = 2*(10**10)
    Su = 5*(10**7)
    Pd = 5*(10**6)
    peerMin = F/Pd
    if P2P:
        servMin = F/Su
        p2pMin = (N*F)
        p2pMinDenom = Su
        for i in range(N - 1):
            p2pMinDenom += u
        p2pMin = p2pMin/p2pMinDenom
        return max(servMin, peerMin, p2pMin)
    else:
        servMin = (N*F)/Su
        return max(servMin, peerMin)

print("Downtimes based on a 20 Gigabit file, Server upspeed of 50 Mbps, client downspeed of 5 Mbps, and client upspeed increasing with number of clients.")

print()
print("Downtimes for P2P distribution:")
print("10 clients:", downtime(10, 3*(10**5)), "seconds.")
print("100 Clients:", downtime(100, 8*(10**5)), "seconds.")
print("1000 Clients:", downtime(1000, 3*(10**6)), "seconds." )

print()
print("Downtimes for Server-Client distribution:")
print("10 clients:", downtime(10, 3*(10**5), False), "seconds.")
print("100 clients:", downtime(100, 8*(10**5), False), "seconds.")
print("1000 clients:", downtime(1000, 3*(10**6), False), "seconds.")
