
import chess
import chess.svg
import networkx as nx
import json
import os
import random
import time

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
    for sq in chess.SQUARES:
        piece = board.piece_at(sq)
        if piece and piece.color == color:
            G.add_node(sq, weight=WEIGHTS[piece.piece_type])
    
    for s1 in list(G.nodes):
        for s2 in list(G.nodes):
            if s1 != s2 and is_orthogonal_adjacent(s1, s2):
                G.add_edge(s1, s2)
    
    if target_square not in G.nodes or G.degree(target_square) == 0:
        return 1
    
    component = nx.node_connected_component(G, target_square)
    return sum(G.nodes[s]["weight"] for s in component)

def simulate_capture(board, move):
    """Simulate a capture move and return if it succeeds, and the updated board."""
    attacker_square = move.from_square
    target_square = move.to_square
    attacker_piece = board.piece_at(attacker_square)
    attacker_color = attacker_piece.color
    defender_color = not attacker_color
    # Determine actual defender square (handle en passant)
    if board.is_en_passant(move):
        defender_square = target_square - 8 if attacker_color == chess.WHITE else target_square + 8
    else:
        defender_square = target_square
    defender_piece = board.piece_at(defender_square)
    defender_strength = compute_chain_strength(board, defender_color, defender_square)
    
    temp_board = board.copy()
    temp_board.push(move)
    attacker_strength = compute_chain_strength(temp_board, attacker_color, target_square)
    
    if attacker_strength >= defender_strength:
        return True, temp_board, attacker_strength, defender_strength
    else:
        failed_board = board.copy()
        failed_board.remove_piece_at(attacker_square)
        # Turn passes to the opponent when the attacker is removed
        failed_board.turn = not board.turn
        return False, failed_board, attacker_strength, defender_strength

def display_board(board):
    """Display the chess board in the console."""
    print("\nCurrent Board:")
    print(board)
    print()

def play_game(max_captures=None, log_file='game_log.json'):
    """Play a human (White) vs script (Black) game."""
    board = chess.Board()
    move_count = 0
    capture_count = 0
    captures = []
    
    print("Welcome to Magnet Chess! You are White. Enter moves in algebraic notation (e.g., 'e4', 'Bxc3'). Type 'quit' to end.")
    display_board(board)
    
    while not board.is_game_over():
        # Human's turn (White)
        if board.turn == chess.WHITE:
            move_input = input("Your move (White): ").strip()
            if move_input.lower() == 'quit':
                return {
                    "captures": captures,
                    "total_moves": move_count,
                    "outcome": "Game quit by player"
                }
            
            try:
                move = board.parse_san(move_input)
                if move not in board.legal_moves:
                    print("Illegal move! Try again.")
                    continue
            except:
                print("Invalid move format! Use algebraic notation (e.g., 'e4', 'Bxc3').")
                continue
            
            move_count += 1
            if board.is_capture(move):
                # Precompute defender piece for logging (handles en passant)
                attacker_color = board.turn
                def_sq = move.to_square if not board.is_en_passant(move) else (move.to_square - 8 if attacker_color == chess.WHITE else move.to_square + 8)
                defender_piece_pre = board.piece_at(def_sq)
                success, new_board, attacker_strength, defender_strength = simulate_capture(board, move)
                if success:
                    print(f"Capture succeeds! Attacker strength: {attacker_strength}, Defender strength: {defender_strength}")
                    if defender_piece_pre:
                        captures.append({
                            "piece": PIECE_NAMES[defender_piece_pre.piece_type],
                            "value": defender_strength,
                            "move": move_count
                        })
                    capture_count += 1
                else:
                    print(f"Capture fails! Attacker captured. Attacker strength: {attacker_strength}, Defender strength: {defender_strength}")
                    attacker_piece = board.piece_at(move.from_square)
                    captures.append({
                        "piece": PIECE_NAMES[attacker_piece.piece_type],
                        "value": attacker_strength,
                        "move": move_count
                    })
                    capture_count += 1
                board = new_board
            else:
                board.push(move)
        else:
            # Script's turn (Black)
            legal_moves = list(board.legal_moves)
            if not legal_moves:
                break
            move = random.choice(legal_moves)
            move_count += 1
            print(f"Script's move (Black): {board.san(move)}")
            
            if board.is_capture(move):
                # Precompute defender piece for logging (handles en passant)
                attacker_color = board.turn
                def_sq = move.to_square if not board.is_en_passant(move) else (move.to_square - 8 if attacker_color == chess.WHITE else move.to_square + 8)
                defender_piece_pre = board.piece_at(def_sq)
                success, new_board, attacker_strength, defender_strength = simulate_capture(board, move)
                if success:
                    print(f"Script's capture succeeds! Attacker strength: {attacker_strength}, Defender strength: {defender_strength}")
                    if defender_piece_pre:
                        captures.append({
                            "piece": PIECE_NAMES[defender_piece_pre.piece_type],
                            "value": defender_strength,
                            "move": move_count
                        })
                    capture_count += 1
                else:
                    print(f"Script's capture fails! Attacker captured. Attacker strength: {attacker_strength}, Defender strength: {defender_strength}")
                    attacker_piece = board.piece_at(move.from_square)
                    captures.append({
                        "piece": PIECE_NAMES[attacker_piece.piece_type],
                        "value": attacker_strength,
                        "move": move_count
                    })
                    capture_count += 1
                board = new_board
            else:
                board.push(move)
        
        display_board(board)
        
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
        "captures": captures,
        "total_moves": move_count,
        "outcome": outcome
    }
    
    with open(log_file, 'a') as f:
        json.dump(data, f)
        f.write('\n')
    
    return data

def run_games(stages, log_file='game_log.json'):
    """Run multiple human vs script games across stages."""
    if os.path.exists(log_file):
        os.remove(log_file)
    
    all_data = []
    for stage_num, (max_captures, num_sessions) in enumerate(stages, 1):
        print(f"\n=== Stage {stage_num}: Up to {max_captures if max_captures else 'Full'} captures, {num_sessions} games ===")
        for session in range(num_sessions):
            print(f"\nGame {session + 1} of Stage {stage_num}")
            game_data = play_game(max_captures=max_captures, log_file=log_file)
            game_data["stage"] = stage_num
            game_data["session"] = session
            all_data.append(game_data)
            print(f"Game ended. Outcome: {game_data['outcome']}, Total moves: {game_data['total_moves']}, Captures: {len(game_data['captures'])}")
            time.sleep(1)
            if game_data["outcome"] == "Game quit by player":
                print("Player quit. Ending simulation.")
                break
        if game_data["outcome"] == "Game quit by player":
            break
    
    with open('full_game_log.json', 'w') as f:
        json.dump(all_data, f, indent=4)
    
    print("\nSimulation completed. Logs in game_log.json and full_game_log.json")

if __name__ == "__main__":
    # Define stages: (max_captures, num_sessions)
    stages = [
        (3, 5),
        (6, 5),  # Change to (6, 100) for full run
        (9, 5),  # Change to (9, 100)
        (None, 5)  # Change to (None, 100)
    ]
    run_games(stages)
