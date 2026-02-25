def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here
    u = len(ground_truth)
    count=0
    for reco, gt in zip(recommendations, ground_truth):
        if(len(set(reco[:k]).intersection(set(gt)))==0):
            continue
        else:
            count+=1
    return float(count)/u     
    