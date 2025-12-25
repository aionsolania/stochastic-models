import numpy as np

def estimate_moments(x: np.ndarray):
    """
    Estimate first and second moments of a sample.
    """
    mean = np.mean(x)
    variance = np.var(x, ddof=0)
    return mean, variance
def convergence_error(estimates, true_value):
    """
    Compute absolute deviation from true parameter.
    """
    return [abs(e - true_value) for e in estimates]
