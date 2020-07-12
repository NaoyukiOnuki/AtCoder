#import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    L,R,d = map(int, input().split())
    
    count = 0
    for i in range(L, R+1):
        if i%d == 0:
            count += 1
            
    print(count)

main()
