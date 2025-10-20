import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def plot_susceptibility(csv_path: Path) -> None:
    df = pd.read_csv(csv_path)
    if not {"material", "chi"}.issubset(df.columns):
        raise ValueError("CSV must contain 'material' and 'chi' columns")

    df_sorted = df.sort_values("chi")
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.bar(df_sorted["material"], df_sorted["chi"], color=["#4caf50" if x < 0 else "#1565c0" for x in df_sorted["chi"]])
    ax.set_ylabel("Magnetic Susceptibility χ (SI, dimensionless)")
    ax.set_title("Representative Magnetic Susceptibilities")
    ax.axhline(0, color="black", linewidth=0.8)
    # Rotate and align x tick labels for readability
    ax.tick_params(axis="x", labelrotation=45)
    for tick in ax.get_xticklabels():
        tick.set_horizontalalignment("right")
    fig.tight_layout()
    out = csv_path.with_name("susceptibility_barplot.png")
    fig.savefig(out, dpi=200)
    print(f"Saved {out}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python plot_chi.py <path-to-susceptibility.csv>")
        sys.exit(1)
    plot_susceptibility(Path(sys.argv[1]))

