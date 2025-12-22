import numpy as np
from model import sample

def run_simulation(mu: float, sigma: float, n: int, seed: int = 0):
    """
    Run a single stochastic simulation with controlled randomness.
    """
    rng = np.random.default_rng(seed)
    return sample(mu, sigma, n, rng)
