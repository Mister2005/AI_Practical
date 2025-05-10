import sys
sys.setrecursionlimit(10000)

def dfs(tree, node, goal, visited, path):
    visited.add(node)
    path.append(node)
    if node == goal:
        return True
    for child in tree.get(node, []):
        if child not in visited:
            if dfs(tree, child, goal, visited, path):
                return True
    path.pop()
    return False

def main():
    print("Depth-First Search on a tree")
    n = int(input("Number of nodes: "))
    print("Enter each node and its children (space-separated):")
    tree = {}
    for _ in range(n):
        parts = input().split()
        node, children = parts[0], parts[1:]
        tree[node] = children

    start = input("Start node: ")
    goal  = input("Goal node: ")
    visited = set()
    path = []
    if dfs(tree, start, goal, visited, path):
        print("Path found:", " → ".join(path))
    else:
        print("No path found.")

if __name__ == "__main__":
    main()