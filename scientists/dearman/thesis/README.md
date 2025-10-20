DeArman Implied Magnetism (DIM) — Thesis
=======================================

Overview
--------
This repository contains the full thesis scaffold arguing that magnetism is universal across materials, modulated by electron configuration and quantum interactions. It includes drafted sections, simulations, datasets, figures/tables placeholders, experimental protocols, and references. We use the term DeArman Implied Magnetism (DIM) for the intuitive framework unifying weak and strong magnetic responses.

Structure
---------
- `docs/` — thesis manuscript in modular sections
  - `index.md` — main entry linking all sections
  - `sections/01_abstract.md` … `08_conclusion.md`
- `data/` — susceptibility datasets and derived tables
- `figures/` — generated plots and diagrams
- `tables/` — rendered tables for manuscript
- `experiments/` — lab protocols (levitation, Gouy balance)
- `simulations/python/` — Python code to simulate fields and plot χ
- `references/` — bibliography (`references.bib`)
- `appendix/` — appendices and supplementary materials

Quickstart
----------
1. Install Python 3.10+.
2. Create a virtual environment and install requirements:
   ```bash
   cd simulations/python
   python -m venv .venv
   .venv\\Scripts\\activate
   pip install -r requirements.txt
   ```
3. Run simulations and plots:
   ```bash
   python run_simulations.py
   python plot_chi.py ..\\..\\data\\susceptibility.csv
   ```

Build Manuscript
----------------
The manuscript is Markdown-first. You can render with any static site generator or an md-to-PDF tool (e.g., Pandoc). Section links are maintained in `docs/index.md`.

Thesis Claim (One-liner)
------------------------
All materials exhibit magnetism; observed differences arise from electron configurations and quantum many-body interactions.

Contact & License
-----------------
Author: DeArman Implied Magnetism (DIM) — Scientists
License: CC BY 4.0 for text; MIT for code
