def input_tree():
    tree = {}
    n = int(input("Enter the number of nodes in the tree: "))
    print("Enter each node and its children (comma-separated), leave blank if none.")
    for _ in range(n):
        node = input("Node: ")
        children = input(f"Children of {node}: ").split(',')
        tree[node] = [child.strip() for child in children if child.strip()]
    return tree

def assign_values(tree):
    values = {}
    
    all_nodes = set(tree.keys())
    for children in tree.values():
        all_nodes.update(children)
    
    all_nodes = sorted(list(all_nodes))
    total_nodes = len(all_nodes)
    
    print(f"\nAssigning values to {total_nodes} nodes")
    print("Higher values are preferred in hill climbing.")
    
    for i, node in enumerate(all_nodes):
        while True:
            try:
                val_input = input(f"[{i+1}/{total_nodes}] Enter value for node '{node}': ")
                val = int(val_input)
                values[node] = val
                break
            except ValueError:
                print("Please enter a valid integer value.")
    
    print("All node values assigned successfully.")
    return values

def simple_hill_climbing(tree, values, start):
    current = start
    path = [current]

    while tree.get(current):
        moved = False
        for child in tree[current]:
            if values[child] > values[current]:
                current = child
                path.append(current)
                moved = True
                break  
        if not moved:
            break

    print("\nSimple Hill Climbing Path:", " -> ".join(path))
    print("Reached Node:", current, "| Value:", values[current])

if __name__ == "__main__":
    tree = input_tree()
    values = assign_values(tree)
    start = input("Enter start node: ")
    simple_hill_climbing(tree, values, start)