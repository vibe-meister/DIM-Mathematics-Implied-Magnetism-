# The Dearman Magnetic Lattice Dynamics  Research Questions

## Core Idea
The 8x8 chessboard becomes a 2D lattice where orthogonal same-color adjacencies form weighted chains. Equality () captures encourage aggressive linkage, while failed attempts remove the attacker. Standard check and castling (clear path) remain unchanged, creating tension between chain-building and king safety.

## Questions and Math Angles
1) Chain Connectivity vs. Castling Trade-offs
   - How do chain sizes/strengths change when castling breaks adjacencies?
   - Model as a grid graph; compute connected components (DFS/BFS) pre/post castling.

2) Risk Dynamics with Equality Rule
   - How does allowing equality alter attack/defense incentives?
   - Estimate P(attacker  defender) via Monte Carlo in dense vs. sparse positions.

3) Orthogonal (Strength) vs. Diagonal (Pawn Attacks)
   - Separate graphs: orthogonal for DIM chains, diagonal for pawn attacks.
   - Compare clustering/connectivity to study asymmetry.

4) Emergent Equilibria with Standard Check and Castling
   - Does check pressure force chain-breaking despite DIM benefits?
   - Use minimax simulations with DIM captures and standard check.

5) Topology and Clustering Analogies
   - Chains as 1D subgraphs; explore Betti numbers/holes.
   - DIM chains resemble DBSCAN-like clusters under orthogonal adjacency.
