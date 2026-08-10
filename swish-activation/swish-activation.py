import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    return [i*(1/(1+np.exp(-i))) for i in x]
    pass