def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    L = (6/fan_in)**(0.5)
    for row in range(len(W)):
        for col in range(len(W[row])):
            W[row][col] = (L*(2*W[row][col]-1))

    return W
    # Write code here