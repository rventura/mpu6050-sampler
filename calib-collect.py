#!/usr/bin/env python3

import sys
import time
import numpy as np
from mpu6050 import mpu6050

NPOINTS = 1000

def data2array(data):
    return np.array([data['x'], data['y'], data['z']])

def main(argv):
    sensor = mpu6050(0x68)
    samples = [data2array(sensor.get_accel_data(g=True)) for n in range(NPOINTS)]
    data = np.vstack(samples)
    mean = data.mean(0)
    sdev = data.std(0)
    print("# mean(3) sdev(3) sdev(3)/sqrt(N)")
    print(str(mean)[1:-1], str(sdev)[1:-1], str(sdev/np.sqrt(len(samples)))[1:-1])

if __name__=='__main__':
    main(sys.argv)

# EOF
