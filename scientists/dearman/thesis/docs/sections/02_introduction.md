Introduction
------------

Hook
----
A frog levitates in a high magnetic field, a graphite flake hovers over a Halbach array, and an MRI scanner images living tissue—all manifestations of the same underlying phenomenon: matter’s magnetic response.

Motivation and Background
-------------------------
From Faraday’s experiments to Maxwell’s synthesis, moving charges and changing fields are inseparable [Jackson 1998]. Quantum mechanics sharpened this picture: electron spin and orbital motion, shaped by the Pauli exclusion principle and Hund’s rule, determine whether materials weakly repel, weakly attract, or develop strong, persistent magnetization [Kittel 2005].

Thesis Statement (DIM)
----------------
This work demonstrates that all materials exhibit magnetism, with variations governed by electron configurations and quantum interactions. We term this perspective DeArman Implied Magnetism (DIM): there are no truly "non-magnetic" materials; χ is measurable even when tiny.

Research Questions
------------------
1. How do different classes of materials manifest magnetism across temperature and field strength?
2. What theoretical mechanisms unify diamagnetism, paramagnetism, and ordered phases?
3. How do simple demonstrations (levitation, susceptibility) convey universality?
4. What are practical implications and limitations of weak magnetic responses?

Operational Universality Test Plan
----------------------------------
We treat the claim “no truly non‑magnetic materials” as an operational proposition. The plan:
- Detection bound: predefine a measurement limit (e.g., |χ| < 10^−8 at 95% CI under specified H, T, and geometry) as the falsification threshold.
- Protocols and scripts: apply calibrated susceptibility measurements and run statistical tests (z‑test and Bayes factor) using provided code to assess χ ≠ 0; generate χ(T) predictions for gases and solids for comparison.
- Reproducibility: publish raw data (CSV), figures, and exact script versions so results can be independently replicated.

Claims of Novelty
-----------------
We articulate the specific contributions beyond prior work:
1) κ-Overlap Formalism for Implied Magnetism: We introduce a spectral/context overlap coefficient κ that maps source–system compatibility into a scalar that modulates observable responses. Unlike traditional expositions that treat magnetism category‑wise (dia/para/ferro) without a unifying, tunable coupling scalar, κ provides an operational handle for design and falsification.
2) Integration with Spin/Precession Dynamics: We embed κ into a spin‑resolved picture using Larmor precession and Bloch dynamics, yielding concrete resonance predictions (ω_res ≈ γ B0, amplitude ∝ κ, linewidth ↔ T2) that connect intuitive “vibration” language to established ESR/NMR observables.
3) Unified Susceptibility Decomposition with Decision Mapping: We combine χ_total = χ_dia + χ_Pauli + χ_local with a decision/response mapping T(χ̃), enabling small‑signal torque/deflection predictions and statistical testing that treats “non‑magnetic” as “below detection bound,” not “zero.”
4) Testable, Pre‑Registered Protocols: We specify falsifiable experiments—κ‑controlled ESR/NMR and SQUID/fluxgate measurements—plus an operational detection threshold that, if unmet, falsifies the implied‑magnetism claim for the tested conditions.
5) Communication Bridge: We translate “everything is magnetic” into a rigorous, quantitative framework compatible with standard electromagnetism and quantum mechanics, avoiding unsupported mechanisms and tying claims to measurable, reproducible quantities.