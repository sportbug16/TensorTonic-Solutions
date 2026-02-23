import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    # Write code here
    k = np.asarray(k)
    pmf = [p*((1-p)**(i-1)) for i in k]
    pmf = np.asarray(pmf)
    return (pmf, 1/p)
    pass