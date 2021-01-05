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
    # print(len(output_nodes))
    # print(len(input_nodes))
    #Setting available moves to the output_nodes
    for i in range(len(output_nodes)):
        output_nodes[i].move = moves[i]
    init_edges(input_nodes, output_nodes)
    return input_nodes,hidden_nodes,output_nodes
def init_edges(input, output):
    #Exclusive number for every edge
    innov = 1
    for parent in output:
        parent.edges = []
        for child in parent.children:
            weight = random.uniform(0,1)
            parent.edges.append(Edge(weight, innov))
            innov += 1
    return None    
def init_genomes(num_agents, num_input, num_output):
    all_agents = []
    for _ in range(num_agents):
        input_nodes,hidden_nodes,output_nodes = init_nodes(num_input, num_output)
        agent = Genome(input_nodes,hidden_nodes,output_nodes,0)
        all_agents.append(agent)
    return all_agents
    
def main():
    agents = init_genomes(num_agents, num_input, num_output)
    for agent in agents:        
        agent.feed_forward(init_run())
        while True:
            print(agent.output_nodes[0].value)
            move = agent.best_move()
            print(move)
            observation, reward, done = main_cartpole(move)
            agent.feed_forward(observation)
            if done:
                agent.reward = reward
                main_cartpole("end")
                break

if __name__ == "__main__":
    main()