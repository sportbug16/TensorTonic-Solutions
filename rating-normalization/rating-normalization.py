def rating_normalization(matrix):
    """
    Mean-center each user's ratings in the user-item matrix.
    """
    ans_mat = []
    for j in range(len(matrix)):
        mean = 0.0
        count = 0.0
        ans_row = []
        for i in range(len(matrix[j])):
            if matrix[j][i]==0:
                ans_row.append(matrix[j][i])
                continue
            else:
                count += 1
                mean += matrix[j][i]
            ans_row.append(matrix[j][i])
        if count!=0:
            mean = float(mean)/count
        for i in range(len(ans_row)):
            if ans_row[i]==0:
                continue
            else:
                ans_row[i] -= mean
        ans_mat.append(ans_row)
    return ans_mat
    # Write code here