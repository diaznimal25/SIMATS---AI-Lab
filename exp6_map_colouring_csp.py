"""Experiment 6 - Map Colouring (frequency allocation) as a CSP with backtracking"""

# Variables: regions of the cellular network
regions = ["R1", "R2", "R3", "R4", "R5", "R6", "R7"]

# Domain: available frequency bands (colours)
domains = {r: ["Red", "Green", "Blue", "Yellow"] for r in regions}

# Constraints: neighbouring regions must differ
neighbours = {
    "R1": ["R2", "R3", "R4"],
    "R2": ["R1", "R3", "R5"],
    "R3": ["R1", "R2", "R4", "R5", "R6"],
    "R4": ["R1", "R3", "R6"],
    "R5": ["R2", "R3", "R6", "R7"],
    "R6": ["R3", "R4", "R5", "R7"],
    "R7": ["R5", "R6"],
}

attempts = 0


def consistent(region, colour, assignment):
    return all(assignment.get(n) != colour for n in neighbours[region])


def backtrack(assignment):
    global attempts
    if len(assignment) == len(regions):
        return assignment
    region = next(r for r in regions if r not in assignment)   # next unassigned variable
    for colour in domains[region]:
        attempts += 1
        if consistent(region, colour, assignment):
            assignment[region] = colour
            result = backtrack(assignment)
            if result:
                return result
            del assignment[region]                              # backtrack
    return None


def verify(assignment):
    ok = True
    for r, ns in neighbours.items():
        for n in ns:
            if assignment[r] == assignment[n]:
                print(f"  VIOLATION: {r} and {n} both {assignment[r]}")
                ok = False
    return ok


if __name__ == "__main__":
    solution = backtrack({})
    if solution is None:
        raise SystemExit("No valid colouring exists.")
    print("Final assignment:")
    for r in regions:
        print(f"  {r}: {solution[r]}")
    print("\nVerifying adjacency constraints...")
    print("All constraints satisfied." if verify(solution) else "Constraints violated!")
    print("Assignments attempted:", attempts)
