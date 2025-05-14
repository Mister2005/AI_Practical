import math

def dfs_f(tree, heur, node, goal, g, bound, path, visited):
    """Depth-first search with a bound on f-value.
    
    Args:
        tree: Dictionary mapping nodes to their children with costs: {node: [(child1, cost1), ...]}
        heur: Dictionary mapping nodes to their heuristic values: {node: heuristic_value}
        node: Current node being explored
        goal: Goal node
        g: Cost so far from start to the current node
        bound: Current f-value bound (f = g + h)
        path: Current path from start to current node
        visited: Set of nodes already visited in current path
        
    Returns:
        Tuple of (new_bound, path_to_goal)
        - If goal is found, returns (f_value, path_to_goal)
        - If goal not found within bound, returns (new_bound, None)
    """
    # Calculate f-value for current node (f = g + h)
    f = g + heur.get(node, float('inf'))
    
    # If f exceeds the bound, return f as the new bound
    if f > bound:
        return f, None
    
    # If we reached the goal, return the current f-value and path
    if node == goal:
        return f, path.copy()
    
    # Initialize minimum bound for next iteration
    min_bound = float('inf')
    
    # Mark current node as visited to avoid cycles
    visited.add(node)
    
    # Try all possible child nodes
    for child, cost in tree.get(node, []):
        # Skip already visited nodes
        if child in visited:
            continue
        
        # Add child to the path
        path.append(child)
        
        # Recursively search from this child
        t, result = dfs_f(tree, heur, child, goal, g + cost, bound, path, visited)
        
        # If goal found, propagate the result up
        if result is not None:
            return t, result
            
        # Update minimum bound for next iteration
        if t < min_bound:
            min_bound = t
            
        # Remove child from path (backtrack)
        path.pop()
    
    # Remove node from visited set as we're backtracking
    visited.remove(node)
    
    # Return the new bound and None (no path found within current bound)
    return min_bound, None

def ida_star(tree, heur, start, goal):
    """Iterative Deepening A* search algorithm.
    
    Args:
        tree: Dictionary mapping nodes to their children with costs
        heur: Dictionary mapping nodes to their heuristic values
        start: Starting node
        goal: Goal node
        
    Returns:
        Path from start to goal if found, None otherwise
    """
    # Initial bound is the heuristic value of the start node
    bound = heur.get(start, float('inf'))
    
    # Initialize path with start node
    path = [start]
    
    # Iteratively increase bound until goal is found or no path exists
    while True:
        # Perform depth-first search with current bound
        t, result = dfs_f(tree, heur, start, goal, 0, bound, path, set())
        
        # If goal found, return the path
        if result is not None:
            return result
            
        # If bound is infinity, no path exists
        if t == float('inf'):
            return None
            
        # Increase bound for next iteration
        bound = t

def main():
    print("IDA* (Iterative Deepening A*) Search Algorithm")
    print("---------------------------------------------")
    print("IDA* combines the memory efficiency of iterative deepening")
    print("with the effectiveness of A* search using heuristics.")
    
    # Get user input for the tree structure with heuristics and costs
    print("\nInput Format:")
    print("For each node enter: node heuristic child1:cost1 child2:cost2 ...")
    print("Example: A 5 B:2 C:3 (means node A has heuristic 5 and connects to B with cost 2 and C with cost 3)")
    
    n = int(input("\nNumber of nodes: "))
    tree = {}
    heur = {}
    
    for i in range(n):
        line = input(f"Node {i+1}/{n}: ")
        parts = line.split()
        
        # Handle empty input
        if not parts:
            print("Empty input, please try again.")
            i -= 1
            continue
            
        # Need at least node and heuristic
        if len(parts) < 2:
            print("Each line must have at least a node name and heuristic value.")
            i -= 1
            continue
            
        # Extract node and heuristic
        node = parts[0]
        try:
            heur[node] = float(parts[1])
        except ValueError:
            print(f"Heuristic must be a number. Using 0 for node {node}.")
            heur[node] = 0
            
        # Extract children with costs
        children = []
        for ch in parts[2:]:
            if ':' not in ch:
                print(f"Warning: {ch} doesn't have format child:cost. Skipping.")
                continue
            try:
                c, w = ch.split(':')
                cost = float(w)
                children.append((c, cost))
            except ValueError:
                print(f"Warning: Cost must be a number in {ch}. Skipping.")
                
        tree[node] = children

    # Get start and goal nodes
    start = input("Start node: ")
    goal = input("Goal node: ")
    
    # Validate input
    if start not in tree:
        print(f"Error: Start node '{start}' not found in tree")
        return
    if goal not in heur:
        print(f"Error: Goal node '{goal}' not found in tree")
        return
    
    # Run IDA* search
    print("\nSearching for path using IDA*...")
    path = ida_star(tree, heur, start, goal)
    
    # Display result
    if path:
        print("\nPath found:", " → ".join(path))
        
        # Calculate path cost
        total_cost = 0
        for i in range(len(path) - 1):
            current = path[i]
            next_node = path[i+1]
            for child, cost in tree.get(current, []):
                if child == next_node:
                    total_cost += cost
                    break
        print(f"Total path cost: {total_cost}")
    else:
        print("\nNo path found from", start, "to", goal)

if __name__ == "__main__":
    main()
