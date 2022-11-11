#!/usr/bin/env python3

import sys
import numpy as np
import scipy.optimize as opt
import pickle

def main(argv):
    if len(argv)<2:
        print(f"Usage: {argv[0]} <dataset> [<output calibration file>]")
        return
    data = np.loadtxt(argv[1])
    print("Loaded", data.shape, "dataset")
    z = data[:, 0:3].T
    n = z.shape[1]
    u1 = np.array([0, 0, -1]).reshape(3,1)
    def cost(x):
        A = x[0:9].reshape(3, 3)
        b = x[9:12]
        u = np.hstack([u1, x[12:].reshape(3, -1)])
        D = z - np.dot(A, u) - b[:,None]
        return np.sum(D*D)
    def eqcons(x):
        u = x[12:].reshape(3, -1)
        return (u*u).sum(0) - 1
    #x0 = np.hstack([np.eye(3).flatten(), np.zeros(3), np.tile(np.array([1, 0, 0]), n-1)])
    x0 = 0.1*np.random.randn(9+3+3*(n-1))
    print("Dim:", n, x0.shape)
    print("J0 =", cost(x0))
    print("g0 =", eqcons(x0))
    out = opt.fmin_slsqp(cost, x0, f_eqcons=eqcons, disp=1, full_output=True)
    x = out[0]
    A = x[0:9].reshape(3, 3)
    b = x[9:12]
    print("Jf =", cost(x))
    print("gf =", eqcons(x))
    print("A =", A)
    print("|A| =", np.linalg.det(A))
    print('\n'.join([str(m) for m in np.linalg.svd(A)]))
    print("b =", b)
    print("u =", np.hstack([u1, x[12:].reshape(3, -1)]))
    print("||u|| =", np.sqrt((np.hstack([u1, x[12:].reshape(3, -1)])**2).sum(0)))
    if len(argv)>2:
        with open(argv[2], "wb") as fh:
            package = dict(A=A, b=b)
            pickle.dump(package, fh)


        
            

if __name__=='__main__':
    main(sys.argv)

# EOF
