import gym
import numpy as np

class LinearObservationWrapper(gym.ObservationWrapper):
    """
    Yields linear observation data only.
    """

    def __init__(self, env):
        super(LinearObservationWrapper, self).__init__(env)
        self.observation_space = env.observation_space["linear"]

    def observation(self, observation):
        return observation["linear"]


class LidarObservationWrapper(gym.ObservationWrapper):
    """
    Yields lidar observation data only.
    """

    def __init__(self, env):
        super(LidarObservationWrapper, self).__init__(env)
        self.observation_space = env.observation_space["lidar"]

    def observation(self, observation):
        return observation["lidar"]


class ClipRewardsWrapper(gym.RewardWrapper):
    """
    Clips the rewards.
    """

    def __init__(self, env):
        super(ClipRewardsWrapper, self).__init__(env)

    def reward(self, reward):
        return np.clip(reward, -1., 1.)