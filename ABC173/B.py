#import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    N = int(input())
    AC, WA, TLE, RE = 0,0,0,0
    for _ in range(N):
        i = input()
        if i == 'AC':
            AC += 1
        elif i == 'WA':
            WA += 1
        elif i == 'TLE':
            TLE += 1
        elif i == 'RE':
            RE += 1
    
    print('AC x ' + str(AC))
    print('WA x ' + str(WA))
    print('TLE x ' + str(TLE))
    print('RE x ' + str(RE))

main()
