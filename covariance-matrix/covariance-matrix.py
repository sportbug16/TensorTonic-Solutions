import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X = np.asarray(X)
    X_cent = X - np.mean(X, axis=0, keepdims=True)
    X_cent_trans = X_cent.T
    if X.ndim != 2 or X.shape[0] < 2:
        return None
    else:
        return (1 / (len(X) - 1)) * (X_cent_trans @ X_cent)
    pass