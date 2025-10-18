import chess
import networkx as nx
import json
import os
import random
import time
from datetime import datetime

# Piece weights
WEIGHTS = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 6,
    chess.QUEEN: 9,
    chess.KING: 11
}

# Map chess.PieceType to string for logging
PIECE_NAMES = {
    chess.PAWN: "Pawn",
    chess.KNIGHT: "Knight",
    chess.BISHOP: "Bishop",
    chess.ROOK: "Rook",
    chess.QUEEN: "Queen",
    chess.KING: "King"
}

def square_to_coords(square):
    """Convert chess square (0-63) to (row, col)."""
    row = square // 8
    col = square % 8
    return row, col

def is_orthogonal_adjacent(square1, square2):
    """Check if two squares are orthogonally adjacent (no diagonals)."""
    r1, c1 = square_to_coords(square1)
    r2, c2 = square_to_coords(square2)
    return abs(r1 - r2) + abs(c1 - c2) == 1

def compute_chain_strength(board, color, target_square):
    """Compute the magnetic chain strength for a piece at target_square."""
    G = nx.Graph()
    # Add nodes for same-color pieces
    for sq in chess.SQUARES:
        piece = board.piece_at(sq)
        if piece and piece.color == color:
            G.add_node(sq, weight=WEIGHTS[piece.piece_type])
    
    # Add edges for orthogonal adjacencies
    for s1 in list(G.nodes):
        for s2 in list(G.nodes):
            if s1 != s2 and is_orthogonal_adjacent(s1, s2):
                G.add_edge(s1, s2)
    
    # If target is isolated, strength is 1
    if target_square not in G.nodes or G.degree(target_square) == 0:
        return 1
    
    # Sum weights of connected component
    component = nx.node_connected_component(G, target_square)
    return sum(G.nodes[s]["weight"] for s in component)

def compute_chain_metrics(board, color, target_square):
    """Return (strength, component_size) for target_square; solo => (1, 1)."""
    G = nx.Graph()
    for sq in chess.SQUARES:
        piece = board.piece_at(sq)
        if piece and piece.color == color:
            G.add_node(sq, weight=WEIGHTS[piece.piece_type])
    for s1 in list(G.nodes):
        for s2 in list(G.nodes):
            if s1 != s2 and is_orthogonal_adjacent(s1, s2):
                G.add_edge(s1, s2)
    if target_square not in G.nodes or G.degree(target_square) == 0:
        return 1, 1
    component = nx.node_connected_component(G, target_square)
    strength = sum(G.nodes[s]["weight"] for s in component)
    return strength, len(component)

def simulate_capture(board, move):
    """Simulate a capture move and return (success, updated_board, event_log)."""
    attacker_square = move.from_square
    target_square = move.to_square
    attacker_piece = board.piece_at(attacker_square)
    defender_piece = board.piece_at(target_square)
    attacker_color = attacker_piece.color
    defender_color = not attacker_color
    san_before = board.san(move)
    fen_before = board.fen()

    # Determine defender square (handle en passant)
    if board.is_en_passant(move):
        # Captured pawn is behind the target square relative to attacker color
        defender_square = target_square - 8 if attacker_color == chess.WHITE else target_square + 8
        defender_piece = board.piece_at(defender_square)
    else:
        defender_square = target_square

    # Defender metrics (pre-move)
    defender_strength, defender_component_size = compute_chain_metrics(board, defender_color, defender_square)
    
    # Simulate move: Temporarily apply the move
    temp_board = board.copy()
    temp_board.push(move)
    
    # Attacker metrics post-move (evaluated on the destination square)
    attacker_strength, attacker_component_size = compute_chain_metrics(temp_board, attacker_color, target_square)
    
    # Outcome
    event = {
        "move_uci": move.uci(),
        "move_san": san_before,
        "attacker": PIECE_NAMES[attacker_piece.piece_type],
        "defender": PIECE_NAMES[defender_piece.piece_type] if defender_piece else "Pawn",
        "attacker_strength": attacker_strength,
        "attacker_component_size": attacker_component_size,
        "defender_strength": defender_strength,
        "defender_component_size": defender_component_size,
        "equality_case": attacker_strength == defender_strength,
        "is_en_passant": board.is_en_passant(move),
        "fen_before": fen_before,
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }

    if attacker_strength >= defender_strength:
        # Capture succeeds
        event["result"] = "attacker_wins"
        event["fen_after"] = temp_board.fen()
        return True, temp_board, event
    else:
        # Capture fails, attacker captured and turn passes
        failed_board = board.copy()
        failed_board.remove_piece_at(attacker_square)
        failed_board.turn = not board.turn
        event["result"] = "attacker_removed"
        event["fen_after"] = failed_board.fen()
        return False, failed_board, event

def simulate_game(max_captures=None, log_dir='logs', game_id=None):
    """Simulate a single game up to max_captures or completion and write per-game log."""
    board = chess.Board()
    move_count = 0
    capture_count = 0
    capture_events = []
    os.makedirs(log_dir, exist_ok=True)
    
    while not board.is_game_over():
        legal_moves = list(board.legal_moves)
        if not legal_moves:
            break
        move = random.choice(legal_moves)
        move_count += 1
        
        if board.is_capture(move):
            success, new_board, event = simulate_capture(board, move)
            if success:
                event["move_number"] = move_count
                capture_events.append(event)
                capture_count += 1
            else:
                event["move_number"] = move_count
                capture_events.append(event)
                capture_count += 1
            board = new_board
        else:
            board.push(move)
        
        if max_captures is not None and capture_count >= max_captures:
            outcome = "Incomplete (max captures reached)"
            break
    else:
        outcome = board.result()
        if board.is_checkmate():
            outcome = "Checkmate"
        elif board.is_stalemate():
            outcome = "Stalemate"
        elif board.is_insufficient_material():
            outcome = "Insufficient material"
        else:
            outcome = "Other draw"
    
    data = {
        "game_id": game_id,
        "total_moves": move_count,
        "total_captures": capture_count,
        "outcome": outcome,
        "final_fen": board.fen(),
        "captures": capture_events,
    }

    gid = game_id if game_id is not None else int(time.time() * 1000)
    path = os.path.join(log_dir, f"game_{gid}.json")
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return data

def run_n_simulations(num_sessions=100, log_dir='logs'):
    """Run a number of full games and log each to its own file, plus an index."""
    all_index = []
    os.makedirs(log_dir, exist_ok=True)
    for session in range(1, num_sessions + 1):
        game_data = simulate_game(max_captures=None, log_dir=log_dir, game_id=session)
        all_index.append({
            "game_id": session,
            "total_moves": game_data["total_moves"],
            "total_captures": game_data["total_captures"],
            "outcome": game_data["outcome"]
        })
    index_path = os.path.join(log_dir, 'index.json')
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(all_index, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    run_n_simulations(100, log_dir='logs')
    print("Simulation completed. Per-game logs written to logs/game_*.json and logs/index.json")