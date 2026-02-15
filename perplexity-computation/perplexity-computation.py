def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    ans = 1
    vec = [prob_distributions[i][actual_tokens[i]] for i in range(len(prob_distributions))]
    for num in vec:
        ans *= num
    ans = ans**(-1/len(prob_distributions))
    return ans
    # Write code here
    