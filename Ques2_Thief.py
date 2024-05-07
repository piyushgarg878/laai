import random
MAX_CAPACITY=9
POPULATION_SIZE=4
ITERATIONS=4
MUTATION_BITS=[2,0,3,1]
items=[
    {"name":"Mirror","weight":2,"value":3},
    {"name":"Silver Nugget","weight":3,"value":5},
    {"name":"Painting","weight":4,"value":7},
    {"name":"Vase","weight":5,"value":9},
]

def create_initial_population():
    return [
        [1,1,1,1],
        [1,0,0,0],
        [1,0,1,0],
        [1,0,0,1]
    ]

def calculate_fitness(chromosome):
    total_weight=sum(chromosome[i]*items[i]["weight"] for i in range(len(items)))
    total_value=sum(chromosome[i]*items[i]["value"] for i in range(len(items)))
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

population=create_initial_population()

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
selected_items=[items[i]["name"] for i in range(len(items)) if best_chromosome[i]==1]
print("Final Best Chromosome: ",best_chromosome)
print("Selected Items: ",selected_items)
print("Final Fitness Value: ", calculate_fitness(best_chromosome))
    