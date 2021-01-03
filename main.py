import gym
import random
from config import *
from cartpole import *
from NEAT import *
def init_nodes(num_input,num_output):
    #Index, value, children, move
    #Random move first
    inputs = [Node(i, random.uniform(0,1), [], None) for i in range(num_input)]
    hidden = []
    #Output node gets every input node as children
    input_index = [i for i in range(num_input)]
    outputs = [Node(i, -1, input_index, None) for i in range(num_input, num_input+num_output)]
    return inputs,hidden,outputs
def init_edges(num_input,num_output):
    edges = []
    for i in range(num_output):
        for j in range(num_input):
            edges.append(Edge(j,num_input+i, random.uniform(0,1), j + num_input*j))
    # edges = [[Edge(i, j, random.uniform(0,1), True, i + num_input*j) for i in range(num_input)] for j in range(num_input, num_input+num_output)]
    return edges      
def init_genomes(num_agents, num_input, num_output):
    all_agents = []
    for _ in range(num_agents):
        inputs,hidden,outputs = init_nodes(num_input, num_output)
        edges = init_edges(num_input,num_output)
        agent = Genome(inputs,hidden,outputs,edges,0)
        all_agents.append(agent)
    return all_agents
    
def main():
    init_genomes(num_agents, num_output, num_input)
    feed_observation(obs)
    for agent in num_agents:
        print("Hei")
        agent.feed_observation(init_run())
        while True:
            move = agent.feed_forward()
            env_output = env(move)
            agent.feed_observation(obs)
            if done:
                env("end")
                break

if __name__ == "__main__":
    main()