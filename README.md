# MPU6050 sampler

## About

This repos contains calibration and compensation software, providing
sampling of the MPU6050 accelerometer on a Raspberry Pi platform. It
assumes the MPU6050 is on the I2C bus.

## Calibration procedure

1. Collect some data using the calib-collect.py. It collects
   NPOINTS=1000 datapoints and ouputs to stdout the average and std dev.
2. Run the callibration solver in calib-solver.py, which solves the
   following optimization problem for N datapoints:
> minimize (z - A.u - b)^2
> w.r.t. A(3x3), b(3),V(3xN-1)
> s.t. ||ui||^2=1, u=[g | V]
where z is a 3xN matrix of acceleration measurements, 

## Author

Rodrigo Ventura <rodrigo.ventura.isr@gmail.com>
