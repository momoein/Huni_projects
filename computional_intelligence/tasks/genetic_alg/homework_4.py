import numpy as np
import random



def calculate_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# edge distances
def individual_edges_distance(array):
    distances = np.zeros(array.shape[0] - 1)
    for i in range(len(array)-1):
        distances[i] = calculate_distance(array[i], array[i+1])
    return distances


# Function to calculate the total distance of a route
def calculate_total_distance(rout):
    edges_distance = individual_edges_distance(rout)
    return np.sum(edges_distance)


# Function to generate an initial population of routes
def generate_initial_population(num_individuals, cities):
    population = []
    for _ in range(num_individuals):
        new_citise = np.array(cities)
        np.random.shuffle(new_citise)
        population.append(new_citise)
    return population


# Function to perform crossover between two parent routes
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    parent1_ = list(parent1)
    parent2_ = list(parent2)
    #
    child1 = parent1_[:crossover_point] + parent2_[crossover_point:]
    child2 = parent2_[:crossover_point] + parent1_[crossover_point:]
    return np.array(child1), np.array(child2)

# Function to perform mutation on a route
def mutate(route):
    index1, index2 = random.sample(range(len(route)), 2)
    route[index1], route[index2] = route[index2], route[index1]
    return route

# Fmax - F(x) 
def fitness(individual, Fmax=20*500): # 500 is biggest distance between two city
    fitx = calculate_total_distance(individual)
    return Fmax - fitx

# Function to select individuals for the next generation
def selection(population):
    fitness_scores = [1 / calculate_total_distance(route) for route in population]
    total_fitness = sum(fitness_scores)
    probabilities = [score / total_fitness for score in fitness_scores]
    selected_indices = random.choices(range(len(population)), probabilities, k=len(population))
    selected_population = [population[i] for i in selected_indices]
    return selected_population 


# Function to evolve the population using crossover and mutation
def evolve_population(population, mutation_rate):
    selected_population = selection(population)
    next_generation = []

    # Perform crossover
    for i in range(0, len(selected_population)-1, 2):
        parent1 = selected_population[i]
        parent2 = selected_population[i + 1]
        child1, child2 = crossover(parent1, parent2)
        next_generation.extend([child1, child2])

    # Perform mutation
    for i in range(len(next_generation)):
        if random.random() < mutation_rate:
            next_generation[i] = mutate(next_generation[i])

    return next_generation


# Main Genetic Algorithm function
def genetic_algorithm(cities, num_generations, num_individuals, mutation_rate):
    population = generate_initial_population(num_individuals, cities)

    for generation in range(num_generations):
        population = evolve_population(population, mutation_rate)
        best_route = min(population, key=lambda route: calculate_total_distance(route))
        best_distance = calculate_total_distance(best_route)
        # print(f"Generation {generation + 1}, Best Distance: {best_distance}")

    best_route = min(population, key=lambda route: calculate_total_distance(route))
    best_distance = calculate_total_distance(best_route)
    # print(f"\nBest Route: {[tuple(city) for city in best_route]}")
    print(f"Best Distance: {best_distance}")





if __name__ == "__main__":

    citise = [
        [35, 51],
        [113, 213],
        [82, 280],
        [322, 340],
        [256, 352],
        [160, 24],
        [322, 145],
        [12, 349],
        [282, 20],
        [241, 8],
        [398, 153],
        [182, 305],
        [153, 257],
        [275, 190],
        [242, 75],
        [19, 229],
        [303, 352],
        [39, 309],
        [383, 79],
        [226, 343]
    ]
    
    num_generations = 70
    num_individuals = 25
    mutation_rate = 0.1

    genetic_algorithm(citise, num_generations, num_individuals, mutation_rate)
    