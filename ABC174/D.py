#import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    N = int(input())
    C = input()
    l = 0
    r = N-1
    count = 0
    while l < N and C[l] == 'R':
        l += 1
    while 0 <= r and C[r] == 'W':
        r -= 1
    while l < r:
        C = C[:l] + C[r] + C[l+1:r] + C[l] + C[r+1:]
        count += 1
        while l < N and C[l] == 'R':
            l += 1
        while 0 <= r and C[r] == 'W':
            r -= 1

    print(count)
    

main()
