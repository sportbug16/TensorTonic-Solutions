def priority_replay_sample(priorities, alpha, beta):
    """
    Compute sampling probabilities and importance sampling weights for PER.
    """

    probs = [(float(i))**alpha for i in priorities]
    suma = 0.0
    for i in probs:
        suma += i
    probs = [(float(i)/float(suma)) for i in probs]
    imps = [(len(probs)*float(i))**(-beta) for i in probs]
    imps = [float(i)/float(max(imps)) for i in imps]
    return [probs, imps]
    # Write code here 