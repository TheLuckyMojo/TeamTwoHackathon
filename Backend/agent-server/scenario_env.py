from gym import Env
from gym.spaces import Discrete, MultiDiscrete 
import numpy as np

from scenario_stepper import ScenarioStepper

class ScenarioEnv(Env):
    def __init__(self, numberOfMissles, tD1, tD2, tD3, tD4, tD5, tD6):
        # Actions we can take: 0 - Do Nothing, 1 - Launch
        self.action_space = Discrete(7)
        # Target Damage state array: 0 - Untouched, 1 - Disabled, 2 - Destroyed
        self.observation_space = MultiDiscrete([100, 3, 3, 3, 3, 3, 3, 14, 14, 14, 14, 14, 14])
        # store initial state
        self.numberOfMissles = numberOfMissles
        self.tD1 = tD1
        self.tD2 = tD2
        self.tD3 = tD3
        self.tD4 = tD4
        self.tD5 = tD5
        self.tD6 = tD6
        # Set start state
        self.state = np.array([self.numberOfMissles, self.tD1, self.tD2, self.tD3, self.tD4, self.tD5, self.tD6, 0, 0, 0 ,0 ,0 ,0])
        self.stepper = ScenarioStepper()

    def step(self, action):
        # Return step information
        return self.stepper.step(self.state, action)

    def render(self):
        # Implement viz
        pass

    def reset(self):
        # Reset shower temperature
        self.state = np.array([self.numberOfMissles, self.tD1, self.tD2, self.tD3, self.tD4, self.tD5, self.tD6, 0, 0, 0 ,0 ,0 ,0])
        return self.state
