import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    dic = {}
    for i in range(len(vocab)):
        dic[vocab[i]] = i 
    ans = np.zeros(len(vocab), dtype=int)
    for w in tokens:
        if w in dic:
            ans[dic.get(w)] += 1
    return ans
    pass