import numpy as np

from pyfortran.blas import dot, matvec


def test_dot():

    x = np.array([1.0, 2.0, 3.0], dtype=np.float64, order="F")
    y = np.array([2.0, 2.0, 1.0], dtype=np.float64, order="F")

    xy = dot(x, y, 3)

    assert xy == 9.0


def test_matvec():

    a = np.array(
        [
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
            [7.0, 8.0, 9.0],
        ],
        order="F"
    )
    x = np.array([1.0, 2.0, 3.0], dtype=np.float64, order="F")
    y = np.zeros_like(x, dtype=np.float64, order="F")

    matvec(a, x, y, 3)
    assert y[0] == 14.0
    assert y[1] == 32.0
    assert y[2] == 50.0
