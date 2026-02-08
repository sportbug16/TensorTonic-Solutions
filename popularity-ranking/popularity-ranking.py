def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    return [(float(x[1]*x[0])/float(x[1]+min_votes)) + (float(min_votes*global_mean)/float(x[1]+min_votes)) for x in items]
    # Write code here