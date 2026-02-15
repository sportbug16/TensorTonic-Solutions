def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    min_c = []
    for point in points:
        min_c.append(0)
        mini = 0
        min_dist = 1e9
        for i in range(len(centroids)):
            dist = sum((point[j]-centroids[i][j])**2 for j in range(len(point)))
            if(dist<min_dist):
                min_dist = dist
                mini = i
        min_c[len(min_c)-1] = mini    
    return min_c
    # Write code here