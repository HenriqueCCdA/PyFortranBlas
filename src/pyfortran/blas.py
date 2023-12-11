import numpy as np

from .lib import fblas


def pcg(a: np.ndarray, b: np.ndarray, x: np.ndarray, *, tol: float=1e-11, maxit: int=100, fprint: bool=False):
    fblas.pcg(a, b, x, tol, maxit, fprint)


def dot(x: np.ndarray, y: np.ndarray) -> float:
    return fblas.dot(x, y)


def matvec(a: np.ndarray, x: np.ndarray, y: np.ndarray):
    fblas.matvec(a, x, y)
