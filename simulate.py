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
