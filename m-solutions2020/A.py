#import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    X = int(input())
    if X >= 1800:
        print(1)
    elif X >= 1600:
        print(2)
    elif X >= 1400:
        print(3)
    elif X >= 1200:
        print(4)
    elif X >= 1000:
        print(5)
    elif X >= 800:
        print(6)
    elif X >= 600:
        print(7)
    else:
        print(8)

main()
