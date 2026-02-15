def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    # Write code here
    ans = [[0.0 for dim in range(len(points[i]))] for i in range(k)]
    counts = [0 for i in range(k)]
    for i in range(len(points)):
        counts[assignments[i]] += 1
        for j in range(len(points[0])):
            ans[assignments[i]][j] += points[i][j]
    for i in range(k):    
        if(counts[i]):
            for j in range(len(points[i])):
                ans[i][j] /= counts[i] 
        else:
            continue
    return ans