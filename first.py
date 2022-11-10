#!/usr/bin/env python3

import sys
from mpu6050 import mpu6050

def main(argv):
    sensor = mpu6050(0x68)
    while True:
        data = sensor.get_all_data()
        print(data)


if __name__=='__main__':
    main(sys.argv)

# EOF
