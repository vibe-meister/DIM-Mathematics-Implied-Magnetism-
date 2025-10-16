# DIM — Mathematics-Implied Magnetism

A structured research workspace for magnetism theory and experiments, organized into formal mathematical specifications (pure math) and lab-linked theories with datasets, manifests, and notes.

## Repository Structure

- `DIM/`
  - `Purely Mathematical/` — formal specs that can be advanced without hardware
    - `Coherent Energy Metrics/main.txt`
    - `Resonance Amplification Factor/main.txt`
    - `Toroidal Harmonic Modulation/main.txt`
    - `Magnetic Scalar Waves/main.txt`
    - `Time-Dependent Magnetic Flux Vector/main.txt`
    - `Rodin Coil Winding Sequence/main.txt`
    - `Gray Literature Reproducibility Metric/main.txt`
    - `Fringe Energy Propagation/main.txt`
  - Lab-linked theories (e.g., Phase-Coherent Energy Transfer, Inductive Coupling, etc.) with per-theory `datasets/` and notes
- `measurement_schema.json` — measurement template for per-theory datasets
- `maxwell_sources/`, `tesla_sources/`, `rodin_sources/` — source manifests and references

Each theory folder typically contains:
- `main.txt` — the formal specification (definitions, bounds, estimators, validation)
- `datasets/` — `raw/`, `processed/`, `manifests/`, `README.txt`, and `measurement_template.json`
- Notes where applicable (e.g., `01_theory_notes.txt`, `02_proof_strategies.txt`, `03_open_questions.txt`)

## Quick Links (Purely Mathematical Specs)

- Coherent Energy Metrics: `DIM/Purely Mathematical/Coherent Energy Metrics/main.txt`
- Resonance Amplification Factor: `DIM/Purely Mathematical/Resonance Amplification Factor/main.txt`
- Toroidal Harmonic Modulation: `DIM/Purely Mathematical/Toroidal Harmonic Modulation/main.txt`
- Magnetic Scalar Waves: `DIM/Purely Mathematical/Magnetic Scalar Waves/main.txt`
- Time-Dependent Magnetic Flux Vector: `DIM/Purely Mathematical/Time-Dependent Magnetic Flux Vector/main.txt`
- Rodin Coil Winding Sequence: `DIM/Purely Mathematical/Rodin Coil Winding Sequence/main.txt`
- Gray Literature Reproducibility Metric: `DIM/Purely Mathematical/Gray Literature Reproducibility Metric/main.txt`
- Fringe Energy Propagation: `DIM/Purely Mathematical/Fringe Energy Propagation/main.txt`

## Getting Started

1) Explore pure-math specs under `DIM/Purely Mathematical/` for definitions and validation checklists.
2) For lab-linked theories, consult `main.txt` plus `datasets/README.txt` and the copied `measurement_template.json`.
3) Use `measurement_schema.json` as a reference for structuring new measurement records.

## Contributing

- Add new theory folders under `DIM/` following the same structure.
- Keep pure-math specs self-contained and hardware-agnostic; put empirical protocols in lab-linked theories.

## License

TBD.

---

Repo: `https://github.com/vibe-meister/DIM-Mathematics-Implied-Magnetism-`
