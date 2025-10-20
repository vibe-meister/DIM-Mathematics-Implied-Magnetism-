# Implied Magnetism — Core Definitions (Spin and Precession)

## Spin (Intrinsic)
- Spin is an intrinsic quantum degree of freedom, not literal mechanical rotation of a charged sphere. For electrons (spin-½), measurements yield discrete projections ±ħ/2 along any axis.
- The electron’s magnetic moment is tied to spin: μ = −g μ_B ŝ, with g ≈ 2.0023 and μ_B the Bohr magneton.

## Magnetic Moment
- The magnetic moment μ is the torque-coupling vector to a magnetic field B. Energy: U = −μ · B. For electrons, μ includes spin and (when present) orbital contributions.

## Larmor Precession
- In a static field B, a magnetic moment precesses about B at the Larmor frequency ω_L = γ B, where γ is the gyromagnetic ratio (electron: γ ≈ 1.7609×10^11 rad·s⁻¹·T⁻¹).
- Observable manifestations include resonance absorption/emission when driven near ω_L (ESR/NMR) and coherent transverse magnetization dynamics.

## Bloch (Phenomenological) Dynamics
- Macroscopic magnetization M obeys: dM/dt = γ (M × B) − (M_⊥/T2) − ((M_z − M_eq)/T1), capturing precession and relaxation toward equilibrium M_eq with time constants T1 (longitudinal) and T2 (transverse).

## Paramagnetism (Localized Moments)
- For dilute, non-interacting moments of spin S, the static susceptibility follows Curie behavior: χ = N μ_eff^2 / (3 k_B T), with μ_eff = g μ_B √(S(S+1)). Weak exchange modifies this to Curie–Weiss: χ = C/(T − Θ).

## Pauli Paramagnetism (Conduction Electrons)
- In metals, spin polarization of conduction electrons yields a small, nearly temperature-independent susceptibility proportional to the electronic density of states at the Fermi level.

## Diamagnetism
- Induced orbital currents oppose applied fields, giving χ < 0. Core diamagnetism is ubiquitous; in conductors, Landau diamagnetism adds an orbital contribution that partially cancels Pauli paramagnetism.

## “Vibration” in DIM Vocabulary (Interpretation)
- Where intuition suggests “vibration,” in the spin context this maps to precession and driven spin transitions, not ultra-fast classical spinning. In Dearman Implied Magnetism (DIM), we interpret dynamic responses via ω_L, relaxation (T1, T2), and their impact on the observable magnetization and susceptibility.