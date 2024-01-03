#!/usr/bin/env python3

import sys
import time
import numpy as np
import pickle
from mpu6050 import mpu6050

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from geometry_msgs.msg import Vector3


PERIOD = 1/25

def data2array(data):
    return np.array([data['x'], data['y'], data['z']])


class MPU6050Node(Node):

    def __init__(self):
        super().__init__("mpu6050_node")
        self.pub_vector = self.create_publisher(Vector3, "acceleration_vector", 1)
        self.pub_scalar = self.create_publisher(Float64, "acceleration_scalar", 1)
        #
        if len(sys.argv)>1:
            with open(sys.argv[1], "rb") as fh:
                calib = pickle.load(fh)
            A, b = calib['A'], calib['b']
            Ai = np.linalg.inv(A)
            self.calib = (Ai, b)
        else:
            self.calib = None
        self.sensor = mpu6050(0x68)

    def run(self):
        t, samples = time.time(), []
        while True:
            samples.append(data2array(self.sensor.get_accel_data(g=True)))
            tt = time.time()
            if tt-t >=PERIOD:
                data = np.vstack(samples)
                m = data.mean(0)
                s = data.std()
                if self.calib is None:
                    c = m
                else:
                    (Ai, b) = self.calib
                    c = np.dot(Ai, (m-b))
                msg_vec = Vector3()
                (msg_vec.x, msg_vec.y, msg_vec.z) = c
                self.pub_vector.publish(msg_vec)
                msg_scal = Float64()
                msg_scal.data = np.linalg.norm(m)
                self.pub_scalar.publish(msg_scal)
                t, samples = tt, []


def main():
    rclpy.init()
    node = MPU6050Node()
    node.run()
    rclpy.shutdown()

if __name__=='__main__':
    main()

# EOF
