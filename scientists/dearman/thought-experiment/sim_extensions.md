# DIM Chess — Simulation Extensions for Implied Magnetism

## Goals
- Generalize from orthogonal adjacency to distance-weighted coupling.
- Support diagonal links and tunable decay.
- Add instrumentation for component sizes and edge statistics.

## Proposed Model Changes
- Metric: use Manhattan distance d_1; optional Chebyshev d_∞ switch.
- Kernel: K(d) = exp(−λ d), λ > 0; original model recovered by large λ and thresholding at d=1.
- Edge weight: w_ij = q_i q_j K(d(i,j)); keep edges with w_ij ≥ τ.
- Chain strength: C(t) = ∑ weights q_s over connected component above τ.
- Capture rule: unchanged (C_att ≥ C_def), tie handling configurable.

## Implementation Plan
- Config: add JSON/YAML for {lambda, tau, metric, diag_links: bool}.
- Functions: refactor adjacency builder to accept kernel/metric.
- Telemetry: log (attacker_strength, defender_strength, component_sizes, edge_counts).
- Tests: golden tests with λ→∞ to match current behavior.

## Analysis
- Sweep λ and τ; measure capture outcome distributions.
- Compare orthogonal vs diagonal-enabled graphs.


