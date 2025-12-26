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
def scaled_error(errors, sizes):
    """
    Scale estimation error by sample size.
    """
    return [e * (n ** 0.5) for e, n in zip(errors, sizes)]
