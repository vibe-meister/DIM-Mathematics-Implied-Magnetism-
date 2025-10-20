import argparse
import math
from typing import Tuple

import numpy as np
from scipy import stats


def z_test_against_zero(values: np.ndarray, sigma: np.ndarray) -> Tuple[float, float]:
    """One-sample z-test for mean != 0 using known/estimated per-point sigmas.

    Aggregates by inverse-variance weighting to test whether chi differs from 0.
    Returns (z, p_two_tailed).
    """
    weights = 1.0 / np.square(sigma)
    weighted_mean = np.sum(weights * values) / np.sum(weights)
    se = 1.0 / math.sqrt(np.sum(weights))
    z = weighted_mean / se
    p = 2 * (1 - stats.norm.cdf(abs(z)))
    return z, p


def jeffreys_bayes_factor(values: np.ndarray, sigma: np.ndarray) -> float:
    """Approximate Bayes factor (Jeffreys-Zellner-Siow style heuristic) comparing
    H1: mean != 0 vs H0: mean = 0 under weakly-informative prior.
    Smaller BF_01 (< 1) favors H1; report BF_10 = 1/BF_01.
    """
    weights = 1.0 / np.square(sigma)
    mu_hat = np.sum(weights * values) / np.sum(weights)
    se2 = 1.0 / np.sum(weights)
    z2 = mu_hat * mu_hat / se2
    # Jeffreys-scale approximation: BF_01 ≈ sqrt(1 + z2) * exp(-z2/2)
    bf01 = math.sqrt(1 + z2) * math.exp(-0.5 * z2)
    # Numerical floor to avoid division by zero for very large evidence
    bf01 = max(bf01, 1e-300)
    return 1.0 / bf01


def main() -> None:
    parser = argparse.ArgumentParser(description="Test if chi differs from zero")
    parser.add_argument("values", nargs="+", type=float, help="chi measurements")
    parser.add_argument("--sigma", nargs="+", type=float, required=True, help="per-measurement std dev")
    args = parser.parse_args()

    values = np.array(args.values, dtype=float)
    sigma = np.array(args.sigma, dtype=float)
    if values.shape != sigma.shape:
        raise SystemExit("values and sigma must have same length")

    z, p = z_test_against_zero(values, sigma)
    bf10 = jeffreys_bayes_factor(values, sigma)
    print(f"Weighted mean test: z={z:.3f}, p(two-tailed)={p:.3e}, Bayes factor BF10={bf10:.2f}")


if __name__ == "__main__":
    main()


