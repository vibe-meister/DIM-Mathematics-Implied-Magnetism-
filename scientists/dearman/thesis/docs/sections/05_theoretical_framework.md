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
