#import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    K = int(input())

    rest = [False]*K
    a = 7
    count = 1
    while a < K:
        a = 10*a+7
        count += 1
    r = a % K
    while r != 0:
        if rest[r-1]:
            print(-1)
            return
        else:
            rest[r-1] = True
            a = 10*r+7
            count += 1
            r = a % K
    print(count)
    
main()
