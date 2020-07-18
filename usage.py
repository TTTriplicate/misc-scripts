#!/usr/bin/python3
'''
Written for networking class.  With some given values,
calculates  the percent-utilization by a stop-and-wait 
protocol, and the window size in packets required to 
reach 98% utilization during a pipelined transfer.
'''

def maxWindow(RTT, dtrans):
    '''
gives the window for 100% utilization to start
a binary search.
(N * dtrans)/(RTT + dtrans) = 1
(N * dtrans) = (RTT + dtrans)
N = (RTT + dtrans) * (1/dtrans)
N = (RTT/dtrans + 1)
Want a whole number, so use integer division
    '''
    return (1 + (RTT//dtrans))

def window(RTT, dtrans):
    '''
finds window size to result in 98% utilization
by establishing a binary search window and executing
    '''
    percent = .00001
    low = 1
    high = maxWindow(RTT, dtrans)

    while True:
        window = (high + low)//2
        #print(window)
        percent = ((window * dtrans)/(dtrans + RTT))
        if percent < .98:
            low = window
        elif percent > .9801:
            high = window
        else:
            print(percent)
            return window


def pipelineDiff():
    '''
calculates the utilization of stop and wait
then makes a tuple of that and the window size 
for 98% utilization
    '''
    dprop = (2*(10**8))/(10000 * 1000)
    rate = 1000000000
    packetSize = 1000 * 8
    dtrans = packetSize/rate

    stopWait = dtrans/((2 * dprop) + dtrans)

    
    return (stopWait, window((2 * dprop), dtrans))


print(pipelineDiff())
