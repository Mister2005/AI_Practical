import random
import math

def distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def tour_length(tour, coords):
    return sum(distance(coords[tour[i]], coords[tour[(i+1) % len(tour)]])
               for i in range(len(tour)))

def get_neighbors(tour):
    n = len(tour)
    for i in range(n - 1):
        for j in range(i + 1, n):
            neighbor = tour.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            yield neighbor

def simple_hill_climbing(coords, max_iter=1000):
    n = len(coords)
    current = list(range(n))
    random.shuffle(current)
    current_length = tour_length(current, coords)
    initial_length = current_length
    iterations = 0

    for _ in range(max_iter):
        iterations += 1
        improved = False
        for neighbor in get_neighbors(current):
            length = tour_length(neighbor, coords)
            if length < current_length:
                current, current_length = neighbor, length
                improved = True
                break
        if not improved:
            break

    return current, current_length, initial_length, iterations

def main():
    print("Simple Hill Climbing for TSP")
    n = int(input("Enter number of cities: "))
    
    print("Enter coordinates for each city (x y), one per line:")
    coords = []
    for i in range(n):
        x, y = map(float, input().split())
        coords.append((x, y))
    
    max_iter = int(input("Enter maximum iterations (default 1000): ") or "1000")
    
    print("\nRunning Simple Hill Climbing...")
    tour, final_length, initial_length, iterations = simple_hill_climbing(coords, max_iter)
    
    print("\nSimple Hill Climbing Results:")
    print("Initial Tour Length:", initial_length)
    print("Final Tour Length:", final_length)
    print("Improvement:", f"{initial_length - final_length:.2f} ({(initial_length - final_length) / initial_length * 100:.2f}%)")
    print("Iterations performed:", iterations)
    print("\nFinal Tour:", " -> ".join(str(city) for city in tour) + " -> " + str(tour[0]))
    
    print("\nCity Order:")
    for i, city_idx in enumerate(tour):
        print(f"Stop {i+1}: City {city_idx} at coordinates {coords[city_idx]}")

if __name__ == "__main__":
    main()