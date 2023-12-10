import numpy as np

from .lib.fblas import pcg as _pcg
from .lib.fblas import dot as _dot
from .lib.fblas import matvec as _matvec


#TODO: Tipar
def pcg(a: np.ndarray, b: np.ndarray, x: np.ndarray, tol: float=1e-11, maxit: int=100):
    _pcg(a, b, x, 1e-11, 1)


#TODO: Tipar
def dot(x: np.ndarray, y: np.ndarray) -> float:
    return _dot(x, y)


#TODO: Tipar
def matvec(a: np.ndarray, x: np.ndarray, y: np.ndarray):
    _matvec(a, x, y)
