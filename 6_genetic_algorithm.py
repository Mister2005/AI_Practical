import random

def fitness(chromosome):
    """Calculate fitness of a chromosome (count of 1s in the bitstring).
    
    Args:
        chromosome: A string of 0s and 1s representing a chromosome
        
    Returns:
        The number of 1s in the chromosome (higher is better)
    """
    return sum(int(bit) for bit in chromosome)

def select_parent(population, fitness_values):
    """Select a parent from the population using fitness proportionate selection (roulette wheel).
    
    Args:
        population: List of chromosomes
        fitness_values: List of fitness values corresponding to each chromosome
        
    Returns:
        A selected chromosome
    """
    # Calculate total fitness
    total_fitness = sum(fitness_values)
    
    # Generate a random value between 0 and total fitness
    selection_point = random.uniform(0, total_fitness)
    
    # Find the chromosome that corresponds to this point
    current_sum = 0
    for i, fitness_value in enumerate(fitness_values):
        current_sum += fitness_value
        if current_sum >= selection_point:
            return population[i]
    
    # Fallback (should not reach here)
    return population[-1]

def crossover(parent1, parent2):
    """Create two offspring by crossing over two parents at a random point.
    
    Args:
        parent1: First parent chromosome
        parent2: Second parent chromosome
        
    Returns:
        Tuple of (child1, child2) resulting from crossover
    """
    # Choose a random crossover point (excluding endpoints)
    crossover_point = random.randint(1, len(parent1) - 1)
    
    # Create children by swapping segments
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    
    return child1, child2

def mutate(chromosome, mutation_rate):
    """Randomly mutate bits in a chromosome based on mutation rate.
    
    Args:
        chromosome: The chromosome to mutate
        mutation_rate: Probability of each bit being flipped
        
    Returns:
        Mutated chromosome
    """
    # For each bit, flip it with probability = mutation_rate
    mutated = ''.join(
        '1' if bit == '0' else '0' if random.random() < mutation_rate else bit
        for bit in chromosome
    )
    return mutated

def genetic_algorithm(pop_size, chrom_length, crossover_rate, mutation_rate, generations):
    """Run the genetic algorithm to maximize the number of 1s in a bitstring.
    
    Args:
        pop_size: Size of the population
        chrom_length: Length of each chromosome (bitstring)
        crossover_rate: Probability of crossover occurring
        mutation_rate: Probability of each bit being mutated
        generations: Number of generations to run
        
    Returns:
        The best chromosome found
    """
    # Create initial random population
    population = [
        ''.join(random.choice('01') for _ in range(chrom_length))
        for _ in range(pop_size)
    ]
    
    # Evolution process
    for generation in range(generations):
        # Calculate fitness for each chromosome
        fitness_values = [fitness(chromosome) for chromosome in population]
        
        # Create the next generation
        new_population = []
        
        # Keep creating offspring until we have a full new population
        while len(new_population) < pop_size:
            # Select two parents
            parent1 = select_parent(population, fitness_values)
            parent2 = select_parent(population, fitness_values)
            
            # Apply crossover with some probability
            if random.random() < crossover_rate:
                child1, child2 = crossover(parent1, parent2)
            else:
                # No crossover, just copy the parents
                child1, child2 = parent1, parent2
            
            # Apply mutation
            child1 = mutate(child1, mutation_rate)
            new_population.append(child1)
            
            # Add second child if we still need more chromosomes
            if len(new_population) < pop_size:
                child2 = mutate(child2, mutation_rate)
                new_population.append(child2)
        
        # Replace old population with new generation
        population = new_population
    
    # Return best chromosome from final population
    return max(population, key=fitness)

def main():
    print("Genetic Algorithm")
    print("----------------")
    print("This algorithm evolves a bitstring to maximize the number of 1s.")
    print("It demonstrates selection, crossover, and mutation operations.")
    
    # Get algorithm parameters from user
    pop_size = int(input("Population size: "))
    chrom_len = int(input("Chromosome length: "))
    cross_rate = float(input("Crossover rate [0-1]: "))
    mut_rate = float(input("Mutation rate [0-1]: "))
    generations = int(input("Number of generations: "))
    
    # Run the genetic algorithm
    best_chromosome = genetic_algorithm(pop_size, chrom_len, cross_rate, mut_rate, generations)
    
    # Calculate and display the result
    best_fitness = fitness(best_chromosome)
    max_possible = chrom_len
    percentage = (best_fitness / max_possible) * 100
    
    print("\nResults:")
    print("-" * 30)
    print(f"Best solution: {best_chromosome}")
    print(f"Fitness: {best_fitness}/{max_possible} ones ({percentage:.1f}%)")

if __name__ == "__main__":
    main()