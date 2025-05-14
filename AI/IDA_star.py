def ida_star(start, goal_test, successors, h):
    bound = h(start)
    path = [start]
    while True:
        t = search(path, 0, bound, goal_test, successors, h)
        if t == 'FOUND':
            return path
        if t == float('inf'):
            return []
        bound = t

def search(path, g, bound, goal_test, successors, h):
    node = path[-1]
    f = g + h(node)
    if f > bound:
        return f
    if goal_test(node):
        return 'FOUND'
    min_bound = float('inf')
    for succ, cost in successors(node):
        if succ not in path:
            path.append(succ)
            t = search(path, g+cost, bound, goal_test, successors, h)
            if t == 'FOUND':
                return 'FOUND'
            if t < min_bound:
                min_bound = t
            path.pop()
    return min_bound

def main():
    print("Enter number of nodes:")
    n = int(input())
    
    graph = {}
    print("Enter edges in format 'source destination weight', one per line (empty line to finish):")
    
    while True:
        line = input().strip()
        if not line:
            break
        parts = line.split()
        if len(parts) >= 3:
            source, dest, weight = parts[0], parts[1], int(parts[2])
            if source not in graph:
                graph[source] = []
            graph[source].append((dest, weight))
    
    start = input("Enter start node: ")
    goal = input("Enter goal node: ")
    
    print("Enter heuristic values for each node in format 'node value':")
    heuristic_values = {}
    for _ in range(n):
        line = input().strip()
        if not line:
            break
        parts = line.split()
        if len(parts) == 2:
            node, value = parts[0], int(parts[1])
            heuristic_values[node] = value
    
    def h(node):
        return heuristic_values.get(node, 0)
    
    def successors(node):
        return graph.get(node, [])
    
    def goal_test(node):
        return node == goal
    
    path = ida_star(start, goal_test, successors, h)
    
    print("\nIDA* Search Result:")
    if path:
        print("Path Found:", " -> ".join(path))
        
        total_cost = 0
        for i in range(len(path) - 1):
            current = path[i]
            for neighbor, weight in graph.get(current, []):
                if neighbor == path[i + 1]:
                    total_cost += weight
                    break
        
        print("Path Length:", len(path))
        print("Total Cost:", total_cost)
    else:
        print("No path found from", start, "to", goal)

if __name__ == "__main__":
    main()