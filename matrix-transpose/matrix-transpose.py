import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.asarray(A)
    rows, cols = A.shape
    ans = np.zeros((cols, rows))

    for i in range(len(A[0])):
        for j in range(len(A)):
            ans[i][j] = A[j][i]
    return ans
    pass