import numpy as np
import random
import math

def calculate_path_distance(path, distance_matrix):
    """Calculate the total distance of a path in the TSP.
    
    Args:
        path: List of cities in visit order
        distance_matrix: Matrix of distances between cities
        
    Returns:
        Total distance of the path (including return to start)
    """
    total_distance = 0
    # Add up distances between consecutive cities
    for i in range(len(path)):
        # Use modulo to connect the last city back to the first
        total_distance += distance_matrix[path[i]][path[(i + 1) % len(path)]]
    return total_distance

def get_random_neighbor(path):
    """Generate a neighbor solution by swapping two cities.
    
    Args:
        path: Current path (list of cities)
        
    Returns:
        New path with two random cities swapped
    """
    # Select two random cities (excluding the start city at index 0)
    i = random.randint(1, len(path) - 1)
    j = random.randint(1, len(path) - 1)
    while i == j:
        j = random.randint(1, len(path) - 1)
    
    # Create a new path by swapping the cities
    neighbor = path.copy()
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor

def hill_climbing_tsp(distance_matrix, start_city=0):
    """Hill Climbing algorithm for the Traveling Salesman Problem.
    
    Args:
        distance_matrix: Matrix of distances between cities
        start_city: Index of the starting city
        
    Returns:
        Tuple of (best path found, distance of that path)
    """
    n = len(distance_matrix)
    
    # Start with a random path, keeping start_city fixed at the beginning
    current_path = list(range(n))
    current_path.remove(start_city)
    current_path = [start_city] + current_path
    current_distance = calculate_path_distance(current_path, distance_matrix)
    
    # Keep improving until no better neighbor is found
    improved = True
    while improved:
        improved = False
        
        # Generate all neighbors by swapping pairs of cities
        best_neighbor = None
        best_distance = current_distance
        
        # Try all possible swaps of two cities (excluding start city)
        for i in range(1, len(current_path) - 1):
            for j in range(i + 1, len(current_path)):
                neighbor = current_path.copy()
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                
                # Calculate new distance
                distance = calculate_path_distance(neighbor, distance_matrix)
                
                # If better, update best neighbor
                if distance < best_distance:
                    best_distance = distance
                    best_neighbor = neighbor
                    improved = True
        
        # If we found a better neighbor, move to it
        if improved:
            current_path = best_neighbor
            current_distance = best_distance
    
    return current_path, current_distance

def simulated_annealing_tsp(distance_matrix, start_city=0, initial_temp=1000, 
                           cooling_rate=0.995, min_temp=1e-10, max_iterations=100000):
    """Simulated Annealing algorithm for the Traveling Salesman Problem.
    
    Args:
        distance_matrix: Matrix of distances between cities
        start_city: Index of the starting city
        initial_temp: Starting temperature (controls probability of accepting worse solutions)
        cooling_rate: Rate at which temperature decreases
        min_temp: Minimum temperature (stopping condition)
        max_iterations: Maximum number of iterations
        
    Returns:
        Tuple of (best path found, distance of that path)
    """
    n = len(distance_matrix)
    
    # Start with a random path, keeping start_city fixed at the beginning
    current_path = list(range(n))
    current_path.remove(start_city)
    random.shuffle(current_path)
    current_path = [start_city] + current_path
    current_distance = calculate_path_distance(current_path, distance_matrix)
    
    # Keep track of the best solution found
    best_path = current_path.copy()
    best_distance = current_distance
    
    # Initialize temperature
    temp = initial_temp
    iteration = 0
    
    # Main loop - continue until temperature is very low or max iterations reached
    while temp > min_temp and iteration < max_iterations:
        # Generate a neighbor by randomly swapping two cities
        neighbor_path = get_random_neighbor(current_path)
        neighbor_distance = calculate_path_distance(neighbor_path, distance_matrix)
        
        # Decide whether to accept the new solution
        # If better, always accept; if worse, accept with a probability
        delta = neighbor_distance - current_distance
        
        # For worse solutions, acceptance probability decreases as:
        # - The solution gets worse (higher delta)
        # - The temperature decreases
        acceptance_probability = math.exp(-delta / temp) if delta > 0 else 1.0
        
        # Accept the new solution based on probability
        if random.random() < acceptance_probability:
            current_path = neighbor_path
            current_distance = neighbor_distance
            
            # Update best solution if needed
            if current_distance < best_distance:
                best_path = current_path.copy()
                best_distance = current_distance
        
        # Gradually reduce temperature
        temp *= cooling_rate
        iteration += 1
    
    return best_path, best_distance

def main():
    print("Traveling Salesman Problem Solvers")
    print("----------------------------------")
    print("This program compares two optimization algorithms:")
    print("1. Hill Climbing - simple but gets stuck in local optima")
    print("2. Simulated Annealing - can escape local optima to find better solutions")
    
    # Get the number of cities
    n = int(input("Enter number of cities: "))
    
    # Get the distance matrix
    print("\nEnter the distance matrix (space-separated values):")
    print("Example for 3 cities:")
    print("0 10 15")
    print("10 0 20")
    print("15 20 0")
    
    distance_matrix = []
    for i in range(n):
        while True:
            try:
                row = list(map(float, input().split()))
                if len(row) != n:
                    print(f"Error: Please enter exactly {n} values for row {i+1}")
                    continue
                distance_matrix.append(row)
                break
            except ValueError:
                print("Error: Please enter numeric values only")
    
    distance_matrix = np.array(distance_matrix)
    
    # Select start city
    start_city = 0
    if n > 1:
        print("\nCities are numbered from 0 to", n-1)
        start_city = int(input(f"Enter start city (0 to {n-1}): "))
    
    # Run simulated annealing
    print("\nFinding optimal solution using Simulated Annealing...")
    sa_path, sa_distance = simulated_annealing_tsp(distance_matrix, start_city)
    
    # Run hill climbing
    print("Finding solution using Hill Climbing...")
    hc_path, hc_distance = hill_climbing_tsp(distance_matrix, start_city)
    
    # Display results
    print("\nRESULTS:")
    print("-" * 40)
    print("Simulated Annealing path:", " → ".join(map(str, sa_path)))
    print("Total distance:", sa_distance)
    
    print("\nHill Climbing path:", " → ".join(map(str, hc_path)))
    print("Total distance:", hc_distance)
    
    # Compare results
    if sa_distance < hc_distance:
        improvement = ((hc_distance - sa_distance) / hc_distance) * 100
        print("\nSimulated Annealing found a better solution!")
        print(f"Improvement over Hill Climbing: {improvement:.2f}%")
    elif sa_distance == hc_distance:
        print("\nBoth algorithms found the same solution.")
    else:
        print("\nHill Climbing found a better solution (unusual).")

if __name__ == "__main__":
    main()