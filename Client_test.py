import pytest
import unittest
import gym

class smoketest(unittest.TestCase):
    def setUp(self):
        self.env = gym.make('gym_akemon:akemon-v0')
        self.assertNotEqual(self.env, None)

    def test_reset(self):
        obs = self.env.reset()
        self.assertEqual(obs.battle.turn, 0)
    
    def test_step(self):
        obs = self.env.reset()
        self.env.step(action=[])
        self.assertEqual(obs.battle.turn, 1)
    
    def test_render(self):
        page = self.env.render()
        self.assertNotEqual(self.env, None)

