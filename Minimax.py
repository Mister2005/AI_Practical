def minimax(node, is_maximizing, tree, values):
    if node not in tree:
        return values[node]
    
    if is_maximizing:
        best = float('-inf')
        for child in tree[node]:
            best = max(best, minimax(child, False, tree, values))
        return best
    
    else:
        best = float('inf')
        for child in tree[node]:
            best = min(best, minimax(child, True, tree, values))
        return best
    
n = int(input("Enter the number of edges in the tree: "))
tree = {}
print("Enter the edges (parent child) one per line :")

for _ in range (n):
    u, v = input().split()
    tree.setdefault(u, []).append(v)

leaf_count = int(input("Enter the number of leaf nodes: "))
values = {}
print("Enter leaf node values one per line: ")
for _ in range (leaf_count):
    node, val = input(). split()
    values[node] = int(val)

root = input("Enter the root node: ")
result = minimax(root, True, tree, values)
print("Optimal value: ", result)