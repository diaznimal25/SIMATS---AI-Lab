"""Q1. Breadth First Search on the state space tree"""
from collections import deque


def bfs(graph, start):
    visited = [start]
    queue = deque([start])
    print("BFS traversal (queue contents at each step):")
    while queue:
        print("  queue:", list(queue))
        node = queue.popleft()
        print("  visit:", node)
        for child in graph.get(node, []):
            if child not in visited:
                visited.append(child)
                queue.append(child)
    return visited


if __name__ == "__main__":
    print("=" * 50)
    print("Q1. BFS")
    print("=" * 50)
    tree1 = {1: [2, 3], 2: [4, 5], 3: [6], 5: [7]}
    order = bfs(tree1, 1)
    print("BFS order:", order)
