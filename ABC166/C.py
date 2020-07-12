#import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    N,M = map(int, input().split())
    H = list(map(int, input().split()))
    edges = []
    for i in range(M):
        A,B = map(int, input().split())
        edges += (A,B),
    
    good = [True]*N
    for A,B in edges:
        if H[A-1] > H[B-1]:
            good[B-1] = False
        elif H[A-1] < H[B-1]:
            good[A-1] = False
        else:
            good[A-1] = False
            good[B-1] = False
    print(len(list(filter(lambda b: b, good))))

main()
