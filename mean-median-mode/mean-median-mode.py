import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x = np.asarray(x)
    mean = float(np.mean(x))
    median = float(np.median(x))
    mode = float(max(Counter(x), key=Counter(x).get))
    return (mean, median, mode)
    pass