import gym
import random
from config import *
from cartpole import *
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
    #Setting available moves to the output_nodes
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

def init_genomes(num_agents, num_input, num_output):
    all_agents = []
    for _ in range(num_agents):
        input_nodes,hidden_nodes,output_nodes = init_nodes(num_input, num_output)
        agent = Genome(input_nodes,hidden_nodes,output_nodes,0)
        all_agents.append(agent)
    return all_agents

def test_generation(agents):
    for agent in agents:        
        agent.feed_forward(init_run())
        while True:
            move = agent.best_move()
            observation, reward, done = main_cartpole(move)
            agent.feed_forward(observation)
            if done:
                agent.reward = reward
                main_cartpole("end")
                break
        print_agent(agent)
    env_ver.close()
def mutatenpair(agents):
    for agent in agents:
        # agent.add_connection()
        agent.add_node()
def main():
    agents = init_genomes(num_agents, num_input, num_output)
    while True:
        test_generation(agents)
        mutatenpair(agents)


if __name__ == "__main__":
    main()