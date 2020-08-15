#import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    S = input()
    
    if 'RRR' in S:
        print(3)
    elif 'RR' in S:
        print(2)
    elif 'R' in S:
        print(1)
    else:
        print(0)
main()
