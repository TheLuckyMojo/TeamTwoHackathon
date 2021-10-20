import grpc;
from grpc_reflection.v1alpha import reflection
from concurrent import futures;

from stable_baselines3 import PPO

import agent_pb2;
import agent_pb2_grpc;

import agent_data_converter;
import agent_model_driver;

class AgentServicer(agent_pb2_grpc.AgentServicer):
    def __init__(self):
        # The zip contains the brains.
        # It can take a little while to load this, so do once on startup.
        self.model = PPO.load('../../sandbox/rLPython/PPO')

    def GetPlanAssessment(self, request, context):
        scenarioEnv = agent_data_converter.OperatingPictureToScenarioEnvironment(request)

        targetIds = []
        for entry in request.targetIdToDamage.entries:
            targetIds.append(entry.id)
        prediction = agent_model_driver.GeneratePrediction(self.model, scenarioEnv)

        planAssessment = agent_data_converter.PredictionToPlanAssessment(prediction, targetIds)
        return planAssessment

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    agent_pb2_grpc.add_AgentServicer_to_server(
        AgentServicer(), server)
    SERVICE_NAMES = (
        agent_pb2.DESCRIPTOR.services_by_name['Agent'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    port = "50051"
    print("Server started. Listening on port " + port)
    server.add_insecure_port('[::]:' + port)
    server.start()
    server.wait_for_termination()

main()
