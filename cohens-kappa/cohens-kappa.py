from collections import Counter
def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    if len(rater1) != len(rater2):
        raise ValueError("Lengths must match")

    n = len(rater1)

    # observed agreement
    matches = sum(a == b for a, b in zip(rater1, rater2))
    p_o = matches / n

    # label counts
    c1 = Counter(rater1)
    c2 = Counter(rater2)

    labels = set(c1) | set(c2)

    # expected agreement
    p_e = sum((c1[l]/n) * (c2[l]/n) for l in labels)

    # denominator zero case
    if 1 - p_e == 0:
        return 1.0

    return (p_o - p_e) / (1 - p_e)

    pass