#import numpy as np
import math
#from decimal import *
#from numba import njit

#@njit
def main():
    N,K = map(int, input().split())
    A = list(map(int, input().split()))

    def check(x):
        if x <= 0:
            return False
        else:
            return N+K >= sum(map(lambda a: math.ceil(a/x), A))

    s = max(A)//2
    h = s//2
    c = check(s)
    last = c
    while True:
        if c:
            s -= max(1,h)
        else:
            s += max(1,h)
        h //= 2
        last = c
        c = check(s)
        if h <= 0 and last != c:
            if last:
                s += 1
            break
    print(s)

main()
