import gym
from gym import error, spaces, utils
from gym.utils import seeding


class AkemonEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.battle = dict()

    def reset(self):
        print("reset Function"
              "")
        return True

    def step(self, action):
        pass

    def render(self, mode='human', close=False):
        pass
