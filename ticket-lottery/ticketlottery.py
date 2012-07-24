#!/usr/bin/python

import sys, math
from math import factorial as fac
from decimal import *

def nCr(n, k):
    # binomial coefficient
    if k < 0 or k > n:
        return 0
    if k > n - k: # take advantage of symmetry
        k = n - k
    c = 1
    for i in range(k):
        c = c * (n - (k - (i+1)))
        c = c // (i+1)
    return Decimal(c)

def hyperGeo(goodWays, badWays, totalWinners, numberOfWins):
    if numberOfWins > goodWays:
        return Decimal(0)
    if totalWinners - numberOfWins > badWays:
        return Decimal(0)

    return Decimal(nCr(goodWays, numberOfWins) * nCr(badWays, totalWinners - numberOfWins)) / nCr(goodWays + badWays, totalWinners)

def go(arr):
    players, maxWinners, tickets, group = arr
    minGWinners = int(math.ceil(group/tickets))
    if minGWinners > maxWinners:
        return Decimal(0)

    prob = Decimal(0);
    for i in xrange(minGWinners, min(int(maxWinners),int(group))+1):
        prob += hyperGeo(int(group), int(players - group), int(maxWinners), int(i))
    
    return prob

if __name__ == '__main__':
    for line in sys.stdin:
        print '{0:.10f}'.format(go(map(Decimal, map(int, line.strip().split()))))
