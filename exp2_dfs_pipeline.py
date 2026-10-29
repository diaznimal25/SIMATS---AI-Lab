"""Experiment 2 - DFS for Dependency and Reachability Analysis"""

# Directed adjacency list: task -> downstream tasks it depends on / feeds
pipeline = {
    "DataIngest": ["Cleaning", "Validation"],
    "Cleaning": ["FeatureEng"],
    "Validation": ["FeatureEng", "Cleaning"],
    "FeatureEng": ["Training", "Scaling"],
    "Scaling": ["Training"],
    "Training": ["Evaluation"],
    "Evaluation": ["Training", "Deployment"],   # cycle: Evaluation -> Training -> Evaluation
    "Deployment": ["Monitoring"],
    "Monitoring": [],
    "Archive": ["Monitoring"],                  # not reachable from DataIngest
}


def dfs(graph, start, target):
    visited, order, parent = set(), [], {start: None}

    def visit(node):
        visited.add(node)            # mark BEFORE recursing -> prevents revisits / infinite loops
        order.append(node)
        if node == target:
            return True
        for nxt in graph[node]:
            if nxt not in visited:
                parent[nxt] = node
                if visit(nxt):
                    return True
        return False

    found = visit(start)
    path = []
    if found:
        cur = target
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        path.reverse()
    return found, order, path


if __name__ == "__main__":
    print("Tasks:", ", ".join(pipeline))
    s = input("Enter starting task [DataIngest]: ").strip() or "DataIngest"
    t = input("Enter target task [Deployment]: ").strip() or "Deployment"
    if s not in pipeline or t not in pipeline:
        raise SystemExit("Invalid task name.")
    found, order, path = dfs(pipeline, s, t)
    print("\nDFS traversal order:", " -> ".join(order))
    print("Target reachable   :", "YES" if found else "NO")
    if found:
        print("Path to target     :", " -> ".join(path))
