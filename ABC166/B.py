#import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    N,K = map(int, input().split())
    having = [False]*(N)
    for _ in range(K):
        d = int(input())
        for a in map(int, input().split()):
            having[a-1] = True

    print(len(list(filter(lambda b: not b, having))))

main()
