"""Experiment 4 - A* Search for Delivery Robot Route Planning"""
import heapq

# Weighted undirected graph (edge costs are an assumed example; the question
# supplied only the heuristic table).
graph = {
    "A": {"B": 2, "C": 3},
    "B": {"A": 2, "D": 3, "E": 4},
    "C": {"A": 3, "E": 2},
    "D": {"B": 3, "F": 2},
    "E": {"B": 4, "C": 2, "F": 3},
    "F": {"D": 2, "E": 3},
}
h = {"A": 6, "B": 4, "C": 5, "D": 2, "E": 3, "F": 0}


def a_star(start, goal):
    open_list = [(h[start], 0, start)]          # (f, g, node)
    g_cost = {start: 0}
    parent = {start: None}
    closed, expansion = set(), []
    while open_list:
        f, g, node = heapq.heappop(open_list)
        if node in closed:
            continue
        closed.add(node)
        expansion.append((node, g, h[node], f))
        if node == goal:
            path, cur = [], goal
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            return path[::-1], g, expansion
        for nbr, w in graph[node].items():
            new_g = g + w
            if nbr not in g_cost or new_g < g_cost[nbr]:
                g_cost[nbr] = new_g
                parent[nbr] = node
                heapq.heappush(open_list, (new_g + h[nbr], new_g, nbr))
    return None, float("inf"), expansion


if __name__ == "__main__":
    s = input("Start location [A]: ").strip().upper() or "A"
    d = input("Destination [F]: ").strip().upper() or "F"
    if s not in graph or d not in graph:
        raise SystemExit("Invalid location.")
    path, cost, expansion = a_star(s, d)
    print("\nNode expansion order (node, g, h, f):")
    for n, g, hn, f in expansion:
        print(f"  {n}: g={g}, h={hn}, f={f}")
    if path:
        print("\nSelected route:", " -> ".join(path))
        print("Total cost    :", cost)
    else:
        print("No route found.")
