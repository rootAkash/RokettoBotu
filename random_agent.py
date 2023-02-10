import rlgym
import numpy as np

env = rlgym.make()
max_games= 10
for i in range(max_games):
    obs = env.reset()
    done = False

    while not done:
      #Here we sample a random action. If you have an agent, you would get an action from it here.
      action = env.action_space.sample() 
      
      next_obs, reward, done, gameinfo = env.step(action)
      obs_arr = np.array(next_obs)
      
      obs = next_obs
env.close()