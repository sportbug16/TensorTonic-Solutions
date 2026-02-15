import numpy as np

def selu(x, lam=1.0507009873554804934193349852946, alpha=1.6732632423543772848170429916717):
    """
    Apply SELU activation element-wise.
    """
    x = np.asarray(x, dtype=float)
    result = []

    for i in range(len(x)):
        if x[i] > 0:
            val = lam * x[i]
        else:
            val = lam * alpha * (np.exp(x[i]) - 1)
        result.append(round(float(val), 4))

    return result
