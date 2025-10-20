Theoretical Framework (DIM)
---------------------

Core Relations
--------------
We use the constitutive relation between magnetization and applied field: M = χH, with B = μ0(H + M) in SI. For linear, isotropic media at low fields, χ is approximately constant; nonlinearities arise near magnetic ordering and saturation.

Paramagnetism and Curie–Weiss Law
---------------------------------
For localized moments with effective moment μ_eff, the susceptibility follows χ(T) = C/(T − Θ), where C is the Curie constant and Θ encodes mean-field exchange (Θ > 0 for ferromagnetic correlations). Above ordering, this captures temperature dependence.

Diamagnetism
------------
Lenz-like induced currents oppose changes in magnetic flux, yielding χ < 0. Core diamagnetism is ubiquitous; Landau diamagnetism treats conduction electrons’ orbital quantization in metals.

Exchange and Ordering
---------------------
Pauli exclusion and Coulomb interactions yield an effective exchange favoring parallel or antiparallel spin alignment (Heisenberg model). Ferromagnetism, antiferromagnetism, and ferrimagnetism emerge from exchange-coupled lattices and sublattices.

Relativistic View
-----------------
Magnetism arises from electric charge in motion; in special relativity, electric and magnetic fields are components of the same electromagnetic tensor. This motivates the claim of universality: any matter with charged constituents can, in principle, exhibit a magnetic response.

Intuitive Model (DIM)
-------------------------
We frame an intuitive bridge: electron configuration → unpaired spins and orbital currents → χ sign and magnitude → macroscopic response. Within DeArman Implied Magnetism (DIM), this mental model complements the formalism and guides interpretation of weak responses as implied magnetism present in all matter.

State-wise Spin Alignment Probability (P_align)
----------------------------------------------
We summarize the alignment probability factors by state to unify treatment across regimes. These are working forms suitable for low-field, linear-response intuition and may be replaced by system-specific models when needed.

| State  | Representative P_align(T, H)                           | Dominant factors                 |
|--------|---------------------------------------------------------|----------------------------------|
| Solid  | ~ 1 below T_C (ferromagnets); small in diamagnets      | Exchange (J), domains, anisotropy |
| Liquid | ~ tanh(μH/kT) (weak-field: μH/kT)                      | Thermal randomization             |
| Gas    | ~ tanh(μH/kT) (dilute paramagnets)                     | Low density, 1/T scaling          |
| Plasma | ~ f(n_e, T, B); diamagnetism from pressure gradients   | Density, ionization, ω_c          |

Spin and Precession in DIM
--------------------------
Spin is intrinsic (not classical rotation). Electron spin-½ carries a magnetic moment μ = −g μ_B ŝ, producing discrete measurement outcomes (±ħ/2 projections) and a well-defined gyromagnetic ratio γ. In a static field B, spins precess at the Larmor frequency ω_L = γ B. Driven near ω_L, ensembles exhibit resonance (ESR/NMR), with amplitudes governed by equilibrium polarization and coherence. We adopt a Bloch phenomenology for macroscopic magnetization M:

    dM/dt = γ (M × B) − (M_⊥/T2) − ((M_z − M_eq)/T1)

This connects microscopic spin dynamics to observables.

Susceptibility Decomposition and Temperature Dependence
-------------------------------------------------------
We decompose χ as χ_total = χ_dia + χ_Pauli + χ_local, combining diamagnetism (χ_dia < 0), Pauli paramagnetism (small, ~T-independent), and localized-moment contributions following Curie or Curie–Weiss forms. Exchange interactions shift Curie behavior to Curie–Weiss, introducing Θ that captures mean-field correlations; ordering emerges when T approaches Θ.

Integration with κ-Based Implied Magnetism
------------------------------------------
DIM’s κ summarizes spectral/context overlap of a source with a system. We use χ̃ ∝ K_agg({κ}) as a coupling gain that modulates effective drive fields acting on spin ensembles. Predictions: (i) At fixed B0, ESR peak amplitude tracks κ; (ii) ω_res ≈ γ B0 independent of κ; (iii) linewidth encodes T2 and environment, providing a diagnostic for shielding/geometry W.