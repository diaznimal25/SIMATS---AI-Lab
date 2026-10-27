"""Q3. Water Jug Problem (4-gallon and 3-gallon, goal: 2 in the 4-gal jug)"""
from collections import deque


def water_jug(cap_x=4, cap_y=3, goal=2):
    start = (0, 0)
    queue = deque([(start, [start])])
    seen = {start}
    while queue:
        (x, y), path = queue.popleft()
        if x == goal:
            return path
        moves = [
            (cap_x, y),                                      # fill 4-gal jug
            (x, cap_y),                                      # fill 3-gal jug
            (0, y),                                          # empty 4-gal jug
            (x, 0),                                          # empty 3-gal jug
            (x - min(x, cap_y - y), y + min(x, cap_y - y)),  # pour 4 -> 3
            (x + min(y, cap_x - x), y - min(y, cap_x - x)),  # pour 3 -> 4
        ]
        for s in moves:
            if s not in seen:
                seen.add(s)
                queue.append((s, path + [s]))
    return None


if __name__ == "__main__":
    print("=" * 50)
    print("Q3. Water Jug Problem")
    print("=" * 50)
    sol = water_jug()
    print("(4-gal, 3-gal) states:")
    for s in sol:
        print("  ", s)
    print(f"Solved in {len(sol) - 1} steps.")
