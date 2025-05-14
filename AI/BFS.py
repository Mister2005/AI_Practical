from collections import deque

def bfs(tree, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in tree.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
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
    
    result = bfs(tree, start)
    
    print("\nBFS Traversal Result:")
    print("Traversal Order:", " -> ".join(result))
    print("Total Nodes Visited:", len(result))

if __name__ == "__main__":
    main()