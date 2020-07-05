#import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    N = int(input())
    print((1000-N%1000)%1000)

main()
