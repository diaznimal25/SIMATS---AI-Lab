"""Experiment 3 - State-Space Search (BFS) for the 4L / 3L Water Jug problem"""
from collections import deque

CAP_X, CAP_Y = 4, 3
GOAL_X = 2


def successors(state):
    x, y = state
    moves = [
        ("Fill 4L jug",            (CAP_X, y)),
        ("Fill 3L jug",            (x, CAP_Y)),
        ("Empty 4L jug",           (0, y)),
        ("Empty 3L jug",           (x, 0)),
        ("Pour 4L -> 3L",          (x - min(x, CAP_Y - y), y + min(x, CAP_Y - y))),
        ("Pour 3L -> 4L",          (x + min(y, CAP_X - x), y - min(y, CAP_X - x))),
    ]
    return moves


def bfs(start=(0, 0)):
    queue = deque([start])
    parent = {start: (None, "Start")}      # also the visited set
    generated = 1
    while queue:
        state = queue.popleft()
        if state[0] == GOAL_X:             # goal test
            break
        for action, nxt in successors(state):
            generated += 1
            if nxt not in parent:          # repeated-state detection
                parent[nxt] = (state, action)
                queue.append(nxt)
    else:
        return None, len(parent), generated
    path = []
    while state is not None:
        prev, action = parent[state]
        path.append((action, state))
        state = prev
    return path[::-1], len(parent), generated


if __name__ == "__main__":
    solution, distinct, generated = bfs()
    if solution is None:
        raise SystemExit("No solution found.")
    print(f"{'Step':<5}{'Action':<18}State (4L, 3L)")
    for i, (action, state) in enumerate(solution):
        print(f"{i:<5}{action:<18}{state}")
    print("\nSteps in solution      :", len(solution) - 1)
    print("Distinct states visited:", distinct)
    print("Successors generated   :", generated)
