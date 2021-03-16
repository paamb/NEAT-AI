import gym
# from main import render
num_input = 2
num_output = 3
moves = [0,1,2]
env_ver = gym.make('MountainCar-v0')
is_render = False
def init_run():
    observation = env_ver.reset()
    return observation

def main_mountain_car(move,render):
    if move != "end":
        if render:
            env_ver.render()
        observation, reward, done, info = env_ver.step(move)
        return observation,reward,done

# agent.reward = ob_reward*1000/step
# if observation[0] > ob_reward: ob_reward = observation[0]
# step = 0
 # ob_reward = -math.inf