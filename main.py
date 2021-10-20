import gym
import math
import random
import importlib
# importlib.import_module("")
# from config import render
# from cartpole import *
# from mountainCar import *
from flappybird import *
from NEAT import make_species, set_reperesened_agent_best_specie, give_reduced_reward_regarding_lenght_of_specie, reduce_agents, mutatenpair, delete_empty_species
from init_genomes import init_edges, init_genomes, init_nodes, init_species, init_genomes


def test_generation(agents,render):
    for agent in agents:
        render = False
        total_reward = 0
        step = 0 
        if agent == agents[0]:
            render = True       
        agent.feed_forward(init_run())
        ob_reward = -math.inf
        while True:
            move = agent.best_move()
            observation, reward, done = main_flappybird(move, render)
            agent.feed_forward(observation)
            total_reward += 1
            step += 1
            if observation[0] > ob_reward: ob_reward = observation[0]
            if done:
                agent.reward = total_reward
                # agent.reward = ob_reward*1000/step
                main_flappybird("end", render)
                break
    env_ver.close()


def main():
    render = False
    agents = init_genomes()
    #One species represented by one random genome
    species = init_species(agents)

    gen_count = 0
    while True:
        test_generation(agents,render)
        species = make_species(agents,species)
        set_reperesened_agent_best_specie(species)
        give_reduced_reward_regarding_lenght_of_specie(species)
        agents = reduce_agents(agents,species)
        agents = mutatenpair(agents)
        # set_agents_specie_less(agents)
        make_species(agents,species)
        species = delete_empty_species(species)
        print_average_reward(agents)
        print(len(species))
        gen_count += 1

        

        if gen_count == 100:
            input("> ")
            render = True
    
def print_agents(agents):
    print("Agents:")
    print(agents)

def print_species(species):
    print("length of species", len(species))
    for specie in species:
        print("Specie:")
        print(specie.genomes)
        print("-------------")
    

def print_average_reward(agents):
    total_reward = agents[0].reward
    average_reward = sum(agent.reward for agent in agents)/len(agents)
    print("---------------------------------")
    print("Average reward: ", average_reward, "Highest reward", total_reward)
    print("---------------------------------")

if __name__ == "__main__":
    main()