import random
MAX_CAPACITY=100
POPULATION_SIZE=4
ITERATIONS=10
MUTATION_BITS=[3,2,1,0]
items=[
    {"name":"A","weight":45,"value":3},
    {"name":"B","weight":40,"value":5},
    {"name":"C","weight":50,"value":8},
    {"name":"D","weight":90,"value":10},
]

def create_random_chromosome():
    return [random.randint(0,1) for _ in range(len(items))]

def calculate_fitness(chromosome):
    total_weight=sum(chromosome[i]*items[i]["weight"] for i in range(len(items)))
    total_value=sum(chromosome[i]*items[i]["weight"] for i in range(len(items)))
    if total_weight>MAX_CAPACITY:
        total_value=0
    return total_value

def selection(population):
    sorted_population=sorted(population,key=lambda c: calculate_fitness(c), reverse=True)
    return sorted_population[:2]

def crossover(parent1, parent2):
    crossover_point=len(parent1)//2
    child=parent1[:crossover_point]+parent2[crossover_point:]
    return child

def mutation(chromosome):
    mutated_choromosome=chromosome.copy()
    for bit in MUTATION_BITS:
        mutated_choromosome[bit]=1-mutated_choromosome[bit]
    return mutated_choromosome

population=[create_random_chromosome() for _ in range(POPULATION_SIZE)]

for iteration in range(ITERATIONS):
    print(f"Iterantion {iteration+1}:")
    print("Population: ",population)
    selected=selection(population)
    print("Selected: ",selected)
    offspring=crossover(selected[0],selected[1])
    print("Offsprig: ",offspring)
    mutated_offspring=mutation(offspring)
    print("Mutated Offsprig: ",mutated_offspring)
    least_fix_index=min(enumerate(population), key=lambda x:calculate_fitness(x[1]))[0]
    population[least_fix_index]=mutated_offspring
    print("")
best_chromosome=max(population, key=lambda c:calculate_fitness(c))
print("Final Best Chromosome: ",best_chromosome)
print("Final Fitness Value: ", calculate_fitness(best_chromosome))
    