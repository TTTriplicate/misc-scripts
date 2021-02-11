#!/usr/bin/python3

def factorial (n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

P = 0.0
p = 0.1
N = 35
n = 10
'''
for i in range(n, N+1):
    C = (factorial(N)/(factorial(i) * factorial(N-i)))

    rightHalf = p**i * (1 - p)**(N-i)

    P += C * rightHalf

print(P, ": probability of 12 or more users transmitting any any given time.")
P = 0.0
#decided to try it both possible ways to verify results
#came out the same, so I think I did it right
'''
for i in range(n):
    C = (factorial(N)/(factorial(i) * factorial(N-i)))

    rightHalf = p**i * (1 - p)**(N-i)

    P += C * rightHalf
print(1-P, ": probability of", n, "or more users transmitting any any given time.")
P = 0.0
for i in range(1,4):
    C = (factorial(N)/(factorial(i) * factorial(N-i)))

    rightHalf = p**i * (1 - p)**(N-i)

    P += C * rightHalf

print(P, ": probability of fewer than 4 users transmitting at a given time.") 
