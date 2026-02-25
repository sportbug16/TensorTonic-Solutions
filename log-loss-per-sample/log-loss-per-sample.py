import math

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    # Write code here
    ans = []
    for y_org, y_est in zip(y_true, y_pred):
        p = max(eps, min(1-eps, y_est))
        ans.append(-1*(math.log(p)*y_org + (1-y_org)*math.log(1-p)))
    return ans
    pass