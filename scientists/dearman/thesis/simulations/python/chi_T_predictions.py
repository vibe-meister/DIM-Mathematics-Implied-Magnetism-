import argparse
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def chi_curie(T: np.ndarray, C: float) -> np.ndarray:
    return C / T


def chi_curie_weiss(T: np.ndarray, C: float, theta: float) -> np.ndarray:
    return C / (T - theta)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate chi(T) predictions and plots")
    parser.add_argument("--outdir", type=str, default=".")
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    # Example: O2 gas (paramagnet, Curie law, illustrative C)
    T = np.linspace(80, 600, 400)
    C_O2 = 1.0  # arbitrary units for illustration
    chi_O2 = chi_curie(T, C_O2)
    df_O2 = pd.DataFrame({"T_K": T, "chi": chi_O2})
    df_O2.to_csv(outdir / "chi_T_O2.csv", index=False)
    plt.figure(figsize=(6, 4))
    plt.plot(T, chi_O2)
    plt.xlabel("Temperature (K)")
    plt.ylabel("chi (arb.)")
    plt.title("O2: Curie law illustration")
    plt.tight_layout()
    plt.savefig(outdir / "chi_T_O2.png", dpi=200)

    # Example: Fe above Tc (Curie–Weiss), illustrative constants
    T2 = np.linspace(1050, 1500, 400)
    C_Fe = 1.0
    theta_Fe = 1043.0
    chi_Fe = chi_curie_weiss(T2, C_Fe, theta_Fe)
    pd.DataFrame({"T_K": T2, "chi": chi_Fe}).to_csv(outdir / "chi_T_Fe.csv", index=False)
    plt.figure(figsize=(6, 4))
    plt.plot(T2, chi_Fe)
    plt.xlabel("Temperature (K)")
    plt.ylabel("chi (arb.)")
    plt.title("Fe: Curie–Weiss above Tc (illustration)")
    plt.tight_layout()
    plt.savefig(outdir / "chi_T_Fe.png", dpi=200)

    print("Saved chi(T) predictions: chi_T_O2.csv/.png, chi_T_Fe.csv/.png")


if __name__ == "__main__":
    main()


