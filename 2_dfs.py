import sys

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
    n = int(input("Number of nodes: "))
    print("Enter each node and its children (space-separated), e.g.  A B C  means A has children B and C")
    tree = {}
    for _ in range(n):
        parts = input().split()
        if parts:
            node, children = parts[0], parts[1:]
            tree[node] = children
    start = input("Start node: ")
    goal = input("Goal node: ")
    visited = set()
    path = []
    if dfs(tree, start, goal, visited, path):
        print("Path found:", " → ".join(path))
    else:
        print("No path found from", start, "to", goal)

if __name__ == "__main__":
    main()