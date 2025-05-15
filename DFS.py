def dfs(tree, start):
    visited = set()
    order = []

    def dfs(node):
        visited.add(node)
        order.append(node)
        for neighbor in tree.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    return order

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
    
    result = dfs(tree, start)
    
    print("\nDFS Traversal Result:")
    print("Traversal Order:", " -> ".join(result))

if __name__ == "__main__":
    main()