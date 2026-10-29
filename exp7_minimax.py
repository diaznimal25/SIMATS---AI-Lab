"""Experiment 7 - Minimax on a binary game tree"""

# Binary tree as nested lists; integers are terminal utilities.
# Depth 3: MAX (AI) -> MIN (opponent) -> MAX -> leaves
tree = [
    [[3, 5], [6, 9]],      # move 0 (left)
    [[1, 2], [0, -1]],     # move 1 (right)
]


def minimax(node, is_max, label="root", depth=0):
    indent = "  " * depth
    if isinstance(node, int):
        print(f"{indent}{label}: leaf = {node}")
        return node
    values = [minimax(child, not is_max, f"{label}.{i}", depth + 1)
              for i, child in enumerate(node)]
    val = max(values) if is_max else min(values)
    print(f"{indent}{label} ({'MAX' if is_max else 'MIN'}) -> {val}")
    return val


if __name__ == "__main__":
    print("Evaluating game tree:\n")
    child_values = []
    root_val = None
    # evaluate each root move separately so the best move can be reported
    for i, child in enumerate(tree):
        child_values.append(minimax(child, False, f"move{i}", 1))
    root_val = max(child_values)
    best = child_values.index(root_val)
    print(f"\nroot (MAX) -> {root_val}")
    print("Values of root moves:", child_values)
    print(f"Best move for AI: move {best} ({'left' if best == 0 else 'right'}), minimax value = {root_val}")
