import random

population = [
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 0, 0, 1, 0, 0]
]

def fitness(individual):
    return sum(individual)

def select(population):
    selected = random.sample(population, 3)
    selected.sort(key=fitness, reverse=True)
    return selected[0]

def crossover(p1, p2):
    if random.random() < 0.7:
        point = random.randint(1, len(p1) - 1)
        return p1[:point] + p2[point:], p2[:point] + p1[point:]
    return p1[:], p2[:]

def mutate(individual):
    for i in range(len(individual)):
        if random.random() < 0.01:
            individual[i] = 1 - individual[i]
    return individual

def genetic_algorithm():
    global population

    for gen in range(20):
        new_population = []
        while len(new_population) < len(population):
            p1 = select(population)
            p2 = select(population)
            c1, c2 = crossover(p1, p2)
            new_population.append(mutate(c1))
            new_population.append(mutate(c2))

        population = new_population[:len(population)]
        best = max(population, key=fitness)
        print(f"Gen {gen}: Best = {best}, Fitness = {fitness(best)}")

    print("\nFinal Best:", best, "\nwith fitness", fitness(best))

genetic_algorithm()