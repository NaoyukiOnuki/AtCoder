import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    N,K = map(int, input().split())
    A = np.array(list(map(int, input().split())))
    for b in (A[:N-K] < A[K:]):
        print('Yes' if b else 'No')
main()
