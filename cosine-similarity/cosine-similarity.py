import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.asarray(a)
    b = np.asarray(b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    ans = 0.0
    if norm_a == 0 or norm_b == 0:
        return 0.0
    else:
        ans = float(a.dot(b))/float(norm_a*norm_b)
    return ans
    pass