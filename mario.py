from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = JoypadSpace(env, SIMPLE_MOVEMENT)

done = True
for step in range(5000):
    if done:
        state = env.reset()
    state, reward, done, info = env.step(6)
    env.render()

env.close()

MOVEMENT = [
    ['NOOP'],
    ['A'],
    ['B'],
    ['right'],
    ['right', 'A'],
    ['right', 'B'],
    ['left'],
    ['left', 'A'],
    ['left', 'B'],
    ['down'],
    ['down', 'A'],
    ['down', 'B'],
]


SIMPLE_MOVEMENT = [
    ['NOOP'],
    ['A'],
    ['B'],
    ['right'],
    ['left'],
    ['down'],
]

