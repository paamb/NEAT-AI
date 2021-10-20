import gym
import importlib
import random
from config import num_agents
from mountainCar import num_output,num_input, moves
from NEAT import Node, Edge, Genome, Specie, glb_innov, glb_node_index, innov_maker

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

def init_genomes():
    all_agents = []
    for _ in range(num_agents):
        input_nodes,hidden_nodes,output_nodes = init_nodes(num_input, num_output)
        agent = Genome(input_nodes,hidden_nodes,output_nodes,0)
        all_agents.append(agent)
    return all_agents