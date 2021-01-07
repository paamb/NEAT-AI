import gym
import random
from config import *
from cartpole import *
from NEAT import *
from init_genomes import *
#global innovation number
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