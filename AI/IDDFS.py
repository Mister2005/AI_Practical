def dls(tree, node, goal, depth, visited):
    if node == goal:
        return [node]
    if depth == 0:
        return []
    
    for neighbor in tree.get(node, []):
        if neighbor not in visited:
            visited.add(neighbor)
            res = dls(tree, neighbor, goal, depth-1, visited)
            if res:
                return [node] + res
    return []

def iddfs(tree, start, goal, max_depth):
    for depth in range(max_depth+1):
        visited = set([start])
        path = dls(tree, start, goal, depth, visited)
        if path:
            return path, depth
    return [], -1

def main():
    n = int(input("Enter number of nodes: "))
    print("Enter each node and its children (space-separated)")
    tree = {}
    for _ in range(n):
        parts = input().split()
        if parts:
            node, children = parts[0], parts[1:]
            tree[node] = children
    
    start = input("Enter start node: ")
    goal = input("Enter goal node: ")
    max_depth = int(input("Enter maximum depth: "))
    
    path, depth = iddfs(tree, start, goal, max_depth)
    
    print("\nIDDFS Result:")
    if path:
        print("Path Found at Depth:", depth)
        print("Path:", " -> ".join(path))
        print("Path Length:", len(path))
    else:
        print("No path found within the maximum depth")

if __name__ == "__main__":
    main()