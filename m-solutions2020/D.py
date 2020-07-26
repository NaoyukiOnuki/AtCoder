#import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    N = int(input())
    A = list(map(int, input().split()))

    amount = 1000
    kabu = 0
    for i in range(N):
        if i >= N-1:
            amount += kabu * A[i]
            kabu = 0
        else:
            if A[i] < A[i+1]:
                kabu += amount//A[i]
                amount %= A[i]
            elif A[i] > A[i+1]:
                amount += kabu * A[i]
                kabu = 0

    print(amount)
main()
