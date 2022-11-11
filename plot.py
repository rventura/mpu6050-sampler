#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib.pyplot as plt

def main(argv):
    if len(argv)<2:
        print(f"Usage: {argv[0]} <datafile>")
        return
    data = np.loadtxt(argv[1])
    t0 = data[0,0]
    plt.plot(data[:,0]-t0, data[:,4])
    plt.show()

if __name__=='__main__':
    main(sys.argv)

# EOF
