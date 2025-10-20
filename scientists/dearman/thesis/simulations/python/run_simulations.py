import math
from typing import Iterable, Tuple

import numpy as np
import pandas as pd

MU0 = 4 * math.pi * 1e-7  # vacuum permeability (H/m)


def compute_magnetization(chi: float, H: float) -> float:
    """Return magnetization M given susceptibility chi and applied field H.

    Uses linear relation M = chi * H valid for small fields away from saturation.
    """
    return chi * H


def compute_induction(chi: float, H: float) -> float:
    """Return magnetic flux density B = mu0 * (H + M)."""
    M = compute_magnetization(chi, H)
    return MU0 * (H + M)


def curie_weiss_chi(C: float, theta: float, T: float) -> float:
    """Curie–Weiss susceptibility model for paramagnets and ferromagnets above Tc.

    chi(T) = C / (T - theta)
    """
    return C / (T - theta)


def sweep_fields(chi_values: Iterable[float], H_values: Iterable[float]) -> pd.DataFrame:
    rows = []
    for chi in chi_values:
        for H in H_values:
            M = compute_magnetization(chi, H)
            B = compute_induction(chi, H)
            rows.append({"chi": chi, "H_A_per_m": H, "M_A_per_m": M, "B_T": B})
    return pd.DataFrame(rows)


def sweep_temperature(C: float, theta: float, T_values: Iterable[float], H_probe: float) -> pd.DataFrame:
    rows = []
    for T in T_values:
        chi_T = curie_weiss_chi(C, theta, T)
        M = compute_magnetization(chi_T, H_probe)
        B = compute_induction(chi_T, H_probe)
        rows.append({"T_K": T, "chi_T": chi_T, "H_A_per_m": H_probe, "M_A_per_m": M, "B_T": B})
    return pd.DataFrame(rows)


def main() -> None:
    # Representative susceptibilities
    chi_values = [
        -9e-6,  # water (diamagnetic)
        -1.6e-5,  # bismuth (approx., diamagnetic)
        2.2e-5,  # aluminum (paramagnetic)
        0.1,  # effective high susceptibility (ferromagnet, low-field approx.)
    ]

    H_values = np.linspace(0, 2e5, 51)  # 0 to 200 kA/m
    df_fields = sweep_fields(chi_values, H_values)
    df_fields.to_csv("fields_sweep.csv", index=False)

    # Curie–Weiss example (arbitrary constants for illustration)
    C = 1.0  # Curie constant (arb. units)
    theta = 50.0  # Weiss temperature (K)
    T_values = np.linspace(60, 600, 200)
    df_temp = sweep_temperature(C, theta, T_values, H_probe=1e5)
    df_temp.to_csv("curie_weiss.csv", index=False)

    print("Generated: fields_sweep.csv, curie_weiss.csv")


if __name__ == "__main__":
    main()

