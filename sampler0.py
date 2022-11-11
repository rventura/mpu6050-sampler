#!/usr/bin/env python3

import sys
import time
import numpy as np
import pickle
from mpu6050 import mpu6050

def data2array(data):
    return np.array([data['x'], data['y'], data['z']])

def main(argv):
    if len(argv)>1:
        with open(argv[1], "rb") as fh:
            calib = pickle.load(fh)
        A, b = calib['A'], calib['b']
        Ai = np.linalg.inv(A)
    else:
        calib = None
    sensor = mpu6050(0x68)
    t0 = time.time()
    print(f"# time\taccel(3)\tnorm\tn_samples")
    while True:
        t = time.time()
        m = data2array(sensor.get_accel_data(g=True))
        c = m if calib is None else np.dot(Ai, (m-b))
        print(f"{t}\t{str(c)[1:-1]}\t{np.linalg.norm(c)}\t{t-t0}")
        t0 = t

if __name__=='__main__':
    main(sys.argv)

# EOF
