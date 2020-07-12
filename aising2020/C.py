#import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    N = int(input())
    f = [{} for _ in range(N+1)] # [{arg:k}] ホントはsetでよかった
    if len(f) > 6:
        f[6] = {(1,1,1):1}
    for i in range(N):
        args = f[i]
        for (x,y,z),k in args.items():
            index = i + 2*x + y + z + 1
            arg = (x+1,y,z)
            if index < N+1:
                f[index][arg] = 1
            index = i + x + 2*y + z + 1
            arg = (x,y+1,z)
            if index < N+1:
                f[index][arg] = 1
            index = i + x + y + 2*z + 1
            arg = (x,y,z+1)
            if index < N+1:
                f[index][arg] = 1

    for i in range(1,N+1):
        print(sum(f[i].values()))

main()
