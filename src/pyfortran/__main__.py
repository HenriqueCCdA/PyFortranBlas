import numpy as np

from .blas import dot, matvec, pcg

def main():

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

    matvec(a, b, x)
    xAx = dot(x, b)

    print(f"x * Ax = {xAx}")
    pcg(a, b, x)

    print(x) # 1.661, 0.945, 0.502

if __name__ == "__main__":
    main()
