from gym import Env
from gym.spaces import Discrete, MultiDiscrete 
import numpy as np
import random

import ScenarioStepper

class TrainingScenarioEnv(Env):
    def __init__(self):
        # Actions we can take: 0 - Do Nothing, 1 - Launch
        self.action_space = Discrete(7)
        # Target Damage state array: 0 - Untouched, 1 - Disabled, 2 - Destroyed
        self.observation_space = MultiDiscrete([100, 3, 3, 3, 3, 3, 3, 14, 14, 14, 14, 14, 14])
        # Set start state
        self.state = np.array([random.randint(1, 15), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), 0, 0, 0 ,0 ,0 ,0])
        self.stepper = ScenarioStepper()

    def step(self, action):
        # Return step information
        return self.stepper.step(self.state, action)

    def render(self):
        # Implement viz
        pass

    def reset(self):
        # Reset shower temperature
        self.state = np.array([random.randint(1, 15), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), 0, 0, 0 ,0 ,0 ,0])
        return self.state