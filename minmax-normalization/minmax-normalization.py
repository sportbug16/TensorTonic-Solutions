import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # Write code here
    X = np.asarray(X, dtype=float)
    mins = np.min(X, axis=axis, keepdims=True)
    maxs = np.max(X, axis=axis, keepdims=True)

    denom = np.maximum(maxs - mins, eps)

    return (X - mins) / denom
    pass