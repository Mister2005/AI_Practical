import heapq

def astar(tree, heur, start, goal):
    """A* Search Algorithm
    
    Args:
        tree: Dictionary mapping nodes to their children with costs: {node: [(child1, cost1), (child2, cost2)]}
        heur: Dictionary mapping nodes to their heuristic values: {node: heuristic_value}
        start: Starting node
        goal: Goal node
    
    Returns:
        Path list from start to goal, or None if no path exists
    """
    # Priority queue for A*, each entry is: (f_score, g_score, node, path)
    # f_score = g_score + heuristic (estimated total cost)
    # g_score = cost from start to this node (actual path cost so far)
    open_set = [(heur[start], 0, start, [start])]
    
    # Set of nodes already evaluated
    closed = set()
    
    while open_set:
        # Get node with lowest f_score from priority queue
        f, g, node, path = heapq.heappop(open_set)
        
        # If we found the goal, return the path
        if node == goal:
            return path
            
        # Skip if already evaluated
        if node in closed:
            continue
            
        # Mark as evaluated
        closed.add(node)
        
        # Check all neighbors
        for child, cost in tree.get(node, []):
            # Skip already evaluated neighbors
            if child in closed:
                continue
                
            # Calculate new g_score (cost from start to neighbor through current node)
            g2 = g + cost
            
            # Calculate f_score (g_score + heuristic)
            f2 = g2 + heur.get(child, float('inf'))
            
            # Add to priority queue
            heapq.heappush(open_set, (f2, g2, child, path + [child]))
            
    # No path found
    return None

def main():
    print("A* Search Algorithm")
    print("------------------")
    print("A* combines the advantages of Dijkstra's algorithm and Greedy Best-First Search")
    print("to efficiently find the shortest path using heuristics.")
    
    print("\nInput Format:")
    print("- First enter number of nodes")
    print("- For each node enter: node_name heuristic_value [child1:cost1 child2:cost2 ...]")
    print("Example: A 10 B:4 C:3 (means node A has heuristic value 10 and connects to B with cost 4 and C with cost 3)")
    
    n = int(input("\nNumber of nodes: "))
    print("Enter each node, its heuristic value, then children as child:cost ...")
    tree = {}
    heur = {}
    
    try:
        # Build the tree and heuristic dictionary from user input
        for _ in range(n):
            parts = input().split()
            if len(parts) < 2:
                raise ValueError("Each line must have at least node name and heuristic value")
                
            node = parts[0]
            heur[node] = float(parts[1])
            children = []
            
            # Parse each child:cost pair
            for ch in parts[2:]:
                if ':' not in ch:
                    raise ValueError(f"Child format must be 'child:cost', got '{ch}'")
                c, w = ch.split(':')
                children.append((c, float(w)))
            tree[node] = children

        # Get start and goal nodes
        start = input("Start node: ")
        goal = input("Goal node: ")
        
        # Validate input
        if start not in tree:
            raise ValueError(f"Start node '{start}' not found in tree")
        if goal not in heur:
            raise ValueError(f"Goal node '{goal}' not found in tree")
        
        # Run A* search
        path = astar(tree, heur, start, goal)
        
        # Display the result
        if path:
            print("Path found:", " → ".join(path))
        else:
            print("No path found from", start, "to", goal)
            
    except ValueError as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()