"""Q4. A* search   f(n) = g(n) + h(n)"""
import heapq


def a_star(graph, h, start, goal):
    open_list = [(h[start], 0, start, [start])]   # (f, g, node, path)
    best_g = {start: 0}
    step = 1
    while open_list:
        f, g, node, path = heapq.heappop(open_list)
        print(f"Stage {step}: expand {node}  (g={g}, h={h[node]}, f={f})")
        step += 1
        if node == goal:
            return path, g
        for nbr, cost in graph[node]:
            ng = g + cost
            if nbr not in best_g or ng < best_g[nbr]:
                best_g[nbr] = ng
                nf = ng + h[nbr]
                print(f"    {nbr}: g={ng}, h={h[nbr]}, f={nf}")
                heapq.heappush(open_list, (nf, ng, nbr, path + [nbr]))
    return None, float("inf")


if __name__ == "__main__":
    print("=" * 50)
    print("Q4. A* Search (A -> E)")
    print("=" * 50)
    graph = {
        "A": [("B", 7), ("D", 9)],
        "B": [("A", 7), ("C", 7)],
        "C": [("B", 7), ("D", 3), ("E", 10)],
        "D": [("A", 9), ("C", 3), ("E", 3)],
        "E": [("C", 10), ("D", 3)],
    }
    h = {"A": 15, "B": 10, "C": 10, "D": 4, "E": 0}
    path, cost = a_star(graph, h, "A", "E")
    print("Optimal path:", " -> ".join(path), "| total cost:", cost)
