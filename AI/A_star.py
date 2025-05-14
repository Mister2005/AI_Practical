import heapq

def a_star(graph, start, goal, h):
    open_set = [(h(start), 0, start)]
    came_from = {}
    g_score = {start: 0}
    closed = set()

    while open_set:
        f, cost, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from.get(current)
            return path[::-1]
        closed.add(current)
        for neighbor, w in graph.get(current, []):
            tentative_g = g_score[current] + w
            if neighbor in closed and tentative_g >= g_score.get(neighbor, float('inf')):
                continue
            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                heapq.heappush(open_set, (tentative_g + h(neighbor), tentative_g, neighbor))
    return []

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
    
    path = a_star(graph, start, goal, h)
    
    print("\nA* Search Result:")
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