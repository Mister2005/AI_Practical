import random

def input_tsp():
    n = int(input("Enter number of cities: "))
    print("Enter distance matrix row by row (space separated):")
    dist = []
    for i in range(n):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        assert len(row) == n, "Each row must have n entries"
        dist.append(row)
    return dist

def tour_cost(tour, dist):
    cost = 0
    for i in range(len(tour)):
        j = (i + 1) % len(tour)
        cost += dist[tour[i]][tour[j]]
    return cost

def two_opt_neighbors(tour):
    neighbors = []
    n = len(tour)
    for i in range(n - 1):
        for j in range(i + 1, n):
            nbr = tour.copy()
            nbr[i], nbr[j] = nbr[j], nbr[i]
            neighbors.append(nbr)
    return neighbors

def simple_hill_climbing(dist, start_tour):
    current = start_tour
    current_cost = tour_cost(current, dist)
    path = [current_cost]

    while True:
        improved = False
        for nbr in two_opt_neighbors(current):
            c = tour_cost(nbr, dist)
            if c < current_cost:
                current, current_cost = nbr, c
                path.append(current_cost)
                improved = True
                break
        if not improved:
            break

    return current, current_cost, path

if __name__ == "__main__":
    dist = input_tsp()
    n = len(dist)
    start = list(range(n))
    random.shuffle(start)
    print("\nInitial random tour:", start, "cost =", tour_cost(start, dist))
    tour, cost, hist = simple_hill_climbing(dist, start.copy())
    print("\nSimple HC → tour:", tour, "\ncost =", cost)