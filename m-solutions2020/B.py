#import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    A,B,C = map(int, input().split())
    K=int(input())

    while K > 0:
        if B <= A:
            B = B*2
        elif C <= B:
            C = C*2
        K -= 1

    if A < B and B < C:
        print('Yes')
    else:
        print('No')
main()
