import numpy as np

from .blas import dot, matvec

def main():

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
    xAx = dot(x, y, 3)

    print(f"x * Ax = {xAx}")


if __name__ == "__main__":
    main()
