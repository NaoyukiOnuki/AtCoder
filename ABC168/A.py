import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    N = int(input())
    r = N%10
    if r in [2,4,5,7,9]:
        print('hon')
    elif r in [0,1,6,8]:
        print('pon')
    else:
        print('bon')

main()
