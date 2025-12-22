import numpy as np

def sample(mu: float, sigma: float, n: int, rng: np.random.Generator):
    """
    Generate n IID samples from a normal distribution.

    Assumptions:
    - Finite mean and variance
    - Independence
    """
    return rng.normal(loc=mu, scale=sigma, size=n)
