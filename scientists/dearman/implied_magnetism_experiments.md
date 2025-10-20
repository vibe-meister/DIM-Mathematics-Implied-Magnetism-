# Implied Magnetism — Predictions and Experimental Designs (Dearman)

## Principles
- Pre-register hypotheses, parameters, and analysis.
- Use blinded conditions where possible.
- Include null (detuned) and sham controls.
- Log environment (temperature, vibration, RF noise) continuously.

## E1. RF Spectral-Overlap Energy Transfer (Positive Control)
Goal: Validate κ with a mainstream metric. Setup two loosely coupled RLC resonators with tunable f_0 and Q. Measure S21 (VNA) vs frequency and compare with κ from measured spectra H(f). Prediction: η (or S21 peak) increases with κ.
Controls: detune Δf, introduce shielding to alter W, swap coils.

## E2. Torsion Balance Alignment in Faraday Cage (Core Test)
Goal: Detect monotone relationship between χ̃ and deflection θ.
Setup: Lightweight dielectric vane on torsion fiber inside double-shielded cage. External source U with controllable spectrum (e.g., RF noise shaped by filter bank) placed outside inner cage but inside outer chamber to avoid mechanical coupling. Prediction: θ increases with κ(S,U|F) after calibrating G_S.
Controls: detuned spectrum, source-off sham, mechanical vibration injection test, thermal gradient monitoring, randomized blocks.
Analysis: Fit θ = k χ̃ + ε; report CI and Bayes factors.

## E3. Acoustic Analog on Low-Friction Platform (Didactic)
Goal: Demonstrate resonance-mediated coupling analogically.
Setup: Two driven oscillators (metronomes or loudspeaker-mass systems) on a shared low-friction base. Shape drive spectra; measure phase locking probability vs κ. Prediction: Locking probability increases with κ.

## E4. Coil Alignment/Attraction with Nonmagnetic Cores (Risky/Exploratory)
Goal: Probe non-contact tendencies beyond standard inductive forces.
Setup: Two high-Q coils on nonmagnetic supports with minimal mechanical coupling, balanced to null inductive pull. Sweep drive to change H and thus κ. Measure micro-newton forces with optical lever. Strict controls for EMI and air currents required.
Outcome: Either null (preferred for rigor) or bounded micro-effects correlated with κ.

## E5. Null Tests and Bounds
Perform comprehensive nulls to set upper bounds when effects are absent. Report θ_max or F_max as function of κ under multiple W.

## Data Pipeline
- Measure H_S(f) and H_U(f) with calibrated sensors or estimate proxies (envelope spectra).
- Compute κ using chosen W_F.
- Fit outcome models; share code and raw data.


