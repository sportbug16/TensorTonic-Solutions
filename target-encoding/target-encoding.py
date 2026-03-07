def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    # Write code here
    dict = {}
    for i in range(len(categories)):
        cat = categories[i]
        if cat not in dict:
            dict[cat]={'count':0, 'target_sum':0}
        dict[cat]['count']+=1
        dict[cat]['target_sum']+=targets[i]
    ans = []
    for i in range(len(categories)):
        ans.append(dict[categories[i]]['target_sum']/float(dict[categories[i]]['count']))
    return ans

