from collections import deque

def bfs(tree, start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for child in tree.get(node, []):
                new_path = list(path) + [child]
                queue.append(new_path)
    return None

def main():
    print("Breadth-First Search on a tree")
    n = int(input("Number of nodes: "))
    print("Enter each node and its children (space-separated), e.g.  A B C  means A→[B,C]")
    tree = {}
    for _ in range(n):
        parts = input().split()
        node, children = parts[0], parts[1:]
        tree[node] = children

    start = input("Start node: ")
    goal  = input("Goal node: ")
    path = bfs(tree, start, goal)
    if path:
        print("Path found:", " → ".join(path))
    else:
        print("No path found.")

if __name__ == "__main__":
    main()