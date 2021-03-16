import time
import flappy_bird_gym
num_input = 2
num_output = 2
moves = [0,1]
env_ver = flappy_bird_gym.make("FlappyBird-v0")
def init_run():
    obs = env_ver.reset()
    return obs
def main_flappybird(move,render):
    if move != "end":
        if render:
            env_ver.render()
            time.sleep(1 / 30)
        obs, reward, done, info = env_ver.step(move)
        # print(obs[0])
        return obs, reward, done


# def init_run():
#     observation = env_ver.reset()
#     return observation

# def main_cartpole(move,render):
#     if move != "end":
#         if render:
#             env_ver.render()
#         observation, reward, done, info = env_ver.step(move)
        
#         return observation,reward,done