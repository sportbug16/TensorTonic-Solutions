def simple_moving_average(values, window_size):
    """
    Compute the simple moving average of the given values.
    """
    # Write code here
    ans = []
    for i in range(len(values)-window_size+1):
         ans.append(sum(values[i:i+window_size])/window_size)
    return ans