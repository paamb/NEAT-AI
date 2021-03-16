import gym
import math
import random
from config import num_agents, render
# from cartpole import *
from mountainCar import*
# from flappybird import *
from NEAT import *
# from init_genomes import *
#global innovation number
glb_innov = {}
glb_node_index = {}
def init_nodes(num_input,num_output):
    #Is_input_node, Index, value, children, edges, move
    input_nodes = [Node(True, i, None, None, None) for i in range(num_input)]
    hidden_nodes = []
    #Output node gets every input node as children
    output_nodes = [Node(False, i, None, input_nodes, None) for i in range(num_input, num_input+num_output)]
    #Setting available moves 
    for i in range(len(output_nodes)):
        output_nodes[i].move = moves[i]
    init_edges(input_nodes, output_nodes)
    return input_nodes,hidden_nodes,output_nodes
    
def init_edges(input_node, output_node):
    #Exclusive number for every edge
    for parent in output_node:
        parent.edges = []
        for child in parent.children:
            #Puts every edge into the global node innov dictionary
            innov = innov_maker(glb_innov,child,parent)
            #Puts every node_index into the global node index dictionary
            innov_maker(glb_node_index, parent, child)
            weight = random.uniform(0,1)
            parent.edges.append(Edge(weight, innov,True))
    return None

def init_species(agents):
    represent_genome = random.choice(agents)
    species = [Specie(represent_genome)]
    return species

def init_genomes(num_agents, num_input, num_output):
    all_agents = []
    for _ in range(num_agents):
        input_nodes,hidden_nodes,output_nodes = init_nodes(num_input, num_output)
        agent = Genome(input_nodes,hidden_nodes,output_nodes,0)
        all_agents.append(agent)
    return all_agents

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
            observation, reward, done = main_mountain_car(move, render)
            agent.feed_forward(observation)
            total_reward += 1
            step += 1
            if observation[0] > ob_reward: ob_reward = observation[0]
            if done:
                # agent.reward = total_reward
                agent.reward = ob_reward*1000/step
                main_mountain_car("end", render)
                break
        # print_agent(agent)
    env_ver.close()


def main():
    render = False
    agents = init_genomes(num_agents, num_input, num_output)
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
        # print_species(species)   
        # genomic_distance(agents[0], agents[1])
        # print_agents(agents)
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