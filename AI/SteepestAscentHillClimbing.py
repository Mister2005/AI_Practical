import random
import math

def distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def tour_length(tour, coords):
    return sum(distance(coords[tour[i]], coords[tour[(i+1) % len(tour)]])
               for i in range(len(tour)))

def get_neighbors(tour):
    """Generate all 2-swap neighbors."""
    n = len(tour)
    for i in range(n - 1):
        for j in range(i + 1, n):
            neighbor = tour.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            yield neighbor

def steepest_ascent_hc(coords, max_iter=1000):
    """At each step, pick the neighbor with the steepest improvement."""
    n = len(coords)
    current = list(range(n))
    random.shuffle(current)
    current_length = tour_length(current, coords)
    
    iterations = 0
    for _ in range(max_iter):
        iterations += 1
        best_neighbor = None
        best_length = current_length
        for neighbor in get_neighbors(current):
            length = tour_length(neighbor, coords)
            if length < best_length:
                best_length = length
                best_neighbor = neighbor

        if best_neighbor is None:
            break  # no improvement
        current, current_length = best_neighbor, best_length

    return current, current_length, iterations

def main():
    print("Steepest Ascent Hill Climbing for TSP")
    n = int(input("Enter number of cities: "))
    
    print("Enter coordinates for each city (x y), one per line:")
    coords = []
    for i in range(n):
        x, y = map(float, input().split())
        coords.append((x, y))
    
    max_iter = int(input("Enter maximum iterations (default 1000): ") or "1000")
    
    print("\nRunning Steepest Ascent Hill Climbing...")
    tour, length, iterations = steepest_ascent_hc(coords, max_iter)
    
    print("\nSteepest Ascent Hill Climbing Results:")
    print("Tour:", " -> ".join(str(city) for city in tour) + " -> " + str(tour[0]))
    print("Tour Length:", length)
    print("Iterations performed:", iterations)
    
    print("\nCity Order:")
    for i, city_idx in enumerate(tour):
        print(f"Stop {i+1}: City {city_idx} at coordinates {coords[city_idx]}")

if __name__ == "__main__":
    main()