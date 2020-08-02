#import numpy as np
import math
#from decimal import *
#from numba import njit

#@njit
def main():
    N,D = map(int, input().split())
    count = 0
    D2 = D*D
    for _ in range(N):
        X,Y = map(int, input().split())
        if X*X+Y*Y <= D2:
            count += 1
    print(count)
main()
