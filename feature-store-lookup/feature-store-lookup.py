def feature_store_lookup(feature_store, requests, defaults):
    """
    Join offline user features with online request-time features.
    """
    # Write code here
    answer = []
    for obj in requests:
        key = obj.get('user_id')
        online = obj.get('online_features')
        # merging 2 dicts into a new one without mutating source
        ans = {**feature_store.get(key, defaults), **online}
        answer.append(ans)
    return answer
    pass