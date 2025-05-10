def hill_climbing(tree, heur, start):
    current = start
    path = [current]
    while True:
        neighbors = tree.get(current, [])
        if not neighbors:
            break
        nxt = min(neighbors, key=lambda n: heur.get(n, float('inf')))
        if heur.get(nxt, float('inf')) >= heur.get(current, float('inf')):
            break
        current = nxt
        path.append(current)
    return path

def main():
    print("Greedy Hill-Climbing on a tree (minimize heuristic)")
    n = int(input("Number of nodes: "))
    print("Enter each node, its heuristic, then children (space-separated):")
    tree = {}
    heur = {}
    for _ in range(n):
        parts = input().split()
        node = parts[0]
        heur[node] = float(parts[1])
        tree[node] = parts[2:]

    start = input("Start node: ")
    path = hill_climbing(tree, heur, start)
    print("Hill-climbing path:", " → ".join(path))
    print("Final heuristic:", heur[path[-1]])

if __name__ == "__main__":
    main()