from collections import deque

def bfs(tree, start, goal):
    visited = set()
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        current_node = path[-1]
        if current_node == goal:
            return path
        if current_node not in visited:
            visited.add(current_node)
            for neighbor in tree.get(current_node, []):
                new_path = list(path) + [neighbor]
                queue.append(new_path)
    return None

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
    path = bfs(tree, start, goal)
    if path:
        print("Path found:", " → ".join(path))
    else:
        print("No path found from", start, "to", goal)

if __name__ == "__main__":
    main()