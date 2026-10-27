"""Q2. Depth First Search to find goal L"""


def dfs(graph, start, goal):
    
    stack = [(start, [start])]
    visited = []
    while stack:
        node, path = stack.pop()
        if node in visited:
            continue
        visited.append(node)
        print("  visit:", node)
        if node == goal:
            return path, visited
        # push children in reverse so the left child is explored first
        for child in reversed(graph.get(node, [])):
            if child not in visited:
                stack.append((child, path + [child]))
    return None, visited


if __name__ == "__main__":
    print("=" * 50)
    print("Q2. DFS (goal = L)")
    print("=" * 50)
    tree2 = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F", "G"],
        "D": ["H", "I"],
        "E": ["J"],
        "F": ["K", "L"],
        "G": ["M"],
    }
    path, visited = dfs(tree2, "A", "L")
    print("Goal found! Path:", " -> ".join(path))
    print("Nodes visited:", visited)
