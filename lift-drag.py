#!/usr/bin/python3
'''
used for physics I.
could be used by anyone by replacing p, v, and s with their own
required variables of....I don't remember p, (v)elocity, and
(s)urface area.
'''
def coefficient(actual):
    p = 1.225
    v = 1
    s = 25
    return (2*float(actual))/(p * (v**2) * s)

while True:
    num = input()
    if num == "end":
        break
    print("Coefficient =", coefficient(num))
    print()
