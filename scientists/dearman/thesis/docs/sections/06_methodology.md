Methodology
-----------

Simulations
-----------
- Analytical/parametric: compute M = χH for representative χ values and visualize B = μ0(H + M).
- Temperature dependence: plot Curie–Weiss χ(T) for paramagnets with varying Θ.
- Geometry: simple dipole and uniform-field approximations sufficient for thesis scope; FEM is optional future work.

Experiments
-----------
- Diamagnetic levitation: pyrolytic graphite over a Halbach array (document magnet dimensions, field map, levitation height vs. mass).
- High-field demonstrations (literature cited): frogs/strawberries levitating; used as corroborating evidence.
- Susceptibility measurement: Gouy balance (force on sample in field gradient), calibration procedure, uncertainty analysis.

Data Analysis
-------------
- Aggregate χ values across classes (diamagnetic, paramagnetic, etc.).
- Compare measured/simulated responses; evaluate temperature trends.
- Report uncertainties and limitations (field uniformity, alignment, hysteresis for ferro/ferri).

Mathematical Test of Universality (DIM)
---------------------------------------
- Hypothesis test: Using repeated χ measurements with known/estimated uncertainties, perform an inverse-variance weighted one-sample z-test of H0: χ = 0 vs H1: χ ≠ 0; report z and two-tailed p.
- Bayes factor: Compute a Jeffreys-scale approximate BF10 to quantify evidence for χ ≠ 0.
- χ(T) predictions: Generate illustrative Curie and Curie–Weiss trends for gases (e.g., O2) and solids (e.g., Fe above Tc); compare qualitatively with literature values.
- Reproducibility: Scripts `chi_significance_test.py` and `chi_T_predictions.py`; figures saved alongside CSV outputs in `data/`.
