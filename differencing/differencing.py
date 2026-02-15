def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    # series = np.asarray(series)
    result = []
    while(order):
        result = [series[i]-series[i-1] for i in range(1, len(series))]
        series = result
        order-=1
    return result
    # Write code here