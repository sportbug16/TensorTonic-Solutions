import numpy as np
def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    # Write code here
    r1 = np.array(rater1)
    r2 = np.array(rater2)

    n = len(r1)

    # observed agreement
    p_o = np.mean(r1 == r2)

    labels = np.unique(np.concatenate([r1, r2]))

    p_e = 0
    for l in labels:
        p_e += (np.mean(r1 == l)) * (np.mean(r2 == l))

    if 1 - p_e == 0:
        return 1.0

    return float((p_o - p_e) / (1 - p_e))
    pass