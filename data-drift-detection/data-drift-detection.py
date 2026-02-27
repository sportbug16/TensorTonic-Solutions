def detect_drift(reference_counts, production_counts, threshold):
    """
    Compare reference and production distributions to detect data drift.
    """
    # Write code here
    total_ref = float(sum(reference_counts))
    total_prod = float(sum(production_counts))
    reference_counts = [i/total_ref for i in reference_counts]
    production_counts = [i/total_prod for i in production_counts]
    ans = {}
    ans["score"] = 0.5*(sum([abs(i-j) for i, j in zip(reference_counts, production_counts)]))
    if ans['score']>threshold:
        ans['drift_detected']=True
    else:
        ans['drift_detected']=False
    return ans
    pass