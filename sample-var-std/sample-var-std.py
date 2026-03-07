import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x = np.array(x)
    mean = np.mean(x)
    ssq = sum([(i-mean)**2 for i in x])
    return (ssq/float(len(x)-1), np.sqrt(ssq/float(len(x)-1)))
    pass