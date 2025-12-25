import numpy as np
from model import sample

def run_simulation(mu: float, sigma: float, n: int, seed: int = 0):
    """
    Run a single stochastic simulation with controlled randomness.
    """
    rng = np.random.default_rng(seed)
    return sample(mu, sigma, n, rng)
def convergence_path(mu: float, sigma: float, sizes, seed: int = 0):
    """
    Track convergence of sample mean as sample size increases.
    """
    rng = np.random.default_rng(seed)
    estimates = []

    for n in sizes:
        x = sample(mu, sigma, n, rng)
        estimates.append(np.mean(x))

    return estimates
