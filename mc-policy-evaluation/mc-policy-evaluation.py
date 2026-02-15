import numpy as np

def mc_policy_evaluation(episodes, gamma, n_states):
    """
    Returns: V (NumPy array of shape (n_states,))
    """
    # Write code here
    count = np.zeros(n_states)
    V = np.zeros(n_states)

    for episode in episodes:
        G = 0.0
        visited_states = set()
        visit = np.zeros(n_states)
        for t in reversed(range(len(episode))):
            state, reward = episode[t]
            G = reward + gamma * G
            if state not in visited_states:
                visit[state] = G
                count[state] += 1
                visited_states.add(state)
        for s in range(n_states):
            V[s] += visit[s]
            
    for s in range(n_states):
        if count[s] != 0:
            # print(V[s])
            V[s] = float(V[s]) / count[s]

    return V
    pass
