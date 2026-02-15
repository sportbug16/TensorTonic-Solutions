def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    min_val = min(values)
    max_val = max(values)
    if(min_val==max_val):
        return [0 for i in range(len(values))]
    else:
        bin_w = float((max_val - min_val)/(num_bins))
        ans = []
        for v in values:
            bin_n = int((v-min_val)/bin_w)
            ans.append(min(bin_n, num_bins-1))
        return ans
    # Write code here