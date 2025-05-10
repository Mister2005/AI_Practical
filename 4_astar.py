import heapq

def astar(tree, heur, start, goal):
    open_set = [(heur[start], 0, start, [start])]
    closed = set()
    while open_set:
        f, g, node, path = heapq.heappop(open_set)
        if node == goal:
            return path
        if node in closed:
            continue
        closed.add(node)
        for child, cost in tree.get(node, []):
            if child in closed:
                continue
            g2 = g + cost
            f2 = g2 + heur.get(child, float('inf'))
            heapq.heappush(open_set, (f2, g2, child, path + [child]))
    return None

def main():
    print("A* Search on a tree (weighted edges + heuristic)")
    print("\nInput Format:")
    print("- First enter number of nodes")
    print("- For each node enter: node_name heuristic_value [child1:cost1 child2:cost2 ...]")
    print("Example: 0 10 1:4 2:3")
    
    n = int(input("\nNumber of nodes: "))
    print("Enter each node, its heuristic value, then children as child:cost ...")
    tree = {}
    heur = {}
    
    try:
        for _ in range(n):
            parts = input().split()
            if len(parts) < 2:
                raise ValueError("Each line must have at least node name and heuristic value")
                
            node = parts[0]
            heur[node] = float(parts[1])
            children = []
            
            for ch in parts[2:]:
                if ':' not in ch:
                    raise ValueError(f"Child format must be 'child:cost', got '{ch}'")
                c, w = ch.split(':')
                children.append((c, float(w)))
            tree[node] = children

        start = input("Start node: ")
        goal = input("Goal node: ")
        
        if start not in tree:
            raise ValueError(f"Start node '{start}' not found in tree")
        if goal not in heur:
            raise ValueError(f"Goal node '{goal}' not found in tree")
            
        path = astar(tree, heur, start, goal)
        if path:
            print("Path found:", " → ".join(path))
        else:
            print("No path found.")
            
    except ValueError as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()