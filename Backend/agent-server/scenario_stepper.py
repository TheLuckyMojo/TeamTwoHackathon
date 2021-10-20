class ScenarioStepper:
    def step(self, state, action):
        done = False
        numberOfTargets = 6
        targetsOffset = 1
        # Apply action
        if action == 0:
            reward = 0
        elif action > 0 and action <= numberOfTargets:
            target = action - 1
            reward = 1
            expectedDamageIndex = targetsOffset + (target)
            currentDamageIndex = targetsOffset + (target + numberOfTargets)
            state[currentDamageIndex] += 1
            if state[currentDamageIndex] > state[expectedDamageIndex]:
                reward = -5
        else:
            reward = 0
        
        shouldReward = True
        for myTarget in range(1, numberOfTargets+1):
            expectedDamageIndex = myTarget
            currentDamageIndex = myTarget + numberOfTargets
            if state[currentDamageIndex] != state[expectedDamageIndex]:
                shouldReward = False
                break
        
        if shouldReward:
            reward = 100
            done = True

        # Reduce shower length by 1 second
        state[0] -= 1

        # Check if shower is done
        if state[0] <= 0:
            done = True

        # Set placeholder for info
        info = {}

        # Return step information
        return state, reward, done, info
