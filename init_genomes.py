import gym
import random
from config import *
from cartpole import *
from NEAT import *
def init_nodes(num_input,num_output):
    #Is_input_node, Index, value, children, edges, move
    input_nodes = [Node(True, i, None, None, None) for i in range(num_input)]
    hidden_nodes = []
    #Output node gets every input node as children
    output_nodes = [Node(False, i, None, input_nodes, None) for i in range(num_input, num_input+num_output)]
    #Setting available moves to the output_nodes
    for i in range(len(output_nodes)):
        output_nodes[i].move = moves[i]
    innov_counter = init_edges(input_nodes, output_nodes)
    return input_nodes,hidden_nodes,output_nodes, innov_counter
    
def init_edges(input, output):
    #Exclusive number for every edge
    innov = 1
    for parent in output:
        parent.edges = []
        for child in parent.children:
            weight = random.uniform(0,1)
            parent.edges.append(Edge(weight, innov,True))
            innov += 1
    return innov
    
def init_genomes(num_agents, num_input, num_output):
    all_agents = []
    for _ in range(num_agents):
        input_nodes,hidden_nodes,output_nodes,innov_counter = init_nodes(num_input, num_output)
        agent = Genome(input_nodes,hidden_nodes,output_nodes,innov_counter,0)
        all_agents.append(agent)
    return all_agents