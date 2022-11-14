#!/usr/bin/env python3

import sys
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def main(argv):
    if len(argv)<2:
        print(f"Usage: {argv[0]} <datafile> [<moving average width>]")
        return
    data = np.loadtxt(argv[1])
    t0 = data[0,0]
    a  = data[:,4]
    if len(argv)>2:
        nw = int(argv[2])
        w  = np.ones(nw)
        a = sp.signal.convolve(a, w, mode='same')
    plt.plot(data[:,0]-t0, a)
    plt.show()

if __name__=='__main__':
    main(sys.argv)

# EOF
