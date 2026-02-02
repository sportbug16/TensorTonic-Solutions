
def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    # Write code here
    Y = []
    for i in range(0, len(X)):
        Y.append([])
        for j in range(0, len(W[0])):
            Y[i].append(b[j])
            for k in range(0, len(W)):
                Y[i][j] += X[i][k]*W[k][j]
    return Y