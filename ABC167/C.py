import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    (N, M, X) = map(int, input().split())
    A = np.zeros((N,M+1), dtype='int32')
    for i in range(N):
        A[i] = list(map(int, input().split()))
    
    A = A[np.argsort(A[:,0])]

    i = 0
    m = -1
    while i < 2**N:
        i += 1
        c = 0
        sum = np.zeros(M, dtype='int32')
        for j in range(N):
            if i & 2**j == 2**j:
                c += A[j][0]
                sum += A[j][1:]
        if np.all(sum >= X):
            m = c if m < 0 else min(m, c)
    
    print(m)
main()
