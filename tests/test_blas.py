from pytest import approx
import numpy as np



from src.pyfortran.blas import dot, matvec, pcg


def test_dot():

    x = np.array([1.0, 2.0, 3.0], dtype=np.float64, order="F")
    y = np.array([2.0, 2.0, 1.0], dtype=np.float64, order="F")

    xy = dot(x, y)

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

    matvec(a, x, y)
    assert y[0] == 14.0
    assert y[1] == 32.0
    assert y[2] == 50.0


def test_pcg():

    a = np.array(
        [
            [1.0, 0.2, 0.3],
            [0.2, 6.0, 0.0],
            [0.3, 0.0, 1.0],
        ],
        order="F"
    )
    b = np.array([2.0, 6.0, 1.0], dtype=np.float64, order="F")
    x = np.zeros_like(b, dtype=np.float64, order="F")

    pcg(a, b, x)

    assert x[0] == approx(1.6605166051660516)
    assert x[1] == approx(0.9446494464944649)
    assert x[2] == approx(0.5018450184501844)
