# selection
# mutuation
# reproduction

from statistics import mean
import random
import os

import item_reader
import item_generator
import bruteforce

def get_total_value(items):
    total_value = 0
    for item in items:
        total_value += item[1]
    return total_value

def get_total_volume(items):
    total_volume = 0
    for item in items:
        total_volume += item[2]
    return total_volume

def summarise_combination(dna_string):
    combination = items_from_dna(dna_string)
    print("Fitness:", fitness(dna_string), "Total value:", get_total_value(combination), "Total volume:", get_total_volume(combination))


def summarise_combinations(dna_strings):
    combinations = list(map(items_from_dna, dna_strings))
    average_fitness = mean(map(fitness, dna_strings))
    average_value = mean(map(get_total_value, combinations))
    average_volume = mean(map(get_total_volume, combinations))
    print("Average fitness:", average_fitness, "Average value:", average_value, "Average volume:", average_volume)


def random_combination(items):
    dna_string = ""
    for _ in range(len(items)):
        # dna_string += str(random.sample(range(2), k=1, counts=(15, 1))[0])
        dna_string += str(random.choice([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]))
    return dna_string


def random_population(amount):
    population = []
    for _ in range(amount):
        dna_string = random_combination(items)
        population.append(dna_string)
    return population


def items_from_dna(dna_string):
    combination = []
    zipped = zip(dna_string, items)
    for gene, item in zipped:
        if gene == "1":
            combination.append(item)
    return combination


def fitness(dna_string):
    combination = items_from_dna(dna_string)
    value = get_total_value(combination)
    volume = get_total_volume(combination)
    if volume > 100:
        return 0
    else:
        return value


def selection(population):
    weights = []
    for dna in population:
        f = fitness(dna)
        f_constrained = max([f, selection_floor])
        weights.append(f_constrained)
    parents = random.choices(population, k=2, weights=weights)
    return parents


def mutate(dna_string, rate=0.025):
    if random.random() < rate:
        mutated_index = random.randrange(len(dna_string))
        current = dna_string[mutated_index]
        if current == "1":
            return dna_string[:mutated_index] + "0" + dna_string[mutated_index+1:]
        else:
            return dna_string[:mutated_index] + "1" + dna_string[mutated_index+1:]
    return dna_string


def reproduce(parents):
    # single point crossover
    parent_a, parent_b = parents
    crossover_point = random.randrange(len(parent_a))
    child_a = parent_a[:crossover_point] + parent_b[crossover_point:]
    child_b = parent_b[:crossover_point] + parent_a[crossover_point:]
    return child_a, child_b



def simulate(population, elitism=0):
    pairs = (len(population) - elitism) // 2
    next_generation = []
    if elitism:
        next_generation.extend(sorted(population, key=fitness, reverse=True)[0:elitism])
    for _ in range(pairs):
        parents = selection(population)
        children = reproduce(parents)
        for child in children:
            next_generation.append(mutate(child, rate=mutation_rate))
    return next_generation



def evolve(items):
    population = random_population(population_size)

    for generations in range(number_of_generations):
        population = simulate(population, elitism=elitism)
        best = max(population, key=fitness)

        os.system("cls")
        print("Generation:", generations, end=",  ")
        summarise_combinations(population)
        print("Best:", fitness(best))


    print("Best:", best, end=",  ")
    summarise_combination(best)

    for item in items_from_dna(best):
        print(item[0], end=", ")



population_size = 50
number_of_generations = 500
mutation_rate = 0.15
selection_floor = 50
elitism = 2
items = item_generator.create()

evolve(items)