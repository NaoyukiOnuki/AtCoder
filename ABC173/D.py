#import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    s = 0
    for i in range(1,N):
        s += A[i//2]
    print(s)

main()
