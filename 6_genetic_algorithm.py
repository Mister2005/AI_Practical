import random

def fitness(chrom):
    return sum(int(bit) for bit in chrom)

def select_pair(pop, fits):
    total = sum(fits)
    pick = random.uniform(0, total)
    upto = 0
    for i, f in enumerate(fits):
        if upto + f >= pick:
            return pop[i]
        upto += f

def crossover(a, b):
    i = random.randint(1, len(a)-1)
    return a[:i] + b[i:], b[:i] + a[i:]

def mutate(chrom, rate):
    return ''.join(
        bit if random.random() > rate else str(1-int(bit))
        for bit in chrom
    )

def main():
    print("Genetic Algorithm (maximize number of 1s in a bitstring)")
    pop_size = int(input("Population size: "))
    chrom_len = int(input("Chromosome length: "))
    cross_rate = float(input("Crossover rate [0-1]: "))
    mut_rate   = float(input("Mutation rate [0-1]: "))
    gens       = int(input("Number of generations: "))

    population = [
        ''.join(random.choice('01') for _ in range(chrom_len))
        for _ in range(pop_size)
    ]

    for g in range(gens):
        fits = [fitness(c) for c in population]
        new_pop = []
        while len(new_pop) < pop_size:
            p1 = select_pair(population, fits)
            p2 = select_pair(population, fits)
            if random.random() < cross_rate:
                c1, c2 = crossover(p1, p2)
            else:
                c1, c2 = p1, p2
            new_pop.append(mutate(c1, mut_rate))
            if len(new_pop) < pop_size:
                new_pop.append(mutate(c2, mut_rate))
        population = new_pop

    best = max(population, key=fitness)
    print("Best solution:", best, "\nfitness =", fitness(best))

if __name__ == "__main__":
    main()