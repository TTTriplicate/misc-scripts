#!/usr/bin/python3
'''
Written for a networking class.  With a couple of givens, calculate
the estimated RTT and timeout interval i accordance with the guide-
lines laid out in RFC 6298.

Could be quickly modified to take any values or samples,
or manually altered to different givens.
'''
def updateEst(currEst,currDev, sample):
    alpha = .1
    beta = .25
    newEst = ((1-alpha)*currEst) + (alpha*sample)
    newDev = ((1 - beta)*currDev) + beta * abs(sample - newEst)

    return (newEst, newDev)

def timeout(estRTT, devRTT):
    return estRTT + (4 * devRTT)
estRTT = 0
devRTT = 0

samples = [22.78, 28.64, 10.28, 12.45, 19.04, 18.74]#insert sample times here

estRTT = samples[0]
devRTT = ((.75)*devRTT) + .25 * abs(samples[0] - estRTT)

print("Starting estimated RTT is", samples[0])
print("Timeout interval is", timeout(estRTT, devRTT))
for i in range(1, len(samples)):
   estRTT, devRTT = updateEst(estRTT, devRTT, samples[i])
   print("Estimated RTT after sample", i, "is", estRTT)
   print("Timeout Interval is now", timeout(estRTT, devRTT))
