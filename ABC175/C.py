#import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    X,K,D = map(int, input().split())

    X = abs(X)
    if X//D > K:
        print(X-K*D)
        return
    
    K -= X//D
    X %= D

    if K%2 == 0:
        print(X)
    else:
        print(abs(X-D))

main()
