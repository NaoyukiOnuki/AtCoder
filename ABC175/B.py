#import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    N = int(input())
    L = list(map(int, input().split()))

    i1 = 0
    i2 = 1
    i3 = 2

    c = 0
    while i1 < N-2:
        if L[i1] != L[i2] and L[i2] != L[i3] and L[i3] != L[i1] and \
            L[i1]+L[i2] > L[i3] and \
            L[i2]+L[i3] > L[i1] and \
        L[i3]+L[i1] > L[i2]:
            c += 1
        if i3 < N-1:
            i3 += 1
        elif i2 < N-2:
            i2 += 1
            i3 = i2 + 1
        else:
            i1 += 1
            i2 = i1 + 1
            i3 = i2 + 1

    print(c)

main()
