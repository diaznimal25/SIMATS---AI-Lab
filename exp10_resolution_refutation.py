# Experiment 10 - Resolution Refutation (Is the student Happy?)
#
# Knowledge base (English):
#   EnjoysLearning
#   HasFreeTime
#   EnjoysLearning ^ HasFreeTime -> Happy
# CNF of the rule: ~EnjoysLearning v ~HasFreeTime v Happy
# (the original lab version used two simpler clauses; this one is the exact CNF)

def negate(lit):
    return lit[3:] if lit.startswith("Not") else "Not" + lit

def fmt(clause):
    return "{ " + " OR ".join(sorted(clause)) + " }" if clause else "{ } (empty clause)"

clauses = [
    frozenset({"EnjoysLearning"}),                              # C1
    frozenset({"HasFreeTime"}),                                 # C2
    frozenset({"NotEnjoysLearning", "NotHasFreeTime", "Happy"}) # C3
]
goal = "Happy"

print("Resolution Refutation\n")
print("--- Knowledge Base (CNF) ---")
for i, c in enumerate(clauses, 1):
    print(f"C{i}: {fmt(c)}")

negated_goal = negate(goal)
clauses.append(frozenset({negated_goal}))
print(f"\nNegated goal added: C{len(clauses)}: {fmt(clauses[-1])}")

print("\n--- Resolution Steps ---")
seen = set(clauses)
found_empty = False
step = 0

while not found_empty:
    new = []
    n = len(clauses)
    for i in range(n):
        for j in range(i + 1, n):
            c1, c2 = clauses[i], clauses[j]
            for lit in c1:
                comp = negate(lit)
                if comp in c2:
                    resolvent = frozenset((c1 - {lit}) | (c2 - {comp}))
                    # skip tautologies
                    if any(negate(l) in resolvent for l in resolvent):
                        continue
                    if resolvent in seen:
                        continue
                    seen.add(resolvent)
                    step += 1
                    new.append(resolvent)
                    print(f"Step {step}: Resolve C{i+1} {fmt(c1)} and C{j+1} {fmt(c2)} "
                          f"on {lit} -> {fmt(resolvent)}")
                    if not resolvent:
                        found_empty = True
                        break
            if found_empty:
                break
        if found_empty:
            break
    if not new:
        break
    clauses.extend(new)

print("\n--- Final Result ---")
if found_empty:
    print("Empty clause derived: Yes")
    print("Contradiction found.")
    print(f"Therefore, the goal '{goal}' is proved.")
else:
    print("Empty clause derived: No")
    print("The goal could not be proved.")
