import random
import math

def distance(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

def path_length(path, coords):
    return sum(distance(coords[path[i]], coords[path[(i+1)%len(path)]]) for i in range(len(path)))

def genetic_tsp(coords, pop_size=100, generations=500, mutate_rate=0.01):
    num_cities = len(coords)
    def create_ind():
        return random.sample(range(num_cities), num_cities)
    def crossover(a, b):
        start, end = sorted(random.sample(range(num_cities), 2))
        child = a[start:end] + [c for c in b if c not in a[start:end]]
        return child
    def mutate(ind):
        if random.random() < mutate_rate:
            i,j = sorted(random.sample(range(num_cities), 2))
            ind[i],ind[j] = ind[j],ind[i]
    
    population = [create_ind() for _ in range(pop_size)]
    best_individual = None
    best_distance = float('inf')
    
    for gen in range(generations):
        population.sort(key=lambda ind: path_length(ind, coords))
        current_best = population[0]
        current_distance = path_length(current_best, coords)
        
        if current_distance < best_distance:
            best_distance = current_distance
            best_individual = current_best.copy()
            
        next_gen = population[:pop_size//2]
        while len(next_gen) < pop_size:
            parents = random.sample(next_gen, 2)
            child = crossover(*parents)
            mutate(child)
            next_gen.append(child)
        population = next_gen
        
    return best_individual, best_distance

def main():
    print("Genetic Algorithm for Traveling Salesman Problem")
    n = int(input("Enter number of cities: "))
    
    print("Enter coordinates for each city (x y), one per line:")
    coords = []
    for i in range(n):
        x, y = map(float, input().split())
        coords.append((x, y))
    
    pop_size = int(input("Enter population size (default 100): ") or "100")
    generations = int(input("Enter number of generations (default 500): ") or "500")
    mutate_rate = float(input("Enter mutation rate (default 0.01): ") or "0.01")
    
    print("\nRunning genetic algorithm...")
    best_path, best_distance = genetic_tsp(coords, pop_size, generations, mutate_rate)
    
    print("\nGenetic Algorithm TSP Result:")
    print("Best Path Found:", " -> ".join(str(city) for city in best_path) + " -> " + str(best_path[0]))
    print("Total Distance:", best_distance)
    
    print("\nCity Order:")
    for i, city_idx in enumerate(best_path):
        print(f"Stop {i+1}: City {city_idx} at coordinates {coords[city_idx]}")

if __name__ == "__main__":
    main()