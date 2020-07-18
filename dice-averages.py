#!/usr/bin/python3

'''
this was an  attempt to solve a fivethirtyeight riddler puzzle
involving the probability of a convoluted variant of advantage
and disadvantage from D&D 5e
'''
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

def advantage():
    return [((i**2) - ((i-1)**2))/20**2 for i in range(1, 21)]

def advantage_of_disadvantage():
    return(avg, probList)

def disadvantage_of_advantage():

    return (avg, probList)

def avgRoll(n = 20):
    return (((n+1)/2), [.05 for i in range(1, 21)])

n = 2
x = 1
p = 1/20

fact = (factorial(n)/factorial(n-x))
first = p**x
second = (1-p)**(n-x)
#print(fact, first, second, (fact*first*second))
print(advantage())
