import numpy as np

def wasserstein_critic_loss(real_scores, fake_scores):
    """
    Compute Wasserstein Critic Loss for WGAN.
    """
    # Write code here
    real_scores = np.asarray(real_scores)
    fake_scores = np.asarray(fake_scores)
    fake_mean = np.mean(fake_scores)
    real_mean = np.mean(real_scores)
    return fake_mean - real_mean
    pass