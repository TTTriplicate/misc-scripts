#!/usr/bin/python3

import statistics

experimental = [1.976, 1.613, 1.374, 0.806]
theoretical = [1.01, 1.39, 1.65, 1.89]

err = (statistics.mean(theoretical) - statistics.mean(experimental))/statistics.mean(theoretical)

print(err)
