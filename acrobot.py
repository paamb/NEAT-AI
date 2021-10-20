import gym
# from main import render
num_input = 6
num_output = 3
moves = [0,1,-1]
env_ver = gym.make('Acrobot-v1')
is_render = False
def init_run():
    observation = env_ver.reset()
    return observation

def main_acrobot(move,render):
    if move != "end":
        if render:
            env_ver.render()
        observation, reward, done, info = env_ver.step(move)
        return observation,reward,done