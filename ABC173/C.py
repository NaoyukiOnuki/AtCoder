import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    H,W,K = map(int, input().split())
    C = np.zeros((H,W), dtype='int8')
    for h in range(H):
        s = input()
        for i in range(len(s)):
            if s[i] == '.':
                C[h,i] = 0
            else:
                C[h,i] = 1

    t2 = 0
    count = 0
    while t2 < 2**(H+W):
        t = t2
        h = []
        w = []
        for i in range(H+W):
            if t&1 == 1:
                if i < H:
                    h += i,
                else:
                    w += (i-H),
            t = t >> 1
        a = np.delete(np.delete(C, h, 0), w, 1)
        c = np.count_nonzero(np.delete(np.delete(C, h, 0), w, 1))
        if c == K:
            count += 1
        t2+=1

    print(count)


main()
