import random
import math

def distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def tour_length(tour, coords):
    return sum(distance(coords[tour[i]], coords[tour[(i+1) % len(tour)]])
               for i in range(len(tour)))

def random_neighbor(current):
    n = len(current)
    i, j = random.sample(range(n), 2)
    neighbor = current.copy()
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor

def stochastic_hc(coords, max_iter=1000, restarts=10):
    n = len(coords)
    best_overall, best_len = None, float('inf')
    total_iterations = 0

    for restart in range(restarts):
        current = list(range(n))
        random.shuffle(current)
        current_length = tour_length(current, coords)
        restart_iterations = 0

        for _ in range(max_iter):
            restart_iterations += 1
            total_iterations += 1
            neighbor = random_neighbor(current)
            length = tour_length(neighbor, coords)
            if length < current_length:
                current, current_length = neighbor, length

        if current_length < best_len:
            best_overall, best_len = current, current_length
        
        print(f"Restart {restart+1}: Tour length = {current_length:.2f}")

    return best_overall, best_len, total_iterations

def main():
    print("Stochastic Hill Climbing for TSP")
    n = int(input("Enter number of cities: "))
    
    print("Enter coordinates for each city (x y), one per line:")
    coords = []
    for i in range(n):
        x, y = map(float, input().split())
        coords.append((x, y))
    
    max_iter = int(input("Enter maximum iterations per restart (default 1000): ") or "1000")
    restarts = int(input("Enter number of restarts (default 10): ") or "10")
    
    print("\nRunning Stochastic Hill Climbing...")
    tour, length, iterations = stochastic_hc(coords, max_iter, restarts)
    
    print("\nStochastic Hill Climbing Results:")
    print("Best Tour:", " -> ".join(str(city) for city in tour) + " -> " + str(tour[0]))
    print("Best Tour Length:", length)
    print("Total Iterations:", iterations)
    
    print("\nCity Order:")
    for i, city_idx in enumerate(tour):
        print(f"Stop {i+1}: City {city_idx} at coordinates {coords[city_idx]}")

if __name__ == "__main__":
    main()