import numpy as np

def estimate_moments(x: np.ndarray):
    """
    Estimate first and second moments of a sample.
    """
    mean = np.mean(x)
    variance = np.var(x, ddof=0)
    return mean, variance
