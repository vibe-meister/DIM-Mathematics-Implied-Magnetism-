# Implied Magnetism — Mathematical Model (Dearman)

## Notation
- Discretize frequency to bins f_k. Let H_Sk ≥ 0 be the normalized intensity of system S in bin k.
- Context weights W_k ≥ 0 summarize propagation/attenuation at f_k.

Define overlaps:
J_{AB} = ∑_k W_k H_Ak H_Bk,
κ_{AB} = J_{AB} / √(J_{AA} J_{BB}).

## Invariances and Axioms
- Scale invariance: H_A · c → κ unchanged.
- Symmetry: κ_{AB} = κ_{BA}.
- Boundedness: 0 ≤ κ ≤ 1.
- Composition (optional): κ_{A,{B,C}} ≈ max(κ_{AB}, κ_{AC}) for max-agg, or L_p aggregation for controllable superposition.

## Response and Decision Models
Define χ̃_S = G_S · K_agg({κ_{SU_i}}). Example aggregations:
- Max: K_agg = max_i κ_{SU_i}
- L2: K_agg = (∑_i κ_{SU_i}^2)^{1/2}
- Softmax: K_agg = (1/λ) log ∑_i exp(λ κ_{SU_i})

Map χ̃ to an observable O via a monotone transduction T_S. Examples:
- Logistic outcome: P(success) = σ(α χ̃_att − β χ̃_def + γ)
- Linear efficiency: η = η_0 + α χ̃ + ε (validated in small-signal regime)
- Torque: τ = k_τ χ̃ (when calibrated)

## Identification Strategy
Given data D = {(H, F, outcome)}, estimate parameters Θ = {α, β, γ, G_S, λ, …} by maximizing likelihood or minimizing prediction error under cross-validation. Include:
- Detuned controls: replace H_B by frequency-shifted H_B^Δ to verify κ sensitivity.
- Shielding controls: modify W to W' to test context dependence.
- Shams: remove U while preserving procedures to estimate false positives.

## Chess Thought-Experiment Mapping
Let agents be chess pieces with weights q_s. Define a grid graph with metric d_1 (Manhattan) and kernel K(d) = exp(−λ d). Edge weight w_ij = q_i q_j K(d_1(i,j)). Chain strength C(t) = ∑_{s∈CC_τ(t)} q_s, where CC_τ keeps edges with w_ij ≥ τ.

Capture rule: attacker wins if C_att ≥ C_def (tie rule configurable). Existing orthogonal-adjacent model is recovered by λ → ∞ and τ just below q_i q_j for d=1.

## Testable Predictions (Templates)
1) Monotonicity: Increasing spectral overlap (via tuning) increases χ̃ and improves outcome odds.
2) Context dependence: Changing W (shielding/geometry) modulates effects.
3) Superposition: Adding an additional tuned source increases χ̃ according to chosen K_agg.
4) Null: When κ ≈ 0 (large detune), outcomes match baseline/sham.


## Spin-Resolved Extension (DIM + Quantum Magnetism)

### Magnetic Moments and Larmor Precession
- Magnetic moment: μ = −g μ_B ŝ for electron spin (|ŝ| = 1/2). In a static field B, moments precess: ω_L = γ B with γ ≈ 1.7609×10^11 rad·s⁻¹·T⁻¹.
- Energy splitting: ΔE = ħ ω_L = g μ_B B. This sets resonance conditions for ESR/NMR-style driving.

### Bloch Magnetization Dynamics
- Phenomenology: dM/dt = γ (M × B) − (M_⊥/T2) − ((M_z − M_eq)/T1).
- Linear response (small B1 transverse drive at ω): M_⊥(ω) exhibits a Lorentzian susceptibility with width 1/T2 and amplitude set by equilibrium polarization M_eq ∝ χ B0.

### Static Susceptibility Decomposition
- χ_total = χ_dia + χ_Pauli + χ_local.
  - χ_dia < 0: core/Landau diamagnetism.
  - χ_Pauli ≈ μ_0 μ_B^2 g(E_F): weak, ≈ T-independent (metals).
  - χ_local = N μ_eff^2 /(3 k_B T) for dilute localized moments (Curie), modified to C/(T − Θ) under mean-field exchange (Curie–Weiss).

### Mapping to κ-Based Framework
- Let κ summarize spectral/context overlap as before. We posit χ̃ acts as a coupling gain on the effective driving of spin ensembles: effective drive ∝ κ · B1, leading to observable changes in M_⊥ and in torque/deflection observables.
- Prediction: At fixed B0, ESR amplitude scales with κ; resonance position follows ω ≈ γ B0; linewidth encodes T2 and environmental noise.

### Practical Interfaces
- Use κ to pick drive spectra that maximize on-resonance power at ω_L while minimizing off-resonant artifacts; W encodes shielding/geometry.
- Calibrate χ components by temperature sweeps (Curie/Weiss), Fermi-level proxies (Pauli), and geometry-dependent diamagnetic baselines.


