def lag_features(series, lags):
    """
    Create a lag feature matrix from the time series.
    """
    # Write code here
    max_lags = max(lags)
    result = []
    for t in range(max_lags, len(series)):
        result.append([series[t-lag] for lag in lags])
    return result