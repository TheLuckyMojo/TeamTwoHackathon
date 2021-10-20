import copy

from stable_baselines3.common.evaluation import evaluate_policy

from scenario_env import ScenarioEnv

def GeneratePrediction(model, scenarioEnv: ScenarioEnv):
    """
    Generates prediction from the agent model.
    """

    scenarioEnv.reset()
    evaluate_policy(model, scenarioEnv, n_eval_episodes=1000, render=False)

    sampleEnvObs = scenarioEnv.reset()
    done = False
    score = 0
    prediction = []

    while not done:
        action, _ = model.predict(sampleEnvObs)
        sampleEnvObs, reward, done, info = scenarioEnv.step(action)
        score+=reward
        print('Score:{} Action:{} State:{}'.format(score, action, sampleEnvObs))
        prediction.append([action, copy.deepcopy(sampleEnvObs)])
    scenarioEnv.close()

    return prediction
