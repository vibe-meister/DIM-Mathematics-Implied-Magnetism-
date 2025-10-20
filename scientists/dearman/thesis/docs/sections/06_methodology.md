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
 
Spin-Resolved Measurements and Predictions
-----------------------------------------
Setup Overview:
- ESR: Set static field B0 using a calibrated magnet; apply transverse RF drive B1 via coil. Sweep frequency near ω ≈ γ B0. Use lock-in detection or frequency modulation to enhance SNR.
- NMR (optional): Homogeneous B0 with solenoid; observe FID or CW absorption at ω_L = γ_n B0.
- SQUID/Fluxgate: Place samples within multi-layer magnetic shielding; modulate κ by shaping drive spectra while holding B0 fixed.

Calibration and Controls:
- Validate g using a standard (e.g., DPPH) for ESR; map B0 homogeneity.
- Detune B0 and drive frequency to demonstrate ω_L scaling and nulls.
- Rotate anisotropic samples; insert/removal of shields to alter W.

Analysis Plan:
- ESR/NMR lineshape: Fit Lorentzian/Voigt to extract center ω_res, width (1/T2 proxy), and amplitude. Test amplitude ∝ κ at fixed B0.
- Temperature sweeps: Estimate Curie/Curie–Weiss parameters (C, Θ) from χ(T) and compare with literature ranges.
- Decomposition: Attribute baselines to χ_dia; estimate χ_Pauli via material class and DOS proxies; assign residual to χ_local.

Predicted Outcomes:
- Resonance: ω_res ≈ γ B0 (electrons) or γ_n B0 (nuclei), independent of κ.
- Amplitude: Increases with κ and sample polarization; saturates as B1 increases (T1-limited).
- Linewidth: Broadens with environmental noise; narrows with improved shielding/geometry, reflecting T2.