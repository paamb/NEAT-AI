from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = JoypadSpace(env, SIMPLE_MOVEMENT)

done = True
for step in range(5000):
    if done:
        state = env.reset()
    state, reward, done, info = env.step(0)
    env.render()
    print(state)
env.close()


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


