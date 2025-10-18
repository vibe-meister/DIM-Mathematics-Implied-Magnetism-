# Magnet Chess with Dearman Implied Magnetism (DIM)  Final Rules

## Board
- Standard 8x8 chessboard (64 squares), no wrapping edges.

## Piece Weights
- Pawn 1, Knight 3, Bishop 3, Rook 6, Queen 9, King 11.

## Dearman Implied Magnetism (DIM)
- Same-color pieces that share a side (orthogonal only: up/down/left/right) form a magnetic chain (connected component).
- A chains strength = sum of the weights of all pieces in the chain; every piece in the chain uses this same strength for capture calculations.
- Example: b2 Pawn (1)  b3 Rook (6)  b4 Pawn (1) = chain strength 8.

## Solo Piece Rule
- Any isolated piece (no orthogonal same-color neighbors) has strength 1 regardless of normal weight (e.g., a solo queen is 1).

## Capture Mechanics
- Defender strength: target pieces chain strength (or 1 if solo).
- Attacker strength: computed after the move lands, using the attackers new chain (or 1 if solo).
- Outcome: capture succeeds if attacker strength  defender strength; otherwise attacker is removed and the defender stays.

## Pawns, En Passant, Check/Checkmate
- Pawns attack diagonally; DIM stacks orthogonally only.
- En passant follows standard chess rules; DIM applies to the capture strength comparison.
- Check and checkmate follow standard rules and ignore DIM (a king in check must resolve check regardless of chain strength).

## Castling
- Standard rules: neither piece moved, clear path between king and rook, king not in check, and cannot move through or into check.
- DIM does not affect castling eligibility or execution.

## Other Standard Rules
- Movement and pawn promotion are unchanged.

## Implications
- Equality rule () promotes offensive chain-building.
- Standard check and castling preserve king safety as a core objective.

## Illustrative Scenario
- Position: White b2 pawn in chain with b3 pawn and c2 bishop → strength 5. Black c3 knight in chain with c4 pawn and c5 bishop → strength 7.
- White b2→c3: Attacker post-move chain = pawn (1) + c2 bishop (3) = 4. Since 4 < 7, capture fails; white pawn is removed.
- Equality case: If a white rook were on c2 (6), then post-move chain = 1 + 6 = 7, so 7  7; capture succeeds.
- Check example: b2c3 checking a king still requires standard check resolution; DIM is ignored for the check itself.
- Castling example: Queenside e1c1, a1d1 requires a clear path; DIM does not modify this.
