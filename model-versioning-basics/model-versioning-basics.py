def promote_model(models):

    """
    Decide which model version to promote to production.
    """

    best = sorted(
        models,
        key=lambda m: (-m["accuracy"], m["latency"], -int(m["timestamp"].replace("-", "")))
    )[0]

    return best["name"]