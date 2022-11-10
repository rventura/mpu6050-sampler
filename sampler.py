#!/usr/bin/env python3

import sys
import time
import numpy as np
import pickle
from mpu6050 import mpu6050

PERIOD = 1/25

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
    print(f"# time\taccel(3)\tnorm\tn_samples")
    t, samples = time.time(), []
    while True:
        samples.append(data2array(sensor.get_accel_data(g=True)))
        tt = time.time()
        if tt-t >=PERIOD:
            data = np.vstack(samples)
            m = data.mean(0)
            s = data.std()
            c = m if calib is None else np.dot(Ai, (m-b))
            print(f"{tt}\t{str(c)[1:-1]}\t{np.linalg.norm(c)}\t{len(samples)}")
            t, samples = tt, []




if __name__=='__main__':
    main(sys.argv)

# EOF
