def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    return [len(set(recommended[:k]) & set(relevant))/k, len(set(recommended[:k]) & set(relevant))/len(relevant)]
    # Write code here