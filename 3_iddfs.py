import sys
sys.setrecursionlimit(10000)

def dls(tree, node, goal, depth, path, visited):
    if depth == 0 and node == goal:
        path.append(node)
        return True
    if depth > 0:
        visited.add(node)
        for child in tree.get(node, []):
            if child not in visited:
                if dls(tree, child, goal, depth-1, path, visited):
                    path.insert(0, node)
                    return True
    return False

def iddfs(tree, start, goal, max_depth):
    for depth in range(max_depth+1):
        path = []
        if dls(tree, start, goal, depth, path, set()):
            return path
    return None

def main():
    print("Iterative Deepening DFS on a tree")
    n = int(input("Number of nodes: "))
    print("Enter each node and its children (space-separated):")
    tree = {}
    for _ in range(n):
        parts = input().split()
        node, children = parts[0], parts[1:]
        tree[node] = children

    start = input("Start node: ")
    goal  = input("Goal node: ")
    maxd = int(input("Maximum depth to search: "))
    path = iddfs(tree, start, goal, maxd)
    if path:
        print("Path found at depth ≤", maxd, ":", " → ".join(path))
    else:
        print("No path found within depth", maxd)

if __name__ == "__main__":
    main()