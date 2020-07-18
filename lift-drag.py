#!/usr/bin/python3

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
