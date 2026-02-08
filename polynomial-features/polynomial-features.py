def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    ans = []
    for x in values:
        ans_row = [x**i for i in range(degree+1)]
        ans.append(ans_row)
    return ans
    # Write code here