#!/usr/bin/env python3

import sys
import time
import numpy as np
from mpu6050 import mpu6050

def main(argv):
    sensor = mpu6050(0x68)
    t = time.time()
    (s, n) = (np.zeros(3), 0)
    while True:
        data = sensor.get_accel_data(g=True)
        s += np.array([data['x'], data['y'], data['z']])
        n += 1
        tt = time.time()
        if tt-t >=1 :
            print(f"[{n}]\t{s/n}\t{np.linalg.norm(s/n)}")
            (s, n) = (np.zeros(3), 0)
            t = tt




if __name__=='__main__':
    main(sys.argv)

# EOF
