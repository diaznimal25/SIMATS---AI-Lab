"""Experiment 1 - BFS for Emergency Facility Navigation"""
from collections import deque

# Hospital layout: rooms/junctions = vertices, corridors = edges (undirected, unweighted)
hospital = {
    "Entrance": ["Triage", "Reception"],
    "Triage": ["Entrance", "Junction1", "XRay"],
    "Reception": ["Entrance", "Junction1", "Pharmacy"],
    "Junction1": ["Triage", "Reception", "Junction2", "Lab"],
    "XRay": ["Triage", "Junction2"],
    "Pharmacy": ["Reception", "Lab"],
    "Lab": ["Junction1", "Pharmacy", "ICU"],
    "Junction2": ["Junction1", "XRay", "OT", "ICU"],
    "OT": ["Junction2", "ICU"],
    "ICU": ["Lab", "Junction2", "OT"],
}


def bfs(graph, source, dest):
    queue = deque([source])
    parent = {source: None}      # doubles as visited set
    explored = []                # nodes dequeued/expanded, in order
    while queue:
        node = queue.popleft()
        explored.append(node)
        if node == dest:
            break
        for nbr in graph[node]:
            if nbr not in parent:
                parent[nbr] = node
                queue.append(nbr)
    if dest not in parent:
        return None, explored
    path, cur = [], dest
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    return path[::-1], explored


if __name__ == "__main__":
    print("Available nodes:", ", ".join(hospital))
    src = input("Enter source node [Entrance]: ").strip() or "Entrance"
    dst = input("Enter destination node [ICU]: ").strip() or "ICU"
    if src not in hospital or dst not in hospital:
        raise SystemExit("Invalid node name.")
    path, explored = bfs(hospital, src, dst)
    if path is None:
        print("No route exists.")
    else:
        print("\nShortest route :", " -> ".join(path))
        print("Corridors used :", len(path) - 1)
    print("Nodes explored :", len(explored))
    print("Exploration order:", explored)
