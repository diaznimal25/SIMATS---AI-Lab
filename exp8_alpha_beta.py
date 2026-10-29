"""Experiment 8 - Alpha-Beta Pruning on a chess-inspired game tree"""
import math

# Root = AI (MAX) choosing among candidate moves.
# Level 2 = opponent replies (MIN); level 3 = AI follow-ups (MAX); leaves = utilities.
game_tree = {
    "Nf3": [[3, 5, 6], [4, 2, 9], [7, 8, 1]],
    "e4":  [[2, 1, 3], [9, 4, 5], [6, 0, 2]],
    "d4":  [[1, 2, 0], [3, 1, 2], [2, 4, 1]],
    "Bc4": [[8, 9, 7], [6, 7, 9], [5, 8, 6]],
}

stats = {"evaluated": 0, "pruned": 0}


def alphabeta(node, is_max, alpha, beta, depth, label):
    indent = "  " * depth
    stats["evaluated"] += 1
    if isinstance(node, int):
        return node
    best = -math.inf if is_max else math.inf
    for i, child in enumerate(node):
        val = alphabeta(child, not is_max, alpha, beta, depth + 1, f"{label}.{i}")
        if is_max:
            best = max(best, val)
            alpha = max(alpha, best)
        else:
            best = min(best, val)
            beta = min(beta, best)
        if beta <= alpha:                         # prune remaining siblings
            skipped = len(node) - i - 1
            if skipped:
                stats["pruned"] += skipped
                print(f"{indent}PRUNE at {label} ({'MAX' if is_max else 'MIN'}): "
                      f"alpha={alpha}, beta={beta}, skipping {skipped} branch(es)")
            break
    return best


def plain_minimax_nodes(node):
    return 1 if isinstance(node, int) else 1 + sum(plain_minimax_nodes(c) for c in node)


if __name__ == "__main__":
    alpha, beta = -math.inf, math.inf
    best_move, best_val = None, -math.inf
    for move, subtree in game_tree.items():
        val = alphabeta(subtree, False, alpha, beta, 1, move)
        print(f"Move {move}: value = {val}")
        if val > best_val:
            best_val, best_move = val, move
        alpha = max(alpha, best_val)
    total = 1 + sum(plain_minimax_nodes(t) for t in game_tree.values())
    print("\nSelected move       :", best_move)
    print("Utility value       :", best_val)
    print("Nodes evaluated     :", stats["evaluated"], f"(plain minimax would visit {total - 1})")
    print("Branches pruned     :", stats["pruned"])
