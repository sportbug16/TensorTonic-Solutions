import numpy as np

def td_value_update(V, s, r, s_next, alpha, gamma):
    """
    Returns: updated value function V_new
    """
    # Write code here
    V = np.asarray(V, dtype=float)
    v_copy = V.copy()
    d = r + gamma*V[s_next] - V[s]
    v_copy[s] = V[s] + alpha*d
    return v_copy
    pass