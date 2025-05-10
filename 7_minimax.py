def minimax(tree, node, is_max):
    if not isinstance(tree[node], list):
        return tree[node]
    if is_max:
        best = float('-inf')
        for child in tree[node]:
            val = minimax(tree, child, False)
            best = max(best, val)
        return best
    else:
        best = float('inf')
        for child in tree[node]:
            val = minimax(tree, child, True)
            best = min(best, val)
        return best

def main():
    print("Minimax on a game tree")
    n = int(input("Number of non-leaf nodes: "))
    tree = {}
    print("For each internal node, enter: node child1 child2 ...")
    for _ in range(n):
        parts = input().split()
        tree[parts[0]] = parts[1:]
    m = int(input("Number of leaf nodes: "))
    print("For each leaf, enter: node value")
    for _ in range(m):
        leaf, val = input().split()
        tree[leaf] = int(val)

    root = input("Root node: ")
    result = minimax(tree, root, True)
    print("Minimax value at root:", result)

if __name__ == "__main__":
    main()