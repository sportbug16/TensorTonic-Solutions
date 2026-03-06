import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    x = np.array(x)
    ans = [i*p if i != 0 else (1-p) for i in x]
    return (np.array(ans), p, p*(1-p))
    pass