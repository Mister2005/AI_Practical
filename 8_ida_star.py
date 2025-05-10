import math

def dfs_f(tree, heur, node, goal, g, bound, path, visited):
    f = g + heur.get(node, float('inf'))
    if f > bound:
        return f, None
    if node == goal:
        return f, path.copy()
    min_bound = float('inf')
    visited.add(node)
    for child, cost in tree.get(node, []):
        if child in visited:
            continue
        path.append(child)
        t, res = dfs_f(tree, heur, child, goal, g+cost, bound, path, visited)
        if res is not None:
            return t, res
        if t < min_bound:
            min_bound = t
        path.pop()
    visited.remove(node)
    return min_bound, None

def ida_star(tree, heur, start, goal):
    bound = heur.get(start, float('inf'))
    path = [start]
    while True:
        t, result = dfs_f(tree, heur, start, goal, 0, bound, path, set())
        if result is not None:
            return result
        if t == float('inf'):
            return None
        bound = t

def main():
    print("IDA* Search on a tree")
    n = int(input("Number of nodes: "))
    print("Enter each node, its heuristic, then children as child:cost ...")
    tree = {}
    heur = {}
    for _ in range(n):
        parts = input().split()
        node = parts[0]
        heur[node] = float(parts[1])
        children = []
        for ch in parts[2:]:
            c, w = ch.split(':')
            children.append((c, float(w)))
        tree[node] = children

    start = input("Start node: ")
    goal  = input("Goal node: ")
    path = ida_star(tree, heur, start, goal)
    if path:
        print("Path found:", " → ".join(path))
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
