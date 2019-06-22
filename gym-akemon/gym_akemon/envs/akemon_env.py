import gym
from gym import error, spaces, utils
from gym.utils import seeding


class AkemonEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        pass

    def reset(self):
        self.obs = Observation()
        self.renderer = Renderer()

        return self.obs

    def step(self, action):
        self.obs.battle.turn = self.obs.battle.turn + 1

        return self.obs

    def render(self, mode='human', close=False):
        return self.renderer.getRenderer()


class Observation:

    def __init__(self):
        self.battle = BattleObservation()


class BattleObservation:
    def __init__(self):
        self.turn = 0

class Renderer:
    def __init__(self):
        pass
    
    def getRenderer(self):
        return dict()