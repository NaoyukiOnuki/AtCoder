import numpy as np
import math
#from decimal import *
#from numba import njit

#@njit
def main():
    A,B,H,M = map(int, input().split())
    # 時
    h = H + M/60
    # 時針の角度
    hr = (h%12)/12 * 2*math.pi
    # 分
    m = M/60
    # 分針の角度
    mr = m * 2*math.pi

    C = math.sqrt(A**2 + B**2 - 2*A*B*math.cos(hr-mr))
    print(C)

main()
