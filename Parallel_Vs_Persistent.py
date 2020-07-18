#!/usr/bin/python3

'''
Written for a networking class.  With a list of given info,
the goal was to compare whether a persistent TCP connection
or a series of parallel TCP connection would result in a 
faster download.

connection speed 150 bps
connection length 10 m
100000 Kbits page
10 100000 Kbits objects
ACK/TCP packets 200 bits
N connections get 1/N bandwidth each
Dprop 10/2.8*(10**8) negligible
'''
def requestTime(connections = 1):
    speed = 150/connections
    return (200/speed)#oneway for request and ACK

def objectTime(numObjects, parallel):
    size = 100000
    if parallel:
        return size/(150/numObjects)
    else:
        return (size * numObjects)/150



def totalTime(parallel = True):
    totalTime = 0
    if parallel:
        totalTime += 3 * requestTime()#page connect, ACK, get
        totalTime += 3 * requestTime(10)#10 object connect, ACK, get
        totalTime += objectTime(1, False)#HTML page
        totalTime += objectTime(10, True)#page objects
    else:
        totalTime += 13 * requestTime()#connect, ack, gets
        totalTime += objectTime(11, False)#Page and objects sequentially
    return totalTime


print("Times for 100000 bit page with 10 objects of same size.")
print()
print("Parallel:", totalTime())
print()
print("Persistent:", totalTime(False))
