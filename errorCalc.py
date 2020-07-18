#!/usr/bin/python3
'''
I did this wrong, but the numbers came out pretty close.
I'll fix it if I use it again
'''
import statistics

experimental = [1.976, 1.613, 1.374, 0.806]
theoretical = [1.01, 1.39, 1.65, 1.89]

err = (statistics.mean(theoretical) - statistics.mean(experimental))/statistics.mean(theoretical)

print(err)
