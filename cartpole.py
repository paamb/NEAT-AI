import gym
# from main import render
num_input = 4
num_output = 2
moves = [0,1]
env_ver = gym.make('CartPole-v0')
is_render = False
def init_run():
    observation = env_ver.reset()
    return observation

def main_cartpole(move,render):
    if move != "end":
        if render:
            env_ver.render()
        observation, reward, done, info = env_ver.step(move)
        return observation,reward,done